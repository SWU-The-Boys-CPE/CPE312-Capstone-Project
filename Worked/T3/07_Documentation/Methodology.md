# Modeling Methodology

## 1. Overview

This document describes the methodology used for traffic congestion prediction in the Bangkok Traffic Flow Optimization project.

---

## 2. Problem Formulation

### 2.1 Task Type
- **Primary**: Regression (predict congestion index)
- **Secondary**: Classification (low/medium/high congestion)

### 2.2 Target Variable
- Congestion index (0-100 scale)
- Daily granularity with option for hourly

### 2.3 Prediction Horizon
- Short-term: 1-day ahead
- Medium-term: 7-day ahead

---

## 3. Model Selection Rationale

| Model | Rationale | Expected Strength |
|-------|-----------|-------------------|
| LSTM | Captures long-term dependencies | Sequential patterns |
| XGBoost | Handles tabular features well | Non-linear relationships |
| ARIMA | Statistical baseline | Time-series trends |
| Random Forest | Robust ensemble | Feature importance |

---

## 4. Validation Strategy

### 4.1 Time-Series Cross-Validation
- Walk-forward validation
- No data leakage from future to past
- 5-fold temporal split

### 4.2 Train/Validation/Test Split
- Training: 60%
- Validation: 20%
- Testing: 20%

---

## 5. Evaluation Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| MAE | $\frac{1}{n}\sum\|y_i - \hat{y}_i\|$ | < 5.0 |
| RMSE | $\sqrt{\frac{1}{n}\sum(y_i - \hat{y}_i)^2}$ | < 8.0 |
| MAPE | $\frac{100}{n}\sum\|\frac{y_i - \hat{y}_i}{y_i}\|$ | < 15% |
| R² | $1 - \frac{SS_{res}}{SS_{tot}}$ | > 0.75 |

---

## 6. Hyperparameter Optimization

### 6.1 Grid Search Space

**XGBoost:**
- `n_estimators`: [50, 100, 200]
- `max_depth`: [4, 6, 8]
- `learning_rate`: [0.01, 0.1, 0.2]

**LSTM:**
- `units`: [32, 64, 128]
- `dropout`: [0.1, 0.2, 0.3]
- `learning_rate`: [0.001, 0.005]

---

## 7. Reproducibility

All experiments are reproducible with:
- Fixed random seeds (42)
- Documented environment (`requirements.txt`)
- Version-controlled code

---

**Document Version:** 1.0  
**Last Updated:** November 27, 2025
