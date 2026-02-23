import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter your first number :", step=1, format="%d")
num2 = st.number_input("Enter your second number :", step=1, format="%d")

operation = st.selectbox("Choose Option",["ADD","SUB","MUL","DIV"])

if st.button("Calculate"):
    if operation == "ADD":
        st.write(int(num1+num2))
    elif operation == "SUB":
        st.write(int(num1-num2))
    elif operation == "MUL":
        st.write(int(num1*num2))
    elif operation == "DIV":
        if num2!=0:
            st.write(int(num1/num2))
        else:
            st.write("Oops cannot divide denominator by 0") 
