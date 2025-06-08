# app.py

import streamlit as st

st.set_page_config(page_title="Restaurant Review Sentiment App", layout="wide")

st.title("Restaurant Review Sentiment Analysis App")

st.sidebar.title("Navigation")

# Navigation is handled automatically via Streamlit multi-page feature.
st.write("Please select a page from the sidebar to begin.")
