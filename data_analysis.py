# data_analysis.py

import pandas as pd

def analyze_data(data):
    # Basic descriptive statistics
    desc_stats = data.describe(include="all")
    return desc_stats
