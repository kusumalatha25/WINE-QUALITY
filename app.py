import streamlit as st
import time

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Wine Quality Judge 🍷",
    page_icon="🍷",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

/* ===== App Background ===== */
.stApp {
    background: linear-gradient(135deg, #3a0010, #5a0018, #2a000b);
    background-size: 300% 300%;
    animation: wineFlow 10s ease infinite;
    color: white;
}

@keyframes wineFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===== Titles ===== */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #ffd6df;
    margin-bottom: 35px;
}

/* ===== Sidebar ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2a000b, #420012);
}

/* Sidebar Header */
section[data-testid="stSidebar"] h2 {
    color: white !important;
}

/* Slider Labels & Values */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: white !important;
    font-weight: bold;
}

/* Slider Track */
.stSlider > div[data-baseweb="slider"] > div {
    background: white !important;
}

/* Slider Thumb */
.stSlider [role="slider"] {
    background: white !important;
    border: 2px solid white;
    box-shadow: 0 0 10px rgba(255,255,255,0.8);
}

/* ===== Output Card ===== */
.output-box {
    background: rgba(255,255,255,0.18);
    padding: 55px;
    border-radius: 28px;
    box-shadow: 0 0 45px rgba(255, 100, 150, 0.7);
    text-align: center;
    margin-top: 40px;
}

.result {
    font-size: 46px;
    font-weight: bold;
}

.score {
    font-size: 30px;
    margin-top: 10px;
    color: #ffccd9;
    font-weight: bold;
}

.comment {
    font-size: 22px;
    margin-top: 12px;
    color: #ffe6ec;
}

/* ===== Animations ===== */
.thinking {
    text-align: center;
    font-size: 26px;
    animation: blink 1.5s infinite;
}

@keyframes blink {
    0% { opacity: 0.3; }
    50% { opacity: 1; }
    100% { opacity: 0.3; }
}

.celebrate {
    font-size: 42px;
    animation: pop 1.2s ease-in-out infinite;
}

@keyframes pop {
    0% { transform: scale(1); }
    50% { transform: scale(1.25); }
    100% { transform: scale(1); }
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("<div class='title'>🍷 Wine Quality Judge</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Dataset-Aligned Wine Quality Prediction</div>", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.header("🧪 Chemical Properties")

fixed_acidity = st.sidebar.slider("🍋 Fixed Acidity", 4.0, 16.0, 7.0)
volatile_acidity = st.sidebar.slider("🧂 Volatile Acidity", 0.1, 1.6, 0.5)
citric_acid = st.sidebar.slider("🍊 Citric Acid", 0.0, 1.0, 0.3)
residual_sugar = st.sidebar.slider("🍬 Residual Sugar", 0.5, 16.0, 2.5)
chlorides = st.sidebar.slider("🧪 Chlorides", 0.01, 0.20, 0.05)
free_sulfur = st.sidebar.slider("🧫 Free Sulfur Dioxide", 1, 80, 15)
total_sulfur = st.sidebar.slider("🧫 Total Sulfur Dioxide", 5, 300, 46)
density = st.sidebar.slider("⚖️ Density", 0.9900, 1.0050, 0.9968, step=0.0001)
ph = st.sidebar.slider("⚗️ pH", 2.8, 4.0, 3.3)
sulphates = st.sidebar.slider("🧪 Sulphates", 0.3, 2.0, 0.65)
alcohol = st.sidebar.slider("🍾 Alcohol %", 8.0, 15.0, 10.5)

# ================= BUTTON =================
analyze = st.button("🔍 Analyze Wine Quality")

# ================= LOGIC =================
if analyze:
    st.markdown("<div class='thinking'>🧠 Analyzing wine sample...</div>", unsafe_allow_html=True)
    time.sleep(2)

    rule_score = 0
    if fixed_acidity <= 7.5: rule_score += 1
    if volatile_acidity < 0.7: rule_score += 1
    if citric_acid > 0.2: rule_score += 1
    if residual_sugar < 5: rule_score += 1
    if chlorides < 0.08: rule_score += 1
    if free_sulfur < 35: rule_score += 1
    if total_sulfur < 120: rule_score += 1
    if density < 0.9975: rule_score += 1
    if 3.0 <= ph <= 3.6: rule_score += 1
    if sulphates > 0.5: rule_score += 1
    if alcohol >= 10: rule_score += 2

    if rule_score <= 3: wine_score = 3
    elif rule_score <= 5: wine_score = 4
    elif rule_score <= 7: wine_score = 5
    elif rule_score <= 9: wine_score = 6
    elif rule_score <= 11: wine_score = 7
    elif rule_score <= 13: wine_score = 8
    else: wine_score = 9

    if wine_score <= 4:
        quality, comment, emojis = "❌ POOR", "Low-quality wine with imbalance.", "😞🍷"
    elif wine_score <= 6:
        quality, comment, emojis = "⚠️ AVERAGE", "Acceptable wine quality.", "🙂🍷"
    elif wine_score <= 8:
        quality, comment, emojis = "✅ GOOD", "Well-balanced, high-quality wine.", "🎉🍷✨"
    else:
        quality, comment, emojis = "🌟 EXCELLENT", "Premium wine quality.", "🥂🍾🌟🔥"

    st.markdown(f"""
    <div class="output-box">
        <div class="result">{quality}</div>
        <div class="score">🍷 Predicted Wine Quality: {wine_score}</div>
        <div class="comment">{comment}</div>
        <div class="celebrate">{emojis}</div>
        <p style="margin-top:25px;color:#ffb3c6;font-size:18px;">
        — Created by <b>kusuma</b> 💖
        </p>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown(
    "<p style='text-align:center;margin-top:55px;color:#ffd6df;'>🍷 Streamlit Wine Quality Project | Final Version | kusuma ✨</p>",
    unsafe_allow_html=True
)