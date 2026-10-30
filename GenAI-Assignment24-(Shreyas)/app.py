import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama


#Tracking the application with LangSmith
load_dotenv()

st.title('Llama Chat Bot')

query = st.text_input('Enter your question: ')
LLM = ChatOllama(model='llama3.2')

if query:
    response= LLM.invoke(query)
    st.write(response.content)
