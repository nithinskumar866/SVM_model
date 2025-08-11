import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib
import os

# Load the dataset
data = pd.read_excel("dataset/realistic_fake_diabetes_data.xlsx")

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the SVM model
model = SVC(probability=True)
model.fit(X_train_scaled, y_train)

# Save model and scaler
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/svm.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Model and scaler saved in /model/")
