import plotly.express as px
import streamlit as st

def show_line_chart(df):
    st.subheader("Évolution des indicateurs dans le temps")
    fig = px.line(
        df,
        x="timestamp",
        y="pm25",
        color="region",
        title="PM2.5 en temps réel",
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)
