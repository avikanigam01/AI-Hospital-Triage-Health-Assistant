import streamlit as st
from backend.chatbot import chatbot_response


def show_chatbot(prediction=None):

    st.subheader("💬 AI Health Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for role, message in st.session_state.messages:
        with st.chat_message(role):
            st.write(message)

    user_message = st.chat_input("Ask a health-related question...")

    if user_message:

        st.session_state.messages.append(("user", user_message))

        with st.chat_message("user"):
            st.write(user_message)

        reply = chatbot_response(user_message, prediction)

        st.session_state.messages.append(("assistant", reply))

        with st.chat_message("assistant"):
            st.write(reply)