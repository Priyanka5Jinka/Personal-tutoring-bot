import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import json

with open('cred.json', 'r') as f:
    file = json.load(f)
    token = file['token']

# Title of the streamlit app
st.title('Personal tutoring bot!')


# function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response


# Function to receive user queries
def get_text():
    input_text = st.text_input("My bot:", "   ", key='input')
    return input_text


# url = 'https://images.unsplash.com/photo-1499750310107-5fef28a66643?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2670&q=80'
# data-testid="stAppViewContainer"

changes = '''
<style>
[data-testid="stAppViewContainer"]
        {
        background-image:url('https://images.unsplash.com/photo-1499750310107-5fef28a66643?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2670&q=80');
        background-size:cover;
        }
        html{
        background:transaprent
        }
        div.esravye2 > iframe
        {
        background:transparent
        }
</style>
'''
st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Accepting user input
user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key='user_' + str(i), is_user=True)
