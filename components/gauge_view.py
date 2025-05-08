import streamlit as st
import plotly.graph_objects as go

def show_gauges(df):
    latest = df.groupby("region").last().reset_index()
    st.subheader("Jauges de pollution par region")
    cols = st.columns(3)
    for idx, row in latest.iterrows():
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=row["pm25"],
            title={'text': f"{row['region']}"},
            gauge={
                'axis': {'range': [0, 150]},
                'bar': {'color': "darkred"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgreen"},
                    {'range': [50, 100], 'color': "orange"},
                    {'range': [100, 150], 'color': "red"}
                ]
            }
        ))
        cols[idx % 3].plotly_chart(fig, use_container_width=True)
