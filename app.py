from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model/svm.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

from flask import send_file

@app.route('/download-dataset')
def download_dataset():
    file_path = r'dataset/realistic_fake_diabetes_data.xlsx'
    return send_file(file_path, as_attachment=True)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(request.form.get(f)) for f in [
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
            "BMI", "DiabetesPedigreeFunction", "Age"
        ]]
        input_df = pd.DataFrame([features], columns=[
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
            "BMI", "DiabetesPedigreeFunction", "Age"
        ])

        scaled_input = scaler.transform(input_df)
        pred = model.predict(scaled_input)[0]
        confidence = model.predict_proba(scaled_input)[0][pred] * 100

        result = "Positive for Diabetes" if pred == 1 else "Negative for Diabetes"
        return render_template("index.html", prediction=result, confidence=round(confidence, 2))

    except Exception as e:
        return render_template("index.html", prediction="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
