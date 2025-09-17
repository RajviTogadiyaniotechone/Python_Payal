import streamlit as st
import nltk
import openai
import speech_recognition as sr
import pyttsx3
from transformers import pipeline
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK data
nltk.download("vader_lexicon")

# Load Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Initialize OpenAI API (Replace 'your-api-key' with an actual key)
openai.api_key = "your-api-key"

# Initialize Speech Engine
engine = pyttsx3.init()

# Load Hugging Face Chatbot Model (alternative to OpenAI)
chat_model = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Set up Streamlit UI
st.set_page_config(page_title="AI Chatbot with Sentiment Analysis 🤖", layout="wide")

# Sidebar Settings
st.sidebar.title("Settings ⚙️")
voice_assist = st.sidebar.checkbox("Enable Voice Assistant 🎤", value=False)

st.title("🧠 AI Chatbot with Sentiment Analysis")

# Function to analyze sentiment
def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "😊 Positive", "green"
    elif score["compound"] <= -0.05:
        return "😞 Negative", "red"
    else:
        return "😐 Neutral", "gray"

# Function for speech recognition
def listen_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand."
    except sr.RequestError:
        return "Speech recognition service is down."

# Function for chatbot response
def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for chat in st.session_state["messages"]:
    message, sentiment, color = chat
    st.markdown(f'<p style="color:{color}">{message} {sentiment}</p>', unsafe_allow_html=True)

# Input field for user message
user_input = st.text_input("💬 Type your message:", "")

# Voice input
if voice_assist and st.button("🎙️ Speak"):
    user_input = listen_voice()
    st.write(f"🗣️ You said: {user_input}")

# Generate response and analyze sentiment
if user_input:
    response = chatbot_response(user_input)
    sentiment, color = analyze_sentiment(response)

    # Save chat history
    st.session_state["messages"].append((f"🧑‍💻 You: {user_input}", "", "black"))
    st.session_state["messages"].append((f"🤖 AI: {response}", sentiment, color))

    # Display chatbot response
    st.markdown(f'<p style="color:{color}">🤖 AI: {response} {sentiment}</p>', unsafe_allow_html=True)

    # Text-to-Speech (TTS) output
    if voice_assist:
        engine.say(response)
        engine.runAndWait()

# Button to clear chat history
if st.button("🗑️ Clear Chat"):
    st.session_state["messages"] = []
    st.experimental_rerun()
