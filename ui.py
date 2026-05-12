import streamlit as st
from backend import chatbot
from langchain_core.messages import BaseMessage

from dotenv import load_dotenv
load_dotenv()

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


st.title("Simple Invoice Manager Chatbot")

user_input = st.chat_input("Type here...")

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

