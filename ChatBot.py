
import streamlit as st
import google.generativeai as genai

api = 'AIzaSyA1TqyBmTqNskopy0IJJALmfyQp3GcUmGU'

st.title('Google AI Text Generator')

if api:
    genai.configure(api_key = api)
else:
    st.error('Your API Key Is Not Found')


def Generate_Text(text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)
    return response.text

#keep history
if 'messages' not in st.session_state:
    st.session_state.messages = []
#display all messages
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if user_input := st.chat_input('Please Enter Your Text'):
    with st.chat_message('user'):
        st.markdown(user_input)

    st.session_state.messages.append({'role' : 'uesr', 'content' : user_input})

    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        with st.spinner('Generating Response.........'):
            response_text = Generate_Text(user_input)
            message_placeholder.markdown(f'{response_text}')
    st.session_state.messages.append({'role' : 'assistant', 'content' : response_text})
