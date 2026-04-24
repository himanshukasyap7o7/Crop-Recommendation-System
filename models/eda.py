import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/Crop_recommendation_dataset.csv")

print("Dataset Loaded!")

# -----------------------------
# 1. HEATMAP (Correlation)
# -----------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.drop("label", axis=1).corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# -----------------------------
# 2. BAR CHART 
# -----------------------------
plt.figure(figsize=(12,6))
df['label'].value_counts().plot(kind='bar')
plt.title("Crop Distribution")
plt.xlabel("Crop")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 3. HISTOGRAM (Temperature)
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df['temperature'], bins=20)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 4. HISTOGRAM (Rainfall)
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df['rainfall'], bins=20)
plt.title("Rainfall Distribution")
plt.xlabel("Rainfall")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 5. SCATTER PLOT
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df['temperature'], df['humidity'])
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.show()
