# pages/1_Login.py

import streamlit as st

# Hardcoded user credentials (for demo purpose)
USER_CREDENTIALS = {
    "admin": "admin123",
    "user1": "password1",
    "rahul": "data123"
}

st.title("Login Page")

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.login = True
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid credentials. Please try again.")
else:
    st.success("You are already logged in. Proceed to other pages from sidebar.")
