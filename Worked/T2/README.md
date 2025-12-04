# Phase T2: Data Collection, Cleaning & Initial EDA

## Bangkok Traffic Congestion Index Prediction

**Phase 2: Data Preparation and Exploratory Data Analysis**

**Duration:** Weeks 1-4  
**Status:** ✅ Complete  
**Last Updated:** November 28, 2025

---

## 📊 Data Summary

| Dataset | Records | Columns | Status |
|---------|---------|---------|--------|
| Bangkok Traffic | 1,682 | 12 | ✅ Cleaned |
| Bangkok Weather | 365 | 6 | ✅ Cleaned |

**Target Variable:** `congestion_index` (Daily Traffic Congestion Index)

---

## 📋 Quick Navigation

| Section | Purpose |
|---------|---------|
| [Project Overview](#-project-overview) | What is T2? |
| [Directory Structure](#-directory-structure) | Where are things? |
| [Getting Started](#-getting-started) | How to run code |

---

## 🎯 Project Overview

### Project Focus

This project prepares data for **Bangkok's daily Traffic Congestion Index (TCI)** prediction.

✅ **Data Collection** - Traffic and weather datasets loaded  
✅ **Data Cleaning** - Missing values handled, outliers removed  
✅ **EDA** - Distributions, correlations, patterns analyzed  
✅ **Visualization** - 6 figures generated  

### Key Findings from EDA

1. Traffic data spans 2019-2023 (1,682 daily records)
2. Weather data covers 2019 (365 records)
3. Strong correlation between temperature and congestion
4. Weekly patterns visible in traffic data
5. Seasonal variations in congestion levels

---

## 📂 Directory Structure

```
Worked/T2/
├── README.md                        ← You are here
├── 01_Project_Definition/           Project charter
├── 02_Data/Processed/               ← Cleaned CSV files
├── 03_Notebooks/                    ← Jupyter notebooks
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   └── 03_EDA.ipynb
├── 04_Scripts/                      Python utilities
├── 05_Documentation/                Project docs
├── 06_Configuration/                Config files
└── 07_Results/Figures/              ← EDA visualizations
```

---

## 🚀 Getting Started

### Prerequisites

```bash
# Activate virtual environment
source .venv/bin/activate

# Required packages
pip install numpy pandas matplotlib seaborn
```

### Run Notebooks in Order

1. **01_Data_Exploration.ipynb** - Load and preview data
2. **02_Data_Cleaning.ipynb** - Clean and preprocess
3. **03_EDA.ipynb** - Exploratory analysis

---

## 📈 Generated Outputs

### Cleaned Data Files

- `02_Data/Processed/bangkok_traffic_cleaned.csv`
- `02_Data/Processed/bangkok_weather_cleaned.csv`

### EDA Figures

- `07_Results/Figures/01_traffic_distributions.png`
- `07_Results/Figures/02_weather_distributions.png`
- `07_Results/Figures/03_correlation_matrix.png`
- `07_Results/Figures/04_traffic_trends.png`
- `07_Results/Figures/05_weather_patterns.png`
- `07_Results/Figures/06_traffic_seasonal_patterns.png`

---

## ✅ Completion Checklist

- [x] Data collection complete
- [x] Data cleaning complete
- [x] EDA notebooks executed
- [x] Visualizations generated
- [x] Documentation updated
- [x] Ready for T3 (Modeling)
