# GeoAI Deforestation Risk Prediction Platform

## ملخص سريع بالعربي

هذا المشروع عبارة عن **منصة GeoAI تفاعلية** لعرض وتحليل **مخاطر إزالة الغابات في الأمازون**. أهم نقطة لازم تعرفها هي أن المشروع الحالي **Frontend قوي جدًا في العرض والتحليل البصري**، لكن **ليس Backend Model حي** يشغّل التدريب أو التنبؤ لحظيًا داخل المتصفح. التنبؤات الأساسية موجودة مسبقًا داخل ملف البيانات [`forest_data_clean.json`](./forest_data_clean.json).

### أهم أجزاء المشروع بسرعة

- [`index.html`](./index.html)
  - الصفحة الأساسية والأهم
  - تعرض الخريطة 3D والـ Heatmap والـ Hotspots
- [`forest_data_clean.json`](./forest_data_clean.json)
  - ملف البيانات الرئيسي
  - يحتوي على `150000` نقطة خطر
- [`scenario-simulator.html`](./scenario-simulator.html)
  - صفحة السيناريوهات
  - تغيّر حالة المحاكاة وتحفظها في `localStorage`
- [`ai-model.html`](./ai-model.html)
  - شرح الموديل والـ SHAP والـ ROC والـ Confusion Matrix
- [`reports.html`](./reports.html)
  - صفحة التقارير والتصدير
- [`project-details.html`](./project-details.html)
  - شرح المنهجية والـ pipeline والـ stack

### أهم ملاحظة تقنية

ليس كل ما تراه في الواجهة ناتجًا من موديل حي. هناك أجزاء كثيرة محسوبة داخل الواجهة نفسها لأغراض العرض، مثل:

- `event_year`
- بعض مؤشرات `validation`
- بعض `explainability drivers`
- بعض الرسوم والمؤشرات في الصفحات الثانوية

### أهم تكامل داخل المشروع

أقوى تكامل حقيقي داخل المشروع هو:

1. صفحة [`scenario-simulator.html`](./scenario-simulator.html) تحفظ حالة المحاكاة.
2. صفحة [`index.html`](./index.html) تقرأ هذه الحالة.
3. الـ dashboard يعدّل درجة الخطر المعروضة بناءً عليها.

### كيف تشغل المشروع صح

أفضل تشغيل يكون عبر سيرفر محلي، وليس فتح الملفات مباشرة:

```bash
python -m http.server 8000
```

ثم افتح:

```text
http://localhost:8000/index.html
```

السبب أن الصفحة الأساسية تستخدم `fetch()` لقراءة [`forest_data_clean.json`](./forest_data_clean.json).

## Overview

This repository is a static multi-page GeoAI dashboard focused on **deforestation risk prediction in the Amazon Basin**, especially **Rondonia** and nearby frontier zones.

The project combines:

- a primary interactive **3D dashboard**
- supporting pages for **AI model explanation**
- a **scenario simulator**
- a **spatial analysis page**
- a **reports/export page**
- methodology/documentation pages
- standalone map/film visual outputs

At the current state of the codebase, this is primarily a **frontend visualization and decision-support project**, not a full backend ML system. The model output used by the dashboard is already precomputed in [`forest_data_clean.json`](./forest_data_clean.json).

## What The Project Actually Does

In simple terms, the workflow is:

1. A precomputed dataset of forest-risk points is loaded from [`forest_data_clean.json`](./forest_data_clean.json).
2. The main dashboard renders these points in 3D using **Deck.GL** on top of a map.
3. The user can switch between:
   - `3D`
   - `2D`
   - `Heatmap`
   - `Hotspots`
4. The user can change camera, map style, performance mode, and scenario.
5. Clicking a point opens a right-side analysis panel with:
   - risk score
   - probability
   - local explanation drivers
   - validation-style indicators
   - trajectory chart
6. The scenario simulator writes a custom simulation state into `localStorage`.
7. The main dashboard reads that simulation state and adjusts the displayed risk scores.
8. Reports pages generate downloads or PDF exports from prepared UI content.

## Important Reality Check

To understand the project correctly, separate **real runtime data** from **frontend simulation/demo logic**:

- **Real runtime data**
  - [`forest_data_clean.json`](./forest_data_clean.json)
  - This is the main source used by the dashboard.

- **Frontend-derived or illustrative logic**
  - event year assignment on the dashboard
  - scenario-adjusted score calculations
  - explainability driver percentages
  - validation evidence labels
  - region naming
  - many charts and KPI values on secondary pages

This means the project is excellent as a **presentation/demo/decision-support interface**, but it is **not** currently running a live ML model in the browser.

## Project Type

- **Runtime type:** static web app
- **Backend/API:** none
- **Build tool:** none
- **Package manager:** none
- **Main dependencies:** loaded from CDN inside HTML files
- **Python usage:** helper scripts for diagrams/stats only

## Main Pages

| Page | Purpose | Main Runtime Files | Notes |
| --- | --- | --- | --- |
| [`index.html`](./index.html) | Main 3D GeoAI dashboard | [`assets/pages/index/app.js`](./assets/pages/index/app.js), [`assets/pages/index/styles.css`](./assets/pages/index/styles.css) | The core page of the whole project |
| [`ai-model.html`](./ai-model.html) | AI model architecture and explainability page | [`assets/pages/ai-model/app.js`](./assets/pages/ai-model/app.js), [`assets/pages/ai-model/styles.css`](./assets/pages/ai-model/styles.css) | Mostly static explanatory content with charts |
| [`scenario-simulator.html`](./scenario-simulator.html) | Scenario simulation and what-if controls | [`assets/pages/scenario-simulator/app.js`](./assets/pages/scenario-simulator/app.js), [`assets/pages/scenario-simulator/styles.css`](./assets/pages/scenario-simulator/styles.css) | Writes scenario state to `localStorage` |
| [`spatial-analysis.html`](./spatial-analysis.html) | Spatial hotspot, cluster, corridor exploration | [`assets/pages/spatial-analysis/app.js`](./assets/pages/spatial-analysis/app.js), [`assets/pages/spatial-analysis/styles.css`](./assets/pages/spatial-analysis/styles.css) | Uses hardcoded sample analysis points, not the full dataset |
| [`reports.html`](./reports.html) | Exports and PDF preview | [`assets/pages/reports/app.js`](./assets/pages/reports/app.js), [`assets/pages/reports/styles.css`](./assets/pages/reports/styles.css) | Export logic currently uses demo sample data for GeoJSON/CSV |
| [`project-details.html`](./project-details.html) | Methodology and technical documentation | [`assets/pages/project-details/app.js`](./assets/pages/project-details/app.js), [`assets/pages/project-details/styles.css`](./assets/pages/project-details/styles.css) | Mostly static documentation content |
| [`GeoAI_INTELLIGENCE_MAP.html`](./GeoAI_INTELLIGENCE_MAP.html) | Standalone intelligence map | [`assets/pages/intelligence-map/app.js`](./assets/pages/intelligence-map/app.js), [`assets/pages/intelligence-map/styles.css`](./assets/pages/intelligence-map/styles.css) | Looks like a generated Folium/Leaflet export |
| [`GeoAI_Decision_Film.html`](./GeoAI_Decision_Film.html) | Standalone decision film / Plotly view | [`assets/pages/decision-film/app.js`](./assets/pages/decision-film/app.js), [`assets/pages/decision-film/styles.css`](./assets/pages/decision-film/styles.css) | `app.js` is essentially a large bundled/generated Plotly file |

## Directory Structure

```text
Amazon-Deforestation-Risk-3D/
|- index.html
|- ai-model.html
|- spatial-analysis.html
|- scenario-simulator.html
|- reports.html
|- project-details.html
|- GeoAI_INTELLIGENCE_MAP.html
|- GeoAI_Decision_Film.html
|- forest_data_clean.json
|- framework.py
|- risk_stats.py
|- geoai_framework.png
|- framework_diagram.png
|- model_validation_results.png
|- Graduation_Project_Report.md
|- implementation_plan.md
|- assets/
|  |- css/
|  |  `- platform.css
|  `- pages/
|     |- index/
|     |  |- app.js
|     |  `- styles.css
|     |- ai-model/
|     |  |- app.js
|     |  `- styles.css
|     |- scenario-simulator/
|     |  |- app.js
|     |  `- styles.css
|     |- spatial-analysis/
|     |  |- app.js
|     |  `- styles.css
|     |- reports/
|     |  |- app.js
|     |  `- styles.css
|     |- project-details/
|     |  |- app.js
|     |  `- styles.css
|     |- intelligence-map/
|     |  |- app.js
|     |  `- styles.css
|     `- decision-film/
|        |- app.js
|        `- styles.css
```

## Shared UI Structure

The project follows this layout pattern:

- shared styling in [`assets/css/platform.css`](./assets/css/platform.css)
- each page has its own `app.js`
- each page has its own `styles.css`
- HTML now contains the actual page structure directly

This means:

- **shared platform look** lives in `platform.css`
- **page behavior** lives in each page's `app.js`
- **page layout and appearance** live in each page's `styles.css`

## Deep Dive: Main Dashboard

The main dashboard is the most important part of the repo.

### Files

- [`index.html`](./index.html)
- [`assets/pages/index/app.js`](./assets/pages/index/app.js)
- [`assets/pages/index/styles.css`](./assets/pages/index/styles.css)

### Core Runtime Objects In `index/app.js`

The dashboard logic contains:

- `deckInstance`
  - the Deck.GL visualization instance
- `dataGlobal`
  - the loaded forest-risk dataset
- `currentMode`
  - render mode: `3d`, `heat`, `hotspot`
- `currentScenario`
  - active scenario: baseline, road, protection, or simulated
- `currentYear`
  - timeline year
- `performanceMode`
  - `quality`, `balanced`, `fast`
- `spatialLayersVisible`
  - roads, rivers, protected areas, urban overlays

### How Data Is Loaded

The dashboard uses `loadForestData()` in [`assets/pages/index/app.js`](./assets/pages/index/app.js):

- fetches [`forest_data_clean.json`](./forest_data_clean.json)
- uses `AbortController` timeout
- if loading fails, the UI can:
  - show an error
  - allow selecting a JSON file manually
  - fall back to `DEMO_DATA`

### Render Modes

The dashboard can render:

- **3D columns**
  - using `deck.ColumnLayer`
- **glow/highlight scatter layer**
  - for visual emphasis
- **2D-like view**
  - by forcing height scale to zero
- **heatmap**
  - using `deck.HeatmapLayer`
- **hotspots**
  - using `deck.ScatterplotLayer`

### Map Styles

The dashboard supports:

- `dark`
- `terrain`
- `satellite`

These are raster tile styles assembled in `createRasterStyle()`.

### Scenario Logic

The dashboard does not rerun a model. Instead, it adjusts the baseline score using frontend formulas:

- `baseline`
- `road`
- `protection`
- `simulated`

The key function is `getPointScore(point, scenario)`.

The `simulated` scenario reads from `localStorage` key:

```text
geoai_sim_state
```

That state is created by the Scenario Simulator page.

### Analysis/Explainability Logic

When a point is selected, the dashboard derives:

- risk class
- probability
- validation evidence
- region summary
- explanation drivers
- trajectory chart for 2030-2035

Important: these explanation and validation values are **frontend heuristic outputs**, not direct model inference returned from a backend.

### Spatial Layers

`initSpatialLayers()` builds synthetic overlay features such as:

- roads
- rivers
- protected areas
- urban markers

These are rendered on top of the map as additional Deck.GL layers.

### Timeline

The timeline controls `currentYear` and affects which points are visible through assigned `event_year` values.

Important technical note:

- `event_year` is not loaded from the dataset
- it is generated in the browser via `assignEventYear(point)`

So timeline playback is currently a **derived presentation layer**, not a real historical time-series dataset.

### Chart and PDF

The dashboard also includes:

- a risk distribution / impact chart using **Chart.js**
- a PDF export from the analysis sidebar using **html2pdf**

## Deep Dive: Dataset

### File

- [`forest_data_clean.json`](./forest_data_clean.json)

### Size

- **150,000 points**

### Example Fields

From the current dataset:

- `lat`
- `lon`
- `risk_score`
- `risk_norm`
- `elevation`
- `color`

### Current Value Ranges

Measured from the actual file:

- latitude: `-13.6274` to `-7.9823`
- longitude: `-66.7213` to `-59.9042`
- risk score: `160` to `178`

### Important Interpretation

The current dataset is not a wide `0-255` balanced risk spread. In practice, the current JSON already sits in a **high-risk band**.

That has two consequences:

1. the dashboard's low/medium/high classes are **relative within a high-risk subset**
2. scripts that assume older thresholds may become misleading

## Risk Thresholds Used In Different Places

This repo currently has **more than one thresholding idea**, so it is important to know which one is active where.

### In the main dashboard

The dashboard logic treats points roughly as:

- high risk: `> 170`
- medium risk: `> 165 and <= 170`
- low risk: everything else in the visible set

### In `risk_stats.py`

[`risk_stats.py`](./risk_stats.py) uses:

- low: `<= 80`
- medium: `81-140`
- high: `> 140`

Given the current dataset range (`160-178`), that script will classify **100% of the current dataset as high risk**.

So:

- `risk_stats.py` is useful as a helper script
- but its thresholds do **not** match the current dashboard interpretation

## Deep Dive: AI Model Page

### Files

- [`ai-model.html`](./ai-model.html)
- [`assets/pages/ai-model/app.js`](./assets/pages/ai-model/app.js)
- [`assets/pages/ai-model/styles.css`](./assets/pages/ai-model/styles.css)

### What It Shows

- AUC, precision, recall, F1-score
- training sample count
- feature count
- neural network architecture diagram
- feature importance bars
- ROC curve
- confusion matrix
- training dataset table
- input features table

### What Is Dynamic Here

- SHAP-style feature bars animate in
- ROC chart is rendered via **Chart.js**
- the network connections are drawn on canvas
- background animation is decorative

### Important Note

This page is largely **presentation/explanation content**, not live inference code.

## Deep Dive: Scenario Simulator

### Files

- [`scenario-simulator.html`](./scenario-simulator.html)
- [`assets/pages/scenario-simulator/app.js`](./assets/pages/scenario-simulator/app.js)

### What It Does

The simulator modifies:

- road expansion
- population pressure
- fire frequency
- policy toggles

Then it computes an estimated impact using a frontend formula and updates:

- predicted deforestation change
- baseline vs simulated comparison
- projection chart
- zone change counts
- estimated forest area at risk

### Dashboard Integration

The simulator saves its state into:

```text
geoai_sim_state
```

The main dashboard reads that state and applies it when the user selects the simulated scenario.

This is the most important page-to-page integration in the whole repo.

## Deep Dive: Spatial Analysis Page

### Files

- [`spatial-analysis.html`](./spatial-analysis.html)
- [`assets/pages/spatial-analysis/app.js`](./assets/pages/spatial-analysis/app.js)

### What It Uses

- **Mapbox GL JS**
- **Chart.js**
- a small hardcoded dataset called `ANALYSIS_POINTS`

### What It Shows

- hotspots
- clusters
- corridors
- heatmap
- regional risk distribution chart
- temporal deforestation trend

### Important Note

This page is **not** loading the main 150k JSON dataset. It uses a small illustrative set of points and shapes for a focused analysis demo.

## Deep Dive: Reports Page

### Files

- [`reports.html`](./reports.html)
- [`assets/pages/reports/app.js`](./assets/pages/reports/app.js)

### What It Does

- lets the user export:
  - GeoJSON
  - CSV
  - PNG placeholder action
  - PDF report

### Important Note

The `GeoJSON` and `CSV` export functions currently build output from a **small hardcoded sample FeatureCollection**, not from the live dashboard dataset.

So the reports page is currently:

- good as a UI prototype and workflow demo
- not yet wired to the live 150k-point data pipeline

## Deep Dive: Project Details Page

### Files

- [`project-details.html`](./project-details.html)
- [`assets/pages/project-details/app.js`](./assets/pages/project-details/app.js)

### Purpose

This page explains:

- methodology
- data pipeline
- feature engineering
- AI model architecture
- technology stack
- roadmap
- references

It is mainly static documentation content for presentation and academic reporting.

## Standalone Visual Outputs

### Intelligence Map

- [`GeoAI_INTELLIGENCE_MAP.html`](./GeoAI_INTELLIGENCE_MAP.html)
- [`assets/pages/intelligence-map/app.js`](./assets/pages/intelligence-map/app.js)

This appears to be a standalone **Leaflet/Folium-style generated map export** with:

- a Leaflet base map
- an image overlay
- generated JS

This is better treated as an exported artifact than as a hand-maintained page.

### Decision Film

- [`GeoAI_Decision_Film.html`](./GeoAI_Decision_Film.html)
- [`assets/pages/decision-film/app.js`](./assets/pages/decision-film/app.js)

This page loads a single Plotly graph container, while the corresponding `app.js` is a very large Plotly-generated/bundled file.

This is also closer to an exported artifact than a manually authored frontend module.

## Python Files

### `framework.py`

[`framework.py`](./framework.py) creates a visual diagram of the GeoAI framework and saves:

- [`geoai_framework.png`](./geoai_framework.png)

The diagram sequence is:

1. Satellite Data Input
2. UNet Deep Learning Model
3. Deforestation Risk Prediction
4. Spatial Cluster Analysis
5. Model Validation

### `risk_stats.py`

[`risk_stats.py`](./risk_stats.py) reads the JSON dataset, computes class counts, exports CSV, and saves a pie chart.

Outputs:

- `risk_area_stats.csv`
- `risk_distribution_pie.png`

Again, note the threshold mismatch described earlier.

## Supporting Documents

### [`Graduation_Project_Report.md`](./Graduation_Project_Report.md)

Contains the academic narrative of the project:

- problem statement
- dataset summary
- methodology
- explainable AI drivers
- validation summary
- final conclusion

### [`implementation_plan.md`](./implementation_plan.md)

Contains a UI redesign plan related mainly to dashboard sidebars and control structure.

### [`README.txt`](./README.txt)

This file is **outdated**. It still references older names such as:

- `forest_risk_3D_v2.html`
- `analysis.py`

Those are not the current runtime entry points of the project.

## External Libraries Used

Loaded directly from CDNs in the HTML pages:

- **Deck.GL**
- **Mapbox GL JS**
- **Chart.js**
- **html2pdf.js**
- **D3**
- **Leaflet**
- **Bootstrap**
- **Font Awesome**
- **Plotly** (bundled/generated in decision film)

## How To Run The Project

### Recommended Way

Run a local HTTP server from the project root.

If Python is installed:

```bash
python -m http.server 8000
```

or on Windows:

```bash
py -m http.server 8000
```

Then open:

```text
http://localhost:8000/index.html
```

### Why Local Server Is Better

The main dashboard fetches [`forest_data_clean.json`](./forest_data_clean.json). In many browsers, `fetch()` from direct `file://` paths is restricted, so using a local server is the reliable approach.

## Entry Points

If you are new to the project, start here:

1. [`index.html`](./index.html)
2. [`assets/pages/index/app.js`](./assets/pages/index/app.js)
3. [`forest_data_clean.json`](./forest_data_clean.json)
4. [`scenario-simulator.html`](./scenario-simulator.html)
5. [`assets/pages/scenario-simulator/app.js`](./assets/pages/scenario-simulator/app.js)

That path gives you the fastest understanding of:

- what data is loaded
- how it is rendered
- how scenario state changes the output

## If You Want To Modify The Project

### Change global look and nav

Edit:

- [`assets/css/platform.css`](./assets/css/platform.css)

### Change dashboard behavior

Edit:

- [`assets/pages/index/app.js`](./assets/pages/index/app.js)

### Change dashboard layout/appearance

Edit:

- [`index.html`](./index.html)
- [`assets/pages/index/styles.css`](./assets/pages/index/styles.css)

### Change scenario logic

Edit:

- [`assets/pages/scenario-simulator/app.js`](./assets/pages/scenario-simulator/app.js)
- `getPointScore()` inside [`assets/pages/index/app.js`](./assets/pages/index/app.js)

### Change report export logic

Edit:

- [`assets/pages/reports/app.js`](./assets/pages/reports/app.js)

### Change the primary dataset

Replace or update:

- [`forest_data_clean.json`](./forest_data_clean.json)

## Technical Caveats And Cleanup Opportunities

These are useful to know before extending the repo:

1. The project has **no backend**; most analytics are frontend-side or illustrative.
2. The main dashboard is the only page using the full JSON dataset directly.
3. The reports page exports demo sample data, not the live dashboard dataset.
4. The spatial analysis page uses its own sample analysis points.
5. `risk_stats.py` thresholds do not match the current dataset range.
6. Some pages are clearly generated/exported artifacts rather than modular source pages.
7. External basemap tiles and CDN libraries require internet access.
8. A public Mapbox token is hardcoded in frontend code and should be moved to configuration if this becomes production-grade.
9. Temporary/reference files like [`index_temp.txt`](./index_temp.txt) are present and are likely not part of the main runtime flow.

## In One Sentence

This repo is a **GeoAI deforestation-risk visualization platform** centered on a **3D Amazon dashboard** driven by a **precomputed JSON risk dataset**, with surrounding pages for **model explanation, simulation, reporting, and presentation**.
