import streamlit as st

from components.sidebar import show_sidebar
import components.result_ui as result_ui
import components.chatbot_ui as chatbot_ui

from backend.predictor import predict
from backend.recommendation import get_recommendation

# ------------------------------------------------

st.set_page_config(
    page_title="AI Hospital Triage & Health Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------
# Sidebar
# ------------------------------------------------

patient_data = show_sidebar()

# ------------------------------------------------
# CSS
# ------------------------------------------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(
135deg,
#FFE5D9 0%,
#FFD6CC 30%,
#FFF8F2 60%,
#DDF4E7 80%,
#C7F0DB 100%);
}

.main-title{
font-size:48px;
font-weight:700;
text-align:center;
color:#2F3E46;
}

.subtitle{
text-align:center;
font-size:20px;
color:#5F6F65;
margin-bottom:30px;
}

.card{
background:rgba(255,255,255,0.72);
padding:25px;
border-radius:18px;
backdrop-filter:blur(12px);
box-shadow:0px 8px 20px rgba(0,0,0,.12);
margin-bottom:20px;
}

.metric-card{
text-align:center;
padding:18px;
background:white;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# Hero Section
# ------------------------------------------------

st.markdown(
"<div class='main-title'>🩺 AI Hospital Triage & Health Assistant</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Smarter Healthcare Starts with Intelligent AI</div>",
unsafe_allow_html=True
)

# ------------------------------------------------
# Feature Cards
# ------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='metric-card'>
    <h3>🤖</h3>
    <h4>AI Powered</h4>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-card'>
    <h3>⚡</h3>
    <h4>Instant Analysis</h4>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-card'>
    <h3>🏥</h3>
    <h4>Smart Recommendations</h4>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ------------------------------------------------
# Welcome Card
# ------------------------------------------------

st.markdown("""
<div class='card'>

<h3>👋 Welcome</h3>

Our AI-powered Hospital Triage Assistant analyzes patient symptoms,
predicts the urgency of medical attention,
recommends the most suitable hospital department,
and provides basic first-aid guidance.

Please complete the assessment form from the sidebar.

</div>
""", unsafe_allow_html=True)

prediction = None

# ------------------------------------------------
# Prediction
# ------------------------------------------------

if patient_data["predict"]:

    with st.spinner("🤖 AI is analyzing patient information..."):

        prediction = predict(
            patient_data["age"],
            patient_data["temperature"],
            patient_data["heart_rate"],
            patient_data["pain"],
            patient_data["symptom"],
            patient_data["days"]
        )

        result = get_recommendation(prediction)

    result_ui.show_result(result)

else:

    st.info("👈 Complete the patient assessment from the sidebar.")

st.divider()

# ------------------------------------------------
# Chatbot
# ------------------------------------------------

chatbot_ui.show_chatbot(prediction)

# ------------------------------------------------
# Footer
# ------------------------------------------------

st.divider()

st.caption(
"⚠️ This AI Health Assistant provides educational guidance only and should not replace professional medical advice, diagnosis, or treatment."
)