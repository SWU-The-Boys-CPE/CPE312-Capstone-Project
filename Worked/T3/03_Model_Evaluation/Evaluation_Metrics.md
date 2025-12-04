# Evaluation Metrics

**Project:** Bangkok Traffic Congestion Index Prediction  
**Date:** November 28, 2025

---

## 1. Overview

This document describes the evaluation metrics used to assess model performance in predicting Bangkok's daily Traffic Congestion Index (TCI).

---

## 2. Primary Metrics

### 2.1 Root Mean Squared Error (RMSE)

**Formula:**
$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

**Description:** Square root of average squared errors. Penalizes larger errors more heavily.

**Target:** RMSE < 15

**Achieved Results:**
| Model | RMSE | Status |
|-------|------|--------|
| Random Forest | 0.81 | ✅ |
| Linear Regression | 2.06 | ✅ |
| XGBoost | 2.22 | ✅ |

---

### 2.2 Mean Absolute Error (MAE)

**Formula:**
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

**Description:** Average absolute difference between predicted and actual values.

**Target:** MAE < 10

**Achieved Results:**
| Model | MAE | Status |
|-------|-----|--------|
| Random Forest | 0.63 | ✅ |
| Linear Regression | 1.96 | ✅ |
| XGBoost | 1.95 | ✅ |

---

### 2.3 Coefficient of Determination (R²)

**Formula:**
$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

**Description:** Proportion of variance explained by the model.

**Target:** R² > 0.70

**Achieved Results:**
| Model | R² | Status |
|-------|-----|--------|
| Random Forest | 0.9645 | ✅ |
| Linear Regression | 0.7742 | ✅ |
| XGBoost | 0.7359 | ✅ |

---

## 3. Results Summary

### 3.1 Best Model: Random Forest

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| RMSE | 0.81 | < 15 | ✅ Exceeds |
| MAE | 0.63 | < 10 | ✅ Exceeds |
| R² | 0.9645 | > 0.70 | ✅ Achieved |

### 3.2 Key Observations

1. **All models meet all target metrics** ✅
2. **Random Forest outperforms** with R²=0.9645
3. **Linear Regression is solid alternative** with R²=0.7742
4. **XGBoost performs well** with R²=0.7359

---

## 4. Feature Importance (XGBoost)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | temp_avg | 0.4694 |
| 2 | congestion_index_rolling_mean_7 | 0.1922 |
| 3 | congestion_index_rolling_max_7 | 0.0386 |
| 4 | congestion_index_rolling_mean_14 | 0.0306 |
| 5 | congestion_index_rolling_std_7 | 0.0304 |

---

## 5. Conclusion

Random Forest is recommended as the primary model due to highest R² (0.9645) and excellent predictive accuracy. Linear Regression remains a good alternative for interpretability.
