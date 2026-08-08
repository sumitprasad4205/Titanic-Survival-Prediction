
# 🚢 Titanic Survival Prediction

A machine learning project that predicts whether a passenger survived the Titanic disaster using different classification algorithms. The best-performing model was integrated into a **Flask web application** for real-time predictions.

## 📌 About the Project

This project uses the **Titanic dataset** to predict passenger survival based on features such as passenger class, age, sex, fare, and other passenger information.

The workflow includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering
* Model training
* Model comparison
* Model evaluation
* Flask deployment

## 🛠️ Tech Stack

* Python
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn
* Flask
* HTML & CSS
* Jupyter Notebook

## 🤖 Models Used

* Logistic Regression
* Support Vector Machine (SVM)
* Gaussian Naive Bayes

## 📊 Model Performance

All models were evaluated on the **test dataset** using the same stratified train-test split.

| Model                   | Test Accuracy |
| ----------------------- | ------------: |
| 🥇 Logistic Regression  |    **83.24%** |
| 🥈 SVM                  |    **82.12%** |
| 🥉 Gaussian Naive Bayes |    **80.45%** |

### 🏆 Best Model

**Logistic Regression** achieved the highest test accuracy of **83.24%**.

### Logistic Regression — Test Results

| Class                | Precision | Recall |   F1-Score |
| -------------------- | --------: | -----: | ---------: |
| 0 — Did Not Survive  |    85.71% | 87.27% |     86.49% |
| 1 — Survived         |    79.10% | 76.81% |     77.94% |
| **Overall Accuracy** |           |        | **83.24%** |

The model achieved a **macro F1-score of 82.21%** and a **weighted F1-score of 83.19%**.

## 🌐 Flask Web Application

The best-performing Logistic Regression model was integrated into a **Flask web application**.

Users can enter passenger details through the web interface, and the application returns a prediction:

* ✅ **Passenger Survived**
* ❌ **Passenger Not Survived**

## 📈 Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

The dataset was split using **`stratify=y`** to maintain a similar class distribution in the training and test sets.

## 📂 Project Structure

```text
Titanic-Survival-Prediction/
│
├── app.py
├── model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── main.ipynb
└── README.md
```

## 📊 Dataset

The project uses the **Titanic - Machine Learning from Disaster** dataset from Kaggle.

