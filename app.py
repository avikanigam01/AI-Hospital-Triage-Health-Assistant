import streamlit as st
from components.sidebar import show_sidebar
import components.form_ui as form_ui
import components.chatbot_ui as chatbot_ui
import components.result_ui as result_ui

# Page Configuration
st.set_page_config(
    page_title="AI Hospital Triage Health Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
patient_data = show_sidebar()

# Main Dashboard
st.title("🏥 AI Hospital Triage Health Assistant")

st.markdown("""
Welcome to the AI-powered Hospital Triage System.

This system helps analyze patient symptoms and predict the possible disease with the help of Artificial Intelligence.
""")

st.divider()

st.subheader("📋 Patient Prediction")

if patient_data["predict"]:
    st.success("Prediction Started...")

    st.write("### Patient Details")

    st.write(patient_data)

else:
    st.info("Please fill the patient details from the sidebar and click **Predict Disease**.")