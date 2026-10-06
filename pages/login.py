import streamlit as st
from database import register_student, login_student

st.title("🔐 Student Login")

option = st.radio(
    "Choose an option",
    ["Login", "Register"]
)

username = st.text_input("Username")
password = st.text_input("Password", type="password")


# REGISTER
if option == "Register":

    if st.button("Register"):

        if username and password:

            result = register_student(username, password)

            if result:
                st.success("Registration successful! 🎉")
                st.info("Now select Login and enter your details.")

            else:
                st.error("Username already exists.")

        else:
            st.warning("Please enter username and password.")


# LOGIN
else:

    if st.button("Login"):

        if username and password:

            student = login_student(username, password)

            if student:
                st.success("Login successful! 🎉")
                st.write("Welcome,", username)

                st.page_link(
                    "pages/dashboard.py",
                    label="🎓 Go to Dashboard"
                )

            else:
                st.error("Invalid username or password.")

        else:
            st.warning("Please enter username and password.")