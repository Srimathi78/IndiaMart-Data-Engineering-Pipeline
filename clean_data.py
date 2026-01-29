import json
import pandas as pd
import os

RAW_FILE = "data/raw/alibaba_raw.json"
CLEAN_FILE = "data/processed/alibaba_clean.csv"

if not os.path.exists(RAW_FILE):
    print("❌ Raw JSON file not found")
    exit()

with open(RAW_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

if not data:
    print("❌ No data available. Raw JSON is empty.")
    exit()

df = pd.DataFrame(data)

# Basic cleaning
df.drop_duplicates(inplace=True)
df["product_name"] = df["product_name"].str.strip()

os.makedirs("data/processed", exist_ok=True)
df.to_csv(CLEAN_FILE, index=False, encoding="utf-8")

print(f"✅ Cleaned data saved: {CLEAN_FILE}")
print(df.head())
