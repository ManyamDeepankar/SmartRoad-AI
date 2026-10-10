import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="SmartRoad AI",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 SmartRoad AI")
st.subheader("Intelligent Traffic Management System")

st.info("Hackathon demonstration using sample traffic data.")

data = pd.DataFrame({
    "Road": ["Road A", "Road B", "Road C", "Road D"],
    "Vehicles": [120, 250, 180, 90]
})

col1, col2, col3 = st.columns(3)

col1.metric("Total Vehicles", int(data["Vehicles"].sum()))
col2.metric("Roads Monitored", len(data))
col3.metric("High Traffic Roads", int((data["Vehicles"] >= 200).sum()))

st.header("Traffic Analysis")

fig = px.bar(
    data,
    x="Road",
    y="Vehicles",
    title="Traffic Volume by Road",
    color="Vehicles"
)

st.plotly_chart(fig, use_container_width=True)

st.header("AI Traffic Prediction")

vehicles = st.number_input(
    "Enter expected vehicle count",
    min_value=0,
    max_value=10000,
    value=150
)

if st.button("Predict Traffic"):
    if vehicles < 100:
        st.success("Predicted Traffic: LOW")
    elif vehicles < 250:
        st.warning("Predicted Traffic: MEDIUM")
    else:
        st.error("Predicted Traffic: HIGH")

st.caption(
    "Demo prediction based on simple rules, not a trained AI model or live traffic data."
)
