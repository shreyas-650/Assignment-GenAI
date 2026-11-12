'''
Task 1: Text-to-Math Agent Overview Answer briefly: 
1. What is a Text-to-Math problem? 
Text to math means the string of number we need to use for the math solving purpose.
2. Why agents are useful for math reasoning? 
It help to get the solution faster and has reasoning capablities which help to process natural language too
3. Difference between normal LLM response vs agent-based reasoning
LLM response is next word prediction while agent based reasoning choosed the right tool then uses it efficiently to solve the query.
'''

# Main Code

import streamlit as st
import numexpr
import re
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper

# Streamlit UI

st.title("Text To Math Problem Solver using Groq Llama")
groq_api = st.sidebar.text_input("Enter your Groq API Key", type="password")
if not groq_api:
    st.info("Please enter your Groq API Key")
    st.stop()

# LLM
model = ChatGroq(model="openai/gpt-oss-20b", groq_api_key=groq_api)

# Initialize Wikipedia
wiki = WikipediaAPIWrapper()
@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for information about a topic."""
    return wiki.run(query)

# Calculator Tool
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions like 25*40 or (100+50)/2."""
    try:
        result = numexpr.evaluate(expression, global_dict={}, local_dict={})
        return str(result)
    except Exception as e:
        return f"Calculation error: {e}"
    
# Create Agent
agent = create_agent(model=model, tools=[calculator, wikipedia_search], system_prompt="You are a helpful AI Math Assistant. Solve mathematical questions step by step. Use calculator for calculations. Use Wikipedia for factual information. Explain answers in simple language and provide the final answer clearly.")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I am your AI Math Chatbot. Ask me anything!"}]

# Display Chat History
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
question = st.chat_input("Enter your question...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    with st.spinner("Generating response..."):

        # Detect mathematical expressions
        math_match = re.search(r'\d+(?:\s*[+\-*/]\s*\d+)+', question)
        if math_match:
            # Force calculator tool usage
            expression = math_match.group()
            answer = calculator.invoke({"expression": expression})
            answer = f"Calculator Tool Used\n\nCalculation: {expression}\n\nAnswer: {answer}"
        else:
            # Using AI agent for other ques.
            response = agent.invoke({
                "messages": [{"role": "user", "content": question}]
            })
            answer = response["messages"][-1].content
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
