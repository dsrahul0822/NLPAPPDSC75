# pages/7_Prediction.py

import streamlit as st
import string
import numpy as np
from nltk.corpus import stopwords

st.title("Prediction Page")

# Check if model and pipeline are available
if 'model' not in st.session_state or 'vectorizer' not in st.session_state or 'selector' not in st.session_state:
    st.error("Please complete Model Building before prediction.")
    st.stop()

model = st.session_state['model']
vectorizer = st.session_state['vectorizer']
selector = st.session_state['selector']

# Text cleaning function (same as before)
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

# User input
user_input = st.text_area("Enter restaurant review for prediction:")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some review text.")
        st.stop()

    cleaned_text = clean_text(user_input)
    vectorized_text = vectorizer.transform([cleaned_text])
    selected_features = selector.transform(vectorized_text)

    prediction = model.predict(selected_features)[0]
    proba = model.predict_proba(selected_features)[0]

    if prediction == 1:
        st.success(f"Prediction: Positive Review ✅")
        st.write(f"Confidence: {proba[1]*100:.2f}% Positive")
    else:
        st.error(f"Prediction: Negative Review ❌")
        st.write(f"Confidence: {proba[0]*100:.2f}% Negative")
