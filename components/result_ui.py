import streamlit as st


def show_result(result):
    st.markdown("## 📋 Patient Assessment Report")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🚨 Risk Level", result["risk"])

    with col2:
        st.metric("🏥 Department", result["department"])

    with col3:
        st.metric("🎯 Confidence", f"{result['confidence']}%")

    st.warning(result["seek_care"])

    st.markdown("### 💊 First Aid Guidance")

    for tip in result["first_aid"]:
        st.success(tip)