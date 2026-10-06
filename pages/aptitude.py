import streamlit as st

st.title("🧮 Aptitude Practice")

st.write("Practice aptitude questions for placements.")

q1 = st.radio(
    "1. What is 20% of 150?",
    ["20", "25", "30", "35"]
)

q2 = st.radio(
    "2. What is 15 + 25?",
    ["30", "35", "40", "45"]
)

q3 = st.radio(
    "3. What is 12 × 5?",
    ["50", "60", "70", "80"]
)

if st.button("Submit Test"):

    score = 0

    if q1 == "30":
        score += 1

    if q2 == "40":
        score += 1

    if q3 == "60":
        score += 1

    st.success(f"🎉 Your Score: {score}/3")


st.divider()

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/dashboard.py",
        label="🏠 Dashboard"
    )

with col2:
    st.page_link(
        "pages/technical.py",
        label="Next: Technical ➡️"
    )