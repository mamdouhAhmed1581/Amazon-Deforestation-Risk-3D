# GeoAI Deforestation Risk Platform

An interactive GeoAI dashboard for visualizing and exploring deforestation risk across the Amazon Basin. The project is designed as a presentation-grade spatial intelligence interface, combining 3D map exploration, hotspot views, scenario simulation, focused spatial analysis, and export actions in a static frontend application.

## Overview

The platform centers on a primary dashboard built with Deck.GL and Mapbox-based rendering. It loads a precomputed forest-risk dataset and presents it through multiple analytical modes, including `3D`, `2D`, `Heatmap`, and `Hotspots`.

The repository also includes supporting pages for:

- model explanation
- scenario simulation
- focused spatial analysis
- standalone visual outputs

This is a frontend-driven decision-support project. It does not run live model training or inference in the browser. The main runtime dataset is already prepared and stored in [data/forest_data_clean.json](d:/Amazon-Deforestation-Risk-3D/data/forest_data_clean.json).

## Key Features

- Interactive 3D deforestation risk dashboard
- Multiple visualization modes for the same spatial dataset
- Right-side analytical panel for selected points
- Scenario simulation state integrated into the dashboard
- Spatial deep-dive page for hotspot and corridor exploration
- Export actions for selected locations
- Additional standalone visual artifacts for presentation use

## Project Structure

```text
Amazon-Deforestation-Risk-3D/
|- index.html
|- README.md
|- assets/
|  |- css/
|  |  `- platform.css
|  |- images/
|  |  |- framework_diagram.png
|  |  |- geoai_framework.png
|  |  `- model_validation_results.png
|  `- pages/
|     |- ai-model/
|     |- decision-film/
|     |- index/
|     |- intelligence-map/
|     |- scenario-simulator/
|     `- spatial-analysis/
|- data/
|  `- forest_data_clean.json
|- docs/
|  |- Graduation_Project_Report.md
|  |- implementation_plan.md
|  `- README.txt
|- outputs/
|  |- GeoAI_Decision_Film.html
|  `- GeoAI_INTELLIGENCE_MAP.html
|- pages/
|  |- ai-model.html
|  |- scenario-simulator.html
|  `- spatial-analysis.html
`- scripts/
   |- framework.py
   `- risk_stats.py
```

## Main Runtime Files

| File | Role |
| --- | --- |
| [index.html](d:/Amazon-Deforestation-Risk-3D/index.html) | Main dashboard entry point |
| [assets/pages/index/app.js](d:/Amazon-Deforestation-Risk-3D/assets/pages/index/app.js) | Dashboard logic, dataset loading, rendering, interaction, and export flow |
| [assets/pages/index/styles.css](d:/Amazon-Deforestation-Risk-3D/assets/pages/index/styles.css) | Dashboard styling and HUD layout |
| [data/forest_data_clean.json](d:/Amazon-Deforestation-Risk-3D/data/forest_data_clean.json) | Precomputed forest-risk dataset |
| [pages/spatial-analysis.html](d:/Amazon-Deforestation-Risk-3D/pages/spatial-analysis.html) | Spatial analysis workspace |
| [pages/scenario-simulator.html](d:/Amazon-Deforestation-Risk-3D/pages/scenario-simulator.html) | Scenario simulation page |
| [pages/ai-model.html](d:/Amazon-Deforestation-Risk-3D/pages/ai-model.html) | Model explanation and metrics page |

## How It Works

1. The dashboard fetches [data/forest_data_clean.json](d:/Amazon-Deforestation-Risk-3D/data/forest_data_clean.json).
2. Risk points are rendered on top of the map using Deck.GL.
3. Users switch between visualization modes and map styles.
4. Selecting a point opens detailed analysis in the right panel.
5. Scenario settings can modify the displayed risk interpretation.
6. Spatial analysis opens as a dedicated deep-dive page.

## Running Locally

Use a local web server instead of opening files directly, because the dashboard loads JSON through `fetch()`.

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/index.html
```

## Technology Stack

- HTML, CSS, and vanilla JavaScript
- Deck.GL
- Mapbox GL JS
- Chart.js
- D3.js
- jsPDF
- Python utilities for offline helper outputs

## Notes

- The dashboard is the main product in this repository.
- The dataset is precomputed and presentation-oriented.
- Some metrics and explanatory elements are frontend-derived for visualization purposes.
- The standalone files in [outputs/](d:/Amazon-Deforestation-Risk-3D/outputs) are better treated as exported supporting artifacts than as core application pages.

## Supporting Files

- [docs/Graduation_Project_Report.md](d:/Amazon-Deforestation-Risk-3D/docs/Graduation_Project_Report.md)
- [docs/implementation_plan.md](d:/Amazon-Deforestation-Risk-3D/docs/implementation_plan.md)
- [scripts/framework.py](d:/Amazon-Deforestation-Risk-3D/scripts/framework.py)
- [scripts/risk_stats.py](d:/Amazon-Deforestation-Risk-3D/scripts/risk_stats.py)
