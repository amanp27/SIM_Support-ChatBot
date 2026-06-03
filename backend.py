from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import (
    LLMChainExtractor,
    EmbeddingsFilter,
    DocumentCompressorPipeline
)
from langchain_chroma import Chroma
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, Annotated, Optional
from langgraph.graph.message import add_messages
import sqlite3
import json
import time
import uuid
import tempfile
import os

from dotenv import load_dotenv
load_dotenv()

# -----------------------------------------------------------------------
# LLM & Embeddings
# -----------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
embedding = OpenAIEmbeddings(model="text-embedding-3-small")


# -----------------------------------------------------------------------
# LangGraph State
# -----------------------------------------------------------------------
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# -----------------------------------------------------------------------
# Active retriever (module-level, replaced on each file upload)
# -----------------------------------------------------------------------
_active_retriever = None


def get_retriever():
    return _active_retriever


def set_retriever(retriever):
    global _active_retriever
    _active_retriever = retriever


# -----------------------------------------------------------------------
# RAG pipeline builder  (DocumentCompressor Pipeline — best results)
# -----------------------------------------------------------------------
def build_rag_retriever(file_bytes: bytes, filename: str):
    """
    Accepts raw file bytes + original filename.
    Loads, chunks, embeds, and returns a DocumentCompressorPipeline retriever.
    Supports .md and .pdf files.
    """
    ext = os.path.splitext(filename)[-1].lower()

    # --- Load documents ---
    if ext == ".pdf":
        # Write to a temp file so PyPDFLoader can read it
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name
        try:
            loader = PyPDFLoader(tmp_path)
            docs = loader.load()
        finally:
            os.unlink(tmp_path)

    elif ext == ".md":
        markdown_text = file_bytes.decode("utf-8")
        headers_to_split_on = [
            ('#',   'Header_1'),
            ('##',  'Header_2'),
            ('###', 'Header_3'),
        ]
        splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on,
            strip_headers=False
        )
        docs = splitter.split_text(markdown_text)

    else:
        raise ValueError(f"Unsupported file type: {ext}. Use .md or .pdf")

    # --- Embed into Chroma (in-memory, fresh per upload) ---
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        collection_name=f"rag_{uuid.uuid4().hex[:8]}"
    )

    # --- DocumentCompressor Pipeline (best results from notebook) ---
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    embd_compressor = EmbeddingsFilter(
        embeddings=embedding,
        similarity_threshold=0.4
    )
    llm_compressor = LLMChainExtractor.from_llm(
        ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
    )
    pipeline_compressor = DocumentCompressorPipeline(
        transformers=[embd_compressor, llm_compressor]
    )
    retriever = ContextualCompressionRetriever(
        base_compressor=pipeline_compressor,
        base_retriever=base_retriever
    )

    return retriever


# -----------------------------------------------------------------------
# Chat node — uses RAG context when a retriever is loaded
# -----------------------------------------------------------------------
def chat_node(state: ChatState):
    messages = state["messages"]
    retriever = get_retriever()

    if retriever is not None:
        # Get the latest user message text for retrieval
        last_user_msg = next(
            (m.content for m in reversed(messages) if isinstance(m, HumanMessage)),
            ""
        )
        retrieved_docs = retriever.invoke(last_user_msg)
        context = "\n\n".join(doc.page_content for doc in retrieved_docs)

        system_prompt = (
            """
You are Invo, a friendly and helpful support assistant for Simple Invoice Manager (SIM).

--------------------------------------------------
WHO YOU ARE

You are helpful, warm, and conversational — not robotic.
You answer from the knowledge base, but you never make users feel stuck or ignored.

--------------------------------------------------
CONVERSATIONAL INPUTS — HANDLE FIRST, ALWAYS

If the user sends any of these, respond naturally. Never check the knowledge base. Never fallback.

- Greetings (hi, hii, hello, hey, good morning, etc.) → "Hi! 👋 How can I help you today?"
- Acknowledgements (ok, okay, okk, sure, got it, alright, k, kk) → "Got it! Feel free to ask anything."
- Affirmations (yes, yeah, correct, right, yep) → "Sure! Go ahead."
- Gratitude (thank you, thanks, thankyou, ty, thx) → "You're welcome! 😊"
- Confusion (idk, i don't understand, hmm, not sure) → "No worries! Could you tell me a bit more about what you're looking for?"

Even with typos or repeated characters (hiii, okkk, thankuuu) — treat them the same way.

--------------------------------------------------
OUT OF SCOPE — DECLINE FIRMLY BUT POLITELY

If the user asks anything related to the technical or internal structure of the application, decline clearly. Do not answer, guess, or partially engage.

This includes questions like:
- Programming language or tech stack used to build the app
- Database used (MySQL, MongoDB, MS Access, etc.)
- API endpoints, HTTP requests, backend integration
- Source code, architecture, or internal systems
- App version history or latest release details
- Any technical integration not documented in the knowledge base

Response for these:
→ "That's outside what I can help with. I'm here to assist with using the SIM app — features, settings, and how things work. For technical queries, please reach out to our support team."

Never guess. Never engage partially. Decline and redirect every time.

--------------------------------------------------
ANSWERING QUESTIONS

- Answer from the knowledge base.
- Keep answers clear and to the point.
- Do not add unnecessary suggestions or follow-ups.

--------------------------------------------------
FOLLOW-UP QUESTIONS

- Always remember the context of the previous message.
- If a user asks "why?", "how?", "what about this?" after your answer — treat it as a follow-up to the same topic.
- If the follow-up is something you cannot fully answer from the knowledge base, respond naturally:
  → "That's a great point! This might be something the team is working on. For detailed info, you can reach out to our support team."
- Never drop context and never send a fallback just because the follow-up is short.

--------------------------------------------------
WHEN YOU DON'T HAVE THE ANSWER

- If a question is genuinely not in the knowledge base, respond warmly:
  → "I don't have that info right now, but our support team will be happy to help you with this!"
- Always sound human. Never make the user feel dismissed.

--------------------------------------------------
LANGUAGE

- Respond in the same language the user is writing in.
- If asked "do you speak X language?" → "Yes, I can help you in multiple languages!"
- Never reject a language request.

--------------------------------------------------
WHAT YOU NEVER DO

- Never say "I am only trained on..."
- Never send a fallback for greetings, casual talk, or short replies.
- Never make up information not in the knowledge base.
- Never answer technical/backend questions about how the app is built.
- Never sound cold or robotic.

--------------------------------------------------
SUBSCRIPTION QUERIES

- If the user asks anything related to subscription, plans, payment, renewal, or expiry — answer from the knowledge base as usual.
- At the end of every subscription-related answer, always add:
  → "If your query is not resolved, please Contact WhatsApp support at 📞 "+91 9511884141"
- This line must appear ONLY on subscription-related answers.
- Never add this line to any other topic or answer.

"""
        )
        messages_with_context = [SystemMessage(content=system_prompt)] + list(messages)
        response = llm.invoke(messages_with_context)
    else:
        response = llm.invoke(messages)

    return {"messages": [response]}


# -----------------------------------------------------------------------
# SQLite connection — shared by SqliteSaver + custom conversations table
# -----------------------------------------------------------------------
conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

conn.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        session_id   TEXT PRIMARY KEY,
        created_time INTEGER NOT NULL,
        updated_time INTEGER NOT NULL,
        messages     TEXT NOT NULL DEFAULT '[]'
    )
""")
conn.commit()


# -----------------------------------------------------------------------
# LangGraph graph
# -----------------------------------------------------------------------
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)


# -----------------------------------------------------------------------
# Custom conversation storage helpers
# -----------------------------------------------------------------------
def _now_ms() -> int:
    return int(time.time() * 1000)


def save_message_pair(session_id: str, user_message: str, ai_message: str):
    now = _now_ms()
    message_id = f"msg_{uuid.uuid4().hex[:8]}"
    new_entry = {
        "messageId": message_id,
        "usermessage": user_message,
        "aimessage": ai_message,
        "type": "TEXT",
        "createdTime": now,
    }

    cursor = conn.execute(
        "SELECT messages, created_time FROM conversations WHERE session_id = ?",
        (str(session_id),),
    )
    row = cursor.fetchone()

    if row is None:
        conn.execute(
            "INSERT INTO conversations (session_id, created_time, updated_time, messages) VALUES (?, ?, ?, ?)",
            (str(session_id), now, now, json.dumps([new_entry])),
        )
    else:
        messages_list = json.loads(row[0])
        messages_list.append(new_entry)
        conn.execute(
            "UPDATE conversations SET updated_time = ?, messages = ? WHERE session_id = ?",
            (now, json.dumps(messages_list), str(session_id)),
        )

    conn.commit()


def get_conversation(session_id: str) -> dict | None:
    cursor = conn.execute(
        "SELECT session_id, created_time, updated_time, messages FROM conversations WHERE session_id = ?",
        (str(session_id),),
    )
    row = cursor.fetchone()
    if row is None:
        return None
    return {
        "_id": row[0],
        "createdTime": row[1],
        "updatedTime": row[2],
        "messages": json.loads(row[3]),
    }


def retrieve_all_thread():
    all_thread = set()
    for checkpoint in checkpointer.list(None):
        all_thread.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_thread)