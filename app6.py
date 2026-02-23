import streamlit as st

st.title("Form Page")

first_name = st.text_input("Enter your first name : ")
last_name = st.text_input("Enter your last name : ")
age = st.slider("Select your age : ", 1, 90)
dob = st.number_input("Enter you birth date : ")

if st.button("Show Details"):
    st.write("Name : ",first_name+last_name)
    st.write("Age : ",age)
    st.write("Date of Birth : ",dob)