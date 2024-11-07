import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader
import docx

# Initialize Google Gemini (this requires an API call, replace with correct implementation if needed)
summarizer = pipeline("summarization", model="google/gemini")  # Assuming Google Gemini is supported here.

# Function to extract text from a PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from a Word document
def extract_text_from_word(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Streamlit app layout
st.title("Text Summarization App")
st.write("Upload a PDF or Word document, or paste your text below:")

# Options for the user to provide input
input_method = st.radio("Choose how to provide text", ("Upload File", "Paste Text"))

if input_method == "Upload File":
    uploaded_file = st.file_uploader("Upload a PDF or Word document", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        # Extract text based on file type
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
            st.write("Extracted text from PDF:")
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_word(uploaded_file)
            st.write("Extracted text from Word document:")
        
        # Display the extracted text
        st.text_area("Extracted Text", value=text, height=300)

elif input_method == "Paste Text":
    text = st.text_area("Paste your text here:", height=300)

if text:
    # Summarize the provided text
    st.subheader("Summary:")
    try:
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        st.write(summary[0]["summary_text"])
    except Exception as e:
        st.error(f"An error occurred: {e}")

