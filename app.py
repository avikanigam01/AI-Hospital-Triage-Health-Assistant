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

/* =======================
   Main Background
======================= */

.stApp{

background: linear-gradient(
135deg,
#FFF6F4 0%,
#FFEDE7 25%,
#FFFDFC 55%,
#F3FBF7 80%,
#E5F8EF 100%
);

font-family: 'Segoe UI', sans-serif;

}

/* =======================
   Title
======================= */

.main-title{

font-size:36px;
font-weight:700;
color:#2F3E46;
text-align:center;
letter-spacing:-0.5px;
margin-top:5px;
margin-bottom:5px;

}

.subtitle{

font-size:15px;
font-weight:400;
text-align:center;
color:#6B7772;
margin-bottom:25px;

}

/* =======================
   Glass Card
======================= */

.card{

background:rgba(255,255,255,.88);

padding:22px;

border-radius:18px;

border:1px solid rgba(255,255,255,.7);

box-shadow:0 8px 24px rgba(0,0,0,.08);

margin-bottom:20px;

}

/* =======================
   Feature Cards
======================= */

.metric-card{

text-align:center;

padding:18px;

background:rgba(255,255,255,.95);

border-radius:16px;

border:1px solid #F7D8CF;

box-shadow:0 6px 16px rgba(0,0,0,.06);

transition:all .3s ease;

}

.metric-card:hover{

transform:translateY(-4px);

box-shadow:0 10px 25px rgba(0,0,0,.12);

}

/* =======================
   Sidebar
======================= */

section[data-testid="stSidebar"]{

background:linear-gradient(
180deg,
#FFF6F3 0%,
#FFEAE3 35%,
#FFFDFB 70%,
#ECF9F2 100%
);

border-right:1px solid rgba(255,255,255,.6);

box-shadow:6px 0px 20px rgba(0,0,0,.05);

}

section[data-testid="stSidebar"] > div{

padding:18px;

}

/* Sidebar Headings */

section[data-testid="stSidebar"] h2{

color:#35524A;
font-size:24px;
font-weight:700;

}

section[data-testid="stSidebar"] h3{

color:#55746B;
font-size:18px;
font-weight:600;

}

/* =======================
   Input Boxes
======================= */

.stTextInput input,
.stNumberInput input{

background:#FFFDFC;

border-radius:12px;

border:1px solid #F2D6CF;

padding:8px;

}

/* Selectbox */

.stSelectbox div[data-baseweb="select"]{

border-radius:12px;

border:1px solid #F2D6CF;

background:#FFFDFC;

}

/* Radio */

.stRadio{

background:#FFFDFC;

padding:10px;

border-radius:12px;

}

/* Slider */

.stSlider{

padding-top:10px;
padding-bottom:5px;

}

/* =======================
   Buttons
======================= */

.stButton>button{

width:100%;

height:50px;

border:none;

border-radius:14px;

background:linear-gradient(
90deg,
#F6AAA4,
#F7C0B8,
#BFE9D5
);

color:#2F3E46;

font-size:16px;

font-weight:600;

transition:.3s;

}

.stButton>button:hover{

transform:translateY(-2px);

box-shadow:0 8px 18px rgba(0,0,0,.12);

}

/* =======================
   Metrics
======================= */

[data-testid="metric-container"]{

background:white;

padding:15px;

border-radius:15px;

border:1px solid #F1E4DF;

box-shadow:0 4px 12px rgba(0,0,0,.05);

}

/* =======================
   Assessment Cards
======================= */

.result-card{

background:rgba(255,255,255,.96);

padding:18px 22px;

border-radius:18px;

border:1px solid rgba(255,255,255,.8);

box-shadow:
0 10px 22px rgba(0,0,0,.08),
0 3px 6px rgba(255,255,255,.8) inset;

margin-bottom:18px;

transition:.25s;

}

.result-card:hover{

transform:translateY(-3px);

box-shadow:
0 16px 32px rgba(0,0,0,.12);

}

.result-title{

font-size:15px;

font-weight:600;

color:#68756D;

margin-bottom:8px;

}

.result-value{

font-size:28px;

font-weight:700;

color:#2F3E46;

}

.result-small{

font-size:18px;

font-weight:600;

color:#35524A;

}
/* =======================
   Success / Info / Warning
======================= */

.stSuccess{

border-radius:14px;

}

.stInfo{

border-radius:14px;

}

.stWarning{

border-radius:14px;

}

/* =======================
   Chat Input
======================= */

[data-testid="stChatInput"]{

border-radius:14px;

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
st.markdown(
"""
<div style="text-align:center;
font-size:15px;
color:#68756D;">

🏥 AI Powered &nbsp;&nbsp;|&nbsp;&nbsp;
🩺 Smart Triage &nbsp;&nbsp;|&nbsp;&nbsp;
💬 Health Assistant

</div>
""",
unsafe_allow_html=True)

# ------------------------------------------------
# Feature Cards
# ------------------------------------------------

col1,col2,col3,col4=st.columns(4)

cards=[

("🤖","AI Prediction"),

("⚡","Real-time Analysis"),

("🏥","Department Recommendation"),

("💬","Health Chatbot")

]

for col,(icon,title) in zip([col1,col2,col3,col4],cards):

    with col:

        st.markdown(f"""

<div class="metric-card">

<h2>{icon}</h2>

<b>{title}</b>

</div>

""",unsafe_allow_html=True)

st.write("")

# ------------------------------------------------
# Welcome Card
# ------------------------------------------------

st.markdown("""
<div class='card'>

<h3>Welcome</h3>

AI-powered triage for faster and smarter patient assessment.

Fill in the patient details from the sidebar to receive an AI-generated urgency level, department recommendation, and first-aid guidance.

</div>
""", unsafe_allow_html=True)

prediction = None

left, right = st.columns([1.4, 1])

with left:

    st.markdown("## 🩺 Patient Assessment")

    if patient_data["predict"]:

        with st.spinner("Analyzing patient..."):

            prediction = predict(
                patient_data["age"],
                patient_data["temperature"],
                patient_data["heart_rate"],
                patient_data["pain"],
                patient_data["symptom"],
                patient_data["days"]
            )

            result = get_recommendation(prediction)

        # ---------------- Patient Assessment Report ----------------

        st.markdown("## 🩺 Patient Assessment Report")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(f"""
            <div class="result-card">

            <div class="result-title">
            Risk Level
            </div>

            <div class="result-value">
            {result['risk']}
            </div>

            </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown(f"""
            <div class="result-card">

            <div class="result-title">
            Prediction Confidence
            </div>

            <div class="result-value">
            {result['confidence']}%
            </div>

            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card">

        <div class="result-title">
        🏥 Recommended Department
        </div>

        <div class="result-small">
        {result['department']}
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card">

        <div class="result-title">
        📋 Recommended Action
        </div>

        <div class="result-small">
        {result['seek_care']}
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="result-card">

        <div class="result-title">
        💊 First Aid Recommendations
        </div>
        """, unsafe_allow_html=True)

        for tip in result["first_aid"]:
            st.markdown(f"✅ {tip}")

        st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------
# Footer
# ------------------------------------------------

st.divider()

st.caption(
"⚠️ This AI Health Assistant provides educational guidance only and should not replace professional medical advice, diagnosis, or treatment."
)
st.markdown(
    "<center>Made with ❤️ by <b>Team PhoeniX</b></center>",
    unsafe_allow_html=True,
)