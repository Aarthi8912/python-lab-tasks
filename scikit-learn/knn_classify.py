
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



df = pd.read_csv("titanic.csv")


df = df[["Survived", "Pclass", "Age", "Fare"]]


df["Age"] = df["Age"].fillna(df["Age"].mean())


X = df[["Pclass", "Age", "Fare"]]
y = df["Survived"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


#KNN MODEL


model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("ACCURACY:", accuracy_score(y_test, y_pred))

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))


train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print("\nTraining Accuracy:", train_acc)
print("Testing Accuracy:", test_acc)

if train_acc > test_acc:
    print("Possible Overfitting")
else:
    print("Model is balanced or Underfitting")


cv_scores = cross_val_score(model, X, y, cv=5)

print("\nCross Validation Scores:", cv_scores)
print("Average CV Score:", np.mean(cv_scores))