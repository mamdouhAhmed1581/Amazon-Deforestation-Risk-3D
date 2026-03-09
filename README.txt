# Amazon Risk Project

This repository contains the GeoAI Deforestation Risk Prediction Framework for the Amazon Basin.

## Structure
Amazon_Risk_Project
│
├ forest_risk_3D_v2.html     # Interactive 3D web application
├ forest_data_clean.json     # Spatial dataset (150,000 points)
├ analysis.py                # Validation and metrics computation backend
├ model_validation_results.png # 4-panel visual validation chart
└ README.txt                 # Project structure and metadata

## Abstract
The model predicts deforestation risk using spatial and environmental variables. It processes satellite data, performs U-Net forest segmentation, and outputs a highly accurate risk prediction map. 

## Key Metrics
- Final Accuracy: The model achieved an AUC score of 0.82, indicating strong predictive performance.
- Results: High-risk areas are mainly concentrated along road networks and agricultural expansion zones (specifically in Rondônia).

## Execution
Open `forest_risk_3D_v2.html` (or `index.html`) in any modern web browser to interact with the 3D GeoAI Risk Map.
