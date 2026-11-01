from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableSequence

prompt1 = PromptTemplate(template='Give me answer of this {query}',
                        input_variables=['query'])
prompt2 = PromptTemplate(template='Give me summary of this {query}',
                        input_variables=['query'])
prompt3 = PromptTemplate(template='Give me follow-up questions of {query}',
                        input_variables=['query'])

llm = ChatOllama(model='llama3.2')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'answer': prompt1 | llm | parser,
    'summary': prompt2 | llm | parser,
    'follow_up': prompt3 | llm | parser,
})

prompt4 = PromptTemplate(
    template='''
    Combine all the following information and provide a well-organized response.
    Answer: {answer}
    Summary: {summary}
    Follow-up Questions: {follow_up}
    ''',
    input_variables=['answer', 'summary', 'follow_up']
)


chain_1 = prompt4 | llm | parser



# Runnables Basics

prompt5 = PromptTemplate(template='Explain in short {response}',
                         input_variables=['response'])

parallel_chain2 = RunnableParallel({
    'response': RunnablePassthrough(),
    'Explain': prompt5 | llm | parser
})

final_chain = RunnableSequence(parallel_chain,chain_1,parallel_chain2)
query = input('Enter the query: \n')
result = final_chain.invoke({'query':query})
print(result)