import streamlit as st
from backend import chatbot, retrieve_all_thread, save_message_pair, build_rag_retriever, set_retriever, get_retriever
from langchain_core.messages import BaseMessage, HumanMessage
import uuid

from dotenv import load_dotenv
load_dotenv()


# -----------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------
def generate_thread_id():
    return uuid.uuid4()

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread(st.session_state["thread_id"])
    st.session_state["message_history"] = []

def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(config={"configurable": {"thread_id": thread_id}})
    return state.values.get("messages", [])


# -----------------------------------------------------------------------
# Session state init
# -----------------------------------------------------------------------
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = retrieve_all_thread()

if "uploaded_filename" not in st.session_state:
    st.session_state["uploaded_filename"] = None

add_thread(st.session_state["thread_id"])

CONFIG = {"configurable": {"thread_id": st.session_state["thread_id"]}}


# -----------------------------------------------------------------------
# Streamlit UI — Header
# -----------------------------------------------------------------------
st.title("SIM Support Chatbot")


# -----------------------------------------------------------------------
# Streamlit UI — Sidebar
# -----------------------------------------------------------------------
st.sidebar.title("LangGraph Chatbot")

# --- New Chat button ---
if st.sidebar.button("New Chat"):
    reset_chat()
    # Clear RAG on new chat
    set_retriever(None)
    st.session_state["uploaded_filename"] = None

st.sidebar.divider()

# --- File Upload for RAG ---
st.sidebar.header("📄 Upload Document (RAG)")
uploaded_file = st.sidebar.file_uploader(
    "Upload a .md or .pdf file",
    type=["md", "pdf"],
    help="Once uploaded, the chatbot will answer questions based on this document."
)

if uploaded_file is not None:
    # Only rebuild retriever if a new file is uploaded
    if uploaded_file.name != st.session_state["uploaded_filename"]:
        with st.sidebar.status(f"Processing **{uploaded_file.name}**...", expanded=True) as status:
            st.write("Loading and chunking document...")
            try:
                retriever = build_rag_retriever(
                    file_bytes=uploaded_file.read(),
                    filename=uploaded_file.name
                )
                set_retriever(retriever)
                st.session_state["uploaded_filename"] = uploaded_file.name
                status.update(label=f"✅ Ready: {uploaded_file.name}", state="complete")
            except Exception as e:
                status.update(label=f"❌ Failed: {e}", state="error")
                set_retriever(None)
                st.session_state["uploaded_filename"] = None

# Show active document badge
if st.session_state["uploaded_filename"]:
    st.sidebar.success(f"🔍 RAG active: `{st.session_state['uploaded_filename']}`")
    if st.sidebar.button("❌ Remove Document"):
        set_retriever(None)
        st.session_state["uploaded_filename"] = None
        st.rerun()
else:
    st.sidebar.info("No document uploaded. Using general chat mode.")

st.sidebar.divider()

# --- Chat thread history ---
st.sidebar.header("My Conversations")
st.sidebar.text(st.session_state["thread_id"])

for thread_id in st.session_state["chat_threads"][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state["thread_id"] = thread_id
        messages = load_conversation(thread_id)
        temp_messages = []
        for message in messages:
            role = "user" if isinstance(message, HumanMessage) else "assistant"
            temp_messages.append({"role": role, "content": message.content})
        st.session_state["message_history"] = temp_messages


# -----------------------------------------------------------------------
# Chat area — show RAG mode indicator in header
# -----------------------------------------------------------------------
if st.session_state["uploaded_filename"]:
    st.caption(f"🔍 RAG mode — answering from: `{st.session_state['uploaded_filename']}`")
else:
    st.caption("💬 General chat mode")

# --- Display message history ---
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------------------------------------------------
# User input
# -----------------------------------------------------------------------
user_input = st.chat_input("Type here...")

if user_input:
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {"messages": HumanMessage(content=user_input)},
                config=CONFIG,
                stream_mode="messages",
            )
        )

    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})

    save_message_pair(
        session_id=st.session_state["thread_id"],
        user_message=user_input,
        ai_message=ai_message,
    )