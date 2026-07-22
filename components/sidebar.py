import streamlit as st


def show_sidebar():

    st.sidebar.markdown(
        """
        <h2 style='text-align:center;'>🩺 Patient Assessment</h2>
        <p style='text-align:center;color:gray;font-size:14px;'>
        Please complete the form below
        </p>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("---")

    # ---------------- Patient Information ---------------- #

    st.sidebar.markdown("### 👤 Patient Information")

    age = st.sidebar.select_slider(
        "Age",
        options=list(range(0, 121)),
        value=25
    )

    gender = st.sidebar.radio(
        "Gender",
        ["Male", "Female"],
        horizontal=True
    )

    st.sidebar.markdown("---")

    # ---------------- Vital Signs ---------------- #

    st.sidebar.markdown("### ❤️ Vital Signs")

    temperature = st.sidebar.slider(
        "Body Temperature (°C)",
        34.0,
        42.0,
        37.0,
        0.1
    )

    heart_rate = st.sidebar.slider(
        "Heart Rate (BPM)",
        40,
        180,
        72
    )

    pain = st.sidebar.slider(
        "Pain Level",
        0,
        10,
        3,
        help="0 = No Pain, 10 = Worst Pain"
    )

    st.sidebar.markdown("---")

    # ---------------- Symptoms ---------------- #

    st.sidebar.markdown("### 🤒 Symptoms")

    symptom = st.sidebar.selectbox(
        "Primary Symptom",
        [
            "Fever",
            "Cough",
            "Headache",
            "Chest Pain",
            "Breathing Difficulty",
            "Vomiting",
            "Abdominal Pain",
            "Dizziness"
        ]
    )

    days = st.sidebar.select_slider(
        "Duration (Days)",
        options=list(range(1, 31)),
        value=2
    )

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    predict = st.sidebar.button(
        "🩺 Analyze Patient",
        use_container_width=True,
        type="primary"
    )

    return {

        "age": age,
        "gender": gender,
        "temperature": temperature,
        "heart_rate": heart_rate,
        "pain": pain,
        "symptom": symptom,
        "days": days,
        "predict": predict

    }