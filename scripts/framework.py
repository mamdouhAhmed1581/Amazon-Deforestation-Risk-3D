from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "assets" / "images" / "geoai_framework.png"


fig, ax = plt.subplots(figsize=(10, 8), facecolor="#0a0e17")
ax.set_facecolor("#0a0e17")

steps = [
    ("Satellite Data Input", "(Multispectral imagery & Remote Sensing)", "#3b82f6"),
    ("UNet Deep Learning Model", "(Spatial Feature Extraction & Segmentation)", "#8b5cf6"),
    ("Deforestation Risk Prediction", "(Probability Scoring & Classification)", "#ef4444"),
    ("Spatial Cluster Analysis", "(DBSCAN Hotspot Mapping)", "#f59e0b"),
    ("Model Validation", "(Active Fire Overlay & ROC-AUC Assessment)", "#10b981"),
]

plt.text(
    0.5,
    0.92,
    "GeoAI Risk Prediction Framework",
    color="white",
    fontsize=22,
    fontweight="bold",
    ha="center",
    va="center",
)

box_height = 0.11
box_spacing = 0.155
start_y = 0.77

for i, (title, subtitle, color) in enumerate(steps):
    y_pos = start_y - i * box_spacing

    box = FancyBboxPatch(
        (0.15, y_pos - box_height / 2),
        0.7,
        box_height,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        ec=color,
        fc="#0f172a",
        lw=2,
        alpha=0.9,
        zorder=3,
    )

    glow = FancyBboxPatch(
        (0.15, y_pos - box_height / 2),
        0.7,
        box_height,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        ec=color,
        fc="none",
        lw=6,
        alpha=0.15,
        zorder=2,
    )

    ax.add_patch(box)
    ax.add_patch(glow)

    plt.text(
        0.5,
        y_pos + 0.015,
        title,
        color="white",
        fontsize=13,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=4,
    )
    plt.text(
        0.5,
        y_pos - 0.02,
        subtitle,
        color="#e2e8f0",
        fontsize=11,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=4,
    )

    if i < len(steps) - 1:
        plt.text(
            0.5,
            y_pos - box_height / 2 - 0.02,
            "v",
            color="#64748b",
            fontsize=24,
            ha="center",
            va="center",
            alpha=0.6,
            zorder=1,
        )

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight", facecolor="#0a0e17")
