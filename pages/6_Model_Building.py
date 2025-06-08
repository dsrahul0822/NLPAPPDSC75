# pages/6_Model_Building.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

st.title("Model Building")

# Check if previous data is available
if 'X_full' not in st.session_state or 'y' not in st.session_state:
    st.error("Please complete Data Cleaning before proceeding.")
    st.stop()

X_full = st.session_state['X_full']
y = st.session_state['y']
vectorizer = st.session_state['vectorizer']

# Get maximum number of features available
max_features = X_full.shape[1]

st.subheader("Feature Selection")

k = st.slider("Select number of top features to use:", min_value=100, max_value=max_features, value=min(1000, max_features), step=100)

if st.button("Train Model"):

    # Feature Selection
    selector = SelectKBest(chi2, k=k)
    X_selected = selector.fit_transform(X_full, y)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

    # Model Training
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    st.subheader("Model Performance")
    st.write(f"Accuracy: {accuracy*100:.2f}%")

    st.subheader("Classification Report")
    st.text(classification_report(y_test, y_pred))

    st.subheader("Confusion Matrix")
    st.write(confusion_matrix(y_test, y_pred))

    # Save model & selector for Prediction page
    st.session_state['model'] = model
    st.session_state['selector'] = selector

    st.success("Model training completed and saved!")
