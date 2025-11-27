# Feature Importance Analysis

**Project:** Bangkok Traffic Flow Optimization  
**Date:** November 27, 2025  
**Status:** Template - Results Pending

---

## 1. Overview

This document presents feature importance analysis from the trained models, identifying which features have the greatest impact on traffic congestion prediction.

---

## 2. Feature Categories

### 2.1 Temporal Features

| Feature | Description | Expected Importance |
|---------|-------------|---------------------|
| `hour_of_day` | Hour (0-23) | High |
| `day_of_week` | Day (0-6, Mon-Sun) | High |
| `is_weekend` | Weekend flag | Medium |
| `is_holiday` | Thai holiday flag | High |
| `month` | Month (1-12) | Medium |
| `season` | Thai season | Medium |

### 2.2 Lag Features

| Feature | Description | Expected Importance |
|---------|-------------|---------------------|
| `congestion_lag_1` | Yesterday's congestion | Very High |
| `congestion_lag_7` | Same day last week | High |
| `congestion_rolling_7` | 7-day rolling mean | High |
| `congestion_rolling_30` | 30-day rolling mean | Medium |

### 2.3 Weather Features

| Feature | Description | Expected Importance |
|---------|-------------|---------------------|
| `precipitation` | Daily precipitation (mm) | Medium |
| `temperature` | Temperature (°C) | Low |
| `weather_category` | Weather condition | Medium |
| `visibility` | Visibility (km) | Low |

---

## 3. XGBoost Feature Importance

### 3.1 Top 10 Features by Importance

| Rank | Feature | Importance Score | % Contribution |
|------|---------|-----------------|----------------|
| 1 | ⬜ | ⬜ | ⬜ |
| 2 | ⬜ | ⬜ | ⬜ |
| 3 | ⬜ | ⬜ | ⬜ |
| 4 | ⬜ | ⬜ | ⬜ |
| 5 | ⬜ | ⬜ | ⬜ |
| 6 | ⬜ | ⬜ | ⬜ |
| 7 | ⬜ | ⬜ | ⬜ |
| 8 | ⬜ | ⬜ | ⬜ |
| 9 | ⬜ | ⬜ | ⬜ |
| 10 | ⬜ | ⬜ | ⬜ |

### 3.2 Feature Importance by Category

| Category | Total Importance % | Top Feature |
|----------|-------------------|-------------|
| Temporal | ⬜ | ⬜ |
| Lag | ⬜ | ⬜ |
| Weather | ⬜ | ⬜ |
| Other | ⬜ | ⬜ |

---

## 4. Random Forest Feature Importance

### 4.1 Top 10 Features

| Rank | Feature | Importance Score |
|------|---------|-----------------|
| 1 | ⬜ | ⬜ |
| 2 | ⬜ | ⬜ |
| 3 | ⬜ | ⬜ |
| 4 | ⬜ | ⬜ |
| 5 | ⬜ | ⬜ |
| 6 | ⬜ | ⬜ |
| 7 | ⬜ | ⬜ |
| 8 | ⬜ | ⬜ |
| 9 | ⬜ | ⬜ |
| 10 | ⬜ | ⬜ |

---

## 5. SHAP Analysis (XGBoost)

### 5.1 SHAP Summary

⬜ To be completed with SHAP plots

### 5.2 Key SHAP Insights

| Feature | Effect on Prediction |
|---------|---------------------|
| ⬜ | ⬜ |

---

## 6. Conclusions

### 6.1 Most Important Features

1. ⬜
2. ⬜
3. ⬜

### 6.2 Least Important Features

1. ⬜
2. ⬜

### 6.3 Recommendations

- ⬜

---

**Last Updated:** November 27, 2025
