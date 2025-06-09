import streamlit as st
from utils import load_and_clean_excel
from llm_chain import ExcelChatChain

st.set_page_config(page_title="Excel Insight Chatbot", layout='wide')
st.title("Excel-Based Insights Chatbot")

uploaded = st.file_uploader("Upload an Excel file (.xlsx)", type=['xlsx'])

if uploaded:
    df = load_and_clean_excel(uploaded)
    st.success(f"Loaded spreadsheet: {df.shape[0]} rows, {df.shape[1]} columns.")

    question = st.text_input("Ask a question about your data...")

    if question:
        chain = ExcelChatChain(df)
        with st.spinner("Processing..."):
            answer = chain.query(question)
        st.markdown(f"**Answer:** {answer}")
