# Import Libraries
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Import Data
conn = sqlite3.connect('bmarket_updated.db')
df = pd.read_sql("SELECT * FROM bank_marketing", conn)

# Target column for prediction
target = "Subscription Status"

# Encode
df2 = df.copy()
le = LabelEncoder()

for col in df2.columns:
    if df2[col].dtype == "object":
        df2[col] = df2[col].fillna("Unknown")
        df2[col] = le.fit_transform(df2[col])

# Split feature
X = df2.drop(columns=[target])
y = df2[target]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# RF model
rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    random_state=42
)

rf.fit(X_train, y_train)

# Evaluate
preds = rf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))