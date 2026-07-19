import streamlit as st

def show_sidebar():

    st.sidebar.title("🩺 Patient Assessment")

    st.sidebar.markdown("---")

    age = st.sidebar.number_input(
        "What is your age?",
        min_value=0,
        max_value=120,
        value=18
    )

    temperature = st.sidebar.number_input(
        "What is your current body temperature (°C)?",
        min_value=30.0,
        max_value=45.0,
        value=37.0,
        step=0.1
    )

    heart_rate = st.sidebar.number_input(
        "What is your current heart rate (beats per minute)?",
        min_value=30,
        max_value=220,
        value=72
    )

    pain = st.sidebar.slider(
        "On a scale of 0–10, how severe is your pain?",
        min_value=0,
        max_value=10,
        value=0
    )

    symptom = st.sidebar.selectbox(
        "What is your primary symptom?",
        [
            "Fever",
            "Headache",
            "Chest Pain",
            "Cough",
            "Shortness of Breath",
            "Abdominal Pain",
            "Vomiting",
            "Dizziness",
            "Fatigue",
            "Sore Throat"
        ]
    )

    days = st.sidebar.number_input(
        "For how many days have you been experiencing this symptom?",
        min_value=0,
        max_value=365,
        value=1
    )

    st.sidebar.markdown("---")

    predict = st.sidebar.button(
        "🩺 Analyze Patient",
        use_container_width=True
    )

    return {
        "age": age,
        "temperature": temperature,
        "heart_rate": heart_rate,
        "pain": pain,
        "symptom": symptom,
        "days": days,
        "predict": predict
    }