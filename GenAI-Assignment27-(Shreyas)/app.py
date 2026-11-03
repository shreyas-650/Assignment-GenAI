# Task 5 & 6
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
st.title('Q&A Chatbot')

prompt = ChatPromptTemplate([
    ('system','You are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{input}')
])

LLM = ChatGroq(model='openai/gpt-oss-20b')

if 'store' not in st.session_state:
    st.session_state.store = {}

def get_history(session_id: str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id]=ChatMessageHistory()
    return st.session_state.store[session_id]

chain = prompt | LLM | StrOutputParser()

chatbot = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key='input',
    history_messages_key='chat_history'
)


query = st.text_input('Enter The Query')

if st.button('Invoke'):
    if query:
        response = chatbot.invoke(
            {'input': query},
            config={'configurable': {'session_id': 'shrey123'}}
        )
        st.write(response)

st.subheader('Chat History')

for message in get_history('shrey123').messages:
    st.write(message.type, ':', message.content)