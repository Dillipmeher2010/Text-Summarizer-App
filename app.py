import streamlit as st
import pdfplumber

# File upload widget for PDF files in Streamlit
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Open the uploaded PDF file using pdfplumber
    with pdfplumber.open(uploaded_file) as pdf:
        # Extract text from the first page of the PDF
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        
        # Display the extracted text in Streamlit
        st.write("Extracted Text from PDF:")
        st.text(text)
