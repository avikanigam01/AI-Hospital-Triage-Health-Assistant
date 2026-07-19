import streamlit as st

def show_home():

    st.title("🏥 AI Hospital Triage Health Assistant")

    st.markdown("""
    ### Welcome to the AI-Powered Hospital Triage System

    This intelligent healthcare assistant analyzes patient symptoms
    and predicts the urgency of medical attention using Artificial Intelligence.
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🤖 AI Diagnosis")
        st.write(
            "Analyze patient symptoms using Machine Learning."
        )

    with col2:
        st.info("⚡ Fast Prediction")
        st.write(
            "Receive instant disease prediction within seconds."
        )

    with col3:
        st.info("🏥 Hospital Recommendation")
        st.write(
            "Get the appropriate department based on the prediction."
        )

    st.divider()

    st.subheader("📋 How it Works")

    st.write("""
    1. Fill the patient details in the sidebar.
    2. Click **Predict Disease**.
    3. AI analyzes the information.
    4. View the prediction and recommendation.
    """)