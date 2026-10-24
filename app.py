import streamlit as st

st.set_page_config(page_title="IA Foot Predictor", page_icon="⚽", layout="centered")

st.title("⚽ IA Foot Predictor")
st.write("Bienvenue sur votre application de pronostics !")

# Liste étendue des équipes principales par championnat
TEAMS = sorted([
    # Premier League
    "Arsenal", "Aston Villa", "Chelsea", "Coventry City", "Everton", "Fulham", "Manchester City", "Tottenham Hotspur",
    # LaLiga & LaLiga2
    "Almería", "Atlético Madrid", "Celta Fortuna", "Córdoba CF", "Eibar", "Elche", "Espanyol", "Girona", "Las Palmas", 
    "Leganés", "Racing Santander", "Rayo Vallecano", "RC Deportivo", "RCD Mallorca", "Real Oviedo", "Real Sociedad B", "Valencia", "Villarreal",
    # Serie A & Serie B
    "Avellino", "Bologna", "Cagliari", "Cesena", "Como", "FC Südtirol", "Lazio", "Modena", "Napoli", "Padova", "Parma", "Roma", "Sampdoria", "Sassuolo",
    # Bundesliga
    "B. Dortmund", "Eintracht Frankfurt", "FC Augsburg", "Hamburger SV", "Köln", "Mainz 05", "Paderborn", "RB Leipzig", "Schalke 04", "SV Elversberg", "Union Berlin", "Werder Bremen",
    # Ligue 1 & Ligue 2
    "Lens", "Lyon", "Paris FC", "Paris SG",
    # Competitions CAF
    "AC Douane", "AFAD", "Al Ahli Tripoli", "Al-Merreikh SC", "APR FC", "Asswehly SC", "Azam FC", "Black Bulls Maputo", "CR Belouizdad", "CS Sfaxien", "ES Tunis", "Horoya AC", "Pyramids", "Real Bamako", "Rayon Sport", "RSB Berkane", "Star Sport", "Welwalo Adigrat", "Zamalek", "Zarzis", "Zed FC",
    # MLS
    "Atlanta United", "CF Montréal", "Chicago Fire", "Cincinnati", "Columbus Crew", "DC United", "Inter Miami", "Nashville SC", "New England Revolution", "New York City", "New York RB", "Orlando City", "Philadelphia Union", "Toronto FC",
    # Eredivisie & Liga Portugal
    "ADO Den Haag", "Arouca", "Cambuur", "Casa Pia AC", "Estrela da Amadora", "FC Alverca", "Heerenveen", "PEC Zwolle", "Utrecht", "Willem II"
])

# Interface de sélection
col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox("Équipe à Domicile", TEAMS, index=TEAMS.index("Paris SG") if "Paris SG" in TEAMS else 0)

with col2:
    away_team = st.selectbox("Équipe à l'Extérieur", TEAMS, index=TEAMS.index("Lyon") if "Lyon" in TEAMS else 1)

if st.button("🚀 Lancer l'analyse IA"):
    if home_team == away_team:
        st.warning("Veuillez sélectionner deux équipes différentes.")
    else:
        st.success(f"Analyse terminée pour {home_team} vs {away_team} !")
        st.subheader("🎯 Pronostics :")
        
        # Exemple de logique de simulation
        st.info("• **1N2 :** Victoire à domicile ou Match Nul (1X)")
        st.info("• **Buts :** Plus de 1.5 buts dans le match")
