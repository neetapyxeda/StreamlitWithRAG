import streamlit as st
from pinecone_utils import upload_to_pinecone
from youtube_utils import get_youtube_transcript


def validate_url(url: str) -> bool:
    if (url.startswith("https://") or url.startswith("http://")):
        return True
    
    return False

# title
st.title("Upload YouTube Transcript")

# text input field
youtube_link = st.text_input("Enter a youtube link")

if youtube_link:
    validation = validate_url(youtube_link)
    if not validation:
        st.error("Invaid URL", icon="🚨")
    else:
        transcript = get_youtube_transcript(youtube_link)

        if not transcript:
            st.error("Cannot Extract Transcript for this Link", icon="🚨")

        else:
            with st.spinner("Uploading....."):
                response = upload_to_pinecone(transcript, youtube_link)

                if response:
                    st.toast("Text Embeddings uploaded to Pinecone")



