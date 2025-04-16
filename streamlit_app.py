import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Set page configuration
st.set_page_config(page_title="Model Comparison", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .main-title {
            color: purple;
            font-size: 18px;
            font-weight: bold;
        }
        .sub-title {
            color: purple;
            font-size: 14px;
            font-weight: bold;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar model selection
st.sidebar.title("Model Selector")
selected_models = []
if st.sidebar.checkbox("Linear Regression"):
    selected_models.append("Linear Regression")
if st.sidebar.checkbox("Decision Tree Regressor"):
    selected_models.append("Decision Tree Regressor")

# Load dataset
df = pd.read_csv("BostonHousing.csv")
st.markdown('<p class="main-title">🏡 Boston Housing Dataset Preview</p>', unsafe_allow_html=True)
st.write(df.head())

# Prepare data
X = df.drop(["medv"], axis=1)
y = df["medv"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Available models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree Regressor": DecisionTreeRegressor(random_state=42)
}

# Train and evaluate models
if selected_models:
    st.markdown('<p class="main-title">📊 Model Performance Metrics</p>', unsafe_allow_html=True)
    for model_name in selected_models:
        model = models[model_name]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Metrics
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        # Streamlit display
        st.markdown(f'<p class="sub-title">{model_name}</p>', unsafe_allow_html=True)
        st.success(f"MAE: {mae:.3f}")
        st.success(f"MSE: {mse:.3f}")
        st.success(f"RMSE: {rmse:.3f}")
else:
    st.warning("Please select at least one model from the sidebar to view performance metrics.")
