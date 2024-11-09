# app.py

import streamlit as st
from data_preprocessing import preprocess_data
from data_analysis import analyze_data
from visualization import visualize_data
from ai_training import train_ai_agent
from logging_notification import send_upload_log, send_training_log
import os

st.title("Document Analysis and Visualization Application")

# Upload section
uploaded_file = st.file_uploader("Upload your .xls or .csv file", type=["xls", "csv"])
if uploaded_file:
    # Check file size limit (8MB)
    if uploaded_file.size > 8 * 1024 * 1024:  # 8MB limit
        st.error("File size should be less than 8MB")
    else:
        # Save the uploaded file temporarily
        file_path = f"temp_files/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Preprocess data
        data = preprocess_data(file_path)
        
        # Analyze data
        analysis_results = analyze_data(data)
        
        # Display analysis results
        st.write("Analysis Results:")
        st.write(analysis_results)
        
        # Visualize data
        visualize_data(data)
        
        # AI Training
        st.write("Training AI Agent...")
        train_ai_agent(data, log=True)  # Log set to True to log each training session
        
        # Send training log to Telegram
        send_training_log(uploaded_file.name, status="completed")
        
        # Logging and notification for upload details
        send_upload_log(uploaded_file.name, uploaded_file.type, st.request.remote_ip, st.request.headers.get('user-agent'))
        
        # File download options
        st.download_button("Download Table (.xls)", file_path)
        st.download_button("Download Visualization (.jpg)", "path_to_visualization.jpg")
        
        # Schedule file for deletion
        st.session_state["uploaded_file_path"] = file_path

def cleanup_file():
    file_path = st.session_state.get("uploaded_file_path")
    if file_path and os.path.exists(file_path):
        os.remove(file_path)

st.on_session_expired(cleanup_file)
