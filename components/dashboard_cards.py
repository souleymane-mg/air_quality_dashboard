import streamlit as st

def show_dashboard_cards(df):
    latest = df.groupby("region").last().reset_index()
    st.subheader("Tableau de bord synthétique")
    for _, row in latest.iterrows():
        with st.expander(f"📍 {row['region']}"):
            st.metric("🌡 Température (°C)", f"{row['temperature']}°C")
            st.metric("💧 Humidité (%)", f"{row['humidite']}%")
            st.metric("🌫 PM2.5", f"{row['pm25']} µg/m³")
