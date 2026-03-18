import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("titanic.csv")

print("HEAD")
print(df.head())

print("\nCOLUMNS")
print(df.columns)


df = df[["Survived", "Pclass", "Age", "Fare"]]


df["Age"] = df["Age"].fillna(df["Age"].mean())

X = df[["Pclass", "Age", "Fare"]]
y_class = df["Survived"]   # Logistic
y_reg = df["Fare"]         # Linear


X_train, X_test, y_train_class, y_test_class = train_test_split(X, y_class, test_size=0.2, random_state=42)
_, _, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)

# -----------------------
# LOGISTIC REGRESSION
# -----------------------

log_model = LogisticRegression(max_iter=200)
log_model.fit(X_train, y_train_class)

y_pred_class = log_model.predict(X_test)

print("\nLOGISTIC REGRESSION")
print("Predictions:", y_pred_class[:10])
print("Accuracy:", accuracy_score(y_test_class, y_pred_class))

# -----------------------
# LINEAR REGRESSION
# -----------------------

lin_model = LinearRegression()
lin_model.fit(X_train, y_train_reg)

y_pred_reg = lin_model.predict(X_test)

print("\nLINEAR REGRESSION")
print("Predicted Fare:", y_pred_reg[:10])


mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)
