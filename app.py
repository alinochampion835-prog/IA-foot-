import streamlit as st

st.set_page_config(page_title="IA Foot Predictor", page_icon="⚽")

st.title("⚽ IA Foot Predictor")
st.write("Bienvenue sur votre application de pronostics !")

equipe_dom = st.selectbox("Équipe à Domicile", ["Paris SG", "Marseille", "Real Madrid", "Barcelone"])
equipe_ext = st.selectbox("Équipe à l'Extérieur", ["Lyon", "Monaco", "Atlético Madrid", "Valence"])

if st.button("🚀 Lancer l'analyse IA"):
    st.success(f"Analyse terminée pour {equipe_dom} vs {equipe_ext} !")
    st.markdown("### 🎯 Pronostics :")
    st.info("• **1N2 :** Victoire de l'équipe à domicile")
    st.info("• **Buts :** Plus de 2.5 buts dans le match")
  
