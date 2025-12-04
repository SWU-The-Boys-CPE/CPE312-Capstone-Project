# Data Dictionary

**Project:** Bangkok Traffic Congestion Index Prediction

**Version:** 2.0 (Focused Scope)

**Last Updated:** November 2025

---

## Table of Contents

1. [Bangkok Traffic Congestion Index](#1-bangkok-traffic-congestion-index)
2. [Weather Data](#2-weather-data)
3. [Engineered Features](#3-engineered-features)
4. [Data Types and Formats](#4-data-types-and-formats)

---

## 1. Bangkok Traffic Congestion Index

**Source:** CEIC Data / TrafficIndex.org

**File:** `02_Data/Processed/bangkok_traffic_cleaned.csv`

**Records:** 1,682 observations

**Date Range:** January 1, 2019 - November 2025

### Variables

| Variable Name | Data Type | Description | Valid Range | Missing Values |
|--------------|-----------|-------------|-------------|----------------|
| `date` | Date | Observation date | 2019-01-01 to 2025-11-16 | 0% |
| `congestion_index` | Float | Traffic congestion index | 0.0 - 200.0 | < 0.5% |

### Derived Temporal Features

| Variable Name | Data Type | Description | Valid Range |
|--------------|-----------|-------------|-------------|
| `year` | Integer | Year | 2019-2025 |
| `month` | Integer | Month of year | 1-12 |
| `day` | Integer | Day of month | 1-31 |
| `dayofweek` | Integer | Day of week | 0-6 (0=Monday) |
| `is_weekend` | Boolean | Weekend indicator | 0, 1 |
| `is_holiday` | Boolean | Thai holiday indicator | 0, 1 |
| `season` | String | Thai season | 'dry', 'rainy', 'cool' |

### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Mean | 38.88 |
| Median | 35.20 |
| Std Dev | 18.45 |
| Min | 8.50 |
| Max | 162.13 |
| Range | 153.63 |

### Known Issues
- Outliers > 100 during special events (royal ceremonies, holidays)
- 2 days missing data interpolated

---

## 2. Weather Data

**Source:** Weather API / OpenWeatherMap

**File:** `02_Data/Processed/bangkok_weather_cleaned.csv`

**Records:** 1,682 observations (aligned with traffic data)

**Coverage:** Bangkok (13.7563°N, 100.5018°E)

### Variables

| Variable Name | Data Type | Description | Valid Range | Missing Values |
|--------------|-----------|-------------|-------------|----------------|
| `date` | Date | Observation date | 2019-2025 | 0% |
| `temperature` | Float | Average temperature (°C) | 15.0 - 42.0 | < 1% |
| `humidity` | Float | Average humidity (%) | 30.0 - 100.0 | 2% |
| `precipitation` | Float | Daily precipitation (mm) | 0.0 - 250.0 | 3% |

### Weather Categories

| Category | Precipitation Range | Description |
|----------|---------------------|-------------|
| `dry` | 0 - 0.1 mm | No rain |
| `light_rain` | 0.1 - 10 mm | Light rain |
| `moderate_rain` | 10 - 35 mm | Moderate rain |
| `heavy_rain` | > 35 mm | Heavy rain |

### Weather-Congestion Correlation

| Weather Feature | Correlation with TCI |
|-----------------|---------------------|
| Precipitation | r = 0.52 (moderate positive) |
| Humidity | r = 0.35 (weak positive) |
| Temperature | r = -0.15 (weak negative) |

---

## 3. Engineered Features

Features created for ML modeling (in `T3/02_Data/Processed/`):

### Temporal Features

| Feature | Description |
|---------|-------------|
| `day_sin`, `day_cos` | Cyclical encoding of day of week |
| `month_sin`, `month_cos` | Cyclical encoding of month |
| `week_of_year` | Week number (1-52) |
| `quarter` | Quarter (1-4) |

### Lag Features

| Feature | Description |
|---------|-------------|
| `congestion_lag_1` | Previous day's congestion |
| `congestion_lag_7` | Same day last week |
| `congestion_lag_14` | 2 weeks ago |
| `congestion_lag_30` | 1 month ago |

### Rolling Statistics

| Feature | Description |
|---------|-------------|
| `rolling_mean_7` | 7-day rolling average |
| `rolling_std_7` | 7-day rolling std dev |
| `rolling_mean_30` | 30-day rolling average |

---

## 4. Data Types and Formats

### File Formats

| Format | Extension | Usage |
|--------|-----------|-------|
| CSV | `.csv` | Primary data format |
| Pickle | `.pkl` | Trained models |

### Date Formats

| Format | Example | Usage |
|--------|---------|-------|
| ISO 8601 | `2025-01-15` | Standard date format |

### Missing Value Codes

| Code | Meaning |
|------|---------|
| `NaN` | Missing numeric value |
| Empty string | Missing string value |
| `-999` | Invalid/placeholder (if used) |

---

## Data Processing Notes

1. **Missing Values:** Interpolated using linear method for time-series continuity
2. **Outliers:** Flagged but retained (represent real extreme events)
3. **Date Alignment:** Traffic and weather data merged on date column
4. **Temporal Features:** Created during preprocessing (see `04_Scripts/preprocessing.py`)

---

*Last Updated: November 2025*
