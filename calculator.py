import streamlit as st

st.title("Welcome to Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operator = st.radio("Select any operator:", ("add", "sub", "mul", "div"))

if st.button('Click here'):
    if operator == "add":
        result = num1 + num2
        st.subheader(f"Result: {result}")
    elif operator == "sub":
        result = num1 - num2
        st.subheader(f"Result: {result}")
    elif operator == "mul":
        result = num1 * num2
        st.subheader(f"Result: {result}")
    elif operator == "div":
        if num2 != 0:
            result = num1 / num2
            st.subheader(f"Result: {result}")
        else:
            st.error("Cannot divide by zero!")
