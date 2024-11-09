# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def visualize_data(data):
    # Example of a bar chart
    if "category" in data.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(x="category", data=data)
        plt.title("Category Count")
        st.pyplot(plt)

    # Example of a time series line plot if date column exists
    if "date" in data.columns:
        plt.figure(figsize=(10, 6))
        data.groupby("date").size().plot(kind="line")
        plt.title("Data Over Time")
        st.pyplot(plt)
