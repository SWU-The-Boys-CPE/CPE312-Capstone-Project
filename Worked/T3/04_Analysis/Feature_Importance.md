# Feature Importance Analysis

**Project:** Bangkok Traffic Congestion Index Prediction  
**Date:** November 28, 2025

---

## 1. Overview

This document analyzes feature importance from the trained models to understand which factors most influence traffic congestion predictions.

---

## 2. XGBoost Feature Importance

| Rank | Feature | Importance | Category |
|------|---------|------------|----------|
| 1 | temp_avg | 0.4694 | Weather |
| 2 | congestion_index_rolling_mean_7 | 0.1922 | Rolling Stats |
| 3 | congestion_index_rolling_max_7 | 0.0386 | Rolling Stats |
| 4 | congestion_index_rolling_mean_14 | 0.0306 | Rolling Stats |
| 5 | congestion_index_rolling_std_7 | 0.0304 | Rolling Stats |
| 6 | congestion_index_lag_1 | 0.0289 | Lag Features |
| 7 | humidity | 0.0276 | Weather |
| 8 | congestion_index_rolling_max_14 | 0.0251 | Rolling Stats |
| 9 | rainfall | 0.0198 | Weather |
| 10 | dayofweek | 0.0187 | Temporal |

---

## 3. Category Analysis

### 3.1 Weather Features (54.9%)

- **temp_avg**: 46.9% - Dominant predictor
- **humidity**: 2.8%
- **rainfall**: 2.0%
- **pressure, wind_speed**: <2% combined

**Insight:** Weather is the strongest predictor of traffic congestion.

### 3.2 Rolling Statistics (32.7%)

- **7-day rolling mean**: 19.2%
- **7-day rolling max**: 3.9%
- **14-day rolling mean**: 3.1%
- Other rolling features: ~6.5%

**Insight:** Recent trends strongly predict future congestion.

### 3.3 Lag Features (6.2%)

- **Lag 1 (yesterday)**: 2.9%
- **Lag 7 (last week)**: 1.8%
- **Lag 14 (two weeks ago)**: 1.5%

**Insight:** Previous day's congestion is most predictive.

### 3.4 Temporal Features (6.2%)

- **dayofweek**: 1.9%
- **month_sin/cos**: 1.5%
- **is_weekend**: 1.2%
- Other temporal: ~1.6%

**Insight:** Weekly patterns influence traffic.

---

## 4. Key Findings

### 4.1 Temperature Dominance

Temperature alone accounts for nearly 50% of model importance:
- Hot days may increase air conditioning use → more driving
- Cold/comfortable days may encourage outdoor activities
- Seasonal patterns affect commuting behavior

### 4.2 Rolling Statistics Value

7-day rolling features capture:
- Weekly commute patterns
- Recent trend momentum
- Short-term variability

### 4.3 Minimal Temporal Impact

Day of week and month have low direct importance:
- Already captured in rolling/lag features
- Cyclical encoding reduces redundancy

---

## 5. Recommendations

### 5.1 For Production

1. **Prioritize weather data quality** - Most impactful feature
2. **Maintain 7-day rolling calculations** - High predictive value
3. **Daily updates critical** - Lag features need fresh data

### 5.2 For Improvement

1. Add weather forecast data for forward predictions
2. Include special event calendar (holidays, festivals)
3. Explore hour-of-day features for intraday predictions

---

## 6. Visualization

Feature importance visualizations saved to:
- `09_Results/Figures/feature_importance.png`
- `09_Results/Figures/model_evaluation.png`

---

## 7. Conclusion

Temperature and 7-day rolling statistics are the primary drivers of TCI prediction accuracy. Weather integration is critical for operational deployment.
