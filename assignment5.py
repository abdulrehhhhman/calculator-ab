import streamlit as st

st.title("Welcome to Calculator")

# Text inputs to take keyboard inputs for numbers
num1 = st.text_input("Enter first number", value="0")
num2 = st.text_input("Enter second number", value="0")

# Ensure the inputs are numeric
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    st.error("Please enter valid numbers.")

# Radio buttons to select the operator
operator = st.radio("Select any operator:", ("add", "sub", "mul", "div"))

# Button for calculating
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
