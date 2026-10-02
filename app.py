import streamlit as st
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("student_model.pkl")

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(88, 80, 236, 0.18), transparent 30%),
        radial-gradient(circle at 90% 80%, rgba(14, 165, 233, 0.18), transparent 30%),
        linear-gradient(135deg, #070b1f, #0b1028, #111936);
    color: white;
}

/* Animated glow */
.stApp::before {
    content: "";
    position: fixed;
    width: 350px;
    height: 350px;
    border-radius: 50%;
    background: rgba(99, 102, 241, 0.12);
    filter: blur(80px);
    top: 10%;
    left: 5%;
    animation: float1 8s infinite alternate ease-in-out;
    pointer-events: none;
}

.stApp::after {
    content: "";
    position: fixed;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: rgba(14, 165, 233, 0.12);
    filter: blur(80px);
    bottom: 5%;
    right: 5%;
    animation: float2 10s infinite alternate ease-in-out;
    pointer-events: none;
}

@keyframes float1 {
    from { transform: translate(0, 0); }
    to { transform: translate(80px, 50px); }
}

@keyframes float2 {
    from { transform: translate(0, 0); }
    to { transform: translate(-70px, -40px); }
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    margin-top: 20px;
    background: linear-gradient(90deg, #60a5fa, #a78bfa, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 35px;
}

/* Glass cards */
.card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(15px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.25);
}

/* Input labels */
label {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}

/* Input boxes */
div[data-baseweb="input"] {
    background: rgba(255,255,255,0.08);
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    height: 50px;
    font-size: 17px;
    font-weight: 700;
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(99,102,241,0.4);
}

/* Result */
.result-box {
    text-align: center;
    padding: 25px;
    border-radius: 18px;
    background: linear-gradient(
        135deg,
        rgba(79,70,229,0.25),
        rgba(14,165,233,0.18)
    );
    border: 1px solid rgba(129,140,248,0.35);
    margin-top: 20px;
}

.result-number {
    font-size: 42px;
    font-weight: 800;
    color: #60a5fa;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 50px;
    font-size: 14px;
}
/* AI Particle Background */

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;

    background-image:
        radial-gradient(circle, rgba(96,165,250,0.8) 2px, transparent 3px),
        radial-gradient(circle, rgba(167,139,250,0.7) 2px, transparent 3px),
        radial-gradient(circle, rgba(34,211,238,0.6) 1.5px, transparent 2.5px);

    background-size:
        170px 190px,
        230px 210px,
        130px 150px;

    background-position:
        10px 20px,
        80px 60px,
        30px 100px;

    animation: particlesMove 18s linear infinite;
}

@keyframes particlesMove {
    0% {
        background-position:
            10px 20px,
            80px 60px,
            30px 100px;
    }

    50% {
        background-position:
            100px 80px,
            20px 120px,
            100px 30px;
    }

    100% {
        background-position:
            10px 20px,
            80px 60px,
            30px 100px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🎓 AI Student Performance Predictor</div>',
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="text-align: center;">
        🟢 <b>AI MODEL ONLINE</b> &nbsp; | &nbsp; <b>RANDOM FOREST REGRESSION</b>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------- INPUT SECTION ----------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📋 Student Information")

col1, col2 = st.columns(2)

with col1:

    studytime = st.number_input(
        "📚 Study Time",
        min_value=1,
        max_value=4,
        value=2
    )

    failures = st.number_input(
        "❌ Number of Past Failures",
        min_value=0,
        max_value=4,
        value=0
    )

    absences = st.number_input(
        "📝 Number of Absences",
        min_value=0,
        max_value=100,
        value=5
    )

with col2:

    G1 = st.number_input(
        "📖 First Period Grade (G1)",
        min_value=0,
        max_value=20,
        value=10
    )

    G2 = st.number_input(
        "📖 Second Period Grade (G2)",
        min_value=0,
        max_value=20,
        value=10
    )

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ---------------- PREDICTION ----------------

if st.button("🔮  PREDICT STUDENT PERFORMANCE", use_container_width=True):

    input_data = [[studytime, failures, absences, G1, G2]]

    prediction = model.predict(input_data)

    predicted_grade = prediction[0]

    # Category
    if predicted_grade >= 15:
        category = "Excellent 🌟"
        message = "The predicted academic performance is excellent."

    elif predicted_grade >= 10:
        category = "Good 👍"
        message = "The predicted academic performance is good."

    else:
        category = "Needs Improvement 📚"
        message = "Additional academic support may be helpful."

    # Result
    st.markdown(
        f"""
        <div class="result-box">

        <div style="font-size:20px;">
        🎯 Predicted Final Grade
        </div>

        <div class="result-number">
        {predicted_grade:.2f} / 20
        </div>

        <div style="font-size:22px; margin-top:10px;">
        {category}
        </div>

        <div style="color:#cbd5e1; margin-top:10px;">
        {message}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # Progress
    progress = min(max(predicted_grade / 20, 0.0), 1.0)

    st.write("")
    st.progress(progress)

    st.caption(
        f"Performance level: {predicted_grade:.2f} / 20"
    )

    # Student summary
    st.write("")
    st.subheader("📊 Prediction Summary")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Study Time", studytime)
    c2.metric("Failures", failures)
    c3.metric("Absences", absences)
    c4.metric("G1", G1)
    c5.metric("G2", G2)

# ---------------- RESET ----------------

st.write("")

if st.button("🔄 Clear / Reset", use_container_width=True):
    st.rerun()

# ---------------- ABOUT ----------------

st.divider()

st.subheader("🤖 About the System")

st.write(
    "This application uses a Random Forest Regression model to "
    "predict student final academic performance. The model is "
    "trained using study time, previous failures, absences, "
    "and previous academic grades."
)

st.markdown(
    '<div class="footer">'
    'AI-Based Student Performance Prediction System • '
    'Python • Scikit-learn • Streamlit'
    '</div>',
    unsafe_allow_html=True
)