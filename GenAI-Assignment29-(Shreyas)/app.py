import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
load_dotenv()

if "store" not in st.session_state:
    st.session_state.store = {}

def get_history(session_id : str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id]=ChatMessageHistory()
    return st.session_state.store[session_id]

prompt = ChatPromptTemplate([
    ('system','You are a rude assistant which talk in very rude way'),
    MessagesPlaceholder(variable_name='history'),
    ('human','{query}')
])


st.title('OpenAI / Ollama Q & A ChatBot')
query = st.text_input('Enter The Question:') 
model_type = st.selectbox('Choose the Model:',['OpenAI','Ollama'])

def get_answer(question,model_type='OpenAI'):
    if model_type=='OpenAI':
        LLM = ChatGroq(model='openai/gpt-oss-20b')
    else:
        LLM = ChatOllama(model='llama3.2')
    chain = prompt | LLM | StrOutputParser()
    chatbot = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key='query',
    history_messages_key='history'
    )
    return chatbot.invoke({'query':question},
                config={'configurable':{'session_id':'shrey123'}})

if st.button('Answer'):
    if query and model_type:
        res = get_answer(query,model_type)
        st.write(res)

for i in st.session_state.store['shrey123']:
    st.write(i)
