import pdfplumber

def extract_text_from_pdf(pdf_path):
    print("Opening:", pdf_path)

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        print("Pages:", len(pdf.pages))

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    print("Characters:", len(text))

    return text