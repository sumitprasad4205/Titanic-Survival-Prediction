
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

## 🔧 Feature Engineering
Created the following features:

- FamilySize – Total family members travelling together
- IsAlone – Whether the passenger was travelling alone
- HasCabin – Whether cabin information was available
- Deck – Extracted from the cabin number
- Title – Extracted from passenger names and grouped into categories

## 🛠️ Tech Stack

* Python
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn
* Flask
* HTML & CSS
* Jupyter Notebook

## 🤖 Models Used

* Random Forest Classifier
* Logistic Regression
* Support Vector Machine (SVM)


## 📊 Model Performance

Compared three classification algorithms:

| Model | Accuracy |
|---|---:|
| Random Forest | 79.3% |
| Logistic Regression | 84.4% |
| SVM | 83.8% |

Precision / Recall / F1-Score:

| Class | Precision | Recall | F1 |
|---|---:|---:|---:|
| 0 | 0.860 | 0.891 | 0.875 |
| 1 | 0.815 | 0.768 | 0.791 |

### 🏆 Best Model

Logistic Regression — 84.4% Accuracy

All models were evaluated on the **test dataset** using the same stratified train-test split.

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
