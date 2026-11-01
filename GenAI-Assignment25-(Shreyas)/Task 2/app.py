from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

domain = input('Enter the Hotel Name: ')
# query = input('Enter the Query: ')
template = ChatPromptTemplate([
    ('system','You are a professional hotel information assistant of {domain}'),
    ('human','Give me the detail of {query} in short no extra info in 50 words only')
]
)

LLM = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
# prompt = template.invoke({'domain':domain,'query':query})
# response = LLM.invoke(prompt)
# print(response.content)
while(True):
    query = input('Enter the Query: ')
    if query == 'exit':
        break
    prompt = template.invoke({'domain':domain,'query':query})
    response = LLM.invoke(prompt)
    print(response.content)
