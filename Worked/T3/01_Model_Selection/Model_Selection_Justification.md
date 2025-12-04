# Model Selection Justification

**Project:** Bangkok Traffic Congestion Index Prediction  
**Date:** November 28, 2025

---

## 1. Executive Summary

Three regression models were selected for predicting Bangkok's daily Traffic Congestion Index (TCI):

| Model | Purpose | Selected |
|-------|---------|----------|
| Random Forest | Ensemble trees | ✅ Best performer |
| Linear Regression | Simple baseline | ✅ Interpretable |
| XGBoost | Gradient boosting | ✅ Strong alternative |

---

## 2. Model Selection Criteria

### 2.1 Requirements

- **Interpretability**: Explainable predictions for stakeholders
- **Speed**: Fast inference for daily predictions
- **Accuracy**: RMSE < 15, MAE < 10, R² > 0.70

### 2.2 Data Characteristics

- **Size**: 351 samples (after feature engineering)
- **Features**: 33 numeric predictors
- **Target**: Continuous (TCI value)
- **Temporal**: Daily time-series data

---

## 3. Model Justifications

### 3.1 Linear Regression

**Why Selected:**
- Simplest interpretable model
- Coefficients show feature impact direction
- Fast training and inference
- Works well with engineered features

**Results:**
- RMSE: 2.06 ✅
- MAE: 1.96 ✅
- R²: 0.7742 ✅

**Recommendation:** Primary model for production

---

### 3.2 XGBoost

**Why Selected:**
- Handles non-linear relationships
- Feature importance built-in
- Robust to outliers
- Industry standard for tabular data

**Results:**
- RMSE: 2.22 ✅
- MAE: 1.95 ✅
- R²: 0.7359 ✅

**Recommendation:** Alternative model, good for ensemble

---

### 3.3 Random Forest

**Why Selected:**
- Ensemble reduces overfitting
- No feature scaling required
- Feature importance analysis
- Handles interactions automatically

**Results:**
- RMSE: 0.81 ✅
- MAE: 0.63 ✅
- R²: 0.9645 ✅

**Recommendation:** Primary model for production (best accuracy)

---

## 4. Models Not Selected

### 4.1 LSTM (Deep Learning)

**Reason for Exclusion:**
- Requires larger datasets (>10K samples)
- Complex architecture for daily predictions
- Overfitting risk with 351 samples
- TensorFlow dependency adds complexity

### 4.2 ARIMA (Time-Series)

**Reason for Exclusion:**
- Pure time-series model (no multivariate support)
- Weather features cannot be incorporated easily
- Less flexible than ML approaches
- Assumes stationarity

---

## 5. Final Recommendation

**Primary Model:** Random Forest
- Highest R² (0.9645)
- Best predictive accuracy
- RMSE: 0.81, MAE: 0.63

**Secondary Model:** Linear Regression
- Good accuracy (R² = 0.7742)
- Most interpretable
- Simple deployment

---

## 6. Conclusion

The model selection demonstrates that Random Forest with proper hyperparameter tuning achieves excellent predictive performance (R² = 0.9645). All three models now exceed the R² > 0.70 target, providing flexibility for deployment based on accuracy vs. interpretability trade-offs.
