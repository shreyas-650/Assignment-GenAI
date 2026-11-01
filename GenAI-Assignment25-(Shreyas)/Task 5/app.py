from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

LLM = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
prompt = PromptTemplate(template='Give me recipy of {query} in 10 words',
                        input_variables=['query'])
query = 'Dal Khichadi'
parser = StrOutputParser()

chain = prompt | LLM | parser
response = chain.invoke({'query':query})

print(response)