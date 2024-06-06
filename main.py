import streamlit as st


# Beginning of the program
# Allows the user to input the target values that they want to maintain
# Stores the values for later use in the program
def inputData():
    # User inputs the desired temperature and stores the value
    temp = st.text_input("Enter the Target Temperature:")
    st.write(f"Temperature: {temp} °C")

    # User inputs the desired pH value and stores the value
    pH = st.text_input("Enter the Target pH:")
    st.write(f"pH: {pH}")

    # User inputs the desired flow rate and stores the value
    flowRate = st.text_input("Enter the Target Flow Rate:")
    st.write(f"Flow Rate: {flowRate}")


# Start of the program, calls all the functions
if __name__ == "__main__":
    # Sets up session state which is used to manage the UI content
    if 'key' not in st.session_state:
        st.session_state.key = 0

    if st.session_state.key == 0:
        inputData()
