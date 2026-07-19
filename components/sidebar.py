import streamlit as st

def show_sidebar():
    st.sidebar.title("🏥 AI Hospital Triage Assistant")

    st.sidebar.markdown(
        """
        This is an AI-powered hospital triage assistant that helps in assessing patient symptoms and providing recommendations.
        """
    )

    st.sidebar.markdown("---")

    st.sidebar.subheader("Navigation")