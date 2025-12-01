"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 1.0.0
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import logging

def split_data(df: pd.DataFrame):
    df = df.copy()
    target = "Subscription Status"
    
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")
            df[col] = le.fit_transform(df[col])

    X = df.drop(columns=[target])
    y = df[target]

    # Split Data
    return train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

def train_rf_model(X_train, y_train):
    rf = RandomForestClassifier(n_estimators=300, max_depth=None, random_state=42, class_weight="balanced")
    rf.fit(X_train, y_train)
    return rf

def train_xgb_model(X_train, y_train):
    xgb = XGBClassifier(n_estimators=200, learning_rate=0.1, max_depth=5, eval_metric="logloss", scale_pos_weight=8)
    xgb.fit(X_train, y_train)
    return xgb

def train_mlpclassifier_model(X_train, y_train):
    mlp = MLPClassifier(hidden_layer_sizes=(64, 32), activation="relu", solver="adam", max_iter=500, random_state=42)
    mlp.fit(X_train, y_train)
    return mlp

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)

    logger = logging.getLogger(__name__)
    logger.info(f"Model Accuracy: {acc}")
    logger.info("\nClassification Report:\n" + report)