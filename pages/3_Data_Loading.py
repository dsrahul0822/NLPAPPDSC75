# pages/3_Data_Loading.py

import streamlit as st
import pandas as pd

st.title("Data Loading")

st.write("Please upload a `.tsv` file with restaurant reviews.")

# File uploader
uploaded_file = st.file_uploader("Upload TSV File", type=["tsv"])

# Load data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, delimiter="\t")
    st.session_state['df'] = df
    st.success("File uploaded and loaded successfully!")
else:
    st.warning("No file uploaded. Using default dataset.")
    try:
        df = pd.read_csv("data/Restaurant_Reviews.tsv", delimiter="\t")
        st.session_state['df'] = df
    except:
        st.error("Default dataset not found. Please upload file.")
        st.stop()

# Display data
st.subheader("Sample Data")
st.write(df.head())

st.subheader("Dataset Info")
st.write(f"Total Rows: {df.shape[0]}")
st.write(f"Total Columns: {df.shape[1]}")
st.write(f"Columns: {df.columns.tolist()}")

# Store for next pages
st.session_state.df_loaded = True
