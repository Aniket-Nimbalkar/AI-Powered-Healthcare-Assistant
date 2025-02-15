import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

if __name__ == "__main__":
    pdf_text = extract_text_from_pdf("medical_book.pdf")
    with open("medical_data.txt", "w", encoding="utf-8") as f:
        f.write(pdf_text)
    print("Medical book data extracted and saved!")
