Got it — you want the README in the **same clean, sectioned style** we used for your previous project docs, without extra chatty parts, but still well-structured and visually appealing.

Here’s your README rewritten in that format:

---

# 🩺 Diabetes Prediction System using SVM

## 📌 Overview

A **web-based machine learning application** built using **Flask** and **Support Vector Machine (SVM)** to predict the likelihood of diabetes based on medical parameters.
Provides **prediction results**, **confidence score**, and an option to **download a sample dataset**.

---

## 📊 Features

* Web interface with **Flask + HTML/CSS**.
* Predicts **Positive** or **Negative** for diabetes.
* Displays **confidence percentage** for predictions.
* Downloadable **sample dataset** for quick testing.
* **Validation rules** for realistic input ranges.
* Responsive and modern UI.

---

## 🗂 Project Structure

```
diabetes_svm/
│
├── dataset/
│   └── realistic_fake_diabetes_data.xlsx     # Sample dataset
│
├── model/
│   ├── svm.pkl                               # Trained SVM model
│   └── scaler.pkl                            # StandardScaler
│
├── templates/
│   └── index.html                            # UI template
│
├── app.py                                    # Flask app
├── train_model.py                            # Model training script
└── README.md                                 # Documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-repo/diabetes_svm.git
cd diabetes_svm
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
flask
pandas
numpy
scikit-learn
joblib
openpyxl
```

---

## 🚀 Usage

### Train Model (Optional)

```bash
python train_model.py
```

### Run Application

```bash
python app.py
```

Open browser at:

```
http://127.0.0.1:5000
```

---

## 📥 Sample Dataset

* Download directly from the home page
* Or via:

```
http://127.0.0.1:5000/download-dataset
```

---

## 📋 Input Parameters

| Parameter                  | Type    | Range     |
| -------------------------- | ------- | --------- |
| Pregnancies                | Integer | 0 – 15    |
| Glucose (mg/dL)            | Integer | 50 – 200  |
| Blood Pressure (mm Hg)     | Integer | 40 – 120  |
| Skin Thickness (mm)        | Integer | 0 – 100   |
| Insulin (IU/mL)            | Integer | 0 – 300   |
| BMI                        | Float   | 0 – 60    |
| Diabetes Pedigree Function | Float   | 0.0 – 2.5 |
| Age                        | Integer | 21 – 90   |

---

## 📊 Example

**Input**

```
Pregnancies: 2
Glucose: 130
BloodPressure: 70
SkinThickness: 20
Insulin: 85
BMI: 25.6
DiabetesPedigreeFunction: 0.45
Age: 35
```

**Output**

```
Prediction: Negative
Confidence: 87.45%
```
---
Done By -Nithin.S


---

## 📜 License

This project is for educational purposes.
Free to modify and use.

---


