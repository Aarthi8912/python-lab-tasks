import google.generativeai as genai
from transformers import pipeline
import os
from dotenv import load_dotenv
from prompts import chat_prompt


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")


sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


while True:
    print("\n==== AI TERMINAL APP ====")
    print("1. Sentiment Analysis")
    print("2. Chatbot")
    print("3. Exit")

    choice = input("Enter choice: ")

   
    if choice == "1":
        text = input("Enter text: ")
        result = sentiment_model(text)
        print("Sentiment:", result)

    
    elif choice == "2":
        user_input = input("Ask something: ")
        prompt = chat_prompt(user_input)
        response = model.generate_content(prompt)
        print("Bot:", response.text)

    
    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")