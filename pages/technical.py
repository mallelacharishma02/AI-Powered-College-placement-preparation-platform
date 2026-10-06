import streamlit as st

st.title("💻 Technical Preparation")

st.write("Prepare technical questions for placement interviews.")

topic = st.selectbox(
    "Choose a Technical Topic",
    [
        "Python",
        "Java",
        "C Programming",
        "DBMS",
        "Data Structures",
        "Operating Systems",
        "Computer Networks",
        "SQL"
    ]
)

questions = {
    "Python": [
        "What is Python?",
        "What are lists and tuples in Python?",
        "What is the difference between == and is?"
    ],

    "Java": [
        "What is Java?",
        "What is OOP?",
        "What is inheritance?"
    ],

    "C Programming": [
        "What is a pointer?",
        "What is an array?",
        "What is a structure?"
    ],

    "DBMS": [
        "What is a database?",
        "What is a primary key?",
        "What is normalization?"
    ],

    "Data Structures": [
        "What is an array?",
        "What is a stack?",
        "What is a queue?"
    ],

    "Operating Systems": [
        "What is an operating system?",
        "What is a process?",
        "What is deadlock?"
    ],

    "Computer Networks": [
        "What is a computer network?",
        "What is an IP address?",
        "What is TCP?"
    ],

    "SQL": [
        "What is SQL?",
        "What is a SELECT statement?",
        "What is a JOIN?"
    ]
}

st.subheader(f"📚 {topic} Questions")

for i, question in enumerate(questions[topic], 1):

    st.write(f"**{i}. {question}**")


st.info("💡 Practice these questions before attending technical interviews.")


st.divider()

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/aptitude.py",
        label="⬅️ Previous: Aptitude"
    )

with col2:
    st.page_link(
        "pages/coding.py",
        label="Next: Coding ➡️"
    )