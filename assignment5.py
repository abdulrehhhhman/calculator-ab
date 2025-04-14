import streamlit as st

# Function to handle calculator operations
def calculate(expression):
    try:
        result = eval(expression)
    except:
        result = "Error"
    return result

# Initialize session state for storing the expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to update expression
def update_expression(value):
    st.session_state.expression += str(value)

# Create the calculator layout
st.title("Streamlit Calculator")

# Create a container for the expression display
st.text_input("Expression", value=st.session_state.expression, disabled=True, key="display", label_visibility="collapsed")

# Create columns for buttons
col1, col2, col3 = st.columns([1, 1, 1])

# First row of buttons (numbers 7, 8, 9 and operators)
with col1:
    if st.button("7"): update_expression(7)
with col2:
    if st.button("8"): update_expression(8)
with col3:
    if st.button("9"): update_expression(9)

with col1:
    if st.button("+"): update_expression('+')
with col2:
    if st.button("-"): update_expression('-')
with col3:
    if st.button("*"): update_expression('*')

# Second row of buttons (numbers 4, 5, 6 and operators)
with col1:
    if st.button("4"): update_expression(4)
with col2:
    if st.button("5"): update_expression(5)
with col3:
    if st.button("6"): update_expression(6)

with col1:
    if st.button("/"): update_expression('/')
with col2:
    if st.button("Clear"): st.session_state.expression = ""
with col3:
    if st.button("="):
        result = calculate(st.session_state.expression)
        st.text(f"Result: {result}")

# Third row of buttons (numbers 1, 2, 3 and operator)
with col1:
    if st.button("1"): update_expression(1)
with col2:
    if st.button("2"): update_expression(2)
with col3:
    if st.button("3"): update_expression(3)

# Fourth row of buttons (number 0)
with col1:
    if st.button("0"): update_expression(0)

# Add keyboard input functionality
import streamlit.components.v1 as components

components.html("""
    <script type="text/javascript">
    window.addEventListener("keydown", function(e) {
        var key = e.key;
        var validKeys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "Enter", "Backspace"];
        if (validKeys.includes(key)) {
            window.parent.postMessage(key, "*");
        }
    });
    </script>
""")

# Handle keyboard input
import json

# Check for key press messages from JavaScript
key = st.experimental_get_query_params().get("key", None)

if key:
    key = key[0]
    # Handle backspace for deletion
    if key == "Backspace":
        st.session_state.expression = st.session_state.expression[:-1]
    # Handle Enter for calculation
    elif key == "Enter":
        result = calculate(st.session_state.expression)
        st.text(f"Result: {result}")
    else:
        update_expression(key)

# Display the expression
st.text(f"Expression: {st.session_state.expression}")
