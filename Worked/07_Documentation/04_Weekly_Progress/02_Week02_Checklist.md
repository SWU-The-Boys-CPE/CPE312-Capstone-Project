# Week 2: Data Collection, Cleaning, and Initial EDA - Checklist

**Project:** Urban Traffic Flow Optimization and Public Transit Efficiency Analysis in Bangkok Metropolitan Area

**Week:** 2 (Data Collection, Cleaning, and Initial EDA Phase)

**Date Range:** [Start Date] - [End Date]

**Status:** ⏳ In Progress

---

## Preparing the Dataset for Preprocessing and EDA

To begin this phase, we prepare the datasets that have been identified in Week 1. These datasets will be used for the Preprocessing and Exploratory Data Analysis (EDA) process, which should be completed within weeks 2-4.

### Steps to Prepare the Dataset

1. **Data Collection:** Gather all relevant data from identified sources
   - Ensure that the data is complete and accurate
   - Document data sources and collection methods

2. **Data Cleaning:** Review the collected data for inconsistencies, missing values, or errors
   - Clean the data by addressing issues found
   - Document cleaning procedures

3. **Data Organization:** Organize the dataset in a structured manner
   - Arrange data into appropriate columns, rows, and formats
   - Ready for analysis

---

## 1. การทำความสะอาดข้อมูลและการเตรียมข้อมูล (Data Cleaning and Preprocessing)

### 1.1 การประเมินคุณภาพข้อมูล (Data Quality Assessment)

#### Bangkok Traffic Congestion Index Dataset

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Missing Values** ตรวจสอบขอบเขตของข้อมูลที่ขาดหายและวิธีการจัดการกับข้อมูลที่ขาดหาย | ☐ | Target: <0.5% missing. Method: Linear interpolation for time-series | Data Analyst |
| **Outliers** ระบุค่าที่ผิดปกติและอธิบายวิธีการจัดการกับค่าผิดปกติเหล่านี้ (เช่น การลบ การปรับเปลี่ยน) | ☐ | Use IQR method (1.5x multiplier). Document extreme congestion events | Data Analyst |
| **Duplicates** ตรวจสอบรายการข้อมูลที่ซ้ำกันและวิธีการจัดการกับข้อมูลซ้ำ | ☐ | Check by date-time combinations. Remove exact duplicates | Data Analyst |
| **Data Types** ตรวจสอบความถูกต้องของประเภทข้อมูล (เช่น วันที่ ตัวเลข) | ☐ | Ensure datetime format (UTC+7), numeric types for congestion index | Data Analyst |
| **Temporal Consistency** ตรวจสอบความสม่ำเสมอของช่วงเวลา | ☐ | Verify daily granularity, identify gaps in time series | Data Analyst |

#### US Accidents Dataset (Methodology Reference)

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Missing Values** | ☐ | Document missing patterns by field. Focus on key fields: location, severity, weather | Data Analyst |
| **Outliers** | ☐ | Identify unusual severity levels or geographic outliers | Data Analyst |
| **Duplicates** | ☐ | Check by incident_id and location-time combinations | Data Analyst |
| **Data Types** | ☐ | Validate coordinates (lat/lon), severity (categorical), timestamps | Data Analyst |
| **Geographic Validation** | ☐ | Ensure coordinates within valid ranges, match to road network | Data Analyst |

#### OpenStreetMap Road Network (Bangkok)

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Missing Values** | ☐ | Check road classifications, intersection nodes | Data Analyst |
| **Outliers** | ☐ | Identify disconnected road segments | Data Analyst |
| **Duplicates** | ☐ | Check for duplicate road segments or nodes | Data Analyst |
| **Data Types** | ☐ | Validate GeoJSON structure, coordinate systems (WGS84) | Data Analyst |
| **Network Connectivity** | ☐ | Verify road network connectivity, identify isolated segments | Data Scientist |

#### Weather and Environmental Data

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Missing Values** | ☐ | Handle sensor failures. Max 7-day gap for interpolation | Data Analyst |
| **Outliers** | ☐ | Validate temperature, precipitation ranges for Bangkok climate | Data Analyst |
| **Duplicates** | ☐ | Check by timestamp | Data Analyst |
| **Data Types** | ☐ | Numeric validation for all weather metrics | Data Analyst |
| **Temporal Alignment** | ☐ | Align with traffic data timestamps (daily granularity) | Data Analyst |

#### Public Transit Data (Pending Full Dataset)

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Missing Values** | ☐ | Pending data acquisition from BMA/BTS/MRT | Data Analyst |
| **Data Structure Validation** | ☐ | Validate against reference datasets (Chicago, Helsinki) | Data Analyst |
| **Temporal Coverage** | ☐ | Ensure alignment with traffic data period (2019-2025) | Data Analyst |

### 1.2 Data Transformation

#### Feature Engineering for Traffic Data

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Normalization** ระบุว่ามีตัวแปรใดบ้างที่ถูกปรับสเกลหรือทำให้เป็นปกติและเหตุผลที่ทำ | ☐ | StandardScaler for: congestion_index, traffic_volume, temperature. Document min/max values | Data Scientist |
| **การเข้ารหัส (Encoding)** ตรวจสอบตัวแปรเชิงหมวดหมู่ใดบ้างที่ถูกเข้ารหัสเพื่อใช้ในการวิเคราะห์ | ☐ | One-Hot Encoding: road_type, weather_condition, district. Label Encoding: day_of_week | Data Scientist |
| **Temporal Features Creation** | ☐ | Extract: hour, day_of_week, month, season, is_weekend, is_holiday | Data Scientist |
| **Spatial Features Creation** | ☐ | Create: district clusters, proximity_to_intersection, area_type | Data Scientist |
| **Lagged Features** | ☐ | Create: congestion_lag_1h, congestion_lag_24h, rolling_avg_7day | Data Scientist |

---

## 2. การวิเคราะห์ข้อมูลเบื้องต้น (Exploratory Data Analysis - EDA)

### 2.1 สถิติเชิงพรรณนา (Descriptive Statistics)

#### Bangkok Traffic Congestion Analysis

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| สรุปสถิติหลักสำหรับตัวแปรที่สำคัญ (ค่าเฉลี่ย มัธยฐาน โหมด ช่วง เป็นต้น) | ☐ | Calculate for: congestion_index, traffic_volume, accident_count. Generate summary table | Data Analyst |
| ระบุลักษณะหลักของข้อมูล (เช่น แนวโน้มกลาง การกระจายตัวของข้อมูล) | ☐ | Analyze distribution: normal, skewed? Calculate std, variance, IQR | Data Analyst |
| **Temporal Statistics** | ☐ | Mean congestion by: hour, day_of_week, month, season | Data Analyst |
| **Spatial Statistics** | ☐ | Mean congestion by: district, road_type, intersection | Data Analyst |
| **Correlation Analysis** | ☐ | Calculate Pearson correlation: traffic vs weather, accidents vs congestion | Data Scientist |

#### Accident Pattern Analysis

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Accident Frequency Statistics** | ☐ | Count by severity, road_type, weather_condition, time_of_day | Data Analyst |
| **Geographic Distribution** | ☐ | Identify high-frequency accident zones | Data Analyst |
| **Temporal Patterns** | ☐ | Accidents by hour, day, season | Data Analyst |

#### Weather Impact Analysis

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Weather Condition Distribution** | ☐ | Frequency of: clear, rain, fog, extreme weather | Data Analyst |
| **Temperature Statistics** | ☐ | Mean, range, distribution for Bangkok | Data Analyst |
| **Precipitation Analysis** | ☐ | Frequency and intensity distribution | Data Analyst |

### 2.2 ข้อมูลเชิงลึกและรูปแบบเบื้องต้น (Initial Insights and Patterns)

#### Traffic Pattern Discovery

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| ค้นหารูปแบบ แนวโน้ม หรือความสัมพันธ์ที่พบในข้อมูล | ☐ | Expected: Peak at 17:00-18:00, weekend 30-40% lower, seasonal variations | Data Scientist |
| ระบุข้อมูลที่สำคัญหรือข้อสังเกตที่น่าสนใจจากการวิเคราะห์เบื้องต้น | ☐ | Document unexpected patterns, anomalies, special event impacts | Data Scientist |
| **Rush Hour Analysis** | ☐ | Identify precise peak hours, duration, intensity by day of week | Data Scientist |
| **Weekend vs Weekday Patterns** | ☐ | Compare congestion levels, validate 30-40% reduction hypothesis | Data Scientist |
| **Holiday Impact** | ☐ | Analyze Songkran, Chinese New Year, national holidays impact | Data Scientist |
| **Seasonal Trends** | ☐ | Identify rainy season vs dry season patterns | Data Scientist |

#### Spatial Hotspot Identification

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Primary Hotspot Mapping** | ☐ | Expected: Vibhavadi Rangsit Road, Sukhumvit area. Use Kernel Density Estimation | Data Scientist |
| **Secondary Hotspot Identification** | ☐ | Identify 15-20 secondary congestion zones | Data Scientist |
| **Intersection Analysis** | ☐ | Rank intersections by congestion severity | Data Scientist |
| **Road Type Analysis** | ☐ | Compare: arterial, expressway, secondary, local roads | Data Scientist |

#### Accident-Congestion Relationship

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Correlation Analysis** | ☐ | Quantify accident-congestion correlation (expect 40-60% increase) | Data Scientist |
| **Weather-Accident Correlation** | ☐ | Analyze rain impact (expect 25% increase in accidents) | Data Scientist |
| **Cascade Effect Analysis** | ☐ | Study how accidents propagate congestion to adjacent areas | Data Scientist |
| **High-Risk Zone Identification** | ☐ | Identify zones with both high accidents and high congestion | Data Scientist |

### 2.3 การแสดงข้อมูลด้วยกราฟ (Data Visualization)

#### Must-Create Visualizations

| Visualization | Status | Description | Owner |
|---------------|--------|-------------|-------|
| จัดเตรียมการแสดงข้อมูลที่เกี่ยวข้อง (เช่น histograms, scatter plots, box plots) เพื่อสนับสนุนผลการค้นพบ | ☐ | Create comprehensive visualization suite | Visualization Lead |
| กราฟแต่ละอันควรมีการระบุชื่อและอธิบายอย่างชัดเจนเพื่อความเข้าใจ | ☐ | All plots must have: title, axis labels, legend, data source | Visualization Lead |

**Required Plots:**

| # | Plot Type | Purpose | Status | Owner |
|---|-----------|---------|--------|-------|
| 1 | **Histogram** - Congestion Distribution | Show distribution of congestion index values | ☐ | Visualization Lead |
| 2 | **Heatmap** - Hour x Day of Week | Temporal pattern visualization | ☐ | Visualization Lead |
| 3 | **Geographic Map** - Hotspot Map | Spatial congestion visualization (Bangkok map) | ☐ | Visualization Lead |
| 4 | **Time Series** - Historical Trend | Congestion 2019-2025 trend line | ☐ | Visualization Lead |
| 5 | **Box Plot** - Congestion by Road Type | Compare distributions across road types | ☐ | Visualization Lead |
| 6 | **Scatter Plot** - Accidents vs Congestion | Show correlation relationship | ☐ | Visualization Lead |
| 7 | **Bar Chart** - Congestion by Season | Seasonal comparison | ☐ | Visualization Lead |
| 8 | **Line Plot** - Weekday vs Weekend | Compare average patterns | ☐ | Visualization Lead |
| 9 | **Correlation Matrix** - All Variables | Heatmap of feature correlations | ☐ | Visualization Lead |
| 10 | **Violin Plot** - Weather Impact | Distribution by weather conditions | ☐ | Visualization Lead |

**Visualization Standards:**
- Resolution: 300 DPI minimum
- Format: PNG for reports, PDF for print
- Size: 12x8 inches (1200x800 pixels at 100 DPI)
- Color scheme: Professional, colorblind-friendly
- Font size: Minimum 12pt for labels
- Save location: `06_Results/Figures/`
- Naming: `{number}_{phase}_{description}_{date}.png`

---

## 3. สรุปผลจากการวิเคราะห์ข้อมูลเบื้องต้น (EDA Summary)

### Key Insights Documentation

| Task | Status | Notes | Owner |
|------|--------|-------|-------|
| **Temporal Insights Summary** | ☐ | Document peak hours, day patterns, seasonal trends | Data Scientist |
| **Spatial Insights Summary** | ☐ | Document hotspots, road type impacts, district analysis | Data Scientist |
| **Correlation Insights Summary** | ☐ | Document accident-congestion, weather impacts | Data Scientist |
| **Data Quality Summary** | ☐ | Final completeness, accuracy, validity report | Data Analyst |
| **EDA Report Writing** | ☐ | Create comprehensive EDA report in `06_Results/Reports/` | Visualization Lead |
| **Findings Presentation** | ☐ | Prepare slides for Week 3 team review | Visualization Lead |

### Expected Key Findings (Validation Targets)

| Finding | Expected Result | Actual Result | Status |
|---------|----------------|---------------|--------|
| Peak congestion time | 17:00-18:00 | TBD | ☐ |
| Weekend reduction | 30-40% lower | TBD | ☐ |
| Primary hotspot | Vibhavadi Rangsit, Sukhumvit | TBD | ☐ |
| Accident impact | 40-60% congestion increase | TBD | ☐ |
| Rain impact on accidents | 25% increase | TBD | ☐ |
| Data completeness | >90% | TBD | ☐ |

---

## 4. Deliverables Checklist

### Week 2 Required Deliverables

| Deliverable | Format | Location | Status | Due Date |
|-------------|--------|----------|--------|----------|
| **Cleaned Dataset - Traffic** | CSV | `02_Data/Processed/` | ☐ | End of Week 2 |
| **Cleaned Dataset - Accidents** | CSV | `02_Data/Processed/` | ☐ | End of Week 2 |
| **Cleaned Dataset - Weather** | CSV | `02_Data/Processed/` | ☐ | End of Week 2 |
| **Cleaned Dataset - Road Network** | GeoJSON | `02_Data/Processed/` | ☐ | End of Week 2 |
| **Data Quality Report** | Markdown | `06_Results/Reports/` | ☐ | End of Week 2 |
| **EDA Notebook** | Jupyter | `03_Notebooks/03_EDA.ipynb` | ☐ | End of Week 2 |
| **EDA Visualizations (10+)** | PNG | `06_Results/Figures/` | ☐ | End of Week 2 |
| **Descriptive Statistics Summary** | Markdown | `06_Results/Reports/` | ☐ | End of Week 2 |
| **Initial Findings Report** | Markdown | `06_Results/Reports/` | ☐ | End of Week 2 |
| **Feature Engineering Plan** | Markdown | `07_Documentation/` | ☐ | End of Week 2 |

---

## 5. Timeline and Milestones

### Week 2 Daily Tasks

#### Day 1-2: Data Collection & Initial Cleaning
- [ ] Download all identified datasets
- [ ] Verify data completeness
- [ ] Initial data loading and exploration
- [ ] Document data sources and metadata

#### Day 3-4: Data Cleaning
- [ ] Handle missing values (all datasets)
- [ ] Remove duplicates
- [ ] Detect and handle outliers
- [ ] Validate data types and formats
- [ ] Save cleaned datasets

#### Day 5-6: Initial EDA
- [ ] Calculate descriptive statistics
- [ ] Create initial visualizations
- [ ] Identify patterns and trends
- [ ] Document preliminary findings

#### Day 7: Documentation & Review
- [ ] Complete EDA report
- [ ] Organize all visualizations
- [ ] Team review meeting
- [ ] Prepare for Week 3 (Feature Engineering)

---

## 6. Quality Gates

### Data Quality Gate (Must Pass to Proceed)

| Criteria | Target | Actual | Pass/Fail |
|----------|--------|--------|-----------|
| Data completeness | ≥90% | TBD | ☐ |
| Missing values handled | 100% documented | TBD | ☐ |
| Outliers identified | 100% documented | TBD | ☐ |
| Duplicates removed | 100% | TBD | ☐ |
| Data types validated | 100% | TBD | ☐ |

### EDA Quality Gate (Must Pass to Proceed)

| Criteria | Target | Actual | Pass/Fail |
|----------|--------|--------|-----------|
| Descriptive statistics calculated | All key variables | TBD | ☐ |
| Visualizations created | Minimum 10 plots | TBD | ☐ |
| Key patterns identified | Minimum 5 patterns | TBD | ☐ |
| EDA report written | Complete & clear | TBD | ☐ |
| Team review completed | Approved by PM & TL | TBD | ☐ |

---

## 7. Team Assignments

### Primary Responsibilities

| Phase | Primary Owner | Support | Reviewer |
|-------|--------------|---------|----------|
| Data Collection | Data Analyst | Technical Lead | Project Manager |
| Data Cleaning | Data Analyst | Data Scientist | Technical Lead |
| Statistical Analysis | Data Scientist | Data Analyst | Technical Lead |
| Visualization | Visualization Lead | Data Scientist | Project Manager |
| Documentation | Visualization Lead | All Team | Project Manager |

---

## 8. Risks and Mitigation

### Week 2 Identified Risks

| Risk | Probability | Impact | Mitigation Strategy | Status |
|------|------------|--------|---------------------|--------|
| Missing transit data | High | Medium | Use reference datasets, focus on traffic/accident data | ☐ |
| Data quality issues | Medium | High | Comprehensive cleaning pipeline, validation checks | ☐ |
| Time constraint | Medium | Medium | Prioritize key datasets, parallel processing | ☐ |
| Tool/technical issues | Low | Medium | Early environment setup, backup tools | ☐ |

---

## 9. Next Steps (Week 3 Preview)

### Preparation for Feature Engineering Phase

- [ ] Review EDA findings
- [ ] Identify features for modeling
- [ ] Plan feature engineering pipeline
- [ ] Prepare train/validation/test split strategy
- [ ] Design feature importance analysis

---

## 10. Sign-off

### Week 2 Completion Checklist

- [ ] All data cleaning tasks completed
- [ ] All EDA tasks completed
- [ ] All visualizations created and saved
- [ ] All reports written and reviewed
- [ ] Quality gates passed
- [ ] Team review meeting held
- [ ] Deliverables submitted
- [ ] Week 3 planning completed

### Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Data Analyst | วีร์กวิน นาคนิธิชัยรัชต์ | | |
| Data Scientist | คามิน สุรขจร | | |
| Technical Lead | กฤตภาส อิ่มทั่ว | | |
| Project Manager | นิติภูมิ โพธิชัย | | |

---

**Document Version:** 1.0

**Last Updated:** November 16, 2025

**Next Review:** End of Week 2

---

**Notes:**
- This checklist is a living document. Update status regularly.
- Mark completed items with ✓ or ✅
- Document any deviations or issues in the Notes column
- Escalate blockers to Project Manager immediately
- All file paths are relative to project root: `/Volumes/T9/Documents/CPE/Y3-TR1/CPE312/Capstone Project/Worked/`
