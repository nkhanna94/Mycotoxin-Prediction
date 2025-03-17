import pickle
import numpy as np
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Vomitoxin (DON) Prediction", 
    page_icon="🌽", 
    layout="centered"
)

# Load the trained model
with open("deployment/model.pkl", "rb") as f:
    model = pickle.load(f)

# Load scalers
with open("deployment/x_scaler.pkl", "rb") as f:
    x_scaler = pickle.load(f)

with open("deployment/y_scaler.pkl", "rb") as f:
    y_scaler = pickle.load(f)

# Sidebar
st.sidebar.header("About the Model")
st.sidebar.write("""
🔍 **Purpose:**  
This app predicts **Deoxynivalenol (DON) levels** in corn using **hyperspectral imaging (HSI) data**.

📏 **Measurement Unit:**  
Results are given in **parts per billion (ppb)**.
""")

st.sidebar.markdown("---")
st.sidebar.write("👩🏻‍💻 *Built as part of an Internship Assignment*")

# Main UI
st.title("🌽 Vomitoxin (DON) Prediction")
st.markdown("Predict **Deoxynivalenol (DON) concentration** in **ppb** using advanced **Machine Learning**.")

st.write("### 🔢 Enter Feature Values")
user_input = st.text_area(
    "Input comma-separated values:", 
    placeholder="Example: 0.12, 1.45, -0.98, 2.76, ...", 
    height=100
)

if st.button("🔍 Predict"):
    try:
        # Convert input text to a NumPy array
        user_features = np.array([float(x) for x in user_input.split(",")]).reshape(1, -1)

        # Validate input size
        if user_features.shape[1] != x_scaler.n_features_in_:
            st.error(f"⚠ Expected {x_scaler.n_features_in_} features, but got {user_features.shape[1]}.")
        else:
            # Scale input
            user_input_scaled = x_scaler.transform(user_features)

            # Predict & Unscale
            prediction_scaled = model.predict(user_input_scaled)
            prediction = y_scaler.inverse_transform(prediction_scaled.reshape(-1, 1))

            # Display Result
            st.subheader("📊 Prediction Result")
            st.success(f"Predicted DON Level: **{prediction[0, 0]:.4f} ppb**")

    except ValueError:
        st.error("🚨 Invalid input! Please enter numerical values separated by commas.")

# Footer
st.markdown("---")
st.markdown("👧🏻💻 *Developed as part of a machine learning pipeline for predicting mycotoxin levels in corn.*")
