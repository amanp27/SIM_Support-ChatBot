import streamlit as st
from backend import chatbot, retrieve_all_thread, save_message_pair
from langchain_core.messages import BaseMessage, HumanMessage
import uuid

from dotenv import load_dotenv
load_dotenv()


# --- Utility Functions ---

def generate_thread_id():
    return uuid.uuid4()

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    return state.values.get('messages', [])


# --- Initializing session state ---

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_thread()

add_thread(st.session_state['thread_id'])

# Config is read fresh each render so switching threads works correctly
CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}


# --- Streamlit UI Header ---
st.title("SIM Support Chatbot")

# --- Streamlit UI Sidebar ---
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversation")
st.sidebar.text(st.session_state['thread_id'])

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []
        for message in messages:
            if isinstance(message, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role': role, 'content': message.content})
        st.session_state['message_history'] = temp_messages


# --- Displaying message history ---
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


# --- Getting user input ---
user_input = st.chat_input("Type here...")

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': HumanMessage(content=user_input)},
                config=CONFIG,
                stream_mode='messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})

    # --- Save paired message to clean conversations table ---
    save_message_pair(
        session_id=st.session_state['thread_id'],
        user_message=user_input,
        ai_message=ai_message
    )