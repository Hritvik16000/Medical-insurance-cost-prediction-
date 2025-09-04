# 💸 Medical Insurance Cost Prediction

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)  
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)](https://mlflow.org/)  

Predicting medical insurance costs using machine learning models with full EDA, model evaluation, MLflow experiment tracking, and an interactive Streamlit web app.

---

## 📌 Project Overview
This project builds an end-to-end pipeline for predicting **medical insurance charges** based on demographic and lifestyle features.  
It includes:
- Data cleaning & preprocessing  
- Exploratory Data Analysis (EDA)  
- Training and evaluation of multiple regression models  
- Experiment tracking using **MLflow**  
- Deployment of the best model with a **Streamlit app**  

Dataset: [`medical_insurance.csv`](medical_insurance.csv)

---

## 📊 Features
- **EDA**: Distributions, correlations, outlier detection, multivariate analysis  
- **Models**: Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting, XGBoost  
- **Metrics**: RMSE, MAE, R²  
- **Experiment Tracking**: MLflow logs metrics, parameters, and artifacts  
- **Deployment**: Interactive Streamlit app for real-time predictions  

---

## ⚙️ Tech Stack
- **Language**: Python 3.11  
- **Libraries**: Pandas, NumPy, Matplotlib, Scikit-learn, XGBoost, SHAP  
- **Tracking**: MLflow  
- **Deployment**: Streamlit  
- **Database (optional)**: SQLite  

---

## 📂 Project Structure
medical-insurance/
│── medical_insurance.csv # dataset
│── 01_eda.ipynb # exploratory data analysis
│── 02_modeling.ipynb # model training + MLflow logging
│── app.py # Streamlit web app
│── requirements.txt # dependencies
│── README.md # project documentation


---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Hritvik16000/Medical-insurance-cost-prediction-.git
cd Medical-insurance-cost-prediction-

python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows (PowerShell)
pip install -r requirements.txt
jupyter notebook
mlflow ui --port 5001
```
-------------------------------

streamlit run app.py

The app allows you to input:
Age
Sex
BMI
Smoker / Non-smoker
Number of children
Region
and outputs the predicted insurance cost.

📊 Sample Results
Model	RMSE	MAE	R²
Linear Regression	~6180	~4300	0.74
Ridge Regression	~6175	~4295	0.74
Lasso Regression	~6200	~4310	0.73
Random Forest	~3400	~2100	0.88
Gradient Boosting	~3100	~2000	0.90
XGBoost	~2900	~1900	0.91
(metrics may vary slightly depending on train/test split)
===========================================================
✅ Deliverables

Cleaned dataset (medical_insurance.csv)
EDA notebook with plots and insights
Model training notebook with MLflow logs
Saved best model pipeline (model_pipeline.joblib)
Streamlit app (app.py) for deployment
📜 License
This project is open-source under the MIT License.
👤 Author
Hritvik Dadhich
