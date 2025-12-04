# 📊 02_Data - Data Directory

## Overview

This directory contains all datasets used in the Bangkok Traffic Congestion Index Prediction project.

---

## 📁 Directory Structure

```
02_Data/
├── Processed/                    # Cleaned, ready-to-use data
│   ├── bangkok_traffic_cleaned.csv
│   └── bangkok_weather_cleaned.csv
└── README.md
```

---

## 📋 Dataset Inventory

### 1. Bangkok Traffic Congestion Index

| Attribute | Value |
|-----------|-------|
| **File** | `Processed/bangkok_traffic_cleaned.csv` |
| **Source** | CEIC Data / TrafficIndex.org |
| **Coverage** | 2019-2025 |
| **Records** | 1,682 daily observations |
| **Format** | CSV |

#### Key Statistics
- **Mean TCI:** 38.88
- **Max TCI:** 162.13
- **Min TCI:** ~25
- **Missing Values:** < 1%

#### Columns

| Column | Type | Description |
|--------|------|-------------|
| `date` | datetime | Date of measurement |
| `congestion_index` | float | Daily Traffic Congestion Index (0-200) |

---

### 2. Bangkok Weather Data

| Attribute | Value |
|-----------|-------|
| **File** | `Processed/bangkok_weather_cleaned.csv` |
| **Source** | NOAA / NASA |
| **Coverage** | Aligned with traffic data (2019-2025) |
| **Format** | CSV |

#### Columns

| Column | Type | Description |
|--------|------|-------------|
| `date` | datetime | Date of measurement |
| `temperature` | float | Average temperature (°C) |
| `humidity` | float | Average humidity (%) |
| `precipitation` | float | Daily precipitation (mm) |

---

## 🔧 Data Processing

### Cleaning Steps Applied

1. **Date Standardization**
   - Converted to datetime format
   - Ensured consistent timezone (UTC+7)

2. **Missing Value Handling**
   - Linear interpolation for small gaps (< 7 days)
   - Removed records with excessive missing data

3. **Outlier Treatment**
   - IQR-based detection
   - Winsorization for extreme values

4. **Feature Engineering** (performed in notebooks)
   - `dayofweek`: Day of week (0-6)
   - `month`: Month (1-12)
   - `is_weekend`: Weekend flag
   - `is_holiday`: Thai holiday flag
   - Cyclical encodings (`day_sin`, `day_cos`, `month_sin`, `month_cos`)

---

## 📈 Data Quality Summary

| Dataset | Records | Missing (%) | Duplicates |
|---------|---------|-------------|------------|
| Traffic | 1,682 | < 1% | 0 |
| Weather | 1,682 | < 2% | 0 |

---

## 🔗 Related Files

- **Processing Notebook:** [../03_Notebooks/02_Data_Cleaning.ipynb](../03_Notebooks/02_Data_Cleaning.ipynb)
- **EDA Notebook:** [../03_Notebooks/03_EDA.ipynb](../03_Notebooks/03_EDA.ipynb)
- **Data Dictionary:** [../05_Documentation/03_Technical_Docs/02_Data_Dictionary.md](../05_Documentation/03_Technical_Docs/02_Data_Dictionary.md)

---

*Last Updated: November 2025*
