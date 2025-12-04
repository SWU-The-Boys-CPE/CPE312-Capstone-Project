# Validation Results

**Project:** Bangkok Traffic Congestion Index Prediction  
**Date:** November 28, 2025  
**Status:** ✅ Complete

---

## 1. Data Split Summary

| Split | Samples | Percentage |
|-------|---------|------------|
| Training | 210 | 60% |
| Validation | 70 | 20% |
| Test | 71 | 20% |
| **Total** | **351** | **100%** |

---

## 2. Test Set Results

### 2.1 Overall Performance

| Model | Test MAE | Test RMSE | Test R² | Rank |
|-------|----------|-----------|---------|------|
| Random Forest | 0.63 | 0.81 | 0.9645 | 🥇 |
| Linear Regression | 1.96 | 2.06 | 0.7742 | 🥈 |
| XGBoost | 1.95 | 2.22 | 0.7359 | 🥉 |

### 2.2 Target Achievement

| Model | RMSE < 15 | MAE < 10 | R² > 0.70 | All Targets |
|-------|-----------|----------|-----------|-------------|
| Random Forest | ✅ 0.81 | ✅ 0.63 | ✅ 0.9645 | ✅ |
| Linear Regression | ✅ 2.06 | ✅ 1.96 | ✅ 0.7742 | ✅ |
| XGBoost | ✅ 2.22 | ✅ 1.95 | ✅ 0.7359 | ✅ |

---

## 3. Baseline Comparison

### 3.1 Simple Baselines

| Baseline | RMSE | R² |
|----------|------|----|
| Mean Prediction | 4.55 | 0.00 |
| Last Value (Naive) | 3.21 | 0.45 |
| **Linear Regression** | **2.06** | **0.7742** |

### 3.2 Improvement Over Baselines

| Model | vs Mean | vs Naive |
|-------|---------|----------|
| Random Forest | +96.5% | +51.5% |
| Linear Regression | +77.4% | +32.4% |
| XGBoost | +73.6% | +28.9% |

*Values show R² improvement over baseline*

---

## 4. Model Stability

### 4.1 Training vs Test Performance

| Model | Train R² | Test R² | Difference | Overfitting? |
|-------|----------|---------|------------|--------------|
| Random Forest | 0.97 | 0.9645 | -0.006 | ❌ No |
| Linear Regression | 0.78 | 0.7742 | -0.006 | ❌ No |
| XGBoost | 0.82 | 0.7359 | -0.084 | ⚠️ Slight |

### 4.2 Observations

1. **Linear Regression** shows best generalization (minimal train-test gap)
2. **XGBoost** has slight overfitting but still performs well
3. **Random Forest** shows significant overfitting (high train, low test R²)

---

## 5. Feature Importance Validation

### 5.1 Top Features (XGBoost)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | temp_avg | 46.9% |
| 2 | congestion_index_rolling_mean_7 | 19.2% |
| 3 | congestion_index_rolling_max_7 | 3.9% |
| 4 | congestion_index_rolling_mean_14 | 3.1% |
| 5 | congestion_index_rolling_std_7 | 3.0% |

### 5.2 Category Summary

| Category | Total Importance |
|----------|-----------------|
| Weather | 54.9% |
| Rolling Stats | 32.7% |
| Lag Features | 6.2% |
| Temporal | 6.2% |

---

## 6. Conclusions

1. **Random Forest is the best model** - highest R² (0.9645) with excellent generalization
2. **All models beat baselines** - significant improvement over mean/naive predictions
3. **All models meet targets** - Every model exceeds R² > 0.70 threshold
4. **Weather dominates** - Temperature alone explains 47% of predictions

### Recommendations

- Deploy Random Forest for production (best accuracy)
- Use Linear Regression as interpretable backup
- XGBoost provides good balance of accuracy and speed

---

**Last Updated:** November 28, 2025

---

**Last Updated:** November 27, 2025
