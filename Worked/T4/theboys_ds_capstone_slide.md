# Bangkok Traffic Congestion Index Prediction
## CPE312 Capstone Project - Presentation Slides

### Group: The Boys
**Date:** December 4, 2025

---

## Slide 1: Title Slide
- **Project Title:** Bangkok Traffic Congestion Index Prediction Using Machine Learning
- **Team Members:**
  1. Nitipoom Potichai (66109010194) - Project Manager
  2. Veerakawin Naknithichairat (66109010201) - Data Analyst
  3. Kamin Surakhajorn (66109010322) - Data Scientist
  4. Yossawee Pimratkasem (66109010455) - Visualization & Documentation
  5. Krittapas Imtour (66109010180) - Technical Lead & QA
- **Course:** CPE312 Data Science Capstone

---

## Slide 2: Outline
1. Executive Summary
2. Problem Statement
3. Data & Methodology
4. Exploratory Data Analysis (EDA)
5. Model Development & Results
6. Conclusions & Future Work

---

## Slide 3: Executive Summary
- **Objective:** Predict Bangkok's daily Traffic Congestion Index (TCI) to aid travel planning.
- **Data:** 351 daily observations (merged Traffic & Weather data).
- **Models:** Random Forest, XGBoost, Linear Regression.
- **Best Result:** **Random Forest** with **RMSE = 0.81**, **MAE = 0.63**, **R² = 0.9645**.
- **Key Insight:** Temperature (`temp_avg`) is the dominant predictor (46.9% importance).

---

## Slide 4: Problem Statement
- **Context:** Bangkok is infamous for traffic congestion, costing the economy ~97 million THB daily in wasted fuel.
- **Pain Point:** Commuters lack accurate daily congestion forecasts to plan their trips.
- **Research Question:** Can we accurately predict the daily Traffic Congestion Index using historical traffic patterns and weather data?
- **Target:** Achieve R² > 0.70 and RMSE < 15.

---

## Slide 5: Data Overview
| Dataset | Original Rows | Description |
|---------|---------------|-------------|
| **Traffic Data** | 1,682 | Daily TCI from TomTom (2019-2025) |
| **Weather Data** | 365 | Daily Temp, Humidity, Rain (2023-2024) |
| **Merged Data** | **351** | Intersection used for modeling |

**Features (33 Total):**
- **Target:** `congestion_index`
- **Input:** Weather, Date/Time info, Lagged features, Rolling statistics.

---

## Slide 6: Methodology
1. **Data Collection:** Scraped TomTom traffic index and OpenWeatherMap API.
2. **Data Cleaning:** Handled missing values, aligned dates, removed outliers.
3. **Feature Engineering:**
   - **Temporal:** `dayofweek`, `is_weekend`, Cyclical encoding (`month_sin`, `month_cos`).
   - **Lag/Rolling:** 7-day and 14-day rolling means/max/std.
4. **Model Training:** Split 60/20/20 (Train/Val/Test). Trained RF, XGB, LR.
5. **Evaluation:** Metrics: RMSE, MAE, R².

---

## Slide 7: Feature Engineering Highlights
- **Weather:** `temp_avg`, `humidity`, `rainfall`.
- **Rolling Statistics:** Captures recent trends (e.g., `congestion_index_rolling_mean_7`).
- **Lag Features:** Captures autocorrelation (e.g., `congestion_index_lag_1`).
- **Cyclical Time:** Encoded months and days to preserve cyclical nature (Dec -> Jan).

---

## Slide 8: EDA - Temporal Patterns
- **Weekly Pattern:** Weekdays show significantly higher congestion than weekends.
- **Peak Days:** Friday evenings typically show the highest congestion index.
- **Seasonal:** Congestion varies with school terms and holidays.

---

## Slide 9: EDA - Weather Correlation
- **Temperature:** Strong correlation found. Hotter days often correlate with higher congestion (more AC usage, more driving).
- **Rainfall:** Positive correlation observed; rain slows down traffic flow significantly.
- **Feature Importance:** Weather features collectively explain **54.9%** of the variance.

---

## Slide 10: Model Comparison Results
| Model | RMSE (Lower is better) | MAE (Lower is better) | R² (Higher is better) | Status |
|-------|------------------------|-----------------------|-----------------------|--------|
| **Random Forest** | **0.81** | **0.63** | **0.9645** | 🥇 Best |
| Linear Regression | 2.06 | 1.96 | 0.7742 | 🥈 Good |
| XGBoost | 2.22 | 1.95 | 0.7359 | 🥉 Good |

**Verdict:** Random Forest significantly outperformed others after hyperparameter tuning.

---

## Slide 11: Feature Importance (Random Forest/XGBoost)
**Top 3 Predictive Features:**
1. **`temp_avg` (46.9%)**: Daily average temperature is the strongest driver.
2. **`congestion_index_rolling_mean_7` (19.2%)**: The past week's average congestion.
3. **`congestion_index_rolling_max_7` (3.9%)**: The worst congestion in the past week.

---

## Slide 12: Predictions vs Actual
- **Visual Analysis:** The Random Forest model tracks the actual congestion index very closely.
- **Performance:** It successfully captures both the weekly seasonality and sudden drops (e.g., holidays).
- **Error:** Minimal error observed, with MAE of only 0.63 units on a 0-100 scale.

---

## Slide 13: Conclusions
1. **Success:** We achieved an R² of **0.9645**, far exceeding our target of 0.70.
2. **Key Driver:** Weather (Temperature) is a critical factor in Bangkok's traffic, more so than just historical lag.
3. **Application:** This model is ready for deployment to help commuters plan travel based on weather forecasts.

---

## Slide 14: Limitations & Future Work
**Limitations:**
- **Granularity:** Currently predicts *daily* average, not hourly rush-hour spikes.
- **Spatial:** Predicts city-wide index, not specific roads (e.g., Ladprao vs. Silom).

**Future Work:**
- **Hourly Model:** Collect hourly data to predict morning/evening rush hours.
- **Real-time Integration:** Connect to live traffic APIs for real-time forecasting.
- **Event Data:** Incorporate data on protests, concerts, or special events.

---

## Slide 15: Q&A
**Thank You!**

**GitHub Repository:** https://github.com/SWU-The-Boys-CPE/CPE312-Capstone-Project
**Questions?**
