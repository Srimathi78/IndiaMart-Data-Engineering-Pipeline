import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import Counter

DATA_FILE = "data/processed/alibaba_clean.csv"

if not os.path.exists(DATA_FILE):
    print("❌ Cleaned data file not found. Run clean_data.py first.")
    exit()

df = pd.read_csv(DATA_FILE)

if df.empty:
    print("❌ No data available for EDA. DataFrame is empty.")
    exit()

print("\n📊 BASIC DATA OVERVIEW")
print(df.info())
print("\nSample rows:")
print(df.head())

# -------------------------
# Product name length stats
# -------------------------
df["name_length"] = df["product_name"].str.len()

print("\n📈 Name Length Statistics")
print(df["name_length"].describe())

# -------------------------
# Most common keywords
# -------------------------
all_words = " ".join(df["product_name"].str.lower()).split()
common_words = Counter(all_words)

# Remove common noise words
stopwords = {"and", "for", "with", "of", "to", "in", "on"}
filtered_words = {w: c for w, c in common_words.items() if w not in stopwords}

top_words = Counter(filtered_words).most_common(10)

print("\n🔑 Top Keywords in Product Names")
for word, count in top_words:
    print(f"{word}: {count}")

# -------------------------
# Visualization
# -------------------------
words, counts = zip(*top_words)

plt.figure(figsize=(8, 5))
plt.bar(words, counts)
plt.title("Top Keywords in Alibaba Electrical Products")
plt.xlabel("Keyword")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()

os.makedirs("reports", exist_ok=True)
plt.savefig("reports/top_keywords.png")
plt.show()

print("\n✅ EDA completed. Chart saved to reports/top_keywords.png")
