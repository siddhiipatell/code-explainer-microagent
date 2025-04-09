from llm_utils import call_ollama_api
import streamlit as st

def suggest_improvements(code: str):
    prompt = f"""Review this code and suggest improvements. Include clean code tips, performance suggestions, and naming advice:\n\n```python\n{code}\n```"""
    model = st.secrets["OLLAMA_MODEL"]

    response = call_ollama_api(
        model=model, 
        messages=[{"role": "user", "content": prompt}],
        )
        
    return response
