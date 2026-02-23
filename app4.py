import streamlit as st

st.title("Simple Chatbot")

question = st.text_input("Ask me anything")

if st.button("Send"):
    st.write("You asked", question)
    st.write("Chatbot is in the process, I will reply soon")