import streamlit as st
import google.generativeai as genai

st.title("Welcome to my genai application!!!")

user = st.text_input("Ask me anything!")

genai.configure(api_key="AIzaSyDspE7CCk_QywF7-jwZsnJc5TEktukE6wo")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user :
    response = model.generate_content(user)
    st.write("Response from genai")
    st.write(response.text)