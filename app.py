import streamlit as st

st.set_page_config(page_title="IA Foot Predictor", page_icon="⚽", layout="centered")

# Style CSS personnalisé pour imiter l'interface de l'image
st.markdown("""
<style>
    .stApp {
        background-color: #0b1a30;
        color: white;
    }
    .match-card {
        background-color: #1a365d;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .league-title {
        background-color: #2b4c7e;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 15px;
    }
    .pred-badge {
        background-color: #e2e8f0;
        color: #1a202c;
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: bold;
        margin: 10px 0;
    }
    .stButton>button {
        background-color: #22c55e !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100%;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚽ IA Foot Predictor")

# Onglets de navigation (Aujourd'hui / Demain / Weekend)
tab1, tab2, tab3 = st.tabs(["Aujourd'hui", "Demain", "Weekend"])

def render_match(home, away, home_logo, away_logo, match_time, pred):
    st.markdown(f"""
    <div class="match-card">
        <div style="display: flex; justify-content: space-around; align-items: center;">
            <div style="width: 35%;">
                <img src="{home_logo}" width="50" style="margin-bottom: 5px;"/><br/>
                <strong>{home}</strong>
            </div>
            <div style="width: 30%;">
                <div style="color: #4ade80; font-size: 14px;">{match_time}</div>
            </div>
            <div style="width: 35%;">
                <img src="{away_logo}" width="50" style="margin-bottom: 5px;"/><br/>
                <strong>{away}</strong>
            </div>
        </div>
        <div style="margin-top: 10px;">
            <span class="pred-badge">👉 {pred}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab1:
    st.markdown('<div class="league-title">🏴ⁿ visual ANGLETERRE: PREMIER LEAGUE</div>', unsafe_allow_html=True)
    
    # Match 1
    render_match(
        "Aston Villa", "Manchester City",
        "https://media.api-sports.io/football/teams/66.png",
        "https://media.api-sports.io/football/teams/50.png",
        "24 OCT. 11:30", "1 - 2"
    )
    if st.button("Aperçu, stats et cotes »", key="btn1"):
        st.info("📊 Stats IA : Manchester City favori (65% de chances de victoire). Pronostic Over 2.5 Buts.")

    # Match 2
    render_match(
        "Arsenal", "Everton",
        "https://media.api-sports.io/football/teams/42.png",
        "https://media.api-sports.io/football/teams/45.png",
        "24 OCT. 14:00", "3 - 1"
    )
    if st.button("Aperçu, stats et cotes »", key="btn2"):
        st.info("📊 Stats IA : Arsenal favori à domicile. Pronostic Victoire 1 avec handicap.")
        
