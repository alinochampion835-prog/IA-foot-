import streamlit as st

st.set_page_config(page_title="IA Foot Predictor", page_icon="⚽", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #0b1a30; color: white; }
    .match-card {
        background-color: #1a365d;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 10px;
        text-align: center;
    }
    .league-title {
        background-color: #2b4c7e;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        margin: 20px 0 10px 0;
    }
    .pred-badge {
        background-color: #e2e8f0;
        color: #1a202c;
        display: inline-block;
        padding: 4px 12px;
        border-radius: 15px;
        font-weight: bold;
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

tab1, tab2, tab3 = st.tabs(["Aujourd'hui", "Demain", "Weekend"])

def render_match(home, away, home_logo, away_logo, match_time, pred):
    st.markdown(f"""
    <div class="match-card">
        <div style="display: flex; justify-content: space-around; align-items: center;">
            <div style="width: 35%;">
                <img src="{home_logo}" width="45"/><br/><strong>{home}</strong>
            </div>
            <div style="width: 30%; color: #4ade80;">{match_time}</div>
            <div style="width: 35%;">
                <img src="{away_logo}" width="45"/><br/><strong>{away}</strong>
            </div>
        </div>
        <div style="margin-top: 8px;">
            <span class="pred-badge">👉 {pred}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab1:
    # PREMIER LEAGUE
    st.markdown('<div class="league-title">🏴 ANGLETERRE: PREMIER LEAGUE</div>', unsafe_allow_html=True)
    
    render_match("Aston Villa", "Manchester City", "https://media.api-sports.io/football/teams/66.png", "https://media.api-sports.io/football/teams/50.png", "11:30", "1 - 2")
    if st.button("Aperçu & Stats", key="m1"):
        st.info("Manchester City favori à l'extérieur. Pronostic : V2 ou Over 2.5.")

    render_match("Arsenal", "Everton", "https://media.api-sports.io/football/teams/42.png", "https://media.api-sports.io/football/teams/45.png", "14:00", "3 - 1")
    if st.button("Aperçu & Stats", key="m2"):
        st.info("Arsenal très fort à domicile. Pronostic : V1.")

    render_match("Chelsea", "Tottenham", "https://media.api-sports.io/football/teams/49.png", "https://media.api-sports.io/football/teams/47.png", "16:30", "2 - 2")
    if st.button("Aperçu & Stats", key="m3"):
        st.info("Match équilibré. Pronostic : Les deux équipes marquent.")

    # LALIGA
    st.markdown('<div class="league-title">🇪🇸 ESPAGNE: LALIGA</div>', unsafe_allow_html=True)

    render_match("Valencia", "Villarreal", "https://media.api-sports.io/football/teams/532.png", "https://media.api-sports.io/football/teams/533.png", "16:30", "1 - 1")
    if st.button("Aperçu & Stats", key="m4"):
        st.info("Derby intense. Pronostic : Match nul ou N2.")

    render_match("Atlético Madrid", "Deportivo", "https://media.api-sports.io/football/teams/530.png", "https://media.api-sports.io/football/teams/537.png", "19:00", "2 - 0")
    if st.button("Aperçu & Stats", key="m5"):
        st.info("Atlético favori solide à domicile. Pronostic : V1.")

    # CAF
    st.markdown('<div class="league-title">🌍 AFRIQUE: LIGUE DES CHAMPIONS CAF</div>', unsafe_allow_html=True)

    render_match("ES Tunis", "Asswehly", "https://media.api-sports.io/football/teams/1018.png", "https://media.api-sports.io/football/teams/1020.png", "16:00", "2 - 0")
    if st.button("Aperçu & Stats", key="m6"):
        st.info("ES Tunis largement favori à domicile.")
        
        
