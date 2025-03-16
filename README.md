# Mycotoxin Prediction using Hyperspectral Imaging

## Overview
This repository contains a machine learning pipeline for predicting mycotoxin (DON) levels in corn using hyperspectral imaging data. It includes data preprocessing, feature engineering, model training, evaluation, and deployment via a Flask API and a Streamlit app for real-time predictions.

## Repository Structure
```
📂 mycotoxin-prediction
│-- 📂 data/                # Raw data files
│-- 📂 notebooks/           # Jupyter notebooks for EDA, modeling, and evaluation
│-- 📂 models/              # Saved trained models
│-- 📂 src/                 # Core scripts for preprocessing, training, and inference
│   ├── train.ipynb         # Model training and evaluation
│   ├── predict.py          # Inference script
│-- 📂 deployment/          # Deployment scripts
│   ├── app.py              # Flask API for serving predictions
│   ├── streamlit_app.py    # Interactive app for real-time predictions
│-- README.md               # Project documentation
│-- requirements.txt        # Required dependencies
│-- report.pdf              # Summary of findings and methodology
```

## Setup Instructions
1. **Clone the repository**  
   ```bash
   git clone https://github.com/nkhanna94/mycotoxin-prediction.git
   cd mycotoxin-prediction
   ```

2. **Create a virtual environment and install dependencies**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run model training**
   ```bash
   python src/train.py
   ```

4. **Run the Flask API**
   ```bash
   python deployment/app.py
   ```

5. **Run the Streamlit App**
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
- Feature selection significantly improved model performance.
- Random Forest and XGBoost yielded the best results after hyperparameter tuning.

---

**Created by [Niharika Khanna](https://github.com/nkhanna94). For any queries, DM.**
