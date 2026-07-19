import streamlit as st

def show_chatbot():

    st.subheader("AI Chatbot")

    msg = st.chat_input("Ask your symptom")

    if msg:

        st.write(msg)
