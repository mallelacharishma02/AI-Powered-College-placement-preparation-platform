import streamlit as st
from google import genai

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and get AI-powered suggestions.")

api_key = st.text_input(
    "Enter Gemini API Key",
    type="password"
)

resume_text = st.text_area(
    "Paste your Resume Text Here",
    height=300
)

if st.button("Analyze Resume"):

    if not api_key:

        st.error("Please enter your Gemini API key.")

    elif not resume_text:

        st.warning("Please enter your resume text.")

    else:

        try:

            client = genai.Client(api_key=api_key)

            prompt = f"""
            You are an AI Resume Analyzer for college students
            preparing for placements.

            Analyze the following resume:

            {resume_text}

            Give the analysis in this format:

            1. Resume Summary
            2. Skills Found
            3. Strengths
            4. Missing or Recommended Skills
            5. Resume Improvement Suggestions
            6. Overall Resume Score out of 100

            Keep the explanation simple and useful.
            """

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            st.success("Resume Analysis")

            st.write(response.text)

        except Exception as e:

            st.error(f"Error: {e}")


st.divider()

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/interview.py",
        label="⬅️ Previous: AI Interview"
    )

with col2:
    st.page_link(
        "pages/analytics.py",
        label="Next: Analytics ➡️"
    )