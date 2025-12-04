# Bangkok Traffic Congestion Index Prediction
## Capstone Project - CPE312
### Team: SWU The Boys

---

# Agenda

1. Introduction & Problem Statement
2. Project Objectives & Scope
3. Team Roles & Responsibilities
4. Data Collection & Overview
5. Data Cleaning & Preprocessing
6. Exploratory Data Analysis (EDA)
7. Feature Engineering
8. Model Selection Strategy
9. Model Results: Linear Regression
10. Model Results: XGBoost
11. Model Results: Random Forest
12. Model Comparison & Evaluation
13. Feature Importance Analysis
14. Key Insights & Findings
15. Business Recommendations
16. Future Work & Conclusion

---

# 1. Introduction & Problem Statement

**The Problem:**
- Bangkok is ranked among the most congested cities globally.
- Traffic congestion causes significant economic loss and reduces quality of life.
- Commuters and city planners lack accurate, data-driven predictions for daily congestion levels.

**The Opportunity:**
- Leveraging historical traffic and weather data to predict the **Traffic Congestion Index (TCI)**.
- Enabling better route planning and traffic management.

---

# 2. Project Objectives

**Primary Objective:**
- Develop a Machine Learning model to predict the daily Traffic Congestion Index (TCI) with high accuracy ($R^2 > 0.70$).

**Secondary Objectives:**
- Identify key factors influencing traffic (e.g., Weather, Day of Week).
- Compare performance of different regression models (Linear, XGBoost, Random Forest).
- Provide actionable insights for traffic management.

---

# 3. Scope & Limitations

**Scope:**
- **Area:** Bangkok Metropolitan Region.
- **Data Period:** Historical data from 2019-2025.
- **Target Variable:** Daily Traffic Congestion Index (0-100).
- **Granularity:** Daily aggregation.

**Limitations:**
- Lack of real-time hourly data for rush-hour specific predictions.
- Does not account for unpredictable events like protests or major accidents.

---

# 4. Team Roles & Responsibilities

| Member | Role | Responsibilities |
|--------|------|------------------|
| **Nitipoom Potichai** | Project Manager | Leadership, coordination, reporting |
| **Veerkawin Naknithichairat** | Data Analyst | Data collection, cleaning, EDA |
| **Kamin Surakhajorn** | Data Scientist | Model development, validation |
| **Yossawee Pimratkasem** | Visualization | Visuals, documentation, slides |
| **Krittapas Imtour** | Tech Lead & QA | QA, tool setup, technical support |

---

# 5. Data Collection

**Data Sources:**

1.  **Traffic Data:**
    - Source: TomTom Traffic Index / Historical Records.
    - Metrics: Congestion Index, Average Speed, Travel Time.

2.  **Weather Data:**
    - Source: OpenWeatherMap API / Historical Weather Data.
    - Metrics: Temperature, Rainfall, Humidity, Wind Speed.

---

# 6. Data Overview

**Dataset Statistics:**
- **Total Samples:** 1,682 daily records (Traffic), 365 daily records (Weather).
- **Merged Dataset:** 351 complete samples after cleaning and merging.
- **Features:** 33 engineered features.

**Key Variables:**
- `congestion_index` (Target)
- `temp_avg`, `rainfall`, `humidity` (Weather)
- `dayofweek`, `is_weekend`, `is_holiday` (Temporal)

---

# 7. Data Cleaning & Preprocessing

**Steps Taken:**
1.  **Handling Missing Values:** Imputed minor gaps using linear interpolation; dropped rows with critical missing target data.
2.  **Outlier Detection:** Identified outliers in `traffic_volume` using IQR method.
3.  **Data Merging:** Joined Traffic and Weather datasets on `date`.
4.  **Type Conversion:** Ensured correct data types for dates and numerical features.

---

# 8. Exploratory Data Analysis (Traffic)

**Traffic Trends:**
- **Weekly Pattern:** Higher congestion on Fridays; lower on Sundays.
- **Seasonal Pattern:** Congestion peaks during the dry season (Nov-Feb) and school terms.
- **Distribution:** TCI follows a near-normal distribution, suitable for regression models.

*(Visual: Time series plot of Congestion Index over time)*

---

# 9. Exploratory Data Analysis (Weather)

**Weather Correlations:**
- **Temperature:** Strong positive correlation with congestion. Hotter days $\rightarrow$ More traffic (AC usage, car preference).
- **Rainfall:** Moderate correlation. Rain slows down traffic flow significantly.
- **Humidity:** Correlated with rain and temperature, acting as a secondary factor.

*(Visual: Correlation Heatmap showing TCI vs. Weather variables)*

---

# 10. Feature Engineering

**Creating Predictive Power:**

1.  **Rolling Statistics:**
    - 7-day and 14-day Rolling Mean/Max/Std of Congestion Index.
    - Captures recent trends and momentum.

2.  **Lag Features:**
    - Lag 1, Lag 7, Lag 14 (Congestion from yesterday, last week).
    - Captures autocorrelation.

3.  **Temporal Features:**
    - Cyclical encoding for `month` and `dayofweek` (Sine/Cosine).

---

# 11. Model Selection Strategy

**Models Evaluated:**
1.  **Linear Regression:** Baseline model. Simple, interpretable, fast.
2.  **XGBoost:** Gradient Boosting. Handles non-linear relationships and outliers well.
3.  **Random Forest:** Ensemble method. Robust to overfitting, good for feature importance.

**Evaluation Metrics:**
- **RMSE** (Root Mean Squared Error) < 15
- **MAE** (Mean Absolute Error) < 10
- **$R^2$ Score** > 0.70

---

# 12. Model Results: Linear Regression

**Performance:**
- **RMSE:** 2.06
- **MAE:** 1.96
- **$R^2$:** 0.7742

**Analysis:**
- Surprisingly strong performance.
- Indicates that the relationship between engineered features (like rolling means) and the target is largely linear.
- **Status:** ✅ Exceeds all targets.

---

# 13. Model Results: XGBoost

**Performance:**
- **RMSE:** 2.22
- **MAE:** 1.95
- **$R^2$:** 0.7359

**Analysis:**
- Good performance, slightly lower $R^2$ than Linear Regression.
- Shows slight overfitting (Train $R^2$ > Test $R^2$).
- **Status:** ✅ Exceeds all targets.

---

# 14. Model Results: Random Forest (Best Model)

**Performance:**
- **RMSE:** 0.81
- **MAE:** 0.63
- **$R^2$:** 0.9645

**Analysis:**
- **Best Performer** after hyperparameter tuning.
- Captures complex interactions between weather and temporal features.
- Extremely low error rates.
- **Status:** ✅ Significantly exceeds all targets.

---

# 15. Model Comparison

| Model | RMSE | MAE | $R^2$ | Rank |
|-------|------|-----|-------|------|
| **Random Forest** | **0.81** | **0.63** | **0.9645** | **1st** |
| Linear Regression | 2.06 | 1.96 | 0.7742 | 2nd |
| XGBoost | 2.22 | 1.95 | 0.7359 | 3rd |

**Conclusion:**
- Random Forest is the superior model for accuracy.
- Linear Regression is a viable alternative if interpretability is the priority.

---

# 16. Feature Importance Analysis

**What drives traffic?**

1.  **Temperature (`temp_avg`):** **46.9%** importance. The single biggest predictor.
2.  **Rolling Mean (7-day):** **19.2%**. Recent traffic history predicts the future.
3.  **Rolling Max (7-day):** **3.9%**. Peak congestion levels matter.
4.  **Lag Features:** Previous day's traffic helps, but less than weather.

---

# 17. Key Insights

1.  **Weather Dominance:** Weather features collectively explain **54.9%** of the prediction power.
2.  **Temperature Impact:** High temperatures correlate strongly with increased congestion.
3.  **History Repeats:** 7-day rolling averages are more predictive than simple lag features, smoothing out daily noise.
4.  **Model Simplicity:** Even simple models (Linear Regression) perform well due to high-quality feature engineering.

---

# 18. Hypothesis Validation

| Hypothesis | Finding | Status |
|------------|---------|--------|
| **H1:** Models achieve $R^2 > 0.70$ | Achieved $R^2 = 0.9645$ | ✅ Confirmed |
| **H2:** Complex models outperform simple ones | Random Forest beat Linear Regression | ✅ Confirmed |
| **H3:** Weather affects traffic significantly | Weather importance ~55% | ✅ Confirmed |
| **H4:** Lag features are most predictive | Weather > Rolling > Lag | ❌ Rejected |

---

# 19. Business Recommendations

**For City Planners:**
- **Heat Mitigation:** Since temperature drives traffic, increasing green spaces could indirectly reduce congestion.
- **Weather-Responsive Signals:** Adjust traffic light timings based on weather forecasts (rain/heat).

**For Commuters:**
- **Plan Ahead:** Use the 7-day trend to plan trips.
- **Weather Check:** Expect heavier traffic on hotter days, not just rainy ones.

---

# 20. Deployment Strategy

**Proposed Pipeline:**
1.  **Data Ingestion:** Daily fetch from TomTom & OpenWeatherMap APIs.
2.  **Preprocessing:** Auto-clean and generate rolling features.
3.  **Inference:** Run Random Forest model.
4.  **Output:** Dashboard showing predicted TCI for the next 24 hours.

**Monitoring:**
- Retrain model monthly to adapt to changing traffic patterns (e.g., new road openings).

---

# 21. Challenges & Solutions

**Challenge 1: Data Granularity**
- *Issue:* Only daily data available; cannot predict hourly rush hours.
- *Solution:* Focused on daily TCI for macro-level planning.

**Challenge 2: Model Overfitting**
- *Issue:* Initial Random Forest model had low test accuracy ($R^2 \approx 0.52$).
- *Solution:* Rigorous hyperparameter tuning (depth, estimators) boosted $R^2$ to 0.96.

---

# 22. Future Work

1.  **Hourly Predictions:** Acquire granular data to predict morning/evening rush hours separately.
2.  **Spatial Analysis:** Break down predictions by district (e.g., Sukhumvit vs. Silom).
3.  **Real-time Integration:** Connect to live traffic sensors for minute-by-minute updates.
4.  **Event Integration:** Incorporate data on concerts, protests, and festivals.

---

# 23. Conclusion

**Project Success:**
- Successfully developed a high-accuracy model ($R^2 = 0.9645$).
- Identified **Temperature** as the critical driver of Bangkok traffic.
- Delivered a scalable, reproducible pipeline for traffic prediction.

**Final Thought:**
Data-driven insights can transform how we manage Bangkok's traffic, moving from reactive to proactive management.

---

# 24. Q&A

**Thank You!**

*Team SWU The Boys*

- Nitipoom Potichai
- Veerkawin Naknithichairat
- Kamin Surakhajorn
- Yossawee Pimratkasem
- Krittapas Imtour
