import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Performance Analytics")

st.write("Track your placement preparation progress.")

data = {
    "Subject": [
        "Aptitude",
        "Technical",
        "Coding",
        "Interview"
    ],

    "Score": [
        80,
        70,
        65,
        75
    ]
}

df = pd.DataFrame(data)

st.subheader("📈 Your Performance")

fig = px.bar(
    df,
    x="Subject",
    y="Score",
    title="Preparation Performance"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📋 Performance Details")

st.dataframe(
    df,
    use_container_width=True
)

average = df["Score"].mean()

st.metric(
    "Overall Average",
    f"{average:.1f}%"
)

if average >= 75:

    st.success(
        "🎉 Excellent performance! Keep it up!"
    )

elif average >= 50:

    st.info(
        "👍 Good progress! Keep practicing."
    )

else:

    st.warning(
        "📚 More practice is recommended."
    )


st.divider()

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/resume.py",
        label="⬅️ Previous: Resume"
    )

with col2:
    st.page_link(
        "pages/dashboard.py",
        label="🏠 Back to Dashboard"
    )