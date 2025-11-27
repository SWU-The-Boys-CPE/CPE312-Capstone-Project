# Validation Results

**Project:** Bangkok Traffic Flow Optimization  
**Date:** November 27, 2025  
**Status:** Pending

---

## 1. Cross-Validation Results

### 1.1 Time-Series Cross-Validation (5-Fold)

| Model | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean | Std |
|-------|--------|--------|--------|--------|--------|------|-----|
| **LSTM** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **XGBoost** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **ARIMA** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **RF** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

*Metric: RMSE*

---

## 2. Holdout Test Set Results

### 2.1 Overall Performance

| Model | Test MAE | Test RMSE | Test MAPE | Test R² |
|-------|----------|-----------|-----------|---------|
| LSTM | ⬜ | ⬜ | ⬜ | ⬜ |
| XGBoost | ⬜ | ⬜ | ⬜ | ⬜ |
| ARIMA | ⬜ | ⬜ | ⬜ | ⬜ |
| RF | ⬜ | ⬜ | ⬜ | ⬜ |

### 2.2 Peak Hour Performance (17:00-19:00)

| Model | Peak MAE | Peak RMSE | Peak R² |
|-------|----------|-----------|---------|
| LSTM | ⬜ | ⬜ | ⬜ |
| XGBoost | ⬜ | ⬜ | ⬜ |
| ARIMA | ⬜ | ⬜ | ⬜ |
| RF | ⬜ | ⬜ | ⬜ |

---

## 3. Baseline Comparison

| Model | vs Naive | vs Mean | vs Seasonal |
|-------|----------|---------|-------------|
| LSTM | ⬜ | ⬜ | ⬜ |
| XGBoost | ⬜ | ⬜ | ⬜ |
| ARIMA | ⬜ | ⬜ | ⬜ |
| RF | ⬜ | ⬜ | ⬜ |

*Values show % improvement over baseline*

---

## 4. Statistical Significance Tests

### 4.1 Paired t-test (LSTM vs XGBoost)

| Test | t-statistic | p-value | Significant? |
|------|-------------|---------|--------------|
| MAE | ⬜ | ⬜ | ⬜ |
| RMSE | ⬜ | ⬜ | ⬜ |

### 4.2 Diebold-Mariano Test

| Comparison | DM Statistic | p-value | Winner |
|------------|--------------|---------|--------|
| LSTM vs XGBoost | ⬜ | ⬜ | ⬜ |
| XGBoost vs ARIMA | ⬜ | ⬜ | ⬜ |
| LSTM vs ARIMA | ⬜ | ⬜ | ⬜ |

---

## 5. Conclusions

⬜ To be completed after model training and evaluation.

---

**Last Updated:** November 27, 2025
