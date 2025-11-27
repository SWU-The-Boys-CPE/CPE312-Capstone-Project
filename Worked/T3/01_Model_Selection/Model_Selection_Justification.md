# Model Selection Justification

**Project:** Urban Traffic Flow Optimization and Public Transit Efficiency Analysis in Bangkok Metropolitan Area

**Author:** Data Science Team  
**Date:** November 27, 2025  
**Status:** Draft

---

## Executive Summary

This document provides detailed justification for the machine learning models selected for the Bangkok Traffic Flow Optimization project. The selection is based on research questions, data characteristics, and best practices from traffic prediction literature.

---

## 1. Problem Definition Recap

### 1.1 Primary Research Question
**Can we predict traffic congestion levels 15-60 minutes in advance with 75-85% accuracy?**

### 1.2 Secondary Research Questions
- What are the spatial hotspots of congestion?
- How does weather affect traffic patterns?
- Which features are most predictive?

### 1.3 Data Characteristics

| Characteristic | Value | Implication |
|---------------|-------|-------------|
| Data Type | Time-series | Need sequential models |
| Observations | 1,682+ | Sufficient for ML |
| Features | 20+ (after engineering) | Tabular models work |
| Seasonality | Weekly, yearly | Need seasonal handling |
| Distribution | Right-skewed | Need robust models |

---

## 2. Models Selected

### 2.1 LSTM (Long Short-Term Memory)

**Type:** Deep Learning / Recurrent Neural Network

**Justification:**

| Criterion | Assessment | Score |
|-----------|------------|-------|
| Sequential Pattern Capture | Excellent - designed for sequences | ⭐⭐⭐⭐⭐ |
| Long-term Dependencies | Excellent - memory cells | ⭐⭐⭐⭐⭐ |
| Non-linear Relationships | Excellent | ⭐⭐⭐⭐⭐ |
| Interpretability | Poor - black box | ⭐⭐ |
| Training Time | Moderate-High | ⭐⭐⭐ |
| Data Requirements | High | ⭐⭐⭐ |

**Why LSTM for Traffic Prediction:**
1. Traffic data is inherently sequential - today's congestion depends on previous days
2. Weekly patterns require memory of 7+ days
3. Can capture complex non-linear patterns in rush hour dynamics
4. Proven effectiveness in traffic forecasting literature

**Architecture:**
```
Input Shape: (sequence_length, n_features)
Layer 1: LSTM(64 units, return_sequences=True)
Dropout: 0.2
Layer 2: LSTM(32 units)
Dropout: 0.2
Dense: (1 unit) - output
```

**Expected Performance:** RMSE < 8.0, R² > 0.75

---

### 2.2 XGBoost (eXtreme Gradient Boosting)

**Type:** Gradient Boosting / Ensemble

**Justification:**

| Criterion | Assessment | Score |
|-----------|------------|-------|
| Tabular Data Performance | Excellent | ⭐⭐⭐⭐⭐ |
| Feature Importance | Excellent - built-in | ⭐⭐⭐⭐⭐ |
| Handling Missing Values | Good | ⭐⭐⭐⭐ |
| Training Speed | Fast | ⭐⭐⭐⭐⭐ |
| Interpretability | Good - SHAP values | ⭐⭐⭐⭐ |
| Regularization | Excellent | ⭐⭐⭐⭐⭐ |

**Why XGBoost for Traffic Prediction:**
1. Excellent for structured/tabular data with many features
2. Built-in feature importance helps answer RQ4
3. Handles outliers well (Songkran, protests)
4. Fast training enables extensive hyperparameter tuning
5. State-of-the-art performance on tabular data

**Key Parameters:**
```python
params = {
    'n_estimators': 100,
    'max_depth': 6,
    'learning_rate': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8
}
```

**Expected Performance:** RMSE < 7.5, R² > 0.78

---

### 2.3 ARIMA (Auto-Regressive Integrated Moving Average)

**Type:** Statistical Time-Series

**Justification:**

| Criterion | Assessment | Score |
|-----------|------------|-------|
| Time-series Baseline | Excellent | ⭐⭐⭐⭐⭐ |
| Interpretability | Excellent | ⭐⭐⭐⭐⭐ |
| Stationarity Handling | Good | ⭐⭐⭐⭐ |
| Non-linear Patterns | Poor | ⭐⭐ |
| Multivariate Support | Limited | ⭐⭐ |
| Implementation | Easy | ⭐⭐⭐⭐⭐ |

**Why ARIMA for Traffic Prediction:**
1. Established baseline for time-series comparison
2. Highly interpretable (p, d, q parameters)
3. Captures linear trends and seasonality
4. Required for academic rigor - compare ML vs classical methods
5. Fast training and prediction

**Parameters:**
```python
# ARIMA(p, d, q) x (P, D, Q, s)
order = (1, 1, 1)
seasonal_order = (1, 1, 1, 7)  # Weekly seasonality
```

**Expected Performance:** RMSE < 10.0, R² > 0.65

---

### 2.4 Random Forest

**Type:** Ensemble Learning

**Justification:**

| Criterion | Assessment | Score |
|-----------|------------|-------|
| Robustness | Excellent | ⭐⭐⭐⭐⭐ |
| Feature Importance | Good | ⭐⭐⭐⭐ |
| Overfitting Resistance | Good | ⭐⭐⭐⭐ |
| Training Speed | Moderate | ⭐⭐⭐ |
| Interpretability | Moderate | ⭐⭐⭐ |

**Why Random Forest for Traffic Prediction:**
1. Robust baseline for ensemble comparison
2. Less prone to overfitting than single trees
3. Provides feature importance
4. Handles non-linear relationships
5. Comparison point for XGBoost

**Parameters:**
```python
params = {
    'n_estimators': 100,
    'max_depth': 15,
    'min_samples_split': 5,
    'min_samples_leaf': 2
}
```

**Expected Performance:** RMSE < 9.0, R² > 0.70

---

## 3. Baseline Models

### 3.1 Naive Forecast
- **Method:** Predict tomorrow = today's value
- **Purpose:** Minimum baseline for comparison
- **Expected RMSE:** ~15-20

### 3.2 Mean Forecast
- **Method:** Predict = historical mean
- **Purpose:** Constant prediction baseline
- **Expected RMSE:** ~18-22

### 3.3 Seasonal Naive
- **Method:** Predict = same day last week
- **Purpose:** Capture weekly patterns
- **Expected RMSE:** ~12-15

---

## 4. Model Comparison Matrix

| Aspect | LSTM | XGBoost | ARIMA | Random Forest |
|--------|------|---------|-------|---------------|
| **Data Type** | Sequential | Tabular | Univariate | Tabular |
| **Interpretability** | Low | Medium | High | Medium |
| **Training Time** | High | Low | Low | Medium |
| **Feature Engineering** | Moderate | Low | High | Low |
| **Hyperparameters** | Many | Many | Few | Moderate |
| **Best For** | Temporal patterns | Feature importance | Baseline | Robustness |

---

## 5. Research Question Alignment

| Research Question | Primary Model | Rationale |
|-------------------|---------------|-----------|
| RQ1: Congestion prediction | LSTM, ARIMA | Time-series nature |
| RQ2: Hotspot identification | XGBoost, RF | Spatial features |
| RQ3: Weather correlation | XGBoost | Feature importance |
| RQ4: Feature importance | XGBoost, RF | Built-in importance |

---

## 6. Literature Support

### 6.1 Traffic Prediction Studies Using LSTM
- Zhao et al. (2017): LSTM for traffic speed prediction
- Ma et al. (2015): Deep learning for traffic flow prediction
- Performance: 10-15% improvement over ARIMA

### 6.2 XGBoost in Transportation
- Chen et al. (2016): XGBoost for taxi demand prediction
- Zhang et al. (2019): XGBoost for traffic accident prediction
- Performance: State-of-the-art on tabular transportation data

### 6.3 Classical Methods
- Williams and Hoel (2003): ARIMA for traffic flow
- Established baseline methodology

---

## 7. Implementation Plan

| Week | Task | Model |
|------|------|-------|
| 5.1 | Feature engineering | All |
| 5.2 | Data splitting | All |
| 5.3 | Train LSTM | LSTM |
| 5.4 | Train XGBoost | XGBoost |
| 6.1 | Train ARIMA | ARIMA |
| 6.2 | Hyperparameter tuning | All |
| 6.3 | Cross-validation | All |
| 6.4 | Feature importance | XGBoost, RF |
| 6.5 | Documentation | All |

---

## 8. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| LSTM overfitting | Medium | High | Dropout, early stopping |
| Insufficient data for DL | Low | Medium | Use simpler architectures |
| XGBoost overfitting | Medium | Medium | Regularization, CV |
| ARIMA non-stationarity | Medium | Low | Differencing, ADF test |
| Computation limits | Low | Medium | Use cloud resources |

---

## 9. Conclusion

The selected models (LSTM, XGBoost, ARIMA, Random Forest) provide a comprehensive approach to traffic prediction:

1. **LSTM** captures temporal dependencies for accurate forecasting
2. **XGBoost** provides interpretability and feature importance
3. **ARIMA** establishes a rigorous statistical baseline
4. **Random Forest** offers robust ensemble comparison

This combination addresses all research questions while following best practices in traffic prediction research.

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Data Scientist | | | |
| Technical Lead | | | |

---

**Document Version:** 1.0  
**Last Updated:** November 27, 2025
