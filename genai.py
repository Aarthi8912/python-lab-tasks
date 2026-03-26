
import streamlit as st
from transformers import pipeline
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

sentiment_model = pipeline("sentiment-analysis")

st.title("🤖 AI Chatbot + Sentiment Analysis")

st.header("📊 Sentiment Analysis")
text = st.text_area("Enter text")

if st.button("Analyze"):
    if text:
        result = sentiment_model(text)
        st.write(result)

st.header("💬 Chatbot")
msg = st.text_input("Ask something")

if st.button("Send"):
    if msg:
        response = model.generate_content(msg)
        st.write(response.text)
