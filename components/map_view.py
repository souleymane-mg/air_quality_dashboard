import plotly.express as px
import streamlit as st

def show_map(df):
    if df.empty:
        st.warning("Aucune donnée météo disponible.")
        return

    latest = df.groupby("region").last().reset_index()

    fig = px.scatter_mapbox(
        latest,
        lat="lat",
        lon="lon",
        color="pm25",
        size="pm25",
        hover_name="region",
        hover_data=["temperature", "humidite", "pm25"],
        color_continuous_scale="YlOrRd",
        size_max=20,
        zoom=4.5,  # 🔁 Zoom reculé pour voir tout le Mali
        center={"lat": 17.0, "lon": -3.0},  # 📍 Centre du Mali
        height=650
    )

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})

    st.plotly_chart(fig, use_container_width=True)
