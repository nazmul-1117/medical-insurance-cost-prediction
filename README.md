# 💰 Medical Insurance Cost Prediction Using Linear Regression

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![License](https://img.shields.io/badge/License-Academic-green)

---

## 📌 Project Overview

This project implements a **Multiple Linear Regression model** to predict medical insurance charges based on demographic and health-related features.

The model is trained using the **Medical Cost Personal Dataset** and deployed using **Streamlit** as an interactive web application.

This project demonstrates:

* End-to-end Machine Learning workflow
* Pipeline-based preprocessing
* Model evaluation & diagnostics
* Deployment using Streamlit

---

## 📊 Dataset Description

Features used:

| Feature  | Type        | Description                |
| -------- | ----------- | -------------------------- |
| age      | Numerical   | Age of primary beneficiary |
| sex      | Categorical | Gender                     |
| bmi      | Numerical   | Body Mass Index            |
| children | Numerical   | Number of dependents       |
| smoker   | Categorical | Smoking status             |
| region   | Categorical | Residential region         |
| charges  | Target      | Medical insurance cost     |

---

## ⚙️ Project Architecture

```
medical-insurance-cost-prediction/
│
├── data/
├── notebooks/
├── src/
├── model/insurance_model.pkl
├── app.py
├── requirements.txt
├── README.md
└── report/
```

---

## 🧠 Machine Learning Pipeline

### 🔹 Data Preprocessing

* ColumnTransformer
* StandardScaler → (age, bmi, children)
* OneHotEncoder (drop="first") → (sex, smoker, region)

### 🔹 Model

* Multiple Linear Regression (OLS)
* Ridge Regression (optional comparison)
* Train-Test Split: 80-20
* Random State: 42

### 🔹 Evaluation Metrics

* R² Score
* MAE
* RMSE
* Actual vs Predicted Plot
* Residual Plot
* Residual Distribution

---

## 📈 Model Evaluation

The model was evaluated using regression performance metrics:

* High R² score indicating good explanatory power
* Low MAE and RMSE showing strong predictive performance
* Residual plots verified assumption validity

---

## 💾 Model Saving

The complete preprocessing + model pipeline is saved using:

```python
joblib.dump(pipeline, "model/insurance_model.pkl")
```

This ensures consistent predictions during deployment.

---

## 🌐 Streamlit Deployment

The web app allows users to input:

* Age
* Sex
* BMI
* Number of children
* Smoker status
* Region

And instantly receive predicted insurance charges.

Run locally:

```bash
streamlit run app.py
```

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## 🎯 Key Learning Outcomes

* Practical implementation of regression modeling
* Building production-ready ML pipelines
* Model deployment using Streamlit
* Regression diagnostics & interpretation

---

## 👨‍💻 Author

**Md. Nazmul Hossain**\
4th Year Undergraduate Student\
Machine Learning Enthusiast

---