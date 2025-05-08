import streamlit as st
from datetime import datetime
from services.openweather import get_live_weather_data
import pandas as pd
from components.map_view import show_map
from components.gauge_view import show_gauges
from components.line_chart import show_line_chart
from components.dashboard_cards import show_dashboard_cards
from streamlit_autorefresh import st_autorefresh

# ✅ UNIQUEMENT UNE FOIS, tout en haut
st.set_page_config(page_title="Qualité de l'air - Temps réel", layout="wide")

# 🔄 Rafraîchissement automatique toutes les 10 secondes
st_autorefresh(interval=10000, key="refresh")

st.title("🌍 Dashboard - Qualité de l'air à Bamako (Live API)")

# Afficher les informations dans la sidebar
st.sidebar.title("Informations")
st.sidebar.write("Dernière mise à jour :", datetime.now().strftime("%H:%M:%S"))
with st.sidebar.expander("Détails des données"):
    st.write("Source : OpenWeatherMap API")
    st.write("Mise à jour automatique toutes les 10 secondes")

# Choix de la visualisation
view = st.selectbox("Choisir une visualisation", ["Carte", "Jauges", "Graphique", "Tableau de bord"])

# ⚠️ Cache contrôlé pour limiter les appels API
@st.cache_data(ttl=10)
def fetch_data():
    return pd.DataFrame(get_live_weather_data())

# Récupération des données
df = fetch_data()

# Affichage selon la vue
if view == "Carte":
    show_map(df)
elif view == "Jauges":
    show_gauges(df)
elif view == "Graphique":
    show_line_chart(df)
elif view == "Tableau de bord":
    show_dashboard_cards(df)
