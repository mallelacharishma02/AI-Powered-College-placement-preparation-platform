import streamlit as st
from google import genai

st.title("🎤 AI Mock Interview")

st.write("Practice interview questions with AI.")

api_key = st.text_input(
    "Enter Gemini API Key",
    type="password"
)

topic = st.selectbox(
    "Choose Interview Topic",
    [
        "Python",
        "Java",
        "SQL",
        "DBMS",
        "Data Structures",
        "Web Development"
    ]
)

if "question" not in st.session_state:
    st.session_state.question = ""

if st.button("Generate Interview Question"):

    if not api_key:

        st.error("Please enter your Gemini API key.")

    else:

        try:

            client = genai.Client(api_key=api_key)

            prompt = f"""
            You are an AI placement interview assistant.

            Generate one interview question for a college student
            preparing for placements.

            Topic: {topic}

            Give only the interview question.
            """

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            st.session_state.question = response.text

        except Exception as e:

            st.error(f"Error: {e}")


if st.session_state.question:

    st.subheader("❓ Interview Question")

    st.info(st.session_state.question)

    answer = st.text_area(
        "✍️ Type your answer:",
        height=150
    )

    if st.button("Submit Answer"):

        if answer.strip():

            st.success("Answer submitted successfully! ✅")

            st.write("Your answer:")
            st.write(answer)

        else:

            st.warning("Please enter your answer.")


# Navigation buttons

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/coding.py",
        label="⬅️ Previous: Coding"
    )

with col2:

    st.page_link(
        "pages/resume.py",
        label="Next: Resume Analyzer ➡️"
    )