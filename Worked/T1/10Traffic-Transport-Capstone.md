# CPE312 Capstone Project: Bangkok Traffic Congestion Index Prediction

## Group Information

**Project Title:** Bangkok Traffic Congestion Index Prediction Using Time-Series Machine Learning

**Group Members and Roles:**

| ลำดับที่ | ชื่อ-สกุล | รหัสประจำตัว | บทบาท | ความรับผิดชอบ |
|---------|----------|-----------|--------|------------|
| 1 | นิติภูมิ โพธิชัย | 66109010194 | **Project Manager** | นำแนวทาง, ประสานงาน, รายงานความเคลื่อนไหว |
| 2 | วีร์กวิน นาคนิธิชัยรัชต์ | 66109010201 | **Data Analyst** | เก็บข้อมูล, ทำความสะอาดข้อมูล, EDA |
| 3 | คามิน สุรขจร | 66109010322 | **Data Scientist** | วิเคราะห์ข้อมูล, สร้างโมเดล, ตรวจสอบผล |
| 4 | ยศวีร์ พิมพ์รัฐเกษม | 66109010455 | **Visualization & Documentation** | สร้างกราฟ, เขียนรายงาน, จัดเตรียมนำเสนอ |
| 5 | กฤตภาส อิ่มทั่ว | 66109010180 | **Technical Lead & QA** | ตรวจสอบคุณภาพ, ติดตั้ง tools, support technical |

---

## 1. Problem Definition

### 1.1 Problem Statement

Bangkok's traffic congestion has become a critical urban challenge, with the city experiencing severe congestion during peak hours, particularly between 17:00-18:00. The traffic congestion index in Bangkok averages 38.88 in recent measurements, with historical highs reaching 162.13. Current congestion costs approximately 97 million Thai Baht in wasted fuel daily and increases average travel time by 2 minutes and 40 seconds for every 10 kilometers traveled compared to free-flow conditions.

**Core Problem:** Can we accurately predict Bangkok's daily traffic congestion index using historical congestion data combined with weather features through time-series machine learning models?

**Scope:** This project focuses specifically on predicting the Traffic Congestion Index (TCI) for Bangkok using historical TCI time-series data and weather conditions as input features.

### 1.2 Alignment with Sustainable Development Goals (SDGs)

This capstone project directly supports the following SDGs:

**SDG 11: Sustainable Cities and Communities**
- Target 11.2: Provide sustainable transport systems through data-driven congestion prediction
- Indicator: Improved traffic forecasting accuracy enabling better urban planning

**SDG 13: Climate Action**
- Target 13.2: Support climate-informed transportation decisions
- Indicator: Enable proactive traffic management reducing idle time and emissions

**Project Relevance:** Accurate congestion prediction enables authorities and commuters to make proactive decisions, reducing fuel waste and emissions from unexpected traffic delays.

---

## 2. Research Questions and Objectives

### 2.1 Primary Research Question

**Can machine learning models accurately predict Bangkok's daily Traffic Congestion Index using historical congestion patterns and weather data?**

### 2.2 Secondary Research Questions

1. **Temporal Patterns:** What are the daily, weekly, and seasonal patterns in Bangkok's traffic congestion index?

2. **Weather Impact:** How do weather conditions (temperature, humidity, precipitation) correlate with congestion levels?

3. **Model Performance:** Which machine learning model (Random Forest, XGBoost, or Linear Regression) provides the best prediction accuracy for traffic congestion?

4. **Feature Importance:** Which temporal and weather features are most predictive of congestion levels?

### 2.3 Project Objectives

**Primary Objectives:**

1. **Data Collection:** Collect and clean Bangkok Traffic Congestion Index data (2019-2025) and corresponding weather data.

2. **Exploratory Analysis:** Identify temporal patterns (daily, weekly, seasonal) in congestion levels and correlations with weather.

3. **Feature Engineering:** Create meaningful features including temporal encodings (day of week, month, holidays) and weather metrics.

4. **Predictive Modeling:** Develop and compare machine learning models (Random Forest, XGBoost, Linear Regression) to predict daily congestion index.

5. **Model Evaluation:** Evaluate model performance using RMSE, MAE, and R² metrics to identify the best performing model.

---

## 3. Data Sources

### 3.1 Primary Datasets

| Dataset Name | Source | Description | Data Type | Coverage |
|---|---|---|---|---|
| **Traffic Congestion Index - Bangkok** | CEIC Data / TrafficIndex.org | Daily traffic congestion measurements updated daily | Time-series, Numerical | Bangkok (2019-2025) |
| **Bangkok Weather Data** | OpenWeatherMap / Weather API | Temperature, humidity, precipitation, conditions | Numerical, Time-series | Bangkok (2019-2025) |

### 3.2 Data Quality Assessment

| Quality Dimension | Assessment | Pass/Fail | Explanation |
|---|---|---|---|
| **Completeness** | PASS | ✓ | Bangkok Congestion Index: 1,682+ observations (2019-2025); Weather data aligned with traffic dates |
| **Relevance** | PASS | ✓ | Both datasets directly address research question: can weather and temporal features predict TCI? |
| **Timeliness** | PASS | ✓ | Data updated through November 2025 |
| **Consistency** | PASS | ✓ | Standardized daily measurements with consistent methodology |

---

## 4. Expected Impact

### 4.1 Expected Insights

1. **Temporal Patterns:** Identification of daily, weekly, and seasonal congestion patterns (expected: weekday peaks, Monday/Friday higher, rainy season elevated)

2. **Weather Correlations:** Quantified relationship between weather conditions and congestion levels

3. **Prediction Accuracy:** Machine learning model achieving RMSE < 15 for daily TCI prediction

4. **Feature Importance:** Ranking of most predictive features for congestion forecasting

### 4.2 Practical Applications

- **Commuters:** Better travel planning based on predicted congestion
- **Traffic Authorities:** Proactive traffic management during predicted high-congestion periods
- **Urban Planners:** Data-driven insights for infrastructure planning

---

## 5. Methodology

### 5.1 Data Processing Pipeline

1. **Data Collection:** Download traffic congestion index and weather data
2. **Data Cleaning:** Handle missing values, remove outliers, standardize formats
3. **Feature Engineering:** Create temporal features (day of week, month, cyclical encodings) and weather aggregates

### 5.2 Analytical Methods

- **Exploratory Data Analysis:** Time-series visualization, correlation analysis, distribution analysis
- **Predictive Modeling:** Random Forest, XGBoost, Linear Regression
- **Model Evaluation:** Train/test split, cross-validation, RMSE/MAE/R² metrics

---

## 6. Timeline and Deliverables

### 6.1 Project Phases

| Phase | Duration | Key Activities | Deliverables |
|---|---|---|---|
| Data Collection & Cleaning | Week 1-2 | Download datasets, clean and merge data | Cleaned dataset |
| Exploratory Analysis | Week 3-4 | Statistical analysis, visualization | EDA report, figures |
| Feature Engineering | Week 5 | Create temporal and weather features | Feature dataset |
| Model Development | Week 6-8 | Train and tune ML models | Trained models |
| Model Evaluation | Week 9-10 | Compare models, select best | Evaluation report |
| Documentation | Week 11-12 | Final report and presentation | Final deliverables |

### 6.2 Expected Deliverables

1. **Data:** Cleaned traffic and weather dataset with engineered features
2. **Models:** Trained Random Forest, XGBoost, and Linear Regression models
3. **Evaluation:** Model comparison report with performance metrics
4. **Presentation:** Final slides summarizing methodology and findings

---

## 7. Technical Requirements

**Tools & Libraries:**
- Python 3.x
- Pandas, NumPy (data processing)
- Scikit-learn (machine learning)
- Matplotlib, Seaborn (visualization)
- Jupyter Notebook (analysis environment)

**Skills Required:**
- Time-series data analysis
- Feature engineering
- Machine learning model training and evaluation
- Data visualization
