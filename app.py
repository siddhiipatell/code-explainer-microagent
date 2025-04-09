import streamlit as st
from utils.explainer_util import explain_code
from utils.refactor_util import suggest_improvements

st.set_page_config(page_title="Code Explainer Agent", layout="centered")
st.title("🤖 Code Explainer Agent")
st.markdown("Paste your code below and get an instant explanation + improvement tips!")

code_input = st.text_area("🧾 Paste your code here:", height=300)

if code_input:
    with st.spinner("🔍 Explaining your code..."):
        explanation = explain_code(code_input)
        st.subheader("📘 Code Explanation")
        st.markdown(explanation)

    with st.spinner("💡 Suggesting improvements..."):
        suggestions = suggest_improvements(code_input)
        st.subheader("🛠 Suggestions")
        st.markdown(suggestions)

    st.success("✅ Done! You can now copy or save the results.")
