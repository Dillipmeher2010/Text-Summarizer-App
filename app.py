import streamlit as st
from transformers import pipeline
import PyPDF2
from docx import Document
import io

# Load summarizer pipeline (Specify your model here)
summarizer = pipeline("summarization", model="google/gemini-xx-xxx")  # Replace with your Gemini model

# Function to read PDF content
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to read Word file content
def read_word(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

# Sidebar options
st.sidebar.title("Text Summarizer")
input_option = st.sidebar.selectbox("Select input method", ["Paste Text", "Upload PDF", "Upload Word File"])

# Handling user input
if input_option == "Paste Text":
    text = st.text_area("Enter text to summarize", height=250)

elif input_option == "Upload PDF":
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        text = read_pdf(uploaded_file)

elif input_option == "Upload Word File":
    uploaded_file = st.file_uploader("Choose a Word file", type=["docx"])
    if uploaded_file is not None:
        text = read_word(uploaded_file)

# Displaying summary
if text:
    st.subheader("Original Text")
    st.write(text)
    
    # Summarize the text
    try:
        summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
        st.subheader("Summary")
        st.write(summary[0]['summary_text'])
    except Exception as e:
        st.error(f"Error summarizing text: {e}")
