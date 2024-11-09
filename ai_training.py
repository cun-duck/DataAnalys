# ai_training.py

from sklearn.linear_model import LogisticRegression
import joblib
from logging_notification import send_log

def train_ai_agent(data, log=False):
    # Simple AI model training with Logistic Regression as an example
    # Here assuming 'target' as the label for demonstration
    if "target" in data.columns:
        X = data.drop(columns=["target"])
        y = data["target"]
        model = LogisticRegression()
        model.fit(X, y)
        joblib.dump(model, "model.joblib")  # Save model
        
        if log:
            send_log("Training complete. Model updated.")
