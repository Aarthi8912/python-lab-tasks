
import pandas as pd
import numpy as np
import nltk
import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


nltk.download('stopwords')

df = pd.read_csv("spam.csv", encoding="latin-1")

df = df.rename(columns={"v1": "label", "v2": "message"})

df = df[["label", "message"]]

print("HEAD")
print(df.head())

df["label"] = df["label"].map({"ham": 0, "spam": 1})

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = re.sub("[^a-zA-Z]", " ", text)   
    text = text.lower()
    words = text.split()

    words = [ps.stem(word) for word in words if word not in stop_words]

    return " ".join(words)

df["clean_text"] = df["message"].apply(preprocess)

print("\nCLEANED TEXT")
print(df[["message", "clean_text"]].head())

tfidf = TfidfVectorizer(max_features=3000)

X = tfidf.fit_transform(df["clean_text"]).toarray()
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("\nACCURACY:", accuracy_score(y_test, y_pred))

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))