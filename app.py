import streamlit as st
import numpy as np
from tensorflow import keras

st.title("🎓 Student Marks Predictor")

# -----------------------------
# Train Model (runs once)
# -----------------------------
@st.cache_resource
def train_model():
    x = np.array([
        [1, 6, 60],
        [2, 7, 65],
        [3, 6, 70],
        [4, 7, 75],
        [5, 8, 80],
        [6, 7, 85],
        [7, 8, 90],
        [8, 8, 95]
    ], dtype=float)

    y = np.array([35, 40, 50, 55, 65, 70, 80, 90], dtype=float)

    # Normalize
    x[:,0] /= 10
    x[:,1] /= 10
    x[:,2] /= 100
    y /= 100

    model = keras.Sequential([
        keras.layers.Dense(16, activation='relu', input_shape=[3]),
        keras.layers.Dense(8, activation='relu'),
        keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(x, y, epochs=300, verbose=0)

    return model

model = train_model()

# -----------------------------
# UI Inputs
# -----------------------------
hours = st.slider("📘 Study Hours", 0, 12, 5)
sleep = st.slider("😴 Sleep Hours", 0, 12, 7)
attendance = st.slider("🏫 Attendance (%)", 0, 100, 75)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Marks"):
    input_data = np.array([[hours/10, sleep/10, attendance/100]])
    prediction = model.predict(input_data)

    marks = prediction[0][0] * 100

    st.success(f"📊 Predicted Marks: {marks:.2f}")
