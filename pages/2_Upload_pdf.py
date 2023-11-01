import streamlit as st
from pdf_utils import pdf_to_text
from pinecone_utils import upload_to_pinecone


# title
st.title("Upload Text Content of a PDF File")

pdf_file = st.file_uploader("Upload a pdf file", accept_multiple_files = False, type = "pdf", help = "Upload a pdf file")

if pdf_file:
    # extract text from the pdf
    extracted_text = pdf_to_text(pdf_file)
    if extracted_text:
        st.toast("Text Extraction Completed...")

    # upload to pinecone
    with st.spinner("Uploading Texts"):
        response = upload_to_pinecone(extracted_text, pdf_file.name)
        if response:
            st.toast("Text Uploading Completed...")

    


        