import pandas as pd
import numpy as np
import sqlite3
import os

def clean_data() -> pd.DataFrame:
    """
    Loads raw data from SQLite and cleans it.
    """
    # --- 1. Load Data Directly (The Fix) ---
    # This bypasses the Catalog configuration errors
    db_path = "data/raw-data/bmarket.db"
    
    # Check if file exists to give a clear error if missing
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at: {os.path.abspath(db_path)}")

    # Connect and Read
    con = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM bank_marketing", con)
    con.close()
    
    # --- 2. Cleaning Logic (Same as before) ---
    df = df.copy()
    
    # Clean Age
    df['Age'] = df['Age'].astype(str).str.replace(' years', '', regex=False)
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)
    df.loc[(df['Age'] < 1) | (df['Age'] > 100), 'Age'] = median_age
    df['Age'] = df['Age'].astype(int)

    # Clean Occupation & Education
    df['Occupation'] = df['Occupation'].str.replace('.', '', regex=False)
    df['Education Level'] = df['Education Level'].str.replace('.', ' ', regex=False)
    df['Education Level'] = df['Education Level'].str.replace(r'basic \d+y', 'basic', regex=True)

    # Clean Contact & Calls
    df['Contact Method'] = df['Contact Method'].replace({'Cell': 'cellular', 'Telephone': 'telephone'})
    df.loc[df['Campaign Calls'] < 0, 'Campaign Calls'] = 0

    # Clean Credit Default
    df['Credit Default'] = df['Credit Default'].replace('unknown', 'no')
    
    return df