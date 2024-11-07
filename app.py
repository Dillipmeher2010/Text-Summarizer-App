import pdfplumber

# Path to your PDF file
pdf_path = 'your_pdf_file.pdf'

# Open the PDF with pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    # Extract text from the first page
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    
    # Print the extracted text
    print(text)
