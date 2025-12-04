# Model Comparison Matrix

**Project:** Bangkok Traffic Congestion Index Prediction  
**Date:** November 2025

---

## Selected Models (In Scope)

| Feature | Random Forest | XGBoost | Linear Regression |
|---------|:-------------:|:-------:|:-----------------:|
| **Tabular Data** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Interpretability** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Training Speed** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Feature Importance** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Handles Outliers** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Handles Non-linearity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
| **Data Requirements** | Low | Low | Low |
| **Complexity** | Low | Medium | Very Low |

---

## Performance Targets

| Model | Target RMSE | Target MAE | Target R² |
|-------|-------------|------------|-----------|
| Linear Regression | < 18 | < 12 | > 0.60 |
| Random Forest | < 15 | < 10 | > 0.70 |
| XGBoost | < 15 | < 10 | > 0.75 |

---

## Model Selection Rationale

### Random Forest
- ✅ Handles non-linear relationships
- ✅ Built-in feature importance
- ✅ Robust to outliers
- ✅ Easy to tune

### XGBoost
- ✅ State-of-the-art performance
- ✅ Handles missing values
- ✅ Built-in regularization
- ✅ Fast training

### Linear Regression
- ✅ Simple baseline
- ✅ Highly interpretable
- ✅ Fast inference
- ✅ Statistical significance testing

---

## Why NOT Other Models?

| Model | Reason for Exclusion |
|-------|---------------------|
| LSTM | Overkill for daily tabular data; requires TensorFlow |
| ARIMA | Pure time-series; can't use multivariate features |
| SVR | Slower training; less interpretable |
| Neural Networks | Overkill for dataset size; harder to interpret |

---

*Last Updated: November 2025*
