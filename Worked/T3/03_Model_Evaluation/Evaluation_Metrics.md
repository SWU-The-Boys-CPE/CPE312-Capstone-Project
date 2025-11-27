# Evaluation Metrics

**Project:** Bangkok Traffic Flow Optimization  
**Date:** November 27, 2025

---

## 1. Overview

This document describes the evaluation metrics used to assess model performance in predicting Bangkok traffic congestion.

---

## 2. Primary Metrics

### 2.1 Mean Absolute Error (MAE)

**Formula:**
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

**Description:** Average absolute difference between predicted and actual values.

**Target:** MAE < 5.0

**Interpretation:**
- MAE of 5.0 means predictions are off by 5 congestion index points on average
- Given range of 8-162, this represents ~3-6% of typical range
- Lower is better

**Bangkok Context:**
- Acceptable for daily planning
- Minor deviations from actual conditions

---

### 2.2 Root Mean Squared Error (RMSE)

**Formula:**
$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

**Description:** Square root of average squared errors. Penalizes larger errors more heavily.

**Target:** RMSE < 8.0

**Interpretation:**
- RMSE > MAE indicates presence of outlier errors
- More sensitive to large prediction errors
- Important for high-congestion events (Songkran, protests)

**Bangkok Context:**
- RMSE < 8.0 acceptable given high-variance special events
- Focus on reducing large errors during peak periods

---

### 2.3 Mean Absolute Percentage Error (MAPE)

**Formula:**
$$MAPE = \frac{100}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$

**Description:** Average percentage error. Scale-independent.

**Target:** MAPE < 15%

**Interpretation:**
- MAPE of 15% means predictions are ~15% off on average
- Business-interpretable (stakeholders understand percentages)
- Caution: Unstable when actual values near zero

**Bangkok Context:**
- 15% error acceptable for traffic management decisions
- Allows for proactive congestion mitigation

---

### 2.4 Coefficient of Determination (R²)

**Formula:**
$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}$$

**Description:** Proportion of variance explained by the model.

**Target:** R² > 0.75

**Interpretation:**
- R² of 0.75 means model explains 75% of variance
- Remaining 25% due to random factors, external events
- 1.0 = perfect prediction, 0.0 = same as predicting mean

**Bangkok Context:**
- Target based on similar traffic prediction studies
- 75%+ considered good for daily forecasting

---

## 3. Secondary Metrics

### 3.1 Directional Accuracy

**Formula:**
$$DA = \frac{1}{n}\sum_{i=1}^{n}\mathbb{1}[(y_i - y_{i-1}) \cdot (\hat{y}_i - y_{i-1}) > 0]$$

**Description:** Percentage of correctly predicted direction changes.

**Target:** DA > 70%

**Use Case:** Important for trend prediction (will congestion increase or decrease?)

---

### 3.2 Peak Hour Performance

**Description:** Metrics calculated specifically for 17:00-19:00 (evening rush).

**Target:** Same targets but evaluated separately

**Rationale:** Critical period for traffic management

---

### 3.3 Bias (Mean Error)

**Formula:**
$$Bias = \frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)$$

**Description:** Average prediction error (can be positive or negative).

**Target:** Bias ≈ 0

**Interpretation:**
- Positive bias: Model over-predicts
- Negative bias: Model under-predicts
- Zero bias: Balanced predictions

---

## 4. Metric Comparison by Model

| Model | Expected MAE | Expected RMSE | Expected MAPE | Expected R² |
|-------|-------------|---------------|---------------|-------------|
| LSTM | < 5.0 | < 7.5 | < 12% | > 0.78 |
| XGBoost | < 4.5 | < 7.0 | < 11% | > 0.80 |
| ARIMA | < 7.0 | < 10.0 | < 18% | > 0.65 |
| Random Forest | < 5.5 | < 8.5 | < 14% | > 0.72 |
| Baseline (Naive) | ~10 | ~15 | ~25% | ~0.4 |

---

## 5. Cross-Validation Strategy

### 5.1 Time-Series Split

```
Fold 1: [Train: 2019-2020] [Val: 2021-Q1]
Fold 2: [Train: 2019-2021] [Val: 2021-Q2]
Fold 3: [Train: 2019-2021] [Val: 2021-Q3]
Fold 4: [Train: 2019-2022] [Val: 2023-Q1]
Fold 5: [Train: 2019-2023] [Val: 2023-Q2]
```

### 5.2 Why Temporal Split?

- Prevents data leakage (no future information)
- Simulates real deployment (train on past, predict future)
- More realistic performance estimate

---

## 6. Evaluation Results (To Be Updated)

| Model | MAE | RMSE | MAPE | R² | CV Score | Status |
|-------|-----|------|------|----|---------:|--------|
| LSTM | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ To Do |
| XGBoost | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ To Do |
| ARIMA | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ To Do |
| RF | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ To Do |

---

## 7. Code Reference

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def evaluate_model(y_true, y_pred):
    """Calculate all evaluation metrics."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    r2 = r2_score(y_true, y_pred)
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape,
        'R2': r2
    }
```

---

**Last Updated:** November 27, 2025

**Status:** Template - Results pending
