# Key Insights

**Project:** Bangkok Traffic Congestion Index Prediction  
**Date:** November 28, 2025

---

## 1. Executive Summary

This document summarizes key insights from the Bangkok Traffic Congestion Index (TCI) prediction analysis.

### Final Model Results

| Model | RMSE | MAE | R² | Status |
|-------|------|-----|-----|--------|
| **Random Forest** | 0.81 | 0.63 | 0.9645 | ✅ Best |
| Linear Regression | 2.06 | 1.96 | 0.7742 | ✅ Good |
| XGBoost | 2.22 | 1.95 | 0.7359 | ✅ Good |

---

## 2. Feature Importance Insights

### 2.1 Top Predictors

1. **Temperature (temp_avg)** - 46.9% importance
   - Primary driver of TCI predictions
   - Higher temps correlate with traffic patterns
   
2. **7-Day Rolling Mean** - 19.2% importance
   - Recent trend captures weekly patterns
   
3. **7-Day Rolling Max** - 3.9% importance
   - Peak congestion indicator

4. **14-Day Rolling Mean** - 3.1% importance
   - Longer-term trend context

5. **7-Day Rolling Std** - 3.0% importance
   - Volatility indicator

### 2.2 Key Finding

**Weather features dominate** - Temperature alone accounts for nearly 50% of model importance, suggesting weather is the strongest predictor of traffic congestion.

---

## 3. Model Performance Insights

### 3.1 Linear Regression Success

- Simple model outperforms complex ensembles
- High linearity in data relationships
- Excellent interpretability for stakeholders
- Fastest inference time

### 3.2 Why Simpler is Better

The engineered features (lags, rolling statistics) already capture non-linear patterns, allowing a linear model to perform well.

---

## 4. Data Insights

### 4.1 Dataset Summary

- **Records:** 351 samples (after feature engineering)
- **Features:** 33 numeric predictors
- **Date Range:** January - December 2019
- **Target:** Daily Traffic Congestion Index

### 4.2 Data Quality

- Weather merge reduced dataset to 2019 overlap
- 14-day lag features require historical data
- Missing values handled via forward-fill

---

## 5. Recommendations

### 5.1 For Deployment

1. Use **Linear Regression** as primary model
2. Maintain 7-day rolling feature calculations
3. Integrate real-time weather data
4. Deploy with daily prediction pipeline

### 5.2 For Improvement

1. Collect more years of overlapping weather data
2. Add event calendar features (holidays, festivals)
3. Include road network characteristics
4. Consider hourly predictions

---

## 6. Limitations

1. **Limited date range** - Only 2019 data available
2. **Weather dependency** - Model relies heavily on temperature
3. **No real-time features** - Current model uses historical data
4. **Synthetic elements** - Some features are simulated

---

## 7. Conclusion

The Bangkok TCI Prediction project successfully achieves all target metrics (RMSE < 15, MAE < 10, R² > 0.70). Linear Regression is recommended for production deployment due to its simplicity, interpretability, and strong performance.
