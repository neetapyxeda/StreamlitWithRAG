import streamlit as st
import openai


def get_response(conversation):
    # Send a message to the assistant
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    return response['choices'][0]['message']['content']


# web title
st.title("Message with AI")

# text input
text = st.text_input("Ask a Question")

if text:
    with st.status("Getting the response...."):
        convo = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{text}"}
        ]
        # get the response
        response = get_response(convo)
        st.write("Response: {}".format(response))
