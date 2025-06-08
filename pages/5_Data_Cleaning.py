# pages/5_Data_Cleaning.py

import streamlit as st
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Download stopwords once
nltk.download('stopwords')

st.title("Data Cleaning & Vectorization")

if 'df' not in st.session_state:
    st.error("Please load data first from 'Data Loading' page.")
    st.stop()

df = st.session_state['df']

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

# Apply cleaning
st.write("Cleaning text data...")
df['Cleaned_Review'] = df['Review'].apply(clean_text)

st.write("Sample Cleaned Data:")
st.write(df[['Review', 'Cleaned_Review']].head())

# Vectorization options
st.subheader("Vectorization")

vectorizer_choice = st.radio("Select Vectorizer:", ('CountVectorizer', 'TF-IDF Vectorizer'))

if st.button("Transform Data"):

    if vectorizer_choice == 'CountVectorizer':
        vectorizer = CountVectorizer()
    else:
        vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(df['Cleaned_Review'])
    y = df['Liked']

    # Save to session state
    st.session_state['X_full'] = X
    st.session_state['y'] = y
    st.session_state['vectorizer'] = vectorizer

    st.success("Vectorization complete ✅")

    # Display vectorizer output
    st.subheader("Vocabulary Extracted:")
    st.write(list(vectorizer.get_feature_names_out())[:50])  # show first 50 words

    st.subheader("Shape of Transformed Data:")
    st.write(X.shape)

    st.subheader("Sample Transformed Data (Dense Array Format):")
    st.write(pd.DataFrame(X.toarray()).head())
