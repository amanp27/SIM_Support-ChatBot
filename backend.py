from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, List, Annotated
from langgraph.graph.message import add_messages
import sqlite3

from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model= "gpt-4o-mini", temperature=0.7)


# Defining the state of the chatbot conversation
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# Defining the chatnode function
def chat_node(state: ChatState):
    message = state['messages']
    response = llm.invoke(message)
    return {'messages': [response]}

conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
# checkpointer
checkpointer = SqliteSaver(conn=conn)

# Defining the graph
graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)

# to retrieve all thread
def retrieve_all_thread():
    all_thread = set()
    for checkpoint in checkpointer.list(None):
        all_thread.add(checkpoint.config['configurable']['thread_id'])
        
    return list(all_thread)
