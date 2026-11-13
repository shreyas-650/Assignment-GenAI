
import streamlit as st
from huggingface_hub import InferenceClient

import os

st.title("GenAI Assistant")

token = st.secrets.get("HF_TOKEN", os.getenv("HF_TOKEN", ""))

model = "Qwen/Qwen2.5-7B-Instruct"

question = st.text_area("Enter your question")

if st.button("Generate Answer"):

    if not token:
        st.error("Please configure HF_TOKEN in Secrets.")

    elif question.strip():

        client = InferenceClient(api_key=token)

        with st.spinner("Generating response..."):

            response = client.chat_completion(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                max_tokens=500
            )

        st.subheader("AI Response")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a question.")



'''
# Done Deploying on Streamlit Cloud and HuggingFace Spaces
Task 3: Compare Deployment Platforms
1. Streamlit Cloud vs Hugging Face Spaces
- Streamlit Cloud is Used for deploying Python web apps and dashboards.
- Hugging Face Spaces is Used for deploying and showcasing AI/ML applications.
2. Pros & Cons
- Streamlit Cloudis Easy deployment and GitHub integration, but limited resources.
- Hugging Face Spaces is Great for AI projects and supports multiple SDKs, but Docker setup can be complex.
3. When to Use Which?
- Streamlit Cloud is For dashboards and Python web applications.
- Hugging Face Spaces is For AI/ML projects, LLM demos, and model showcasing.
'''