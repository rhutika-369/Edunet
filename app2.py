import streamlit as st

st.title("Welcome to basic streamlit app!")

age = st.slider("Select your age ", 1, 100)  # min - 1 yr and max - 100 yr
city = st.selectbox("Select your city",["Delhi","Mumbai","Nashik","Pune"]) 

if st.button("Show Details"):
    st.write("Age",age)
    st.write("City",city)