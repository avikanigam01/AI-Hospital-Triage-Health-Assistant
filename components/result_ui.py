import streamlit as st

def show_result(result):

    st.markdown("## 🩺 Patient Assessment Report")

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("Risk Level",result["risk"])

    with c2:
        st.metric("Department",result["department"])

    with c3:
        st.metric("Confidence",f"{result['confidence']}%")

    st.markdown("---")

    st.info(result["seek_care"])

    st.markdown("### 💊 First Aid Guidance")

    for tip in result["first_aid"]:
        st.success(tip)