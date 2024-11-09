# ai_training.py

import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import numpy as np

def identify_column_type(column_data):
    """Function to identify the column type (numeric, categorical, or date)."""
    if pd.to_datetime(column_data, errors='coerce').notna().all():
        return 'datetime'
    elif pd.to_numeric(column_data, errors='coerce').notna().all():
        return 'numeric'
    else:
        return 'categorical'

def train_ai_agent(data, log=False):
    try:
        st.write("Training AI agent with data...")
        
        # Identify column types using unsupervised learning or heuristic methods
        column_types = {}
        
        for column in data.columns:
            column_types[column] = identify_column_type(data[column])
        
        st.write("Identified column types:")
        st.write(column_types)
        
        # Convert categorical columns to numerical using LabelEncoder for easier processing
        label_encoders = {}
        for column, col_type in column_types.items():
            if col_type == 'categorical':
                label_encoders[column] = LabelEncoder()
                data[column] = label_encoders[column].fit_transform(data[column].astype(str))
        
        # Use unsupervised learning (e.g., K-means clustering) to learn patterns in data
        kmeans = KMeans(n_clusters=3, random_state=0)
        kmeans.fit(data.select_dtypes(include=[np.number]))  # Only use numeric data for clustering
        
        st.write("Clustering result (K-means):")
        st.write(kmeans.labels_)
        
        # Log the results if requested
        if log:
            st.write("Training log: AI model has been trained with the uploaded data.")
        
        st.write("AI training complete.")
        
    except Exception as e:
        st.error(f"Error occurred during AI training: {str(e)}")
        # You can log the error details here if needed or send it to your bot
