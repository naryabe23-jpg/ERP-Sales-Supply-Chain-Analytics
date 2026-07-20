"""
ERP Sales & Supply Chain Analytics

Data Cleaning Pipeline

Author: Nitya
"""

import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DATA = BASE_DIR / "data" / "raw"
PROCESSED_DATA = BASE_DIR / "data" / "processed"

PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Load datasets
# -----------------------------

customers = pd.read_csv(RAW_DATA / "customers.csv")
orders = pd.read_csv(RAW_DATA / "orders.csv")
order_items = pd.read_csv(RAW_DATA / "order_items.csv")
products = pd.read_csv(RAW_DATA / "products.csv")

print("Datasets Loaded Successfully\n")

# -----------------------------
# Function
# -----------------------------

def clean_dataframe(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove leading/trailing spaces
    df.columns = df.columns.str.strip()

    object_cols = df.select_dtypes(include="object").columns

    for col in object_cols:
        df[col] = df[col].str.strip()

    return df

# -----------------------------
# Clean datasets
# -----------------------------

customers = clean_dataframe(customers)
orders = clean_dataframe(orders)
order_items = clean_dataframe(order_items)
products = clean_dataframe(products)

# -----------------------------
# Handle Missing Values
# -----------------------------

customers = customers.fillna("Unknown")

orders = orders.fillna("Unknown")

products = products.fillna("Unknown")

order_items = order_items.fillna(0)

# -----------------------------
# Convert Dates
# -----------------------------

date_columns = [
    "order_date",
    "ship_date"
]

for col in date_columns:

    if col in orders.columns:

        orders[col] = pd.to_datetime(
            orders[col],
            errors="coerce"
        )

# -----------------------------
# Save Clean Data
# -----------------------------

customers.to_csv(
    PROCESSED_DATA / "customers_clean.csv",
    index=False
)

orders.to_csv(
    PROCESSED_DATA / "orders_clean.csv",
    index=False
)

order_items.to_csv(
    PROCESSED_DATA / "order_items_clean.csv",
    index=False
)

products.to_csv(
    PROCESSED_DATA / "products_clean.csv",
    index=False
)

print("\nClean datasets exported successfully.")
