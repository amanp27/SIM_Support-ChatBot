from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, List, Annotated
from langgraph.graph.message import add_messages
import sqlite3
import json
import time
import uuid

from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


# Defining the state of the chatbot conversation
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# Defining the chatnode function
def chat_node(state: ChatState):
    message = state['messages']
    response = llm.invoke(message)
    return {'messages': [response]}


# --- SQLite Connection (shared for both SqliteSaver and custom table) ---
conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)

# --- LangGraph checkpointer (handles LangGraph internal state) ---
checkpointer = SqliteSaver(conn=conn)

# --- Create custom conversations table for clean JSON storage ---
conn.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        session_id   TEXT PRIMARY KEY,
        created_time INTEGER NOT NULL,
        updated_time INTEGER NOT NULL,
        messages     TEXT NOT NULL DEFAULT '[]'
    )
""")
conn.commit()


# --- Defining the graph ---
graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)


# -----------------------------------------------------------------------
# Custom conversation storage helpers
# -----------------------------------------------------------------------

def _now_ms() -> int:
    """Return current UTC time in milliseconds."""
    return int(time.time() * 1000)


def save_message_pair(session_id: str, user_message: str, ai_message: str):
    """
    Append a user+AI message pair to the conversations table.
    Creates the session row if it doesn't exist yet.
    """
    now = _now_ms()
    message_id = f"msg_{uuid.uuid4().hex[:8]}"

    new_entry = {
        "messageId": message_id,
        "usermessage": user_message,
        "aimessage": ai_message,
        "type": "TEXT",
        "createdTime": now
    }

    # Upsert: insert new session or update existing one
    cursor = conn.execute(
        "SELECT messages, created_time FROM conversations WHERE session_id = ?",
        (str(session_id),)
    )
    row = cursor.fetchone()

    if row is None:
        # New session
        messages_list = [new_entry]
        conn.execute(
            """INSERT INTO conversations (session_id, created_time, updated_time, messages)
               VALUES (?, ?, ?, ?)""",
            (str(session_id), now, now, json.dumps(messages_list))
        )
    else:
        # Existing session — append to messages list
        messages_list = json.loads(row[0])
        messages_list.append(new_entry)
        conn.execute(
            """UPDATE conversations
               SET updated_time = ?, messages = ?
               WHERE session_id = ?""",
            (now, json.dumps(messages_list), str(session_id))
        )

    conn.commit()


def get_conversation(session_id: str) -> dict | None:
    """
    Retrieve a full conversation session as a clean dict.
    Returns None if not found.
    """
    cursor = conn.execute(
        "SELECT session_id, created_time, updated_time, messages FROM conversations WHERE session_id = ?",
        (str(session_id),)
    )
    row = cursor.fetchone()
    if row is None:
        return None

    return {
        "_id": row[0],
        "createdTime": row[1],
        "updatedTime": row[2],
        "messages": json.loads(row[3])
    }


def retrieve_all_thread():
    """Return all thread IDs from LangGraph checkpointer."""
    all_thread = set()
    for checkpoint in checkpointer.list(None):
        all_thread.add(checkpoint.config['configurable']['thread_id'])
    return list(all_thread)