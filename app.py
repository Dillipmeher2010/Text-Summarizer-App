import streamlit as st
from transformers import pipeline

# Load pre-trained model for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Streamlit app UI
st.title("Text Summarization App")

text_input = st.text_area("Enter Text to Summarize", "Paste your text here...")

if st.button("Summarize"):
    if text_input:
        summary = summarizer(text_input, max_length=150, min_length=50, do_sample=False)
        st.write("Summary: ")
        st.write(summary[0]['summary_text'])
    else:
        st.write("Please enter text to summarize.")
