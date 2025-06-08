# pages/2_Introduction.py

import streamlit as st

st.title("Introduction")

st.write("""
Welcome to the **Restaurant Review Sentiment Analysis App**. 🍽️📝

This application is designed to help analyze restaurant reviews and predict whether the feedback is **positive** or **negative** using Machine Learning.

### 📊 App Features:

- Upload your dataset (.tsv file)
- Perform Data Visualization (Bar Chart, Word Cloud)
- Text Cleaning & Vectorization (CountVectorizer or TF-IDF)
- Train Logistic Regression Model
- Predict sentiment for new reviews with probability scores

---

👉 Please proceed using the sidebar to explore each section step-by-step.
""")
