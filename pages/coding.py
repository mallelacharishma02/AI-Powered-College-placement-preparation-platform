import streamlit as st
import io
import contextlib

st.title("💻 Coding Practice")

st.write("Practice Python coding questions for placements.")

question = st.selectbox(
    "Choose a Coding Question",
    [
        "Check whether a number is Even or Odd",
        "Find the largest of two numbers",
        "Reverse a String",
        "Check whether a number is Prime"
    ]
)

st.subheader("📝 Write Your Python Code")

code = st.text_area(
    "Enter your Python code:",
    height=250
)

if st.button("▶️ Run Code"):

    if not code.strip():

        st.warning("Please write some code first.")

    else:

        output = io.StringIO()

        try:

            with contextlib.redirect_stdout(output):
                exec(code)

            st.success("Code executed successfully! ✅")

            result = output.getvalue()

            if result:

                st.subheader("📤 Output")
                st.code(result)

            else:

                st.info("Code executed, but there is no output.")

        except Exception as e:

            st.error("❌ Error in your code")
            st.code(str(e))


# Navigation buttons

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/dashboard.py",
        label="🏠 Dashboard"
    )

with col2:

    st.page_link(
        "pages/interview.py",
        label="Next: AI Interview ➡️"
    )