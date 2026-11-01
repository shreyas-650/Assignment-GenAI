from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st
load_dotenv()

st.title('RGC Prompting')
role = st.selectbox('Select the Role',['AI Engineer','Data Scientist','Web Developer','Data Analytics'])
goal = st.text_input('Enter the Goal')
context = st.text_area('Context')

template = PromptTemplate(template="""
You are a senior {role}, and your goal is to {goal} in your mind, and your task is to {context}

""",
input_variables=['role','goal','context'],
validate_template=True
)
prompt = template.invoke({'role':role,'goal':goal,'context':context})

LLM = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


if st.button('Answer'):
    response = LLM.invoke(prompt)
    st.write(response.content)