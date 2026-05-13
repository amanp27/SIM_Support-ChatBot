import streamlit as st
from backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage

from dotenv import load_dotenv
load_dotenv()

# Storing the thread_id in the config to maintain the conversation context across multiple interactions with the chatbot. 
# config does NOT store memory. It only tells LangGraph: “which conversation/session this belongs to.”
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# Streamlit UI Header
st.title("SIM Support Chatbot")


# Initializing the session state
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Displaying the message history on the UI screen
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


# Gettig User response
user_input = st.chat_input("Type here...")


if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': HumanMessage(content = user_input)},
                config = CONFIG,
                stream_mode = 'messages'
                )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})