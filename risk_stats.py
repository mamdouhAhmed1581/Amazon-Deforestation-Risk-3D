import json
import pandas as pd
import matplotlib.pyplot as plt

# ===== 1️⃣ قراءة البيانات =====
with open("forest_data_clean.json") as f:
    data = json.load(f)

low = 0
medium = 0
high = 0

# ===== 2️⃣ تصنيف النقاط =====
for point in data:
    score = point["risk_score"]

    if score <= 80:
        low += 1
    elif score <= 140:
        medium += 1
    else:
        high += 1

total = low + medium + high

# ===== 3️⃣ إنشاء جدول =====
df = pd.DataFrame({
    "Class": ["Low", "Medium", "High"],
    "Count": [low, medium, high]
})

df["Percentage"] = (df["Count"] / total) * 100

# حفظ CSV
df.to_csv("risk_area_stats.csv", index=False)

# ===== 4️⃣ طباعة ملخص احترافي =====
print("\n===== RISK ANALYSIS SUMMARY =====")
print(df)
print("\nHigh Risk Percentage: {:.2f}%".format(df.loc[2, "Percentage"]))

# ===== 5️⃣ رسم Pie Chart =====
colors = ["#00aa00", "#ff8c00", "#c80000"]

plt.figure(figsize=(6,6))
plt.pie(df["Percentage"],
        labels=df["Class"],
        autopct='%1.1f%%',
        colors=colors,
        startangle=140)

plt.title("Forest Risk Distribution")
plt.savefig("risk_distribution_pie.png", dpi=300)
plt.show()

print("\n✔ Analysis complete.")
print("✔ CSV saved as risk_area_stats.csv")
print("✔ Pie chart saved as risk_distribution_pie.png")