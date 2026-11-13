
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load Hugging Face Model
llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-base",
    task="text2text-generation",
    pipeline_kwargs={
        "max_new_tokens": 128,
        "do_sample": False
    }
)

print("Model Loaded Successfully!")

# 2. Standard PromptTemplate
prompt = PromptTemplate.from_template(
    "Answer clearly and simply.\n"
    "Question: {question}\n"
    "Answer:"
)

# Create LLM Chain
chain = prompt | llm | StrOutputParser()

# 3. Test with Multiple Prompts
questions = [
    "Explain gradient descent.",
    "What is machine learning?",
    "Explain Python lists and tuples.",
    "What is cloud computing?"
]

for question in questions:
    response = chain.invoke({"question": question})
    print("\nQuestion:", question)
    print("Answer:", response)


# 4. ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI tutor. Give simple answers."),
    ("human", "{question}")
])

chat_chain = chat_prompt | llm | StrOutputParser()
response = chat_chain.invoke({
    "question": "What is an API?"
})

print("\nChatPromptTemplate Output:")
print(response)


# 5. Compare Both Prompt Templates
question = "Explain the importance of data structures."
normal_output = chain.invoke({"question": question})
chat_output = chat_chain.invoke({"question": question})
print("\nStandard PromptTemplate:")
print(normal_output)

print("\nChatPromptTemplate:")
print(chat_output)

# 6. Display Prompt Formats
print("\nFormatted Standard Prompt:")
print(prompt.format(question="What is Python?"))

print("\nFormatted Chat Prompt:")
print(chat_prompt.format_messages(
    question="What is Python?"
))
