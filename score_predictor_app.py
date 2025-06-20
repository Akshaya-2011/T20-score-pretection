import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="T20 Score Predictor", layout="centered")

# ----------------------------
# Session State Initialization
# ----------------------------
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# ----------------------------
# Background Function
# ----------------------------
def set_bg_image(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('{url}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .block-container {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 10px;
        }}
        h1, h2, h3, p, label, .stMarkdown, .stButton > button {{
            color: white;
        }}
        .stButton > button {{
            background-color: #FF5733;
            color: white;
            padding: 0.75em 1.5em;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            transition: 0.3s;
        }}
        .stButton > button:hover {{
            background-color: #e2461f;
            transform: scale(1.05);
        }}
        </style>
    """, unsafe_allow_html=True)

# ----------------------------
# Page 1: Welcome Page
# ----------------------------
if st.session_state.page == 'welcome':
    welcome_bg = "https://images.pexels.com/photos/31739439/pexels-photo-31739439.jpeg"
    set_bg_image(welcome_bg)

    st.markdown("<h1 style='color: gold;'>🏏 Welcome to T20 Score Predictor App</h1>", unsafe_allow_html=True)
    st.markdown("""
        🎯 This app predicts the final score of a T20 match based on current match stats.

        👉 Click the button below to begin!
    """)

    if st.button("🚀 Start Prediction"):
        st.session_state.page = "predict"
        st.rerun()

# ----------------------------
# Page 2: Prediction Page
# ----------------------------
elif st.session_state.page == 'predict':
    prediction_bg = "https://images.pexels.com/photos/4747325/pexels-photo-4747325.jpeg"
    set_bg_image(prediction_bg)

    st.markdown("<h1 style='color: lightgreen;'>📊 T20 Final Score Predictor</h1>", unsafe_allow_html=True)
    st.markdown("Enter current match details:")

    over = st.number_input("Overs Completed (e.g., 10.2)", min_value=0.0, max_value=20.0, step=0.1)
    runs = st.number_input("Current Total Runs", min_value=0, max_value=300, step=1)
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, step=1)

    def predict_score(over, runs, wickets):
        return runs + (20 - over) * ((runs / over) if over != 0 else 7) * (1 - wickets / 10)

    if st.button("🎯 Predict Final Score"):
        predicted_score = predict_score(over, runs, wickets)
        st.success(f"🏆 Predicted Final Score: **{int(predicted_score)} runs**")

    if st.button("🔙 Back to Welcome Page"):
        st.session_state.page = 'welcome'
        st.rerun()
