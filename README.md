# Mycotoxin Prediction using Hyperspectral Imaging

## Overview
This repository contains a machine learning pipeline for predicting mycotoxin (DON) levels in corn using hyperspectral imaging data. It includes data preprocessing, feature engineering, model training, evaluation, and deployment via a Flask API and a Streamlit app for real-time predictions.

## Repository Structure
```
📂 vomitoxin-prediction  
│-- 📂 data/                # Contains raw and preprocessed data files  
│-- 📂 notebooks/           # Jupyter notebook for exploratory data analysis (EDA), modeling, and evaluation  
│   ├── vomitoxin-prediction-using-xgb.ipynb  # Notebook for model training and evaluation  
│-- 📂 deployment/          # Deployment-related files  
│   ├── model.pkl           # Pretrained XGBoost model  
│   ├── x_scaler.pkl        # Feature scaler for input normalization  
│   ├── y_scaler.pkl        # Target scaler for output transformation  
│   ├── streamlit_app.py    # Streamlit web app for real-time predictions  
│-- README.md               # Project documentation and setup instructions  
│-- requirements.txt        # List of dependencies for the project  
│-- runtime.txt             # Specifies the Python version required for deployment  
```

## **Setup Instructions**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/nkhanna94/vomitoxin-prediction.git
   cd vomitoxin-prediction
   ```  

2. **Create a virtual environment and install dependencies**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```  

3. **Run the Streamlit App for Predictions**  
   ```bash
   streamlit run deployment/streamlit_app.py
   ```
   
## Model Development
- **Data Preprocessing:** Scaling, transformation, and outlier handling.
- **Feature Engineering:** Dimensionality reduction and correlation analysis.
- **Modeling:** Random Forest and XGBoost, optimized with Optuna.
- **Evaluation:** RMSE, MAE, R², and interpretability using SHAP.

## Deployment
- **Flask API:** Serves predictions via a RESTful endpoint.
- **Streamlit App:** Interactive UI for users to upload spectral data and get predictions.

## Key Findings  
- **XGBoost outperforms Random Forest** with a higher test R² (0.6756 vs. 0.6502), making it the preferred model.  
- **Residuals follow a bell-shaped curve,** indicating normally distributed errors.  
- **Most actual vs. predicted values** are clustered around zero, with few significant deviations.

---

**Created by [Niharika Khanna](https://github.com/nkhanna94). For any queries, DM.**
