import streamlit as st
import requests
import pandas as pd
import time
import plotly.graph_objects as go

# API Endpoints
COIN_API_URL = "https://api.coingecko.com/api/v3/"
NEWS_API_URL = "https://cryptopanic.com/api/v1/posts/?auth_token=YOUR_API_KEY&public=true"

# Available currencies
CURRENCIES = ["usd", "eur", "inr", "gbp", "jpy"]
st.set_page_config(page_title="Crypto Tracker", page_icon="💰", layout="wide")

# Sidebar
st.sidebar.title("🔍 Cryptocurrency Tracker")
selected_currency = st.sidebar.selectbox("Select Currency", CURRENCIES, index=0)
selected_coins = st.sidebar.multiselect("Select Coins to Track", ["bitcoin", "ethereum", "dogecoin", "cardano", "solana"], default=["bitcoin", "ethereum"])

# Refresh Interval
refresh_rate = st.sidebar.slider("Auto Refresh Interval (sec)", 10, 300, 60)
price_alerts = {coin: st.sidebar.number_input(f"Set Price Alert for {coin.capitalize()} ({selected_currency.upper()})", min_value=0.0, value=0.0) for coin in selected_coins}

# Get Prices & Market Data
@st.cache_data(ttl=60)
def fetch_prices():
    try:
        response = requests.get(f"{COIN_API_URL}coins/markets", params={"vs_currency": selected_currency, "ids": ",".join(selected_coins)})
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException:
        return []  # Return empty list on error

# Fetch Historical Data
def fetch_historical_data(coin, days):
    url = f"{COIN_API_URL}coins/{coin}/market_chart"
    params = {"vs_currency": selected_currency, "days": days, "interval": "daily"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get("prices", [])  # Use .get() to avoid KeyError
    except requests.exceptions.RequestException:
        return []  # Return empty list on error

# Fetch Crypto News
def fetch_crypto_news():
    try:
        response = requests.get(NEWS_API_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get("results", [])  # Use .get() to avoid KeyError
    except requests.exceptions.RequestException:
        return []  # Return empty list on error

# Display Prices
st.title("💰 Real-Time Crypto Prices")
data = fetch_prices()
if data:
    df = pd.DataFrame(data)[["name", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    df.columns = ["Coin", "Price", "Market Cap", "Volume", "24h Change (%)"]
    st.dataframe(df, height=300, width=800)

# Price Alerts
for coin in selected_coins:
    current_price = next((item["current_price"] for item in data if item["id"] == coin), None)
    if current_price and price_alerts[coin] > 0 and current_price >= price_alerts[coin]:
        st.warning(f"🚨 {coin.capitalize()} has reached your alert price of {price_alerts[coin]} {selected_currency.upper()}!")

# Historical Data & Charts
st.subheader("📈 Price Trends & Candlestick Charts")
days = st.radio("Select Timeframe", ["7", "30", "90", "365"], horizontal=True)
for coin in selected_coins:
    st.write(f"### {coin.capitalize()} - {days} Days Chart")
    prices = fetch_historical_data(coin, days)
    if prices:
        df = pd.DataFrame(prices, columns=["Time", "Price"])
        df["Time"] = pd.to_datetime(df["Time"], unit="ms")

        # Candlestick Chart
        fig = go.Figure(data=[go.Candlestick(x=df["Time"], open=df["Price"], high=df["Price"] * 1.02, low=df["Price"] * 0.98, close=df["Price"], increasing_line_color='green', decreasing_line_color='red')])
        fig.update_layout(height=400, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, use_container_width=True)

# Crypto News Feed
st.subheader("📰 Latest Crypto News")
news = fetch_crypto_news()
if news:
    for article in news[:5]:
        st.write(f"🔹 [{article['title']}]({article['url']})")

# Auto Refresh Function
def auto_refresh():
    time.sleep(refresh_rate)  # Wait for refresh time
    st.rerun()  # Correct way to refresh Streamlit

# Call auto_refresh at the end of the script
if refresh_rate > 0:
    auto_refresh()
