import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import requests
import time

# Set Page Configuration (must be the first Streamlit command)
st.set_page_config(page_title="Gold & Market Dashboard", layout="wide")

# Function to fetch gold data
def get_gold_data():
    gold = yf.Ticker("GC=F")  # Gold Futures
    data = gold.history(period="7d", interval="1d")  # Use daily data instead of 15 min
    if data.empty:
        return pd.DataFrame(), {}

    data["SMA_50"] = data["Close"].rolling(window=50, min_periods=1).mean()  # Fix NaN issue
    return data, gold.info

# Function to fetch market indices
def get_market_data():
    indices = {
        "SENSEX": "^BSESN",
        "NIFTY": "^NSEI",
        "DOW": "^DJI",
        "NASDAQ": "^IXIC",
        "NIKKEI 225": "^N225",
        "FTSE 100": "^FTSE"
    }
    market_data = []
    
    for name, index in indices.items():
        stock = yf.Ticker(index)
        info = stock.info
        price = info.get("regularMarketPrice", 0)
        change = info.get("regularMarketChange", 0)
        change_percent = info.get("regularMarketChangePercent", 0)
        
        market_data.append({
            "Index": name,
            "Price": round(price, 2),
            "Change": round(change, 2),
            "Change (%)": round(change_percent, 2),
            "Color": "green" if change > 0 else "red"
        })
    
    return pd.DataFrame(market_data)

# Function to fetch precious metals data
def get_metal_data():
    metals = {"Gold": "GC=F", "Silver": "SI=F", "Platinum": "PL=F"}
    metal_data = {}
    for metal, ticker in metals.items():
        metal_info = yf.Ticker(ticker).info
        metal_data[metal] = {
            "price": round(metal_info.get("regularMarketPrice", 0), 2),
            "change": round(metal_info.get("regularMarketChange", 0), 2),
            "percent_change": round(metal_info.get("regularMarketChangePercent", 0), 2),
        }
    return metal_data

# Function to fetch USD to INR exchange rate
def get_usd_inr():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return round(data["rates"]["INR"], 2)
    except:
        return 82.5  # Default fallback value

# Streamlit UI
st.title("📊 Gold & Market Dashboard")

# Sidebar for Refresh Interval
refresh_time = st.sidebar.slider("🔄 Auto Refresh Interval (sec)", 10, 120, 60)

# Fetch Data
gold_data, gold_info = get_gold_data()
market_df = get_market_data()
metal_data = get_metal_data()
usd_inr = get_usd_inr()

# Gold Price Section
gold_price_usd = gold_info.get("regularMarketPrice", "N/A")
gold_price_inr = round(gold_price_usd * usd_inr, 2) if isinstance(gold_price_usd, (int, float)) else "N/A"

st.header(f"Gold Price: ${gold_price_usd} / ₹{gold_price_inr} 📈")

# Gold Price Chart with Moving Average
fig = go.Figure()
fig.add_trace(go.Scatter(x=gold_data.index, y=gold_data["Close"], mode="lines", name="Gold Price", line=dict(color='gold')))
fig.add_trace(go.Scatter(x=gold_data.index, y=gold_data["SMA_50"], mode="lines", name="50-period SMA", line=dict(color='blue', dash='dot')))
fig.update_layout(title="Gold Price Trend", xaxis_title="Time", yaxis_title="Price (USD)", height=400)
st.plotly_chart(fig, use_container_width=True)

# Market Data with Color Indicators
st.subheader("📈 Market Indices")
def color_text(val):
    color = "green" if val > 0 else "red"
    return f"color: {color}"

st.dataframe(market_df.style.applymap(color_text, subset=["Change", "Change (%)"]), height=250)

# Precious Metal Prices
st.subheader("💰 Precious Metal Prices")
col1, col2, col3 = st.columns(3)
col1.metric("Gold", f"${metal_data['Gold']['price']}", f"{metal_data['Gold']['change']} ({metal_data['Gold']['percent_change']}%)")
col2.metric("Silver", f"${metal_data['Silver']['price']}", f"{metal_data['Silver']['change']} ({metal_data['Silver']['percent_change']}%)")
col3.metric("Platinum", f"${metal_data['Platinum']['price']}", f"{metal_data['Platinum']['change']} ({metal_data['Platinum']['percent_change']}%)")

# Auto-Refresh without Flickering
if "last_refresh" not in st.session_state:
    st.session_state["last_refresh"] = time.time()

if time.time() - st.session_state["last_refresh"] > refresh_time:
    st.session_state["last_refresh"] = time.time()
    st.experimental_rerun()
