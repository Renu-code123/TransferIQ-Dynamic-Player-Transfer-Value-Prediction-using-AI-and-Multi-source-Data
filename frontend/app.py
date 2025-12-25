import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="TransferIQ", layout="centered")

st.title("⚽ TransferIQ")
st.subheader("AI-based Player Transfer Value Prediction")

st.markdown("Enter player details:")

age = st.number_input("Age", 16, 45, 25)
goals = st.number_input("Goals Scored", 0, 60, 10)
assists = st.number_input("Assists", 0, 40, 5)
matches = st.number_input("Matches Played", 0, 60, 20)
injury_days = st.number_input("Injury Days", 0, 365, 15)
sentiment = st.slider("Social Media Sentiment (-1 to 1)", -1.0, 1.0, 0.2)
market_value_last = st.number_input("Last Market Value (in million €)", 0.0, 200.0, 20.0)

if st.button("🔮 Predict Transfer Value"):
    payload = {
        "age": age,
        "goals": goals,
        "assists": assists,
        "matches": matches,
        "injury_days": injury_days,
        "sentiment": sentiment,
        "market_value_last": market_value_last
    }

    try:
        res = requests.post(API_URL, json=payload)
        result = res.json()

        if "predicted_transfer_value" in result:
            st.success(
                f"💰 Predicted Transfer Value: € {result['predicted_transfer_value']} million"
            )
        else:
            st.error(result)

    except Exception as e:
        st.error("⚠️ Backend not running. Please start FastAPI server.")
