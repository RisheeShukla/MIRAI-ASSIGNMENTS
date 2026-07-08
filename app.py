import streamlit as st
def calculator():
    import streamlit as st
    st.title("🧮  :rainbow[Simple Calculator]")
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate button
    if st.button("Calculate"):
     if operation == "Addition":
         result = num1 + num2
     elif operation == "Subtraction":
         result = num1 - num2
     elif operation == "Multiplication":
         result = num1 * num2
     elif operation == "Division":
         if num2 != 0:
             result = num1 / num2
         else:
             result = "Error: Division by zero is not allowed."

     st.success(f"Result: {result}")

def profile():
    import streamlit as st
    st.title("👤  :rainbow[User Profile]")
    st.write("Name : :rainbow[Rishee Shukla]")
    st.write("Age : :rainbow[19]")
    st.write("Bio : :rainbow[MERN FullStack Developer]")



pages={
     "Calculator": calculator,
     "Profile": profile}
   

page=st.sidebar.selectbox("Select a page",pages.keys()) 
pages[page]()