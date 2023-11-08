from openai import OpenAI

def get_response(conversation):
    client = OpenAI(
        #api_key = st.secrets["OPENAI_API_KEY"]
        api_key = st.secrets["OPENAI_API_KEY"]
    )
    # Send a message to the assistant
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    return response.choices[0].message.content