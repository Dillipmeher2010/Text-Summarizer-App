import pdfplumber
import streamlit as st
from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    # Summarize the text using the pre-trained model
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Streamlit UI
st.title("PDF Text Summarizer")
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

if pdf_file is not None:
    with pdfplumber.open(pdf_file) as pdf:
        # Extract text from the first page (you can modify this to process all pages)
        first_page = pdf.pages[0]
        text = first_page.extract_text()

        if text:
            st.write("Extracted Text:")
            st.write(text)

            # Summarize the extracted text
            summary = summarize_text(text)
            st.write("Summary:")
            st.write(summary)
        else:
            st.write("No text found in the PDF.")
