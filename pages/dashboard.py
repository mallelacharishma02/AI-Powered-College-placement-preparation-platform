import streamlit as st

st.title("🎓 Student Dashboard")

st.write("Welcome to your Placement Preparation Dashboard!")

st.subheader("📚 Preparation Sections")

st.page_link("pages/aptitude.py", label="🧮 Aptitude Practice")
st.page_link("pages/technical.py", label="💻 Technical Preparation")
st.page_link("pages/coding.py", label="👨‍💻 Coding Practice")
st.page_link("pages/interview.py", label="🎤 AI Mock Interview")
st.page_link("pages/resume.py", label="📄 Resume Analyzer")
st.page_link("pages/analytics.py", label="📊 Performance Analytics")

st.success("Choose a section above to start your preparation! 🚀")