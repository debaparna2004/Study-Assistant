import streamlit as st
from llm import ask_llm


st.title("AI Study Assistant")
st.write("Let's make concepts smooth with AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("What do you wanna study?")
if question:
    answer = ask_llm(question)
    st.write(answer)

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    
