
import streamlit as st
import ollama

st.title("CodeLlama AI Code Assistant")

# Task 3: Code Assistant Functions

def generate_code(text):
    return f"Generate clean Python code for: {text}"

def explain_code(text):
    return f"Explain this code step by step:\n{text}"

def debug_code(text):
    return f"Find bugs and provide corrected code:\n{text}"

def optimize_code(text):
    return f"Optimize this code and explain improvements:\n{text}"


# Task 5: Prompt Templates
prompts = {
    "Generate Code": generate_code,
    "Explain Code": explain_code,
    "Debug Code": debug_code,
    "Optimize Code": optimize_code
}

# Task 4: Streamlit Interface

task = st.selectbox(
    "Select Task",
    list(prompts.keys())
)

user_input = st.text_area(
    "Enter your prompt or code",
    placeholder="Example: Write a Python function to check prime numbers"
)

if st.button("Submit"):

    if user_input.strip():

        prompt = f"""
        You are an expert Python coding assistant.

        {prompts[task](user_input)}

        Provide a clear, structured and readable response.
        Use properly formatted Python code where needed.
        """

        with st.spinner("CodeLlama is thinking..."):

            response = ollama.chat(
                model="codellama:7b",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        st.subheader("CodeLlama Response")
        st.markdown(response["message"]["content"])

    else:
        st.warning("Please enter a prompt or code.")
