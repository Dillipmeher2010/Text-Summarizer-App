import streamlit as st
from transformers import pipeline

# Streamlit app title
st.title("Text Summarization App")

# Text input from the user
st.write("Enter the text you want to summarize:")

# Create a text area for the user to input text
input_text = st.text_area("Text Input", height=300)

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Process the input text and generate the summary when the button is clicked
if st.button("Summarize"):
    if input_text.strip() != "":
        summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
