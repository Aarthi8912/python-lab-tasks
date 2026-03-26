
import streamlit as st
from transformers import pipeline
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# Sentiment model
sentiment_model = pipeline("sentiment-analysis")

# UI
st.title("🤖 AI Chatbot + Sentiment Analysis")

# Sentiment
st.header("📊 Sentiment Analysis")
text = st.text_area("Enter text")

if st.button("Analyze"):
    if text:
        result = sentiment_model(text)
        st.write(result)

# Chatbot
st.header("💬 Chatbot")
msg = st.text_input("Ask something")

if st.button("Send"):
    if msg:
        response = model.generate_content(msg)
        st.write(response.text)