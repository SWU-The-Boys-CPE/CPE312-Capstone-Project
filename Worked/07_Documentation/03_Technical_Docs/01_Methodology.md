# Methodology Document

**Project:** Urban Traffic Flow Optimization and Public Transit Efficiency Analysis in Bangkok Metropolitan Area

**Version:** 1.0

**Date:** November 16, 2025

**Authors:** CPE312 Capstone Team - The Boys CPE

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Research Design](#2-research-design)
3. [Data Collection](#3-data-collection)
4. [Data Preprocessing](#4-data-preprocessing)
5. [Exploratory Data Analysis](#5-exploratory-data-analysis)
6. [Feature Engineering](#6-feature-engineering)
7. [Modeling Approach](#7-modeling-approach)
8. [Validation Strategy](#8-validation-strategy)
9. [Optimization Methods](#9-optimization-methods)
10. [Evaluation Metrics](#10-evaluation-metrics)
11. [Reproducibility](#11-reproducibility)

---

## 1. Introduction

### 1.1 Research Framework

This capstone project employs a comprehensive data science methodology combining:
- **Exploratory Data Analysis (EDA)** for pattern discovery
- **Statistical Analysis** for hypothesis testing
- **Machine Learning** for predictive modeling
- **Optimization Algorithms** for route recommendations
- **Geospatial Analysis** for hotspot identification

### 1.2 Research Questions

**Primary Question:**
What data-driven insights can be derived from traffic flow, accident patterns, and public transit data to develop actionable recommendations for reducing congestion and improving transportation efficiency in Bangkok?

**Secondary Questions:**
1. What are the temporal and spatial patterns of traffic congestion in Bangkok?
2. What correlations exist between accident frequency and traffic congestion?
3. How efficiently are current public transit routes operating?
4. Can machine learning models predict traffic congestion 15-60 minutes in advance?
5. How do road infrastructure characteristics affect traffic flow?

---

## 2. Research Design

### 2.1 Study Type
- **Approach:** Mixed-methods data analysis
- **Design:** Observational, retrospective analysis with predictive modeling
- **Data:** Secondary data from multiple sources (2019-2025)
- **Scale:** City-level (Bangkok Metropolitan Area)

### 2.2 Research Phases

**Phase 1: Data Preparation (Weeks 1-2)**
- Objective: Acquire, clean, and integrate multi-source datasets
- Output: Cleaned, integrated database ready for analysis

**Phase 2: Exploratory Analysis (Weeks 3-4)**
- Objective: Understand data characteristics, identify patterns
- Output: EDA report with visualizations and initial findings

**Phase 3: Feature Engineering (Weeks 4-5)**
- Objective: Create features for predictive modeling
- Output: Feature-engineered dataset with documentation

**Phase 4: Predictive Modeling (Weeks 6-8)**
- Objective: Develop and validate prediction models
- Output: Trained models with performance metrics

**Phase 5: Optimization & Recommendations (Weeks 9-10)**
- Objective: Generate actionable recommendations
- Output: Route optimization results, policy recommendations

**Phase 6: Documentation & Presentation (Weeks 11-12)**
- Objective: Document findings and prepare deliverables
- Output: Final report, presentation, dashboard

---

## 3. Data Collection

### 3.1 Data Sources

#### Primary Datasets

**1. Bangkok Traffic Congestion Index**
- **Source:** CEIC Data / TrafficIndex.org
- **Type:** Time-series data
- **Coverage:** 2019-2025 (daily measurements, 1,682+ observations)
- **Variables:** date, congestion_index, time_of_day, region
- **Collection Method:** Web scraping / API access
- **Justification:** Provides authentic Bangkok-specific congestion patterns essential for temporal analysis

**2. US Accidents Dataset (Methodology Reference)**
- **Source:** Kaggle (Sobhan Moosavi et al.)
- **Type:** Structured, geospatial
- **Coverage:** 2.8M+ records (2016-2021), 49 US states
- **Variables:** location (lat/lon), severity, weather, road_type, datetime
- **Collection Method:** Kaggle download
- **Justification:** Largest public accident dataset; methodology transferable to Bangkok analysis

**3. OpenStreetMap Road Network (Bangkok)**
- **Source:** OpenStreetMap
- **Type:** Geospatial (GeoJSON/Shapefile)
- **Coverage:** Complete Bangkok road network
- **Variables:** road classifications, intersections, connectivity
- **Collection Method:** Overpass API extraction
- **Justification:** Free, up-to-date, comprehensive road topology for spatial analysis

**4. Weather and Environmental Data**
- **Source:** NOAA, NASA Weather APIs
- **Type:** Time-series
- **Coverage:** 2019-2025 (daily, Bangkok)
- **Variables:** temperature, precipitation, visibility, wind
- **Collection Method:** API calls
- **Justification:** Weather significantly impacts traffic behavior and accident rates

**5. Public Transit Ridership Data**
- **Source:** Bangkok BMA/BTS/MRT (pending) + reference datasets (Chicago, Helsinki)
- **Type:** Time-series
- **Coverage:** Station entries, ridership by route/time
- **Variables:** station_id, route_id, datetime, passenger_count
- **Collection Method:** Official request + Kaggle reference datasets
- **Justification:** Essential for transit efficiency analysis

### 3.2 Data Collection Procedures

**Step 1: Data Acquisition**
1. Download datasets from identified sources
2. Document source URLs, access dates, version numbers
3. Store raw data in `02_Data/Raw/` (not version controlled)
4. Create metadata files documenting each dataset

**Step 2: Data Validation**
1. Verify file integrity (checksums if available)
2. Check completeness (record counts, date ranges)
3. Initial format validation
4. Document any anomalies or issues

**Step 3: Data Documentation**
1. Update Data README with dataset details
2. Create data dictionary for each dataset
3. Document collection procedures
4. Note any access restrictions or terms of use

### 3.3 Ethical Considerations
- All datasets are publicly available or properly authorized
- No personal identifiable information (PII) is collected or used
- Data usage complies with terms of service
- Project is for educational/research purposes only
- Proper attribution given to all data sources

---

## 4. Data Preprocessing

### 4.1 Data Cleaning Pipeline

#### Step 1: Missing Value Analysis
**Method:**
```python
# Identify missing values
missing_summary = df.isnull().sum()
missing_pct = (missing_summary / len(df)) * 100

# Document missing patterns
for col in missing_cols:
    - Pattern: Random, systematic, or clustered?
    - Reason: Sensor failure, data collection gap, or inherent?
```

**Handling Strategy:**
- **Time-series data (traffic, weather):** Linear interpolation (max 7-day gap)
- **Categorical data:** Mode imputation or 'Unknown' category
- **Numerical data (non-time-series):** Median imputation
- **High missingness (>20%):** Consider dropping variable or using indicator variable

#### Step 2: Duplicate Detection and Removal
**Method:**
```python
# Identify duplicates
duplicates = df[df.duplicated(subset=['date', 'location'], keep=False)]

# Remove based on criteria
df_clean = df.drop_duplicates(subset=['date', 'location'], keep='first')
```

**Criteria:**
- Exact duplicates: Remove all but first occurrence
- Near-duplicates: Manual review or fuzzy matching
- Document number of duplicates removed

#### Step 3: Outlier Detection
**Method 1: IQR (Interquartile Range)**
```python
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
```

**Method 2: Z-Score**
```python
z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
outliers = z_scores > 3
```

**Handling Strategy:**
- **Traffic congestion:** Flag but retain (extreme events are real)
- **Weather:** Cap at realistic Bangkok ranges (15-42°C for temperature)
- **Accidents:** Validate geographic bounds, flag statistical outliers
- Document all outliers and treatment decisions

#### Step 4: Data Type Validation
**Conversions:**
- Datetime columns: Convert to pandas datetime, ensure consistent timezone (UTC+7)
- Categorical columns: Convert to appropriate dtype (category or string)
- Numerical columns: Ensure int/float as appropriate
- Coordinates: Validate lat/lon ranges

**Validation Checks:**
- Date ranges within expected bounds (2019-2025)
- Coordinates within Bangkok bounds (13.5-13.95°N, 100.3-100.9°E)
- Congestion index non-negative
- Categorical values match expected categories

### 4.2 Data Integration

#### Temporal Alignment
**Challenge:** Different datasets have different temporal resolutions
- Traffic: Daily
- Weather: Daily
- Accidents: Event-level (aggregate to daily)

**Solution:**
1. Standardize all timestamps to UTC+7 (Bangkok time)
2. Aggregate event-level data to daily granularity
3. Align datasets by date using left join (traffic as base)
4. Fill missing values appropriately

#### Spatial Alignment
**For Geospatial Data:**
1. Ensure consistent coordinate reference system (WGS84)
2. Validate coordinates within Bangkok bounds
3. Spatial join of accident locations to road network
4. Aggregate accidents by district/area for analysis

### 4.3 Quality Assurance Checklist
- [ ] Missing values < 10% overall
- [ ] No duplicate records
- [ ] All outliers documented
- [ ] Data types validated
- [ ] Temporal alignment complete
- [ ] Spatial validation complete
- [ ] Data dictionary updated
- [ ] Quality report generated

---

## 5. Exploratory Data Analysis (EDA)

### 5.1 Descriptive Statistics

#### Univariate Analysis
**For Numerical Variables:**
```python
summary_stats = {
    'count': df[col].count(),
    'mean': df[col].mean(),
    'median': df[col].median(),
    'std': df[col].std(),
    'min': df[col].min(),
    'q1': df[col].quantile(0.25),
    'q3': df[col].quantile(0.75),
    'max': df[col].max(),
    'skewness': df[col].skew(),
    'kurtosis': df[col].kurtosis()
}
```

**For Categorical Variables:**
```python
frequency_table = df[col].value_counts()
mode = df[col].mode()[0]
unique_count = df[col].nunique()
```

#### Bivariate Analysis
**Correlation Analysis:**
```python
# Pearson correlation for continuous variables
correlation_matrix = df[numeric_cols].corr(method='pearson')

# Spearman for ordinal or non-linear relationships
spearman_corr = df[numeric_cols].corr(method='spearman')
```

**Key Relationships to Explore:**
1. Traffic congestion vs time of day
2. Traffic congestion vs day of week
3. Traffic congestion vs weather conditions
4. Accidents vs congestion levels
5. Weather vs accident frequency

### 5.2 Visualization Strategy

#### Required Visualizations (Minimum 10)

**1. Congestion Distribution (Histogram)**
- Purpose: Understand congestion index distribution
- Expected: Right-skewed with peak around mean (38.88)

**2. Temporal Heatmap (Hour x Day of Week)**
- Purpose: Identify peak congestion times
- Expected: Highest values at 17:00-18:00 weekdays

**3. Time Series Plot (2019-2025 Trend)**
- Purpose: Long-term trend analysis
- Expected: Relatively stable with seasonal variations

**4. Seasonal Bar Chart (Monthly Comparison)**
- Purpose: Identify seasonal patterns
- Expected: Variations between dry, rainy, cool seasons

**5. Weekday vs Weekend Line Plot**
- Purpose: Compare traffic patterns
- Expected: 30-40% lower congestion on weekends

**6. Hotspot Geographic Map**
- Purpose: Spatial congestion visualization
- Expected: Vibhavadi Rangsit Road, Sukhumvit as primary hotspots

**7. Scatter Plot (Accidents vs Congestion)**
- Purpose: Correlation analysis
- Expected: Positive correlation (r ~0.4-0.6)

**8. Box Plot (Weather Impact on Congestion)**
- Purpose: Weather condition comparison
- Expected: Higher congestion during rain

**9. Correlation Matrix Heatmap**
- Purpose: Feature relationships overview
- Expected: Strong correlations between temporal features and congestion

**10. Accident Severity Distribution**
- Purpose: Understand accident patterns
- Expected: More minor accidents, fewer severe

### 5.3 Statistical Hypothesis Testing

**Test 1: Weekday vs Weekend Congestion**
- **Null Hypothesis (H0):** No significant difference in mean congestion between weekdays and weekends
- **Alternative (H1):** Weekday congestion significantly higher than weekend
- **Test:** Independent samples t-test
- **Significance Level:** α = 0.05
- **Expected:** Reject H0, weekdays significantly higher

**Test 2: Weather Impact on Accidents**
- **H0:** No association between rain and accident frequency
- **H1:** Rain increases accident frequency
- **Test:** Chi-square test or Mann-Whitney U test
- **Significance Level:** α = 0.05
- **Expected:** Reject H0, rain increases accidents by ~25%

**Test 3: Peak Hour vs Off-Peak Congestion**
- **H0:** No difference between 17:00-18:00 and other hours
- **H1:** 17:00-18:00 significantly more congested
- **Test:** ANOVA with post-hoc Tukey HSD
- **Significance Level:** α = 0.05
- **Expected:** Reject H0, peak hour significantly higher

---

## 6. Feature Engineering

### 6.1 Temporal Features

**Basic Temporal Features:**
```python
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['hour'] = df['datetime'].dt.hour
df['dayofweek'] = df['datetime'].dt.dayofweek  # 0=Monday, 6=Sunday
df['day_of_month'] = df['datetime'].dt.day
df['week_of_year'] = df['datetime'].dt.isocalendar().week
df['quarter'] = df['datetime'].dt.quarter
```

**Derived Temporal Features:**
```python
# Weekend indicator
df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)

# Holiday indicator (Bangkok specific)
bangkok_holidays = {
    (1, 1): 'New Year',
    (4, 13): 'Songkran',
    (4, 14): 'Songkran',
    (4, 15): 'Songkran',
    (5, 1): 'Labour Day',
    (12, 5): 'King Birthday',
    (12, 31): 'New Year Eve'
}
df['is_holiday'] = df.apply(
    lambda x: (x['month'], x['day']) in bangkok_holidays,
    axis=1
).astype(int)

# Season (Thailand)
def get_season(month):
    if month in [3, 4, 5]:
        return 'dry'  # Dry/Hot season
    elif month in [6, 7, 8, 9, 10]:
        return 'rainy'  # Rainy season
    else:
        return 'cool'  # Cool season
        
df['season'] = df['month'].apply(get_season)

# Peak hour indicators
df['is_morning_rush'] = df['hour'].isin([7, 8, 9]).astype(int)
df['is_evening_rush'] = df['hour'].isin([17, 18, 19]).astype(int)
df['is_rush_hour'] = (df['is_morning_rush'] | df['is_evening_rush']).astype(int)
```

### 6.2 Lagged Features

**Purpose:** Capture historical patterns for time-series prediction

```python
# Previous day values
lags = [1, 7, 14, 30]  # 1 day, 1 week, 2 weeks, 1 month
for lag in lags:
    df[f'congestion_lag_{lag}'] = df['congestion_index'].shift(lag)

# Previous week same day
df['congestion_lag_7_same_day'] = df.groupby('dayofweek')['congestion_index'].shift(1)
```

### 6.3 Rolling Window Features

**Purpose:** Capture trends and volatility

```python
windows = [7, 14, 30]
for window in windows:
    # Rolling mean
    df[f'congestion_rolling_mean_{window}'] = df['congestion_index'].rolling(window=window).mean()
    
    # Rolling standard deviation (volatility)
    df[f'congestion_rolling_std_{window}'] = df['congestion_index'].rolling(window=window).std()
    
    # Rolling min/max
    df[f'congestion_rolling_min_{window}'] = df['congestion_index'].rolling(window=window).min()
    df[f'congestion_rolling_max_{window}'] = df['congestion_index'].rolling(window=window).max()
```

### 6.4 Spatial Features

**District/Area Clustering:**
```python
# Group by geographic clusters
df['district'] = map_coordinates_to_district(df['latitude'], df['longitude'])

# Distance to major intersection
df['dist_to_major_intersection'] = calculate_distance_to_nearest_intersection(
    df['latitude'], df['longitude'], major_intersections
)

# Road type from OpenStreetMap
df['road_type'] = map_to_road_type(df['latitude'], df['longitude'], osm_network)
```

### 6.5 Interaction Features

**Purpose:** Capture non-linear relationships

```python
# Weekend * Month interaction
df['weekend_x_month'] = df['is_weekend'] * df['month']

# Weather * Rush hour
df['rain_x_rush_hour'] = (df['weather_category'] == 'rain') * df['is_rush_hour']

# Season * Day of week
df['season_x_dayofweek'] = df['season'] + '_' + df['dayofweek'].astype(str)
```

### 6.6 Feature Selection

**Method 1: Correlation-based**
- Remove features with correlation > 0.95 (multicollinearity)
- Retain features with |correlation to target| > 0.1

**Method 2: Feature Importance (from Tree-based Models)**
```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
feature_importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

# Select top N features
selected_features = feature_importance.head(50)['feature'].tolist()
```

**Method 3: Recursive Feature Elimination (RFE)**
```python
from sklearn.feature_selection import RFE

rfe = RFE(estimator=rf, n_features_to_select=50)
rfe.fit(X_train, y_train)
selected_features = X_train.columns[rfe.support_].tolist()
```

---

## 7. Modeling Approach

### 7.1 Problem Formulation

**Prediction Task:** Regression - Predict congestion index (continuous value)

**Input:** Temporal features, weather, historical congestion, accidents
**Output:** Congestion index for next 15-60 minutes (or next day for daily data)

### 7.2 Model Selection Rationale

#### Baseline Models

**1. Simple Average**
- **Method:** Mean congestion by hour/day
- **Purpose:** Establish minimum performance baseline
- **Expected RMSE:** ~1.2, MAPE ~15%

**2. ARIMA (AutoRegressive Integrated Moving Average)**
- **Purpose:** Classical time-series benchmark
- **Parameters:** (p, d, q) determined by ACF/PACF plots or auto_arima
- **Expected RMSE:** ~0.95, MAPE ~12%
- **Pros:** Interpretable, well-established
- **Cons:** Assumes stationarity, limited feature incorporation

#### Machine Learning Models

**3. Random Forest**
```python
from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)
```
- **Expected RMSE:** ~0.85, MAPE ~10%
- **Pros:** Handles non-linearity, feature importance, robust to outliers
- **Cons:** Can overfit, less effective for time-series patterns

**4. XGBoost (Gradient Boosting)**
```python
import xgboost as xgb

xgb_model = xgb.XGBRegressor(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
```
- **Expected RMSE:** ~0.78, MAPE ~8.5%
- **Pros:** State-of-the-art performance, handles complex patterns
- **Cons:** Requires hyperparameter tuning, can overfit

#### Deep Learning Models

**5. LSTM (Long Short-Term Memory)**
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

lstm_model = Sequential([
    LSTM(64, activation='relu', return_sequences=True, input_shape=(timesteps, features)),
    Dropout(0.2),
    LSTM(32, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

lstm_model.compile(optimizer='adam', loss='mse')
```
- **Expected RMSE:** ~0.82, MAPE ~9%
- **Pros:** Excellent for time-series, captures long-term dependencies
- **Cons:** Requires more data, longer training time, hyperparameter sensitive

### 7.3 Hyperparameter Tuning

**Method: Grid Search or Random Search with Cross-Validation**

**XGBoost Hyperparameter Grid:**
```python
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [4, 6, 8],
    'learning_rate': [0.01, 0.1, 0.3],
    'subsample': [0.7, 0.8, 0.9],
    'colsample_bytree': [0.7, 0.8, 0.9]
}

from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(
    estimator=xgb_model,
    param_grid=param_grid,
    scoring='neg_mean_squared_error',
    cv=5,
    n_jobs=-1
)
```

**LSTM Hyperparameter Search:**
- Units: [32, 64, 128]
- Dropout: [0.1, 0.2, 0.3]
- Layers: [1, 2]
- Batch size: [16, 32, 64]
- Epochs: Determined by early stopping

---

## 8. Validation Strategy

### 8.1 Train-Validation-Test Split

**Temporal Split (for Time-Series):**
```python
# Sort by date
df = df.sort_values('date')

# Split ratios
train_ratio = 0.60  # 60% for training
val_ratio = 0.20    # 20% for validation
test_ratio = 0.20   # 20% for testing

n = len(df)
train_size = int(n * train_ratio)
val_size = int(n * val_ratio)

train_df = df.iloc[:train_size]
val_df = df.iloc[train_size:train_size + val_size]
test_df = df.iloc[train_size + val_size:]
```

**Rationale:**
- Chronological split prevents data leakage
- Validation set used for hyperparameter tuning
- Test set held out until final evaluation

### 8.2 Cross-Validation

**Time-Series Cross-Validation:**
```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
for train_index, val_index in tscv.split(X):
    X_train, X_val = X[train_index], X[val_index]
    y_train, y_val = y[train_index], y[val_index]
    # Train and evaluate model
```

### 8.3 Performance Metrics

**Primary Metrics:**

**1. RMSE (Root Mean Squared Error)**
```python
from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
```
- Penalizes large errors more heavily
- Same unit as target variable
- Target: RMSE < 0.80 for traffic prediction

**2. MAE (Mean Absolute Error)**
```python
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_true, y_pred)
```
- Average absolute difference
- More robust to outliers than RMSE
- Target: MAE < 0.65

**3. MAPE (Mean Absolute Percentage Error)**
```python
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
```
- Percentage error (interpretable)
- Target: MAPE < 10%

**4. R² (Coefficient of Determination)**
```python
from sklearn.metrics import r2_score
r2 = r2_score(y_true, y_pred)
```
- Proportion of variance explained
- Target: R² > 0.85

**Secondary Metrics:**
- Directional Accuracy: % of correct trend predictions (up/down)
- Peak Hour Accuracy: RMSE specifically for 17:00-18:00
- Weekend Accuracy: RMSE specifically for weekends

---

## 9. Optimization Methods

### 9.1 Route Optimization

**Problem:** Find optimal transit routes to minimize congestion and travel time

**Approach: Genetic Algorithm**
```python
class RouteOptimizer:
    def __init__(self, population_size=100, generations=50):
        self.population_size = population_size
        self.generations = generations
    
    def fitness_function(self, route):
        """
        Minimize: travel_time + congestion_penalty
        Maximize: coverage
        """
        travel_time = calculate_travel_time(route)
        congestion = calculate_route_congestion(route)
        coverage = calculate_population_coverage(route)
        
        return -(travel_time + 0.5 * congestion - 2 * coverage)
    
    def optimize(self):
        # Initialize population
        # Selection
        # Crossover
        # Mutation
        # Iterate for generations
        return best_route
```

**Constraints:**
- Max route length: 30 km
- Max deviation from existing route: 20%
- Must serve existing stations

### 9.2 Hotspot Prioritization

**Method: Kernel Density Estimation (KDE)**
```python
from scipy.stats import gaussian_kde

# Create density map
kde = gaussian_kde([latitudes, longitudes])
density = kde([grid_lat, grid_lon])

# Identify hotspots (top 75th percentile)
threshold = np.percentile(density, 75)
hotspots = density > threshold
```

---

## 10. Evaluation Metrics

### 10.1 Model Performance Evaluation

**Confusion Matrix (for Classification Tasks):**
If predicting congestion categories (low, medium, high):
```python
from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_true_cat, y_pred_cat))
print(confusion_matrix(y_true_cat, y_pred_cat))
```

### 10.2 Business Impact Metrics

**Congestion Reduction Potential:**
```python
baseline_congestion = mean(historical_congestion)
optimized_congestion = mean(predicted_with_interventions)
reduction = (baseline_congestion - optimized_congestion) / baseline_congestion * 100
```
Target: 15-25% reduction

**Economic Impact:**
```python
daily_fuel_waste_baseline = 97_000_000  # Thai Baht
reduction_pct = 0.15  # 15% reduction
daily_savings = daily_fuel_waste_baseline * reduction_pct
annual_savings = daily_savings * 365
```

---

## 11. Reproducibility

### 11.1 Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install exact versions
pip install -r requirements.txt
```

### 11.2 Random Seed Setting
```python
# Python
import random
random.seed(42)

# NumPy
import numpy as np
np.random.seed(42)

# TensorFlow
import tensorflow as tf
tf.random.set_seed(42)

# Scikit-learn
# Pass random_state=42 to all estimators
```

### 11.3 Data Versioning
- Raw data: Store with collection date in filename
- Processed data: Version with date and processing script version
- Models: Save with timestamp and hyperparameters

### 11.4 Code Documentation
- All functions have docstrings
- README in each directory
- Comments for complex logic
- Jupyter notebooks with markdown explanations

---

## References

1. Moosavi, S., et al. (2019). "A Countrywide Traffic Accident Dataset"
2. CEIC Data. (2025). "Bangkok Traffic Congestion Index"
3. OpenStreetMap Contributors. (2025). "Bangkok Road Network Data"
4. Hastie, T., Tibshirani, R., & Friedman, J. (2009). "The Elements of Statistical Learning"
5. Hochreiter, S., & Schmidhuber, J. (1997). "Long Short-Term Memory"
6. Chen, T., & Guestrin, C. (2016). "XGBoost: A Scalable Tree Boosting System"

---

**Document Version:** 1.0

**Last Updated:** November 16, 2025

**Authors:**
- วีร์กวิน นาคนิธิชัยรัชต์ (Data Analyst)
- คามิน สุรขจร (Data Scientist)
- กฤตภาส อิ่มทั่ว (Technical Lead)

**Approved by:** นิติภูมิ โพธิชัย (Project Manager)
