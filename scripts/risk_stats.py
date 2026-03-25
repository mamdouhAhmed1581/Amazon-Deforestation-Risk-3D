import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "forest_data_clean.json"
CSV_PATH = BASE_DIR / "data" / "risk_area_stats.csv"
CHART_PATH = BASE_DIR / "assets" / "images" / "risk_distribution_pie.png"


with DATA_PATH.open(encoding="utf-8") as f:
    data = json.load(f)

low = 0
medium = 0
high = 0

for point in data:
    score = point["risk_score"]

    if score <= 80:
        low += 1
    elif score <= 140:
        medium += 1
    else:
        high += 1

total = low + medium + high

df = pd.DataFrame(
    {
        "Class": ["Low", "Medium", "High"],
        "Count": [low, medium, high],
    }
)

df["Percentage"] = (df["Count"] / total) * 100

CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
CHART_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_PATH, index=False)

print("\n===== RISK ANALYSIS SUMMARY =====")
print(df)
print("\nHigh Risk Percentage: {:.2f}%".format(df.loc[2, "Percentage"]))

colors = ["#00aa00", "#ff8c00", "#c80000"]

plt.figure(figsize=(6, 6))
plt.pie(
    df["Percentage"],
    labels=df["Class"],
    autopct="%1.1f%%",
    colors=colors,
    startangle=140,
)

plt.title("Forest Risk Distribution")
plt.savefig(CHART_PATH, dpi=300)
plt.show()

print("\nAnalysis complete.")
print(f"CSV saved as {CSV_PATH}")
print(f"Pie chart saved as {CHART_PATH}")
