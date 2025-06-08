# pages/4_Data_Visualization.py

import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

st.title("Data Visualization")

# Check if data loaded
if 'df' not in st.session_state:
    st.error("Please load data first from 'Data Loading' page.")
    st.stop()

df = st.session_state['df']

# Bar Chart for Sentiment Distribution
st.subheader("Sentiment Distribution")

label_counts = df['Liked'].value_counts()
fig, ax = plt.subplots()
bars = ax.bar(label_counts.index.astype(str), label_counts.values, color=['skyblue', 'salmon'])
ax.set_xlabel("Sentiment (1=Positive, 0=Negative)")
ax.set_ylabel("Number of Reviews")
ax.set_title("Distribution of Reviews")

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + 0.3, yval + 5, yval)

st.pyplot(fig)

# Word Cloud
st.subheader("Word Cloud")

all_text = " ".join(df['Review'].values)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

fig_wc, ax_wc = plt.subplots(figsize=(15, 7.5))
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis('off')

st.pyplot(fig_wc)
