# 🐍 04_Scripts - Python Modules

## Purpose

This directory contains reusable Python modules for the Bangkok Traffic Congestion Index Prediction project.

---

## 📦 Modules

### 1. utils.py
**Purpose:** Core utility functions

**Key Functions:**
- `setup_logger()` - Configure logging
- `load_config()` - Parse YAML configuration
- `validate_dataframe()` - Schema validation
- `calculate_rmse()`, `calculate_mae()`, `calculate_r2()` - Model metrics

**Example:**
```python
from utils import setup_logger, load_config

logger = setup_logger(__name__)
config = load_config("../06_Configuration/config.yaml")
```

---

### 2. data_loader.py
**Purpose:** Data loading and validation

**Key Functions:**
- `load_csv_data()` - Load CSV files
- `load_traffic_data()` - Load Bangkok traffic data
- `load_weather_data()` - Load weather data
- `handle_missing_values()` - Handle missing data
- `create_temporal_features()` - Create time-based features

**Example:**
```python
from data_loader import load_traffic_data, load_weather_data

traffic_df = load_traffic_data("../02_Data/Processed/bangkok_traffic_cleaned.csv")
weather_df = load_weather_data("../02_Data/Processed/bangkok_weather_cleaned.csv")
```

---

### 3. preprocessing.py
**Purpose:** Data preprocessing and feature engineering

**Key Functions:**
- `preprocess_traffic_data()` - Clean traffic data
- `engineer_temporal_features()` - Create day, month, cyclical features
- `normalize_features()` - Standardize numeric features

**Example:**
```python
from preprocessing import preprocess_traffic_data

df_clean = preprocess_traffic_data(df_raw)
```

---

### 4. visualization.py
**Purpose:** Visualization utilities

**Key Functions:**
- `plot_timeseries()` - Time series plots
- `plot_correlation_matrix()` - Correlation heatmaps
- `plot_distribution()` - Distribution plots

**Example:**
```python
from visualization import plot_timeseries

plot_timeseries(df, 'congestion_index', title='Traffic Congestion Over Time')
```

---

## 📁 File Structure

```
04_Scripts/
├── data_loader.py      # Data loading functions
├── preprocessing.py    # Preprocessing pipeline
├── utils.py           # Utility functions
├── visualization.py   # Plotting functions
└── README.md          # This file
```

---

## 🔗 Usage in Notebooks

```python
import sys
sys.path.append('../04_Scripts')

from utils import setup_logger
from data_loader import load_traffic_data
from preprocessing import preprocess_traffic_data
from visualization import plot_timeseries
```

---

*Last Updated: November 2025*
