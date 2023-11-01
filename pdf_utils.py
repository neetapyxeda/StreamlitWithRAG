import PyPDF2


def pdf_to_text(uploaded_file):
    """
    extract text from a given pdf file in ByteIO

    @params
    uploaded_file: pdf file in ByteIO format

    @return
    extracted text from the pdf
    """
    pdfReader = PyPDF2.PdfReader(uploaded_file)
    no_pages = len(pdfReader.pages)
    text=""
    for page_index in range(no_pages):
        page = pdfReader.pages[page_index]
        text=text+page.extract_text()
    return text