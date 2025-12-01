# Import Libraries
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

# Import Data
conn = sqlite3.connect('bmarket_updated.db')
df = pd.read_sql("SELECT * FROM bank_marketing", conn)

# Target column for prediction
target = "Subscription Status"

# Encode
df = df.copy()
le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
        df[col] = le.fit_transform(df[col])

# Split Feature
X = df.drop(columns=[target])
y = df[target]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# MLP Model
model = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation="relu",
    solver="adam",
    max_iter=500,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))