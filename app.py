import streamlit as st

from components.form_ui import show_form
from components.chatbot_ui import show_chatbot
from components.result_ui import show_result
from components.sidebar import show_sidebar

st.set_page_config(
    page_title="AI Hospital Triage",
    page_icon="🏥",
    layout="wide"
)

show_sidebar()
show_form()
show_chatbot()
show_result()
