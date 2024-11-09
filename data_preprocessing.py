# data_preprocessing.py

import pandas as pd

def preprocess_data(file_path):
    # Load data based on file type
    if file_path.endswith(".csv"):
        data = pd.read_csv(file_path)
    else:
        data = pd.read_excel(file_path)
    
    # Basic preprocessing: filling missing values, formatting dates
    data.fillna(method="ffill", inplace=True)
    for col in data.columns:
        if "date" in col.lower():
            data[col] = pd.to_datetime(data[col], errors="coerce")
    return data
