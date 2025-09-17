import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import IsolationForest
import os

# Define the model file path
MODEL_PATH = "anomaly_detector.pkl"

# Function to train and save the model
def train_model():
    st.write("🚀 Training anomaly detection model...")
    
    # Load dataset (Replace with actual dataset path)
    df = pd.read_csv("transaction.csv")

    # Select numerical features only
    features = ["amount", "time", "account_age", "num_transactions", "merchant_score"]
    X = df[features]

    # Train Isolation Forest
    model = IsolationForest(contamination=0.02, random_state=42)
    model.fit(X)

    # Save the model
    joblib.dump(model, MODEL_PATH)
    st.success("✅ Model trained and saved successfully!")

# Function to load model
def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        st.warning("⚠️ Model not found! Training a new one...")
        train_model()
        return joblib.load(MODEL_PATH)

# Streamlit UI
st.title("💰 Financial Fraud Detection")
st.write("Upload transaction data to detect fraudulent activities.")

# Train the model if not present
model = load_model()

# Upload CSV File
uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 🔍 Uploaded Data:", df.head())

    # Select relevant features
    features = ["amount", "time", "account_age", "num_transactions", "merchant_score"]
    
    if not all(col in df.columns for col in features):
        st.error("❌ Error: Missing required columns in uploaded file!")
    else:
        X = df[features]

        # Predict anomalies (-1 means fraud)
        df["anomaly"] = model.predict(X)
        df["anomaly"] = df["anomaly"].apply(lambda x: "Fraud" if x == -1 else "Normal")

        # Show flagged transactions
        fraud_cases = df[df["anomaly"] == "Fraud"]
        
        st.write("### 🚨 Fraudulent Transactions Detected:")
        st.dataframe(fraud_cases)

        # Download results
        st.download_button("⬇️ Download Results", df.to_csv(index=False), file_name="anomaly_results.csv")

st.sidebar.markdown("### ℹ️ About")
st.sidebar.write("This app detects fraudulent transactions using an **Isolation Forest** model.")
st.sidebar.write("📊 Upload a transaction dataset and identify anomalies.")

# Train model button
if st.sidebar.button("🔄 Retrain Model"):
    train_model()
