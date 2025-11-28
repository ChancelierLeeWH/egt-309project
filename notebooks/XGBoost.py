# Import Libraries
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
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

# Split feature
X = df.drop(columns=[target])
y = df[target]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=5,
    eval_metric="logloss"
)

model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))