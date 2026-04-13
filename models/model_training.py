import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Load your dataset
df = pd.read_csv("data/Crop_recommendation_dataset.csv")

print("Dataset Loaded Successfully!\n")
print(df.head())

# Features & Target
X = df.drop("label", axis=1)
y = df["label"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "KNN": KNeighborsClassifier()
}

best_model = None
best_score = 0

print("\nModel Performance:\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.4f}")

    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("-"*50)

    if acc > best_score:
        best_score = acc
        best_model = model

# Save best model
joblib.dump(best_model, "crop_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print(f"\nBest Model Saved with Accuracy: {best_score:.4f}")
