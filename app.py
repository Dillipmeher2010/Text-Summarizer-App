import streamlit as st
from transformers import pipeline
import PyPDF2
import docx

# Initialize text summarizer using HuggingFace's pipeline (or your Gemini model's API)
summarizer = pipeline("summarization")

# Title of the app
st.title("Text Summarizer App")

# Option to upload PDF or Word file or paste text
option = st.selectbox("Choose how to input text", ["Upload PDF/Word File", "Paste Text"])

if option == "Upload PDF/Word File":
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        # If PDF is uploaded
        if uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        
        # If Word file is uploaded
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(uploaded_file)
            text = ""
            for para in doc.paragraphs:
                text += para.text
        
        # Show the extracted text (optional)
        st.subheader("Extracted Text")
        st.text_area("Extracted Text", text, height=200)

elif option == "Paste Text":
    text_input = st.text_area("Paste your text here", height=200)

    # Summarization when text is pasted
    if text_input:
        summary = summarizer(text_input, max_length=200, min_length=50, do_sample=False)
        st.subheader("Summary")
        st.write(summary[0]["summary_text"])

# Button to summarize the extracted text or pasted text
if uploaded_file or text_input:
    if option == "Upload PDF/Word File":
        st.button("Summarize", on_click=lambda: summarize_text(text))
    else:
        st.button("Summarize", on_click=lambda: summarize_text(text_input))

def summarize_text(input_text):
    if input_text:
        summary = summarizer(input_text, max_length=200, min_length=50, do_sample=False)
        st.subheader("Summary")
        st.write(summary[0]["summary_text"])
    else:
        st.error("Please provide some text to summarize.")
