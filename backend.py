from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Annotated
from langgraph.graph.message import add_messages

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model= "gpt-4o-mini", temperature=0.7)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    message = state['messages']
    response = llm.invoke(message)
    return {'messages': [response]}


graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)


chatbot = graph.compile()

