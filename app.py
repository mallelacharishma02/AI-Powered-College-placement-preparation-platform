import streamlit as st
from database import create_database

# Create database
create_database()

st.set_page_config(
    page_title="AI Placement Preparation",
    page_icon="🎓"
)

st.title("🎓 AI-Powered College Placement Preparation Platform")

st.write("Welcome to our AI Placement Preparation Platform!")

st.header("Prepare for Your Placements")

st.write(
    "Practice Aptitude, Technical Questions, Coding and Interviews."
)

st.page_link(
    "pages/login.py",
    label="🚀 Start Preparation"
)