from llm_utils import call_ollama_api
import streamlit as st
def explain_code(code: str):
    prompt = f"""Explain the following code in plain English. Be concise but thorough:\n\n```python\n{code}\n```"""
    model = st.secrets["OLLAMA_MODEL"]
    
    response = call_ollama_api(
        model=model, 
        messages=[{"role": "user", "content": prompt}],
        )
    
    return response