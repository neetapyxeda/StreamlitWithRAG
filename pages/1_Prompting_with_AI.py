import streamlit as st
import openai


SYSTEM_MESSAGE={"role": "system", 
                "content": "Ignore all previous commands. You are a helpful and patient guide."
                }

def get_response(conversation):
    # Send a message to the assistant
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    return response['choices'][0]['message']['content']

# session states
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SYSTEM_MESSAGE)

# set title
st.title("Message with Prompt Engineering")

# text input
text = st.text_input("Set a Prompt", help = "Prompt Engineering")

if text:
    st.session_state.messages.append({
        "role": "user",
        "content": f"{text}"
    })

    with st.status("Getting the response...."):
        # get the response
        response = get_response(st.session_state.messages)
        st.session_state.messages.append({
            "role": "system",
            "content": f"{response}"
        })
        st.write("Response: {}".format(response))
