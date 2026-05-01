import streamlit as st

st.title("🎓 Student Marks Predictor (AI Demo)")

# Inputs
hours = st.slider("📘 Study Hours", 0, 12, 5)
sleep = st.slider("😴 Sleep Hours", 0, 12, 7)
attendance = st.slider("🏫 Attendance (%)", 0, 100, 75)

# Prediction logic (simple but effective)
if st.button("Predict Marks"):
    marks = (hours * 5) + (sleep * 2) + (attendance * 0.5)

    st.success(f"📊 Predicted Marks: {marks:.2f}")
