import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')  
nltk.download('stopwords')

text = "This is a simple NLP example to demonstrate tokenization and stopword removal."

print("Original Text:")
print(text)

tokens = word_tokenize(text)
print("\nTokens:")
print(tokens)

stop_words = set(stopwords.words("english"))
filtered = [word for word in tokens if word.lower() not in stop_words]

print("\nAfter Removing Stopwords:")
print(filtered)