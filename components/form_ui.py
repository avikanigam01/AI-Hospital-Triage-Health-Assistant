import streamlit as st

def show_form():

    st.title("🏥 AI Hospital Triage Assistant")

    name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120
    )

    gender = st.selectbox(
        "Gender",
        ["Male","Female","Other"]
    )

    if st.button("Submit"):

        st.success("Form Submitted")