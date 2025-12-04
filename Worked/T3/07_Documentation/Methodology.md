# Modeling Methodology

## 1. Overview

This document describes the methodology used for the Bangkok Traffic Congestion Index (TCI) Prediction project.

---

## 2. Problem Formulation

### 2.1 Task Type
- **Primary**: Regression (predict daily TCI value)

### 2.2 Target Variable
- Traffic Congestion Index (TCI)
- Daily aggregated values
- Source: TomTom Traffic Index

### 2.3 Prediction Horizon
- **Focus**: Next-day TCI prediction
- **Features**: Weather + historical patterns

---

## 3. Model Selection Rationale

| Model | Rationale | Result |
|-------|-----------|--------|
| Random Forest | Ensemble robustness | 🥇 Best (R²=0.9645) |
| Linear Regression | Simple, interpretable baseline | 🥈 Second (R²=0.7742) |
| XGBoost | Handles non-linear patterns | 🥉 Third (R²=0.7359) |

### 3.1 Models Excluded

| Model | Reason |
|-------|--------|
| LSTM | Overkill for 351 samples; requires TensorFlow |
| ARIMA | Cannot use multivariate features effectively |
| SVR | Slower training; less interpretable |

---

## 4. Feature Engineering

### 4.1 Feature Categories (33 features total)

| Category | Features | Importance |
|----------|----------|------------|
| Weather | temp_avg, humidity, rainfall, pressure, wind_speed | 54.9% |
| Rolling Stats | 7-day and 14-day rolling mean/max/std | 32.7% |
| Lag Features | Lag 1, 7, 14 day TCI values | 6.2% |
| Temporal | dayofweek, month, is_weekend, cyclical encodings | 6.2% |

### 4.2 Data Pipeline

```
Raw Data (Traffic + Weather)
    ↓
Cleaning (handle missing values)
    ↓
Feature Engineering (33 features)
    ↓
Train/Val/Test Split
    ↓
Model Training
    ↓
Evaluation
```

---

## 5. Validation Strategy

### 5.1 Train/Validation/Test Split

| Split | Samples | Percentage |
|-------|---------|------------|
| Training | 210 | 60% |
| Validation | 70 | 20% |
| Test | 71 | 20% |
| **Total** | **351** | **100%** |

### 5.2 Temporal Ordering
- Data kept in chronological order
- No shuffling to prevent data leakage

---

## 6. Evaluation Metrics

| Metric | Formula | Target | Achieved |
|--------|---------|--------|----------|
| RMSE | $\sqrt{\frac{1}{n}\sum(y_i - \hat{y}_i)^2}$ | < 15 | 2.06 ✅ |
| MAE | $\frac{1}{n}\sum\|y_i - \hat{y}_i\|$ | < 10 | 1.96 ✅ |
| R² | $1 - \frac{SS_{res}}{SS_{tot}}$ | > 0.70 | 0.7742 ✅ |

---

## 7. Hyperparameter Settings

### 7.1 XGBoost (Final)

| Parameter | Value |
|-----------|-------|
| n_estimators | 100 |
| max_depth | 5 |
| learning_rate | 0.1 |
| subsample | 0.8 |

### 7.2 Random Forest (Final)

| Parameter | Value |
|-----------|-------|
| n_estimators | 100 |
| max_depth | 10 |
| min_samples_split | 5 |

### 7.3 Linear Regression
- Default sklearn settings
- No regularization (simple OLS)

---

## 8. Reproducibility

All experiments are reproducible with:
- Fixed random seed: **42**
- Environment: `requirements.txt`
- Python: 3.11.10
- Key packages: scikit-learn, xgboost, pandas, numpy

---

**Document Version:** 2.0  
**Last Updated:** November 28, 2025
