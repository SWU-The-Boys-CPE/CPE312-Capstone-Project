# CPE312 Capstone Project: Traffic and Transportation Patterns Analysis

## Group Information

**Project Title:** Urban Traffic Flow Optimization and Public Transit Efficiency Analysis in Bangkok Metropolitan Area

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

**Core Problem:** How can we leverage big data analytics and machine learning models to optimize urban traffic flow and public transit efficiency in Bangkok by identifying congestion hotspots, predicting traffic patterns, and recommending intelligent traffic management strategies and route optimization for both private and public transportation?

**Secondary Problem:** What relationships exist between road infrastructure, traffic volume, accident patterns, and traffic congestion? How can this insight inform sustainable urban transportation planning?

### 1.2 Alignment with Sustainable Development Goals (SDGs)

This capstone project directly supports the following SDGs:

**SDG 11: Sustainable Cities and Communities**
- Target 11.2: Provide safe, affordable, sustainable transport systems that enhance road safety and expand public transport
- Indicator: Proportion of population with convenient access to public transport (measured through ridership and route efficiency analysis)
- Target 11.6: Reduce adverse environmental impact of cities, including air pollution from vehicles

**SDG 9: Industry, Innovation and Infrastructure**
- Target 9.1: Develop quality, reliable, sustainable, and resilient infrastructure to support economic development
- Indicator: Data-driven smart traffic management systems that utilize AI and computer vision

**SDG 13: Climate Action**
- Target 13.2: Integrate climate change mitigation strategies into transportation policies
- Indicator: Reduction in vehicular emissions through optimized traffic flow and increased public transit usage

**Project Relevance:** By optimizing traffic patterns, this project reduces fuel consumption, emissions, and congestion time—directly contributing to sustainable urban environments, improved public health, and economic efficiency in Bangkok.

---

## 2. Research Questions and Objectives

### 2.1 Primary Research Question

**What data-driven insights can be derived from traffic flow, accident patterns, and public transit data to develop actionable recommendations for reducing congestion and improving transportation efficiency in Bangkok?**

### 2.2 Secondary Research Questions

1. **Traffic Pattern Analysis:** What are the temporal and spatial patterns of traffic congestion in Bangkok? Which roads, intersections, and time periods experience the highest congestion levels, and what are the underlying causes?

2. **Accident-Congestion Relationship:** What correlations exist between accident frequency, weather conditions, road type, and traffic congestion severity? Can we identify high-risk accident zones that also contribute to congestion?

3. **Public Transit Optimization:** How efficiently are current public transit routes operating? What optimization strategies (route adjustment, frequency changes, first-mile/last-mile connectivity) could increase ridership and reduce private vehicle dependency?

4. **Predictive Modeling:** Can machine learning models accurately predict traffic congestion levels 15-60 minutes in advance? What features (time of day, day of week, weather, events) are most predictive?

5. **Infrastructure Impact:** How do road infrastructure characteristics (road type, lane configuration, signal timing, intersection design) affect traffic flow and congestion patterns? What infrastructure improvements would have the greatest impact?

### 2.3 Project Objectives

**Primary Objectives:**

1. **Data Integration:** Collect, clean, and integrate multi-source traffic data (traffic flow, accidents, weather, public transit, road networks) into a unified analytical database.

2. **Pattern Discovery:** Identify significant spatial and temporal traffic patterns, congestion hotspots, recurring accident locations, and peak demand periods using exploratory data analysis and statistical methods.

3. **Predictive Modeling:** Develop machine learning models (time-series forecasting, classification, clustering) to predict traffic congestion levels and identify accident-prone conditions with high accuracy.

4. **Route Optimization:** Provide data-driven recommendations for optimizing public transit routes and suggesting alternative routing strategies to distribute traffic loads more efficiently.

5. **Decision Support System:** Create an interactive dashboard or analytical tool that provides real-time insights and enables traffic authorities and urban planners to make informed decisions.

6. **Policy Recommendations:** Generate actionable recommendations aligned with SDG 11, 9, and 13 for sustainable urban transportation improvements.

---

## 3. Data Exploration and Selection

### 3.1 Data Sources Identified

| Dataset Name | Source | Description | Data Type | Coverage |
|---|---|---|---|---|
| **Traffic Congestion Index - Bangkok** | CEIC Data / TrafficIndex.org | Daily traffic congestion measurements (2019-2025) updated daily; provides congestion index by time of day | Time-series, Numerical | Bangkok Metropolitan Area (2017-2025) |
| **US Accidents Dataset** | Kaggle (Sobhan Moosavi) | 2.8+ million accident records (2016-2021); includes location, severity, weather, road conditions, accident type | Structured CSV, Geospatial | 49 US states; transferable methodology for Bangkok |
| **Road Network Data (OpenStreetMap)** | OpenStreetMap (OSM) | Complete road network topology, road classifications, intersections, connectivity for any urban area; crowd-sourced, regularly updated | GeoJSON, Shapefile | Global coverage (including Bangkok) |
| **Public Transit Passenger Data** | Kaggle / Transit Authorities | Station entries, ridership counts by route and time period, passenger flow levels, schedule information | CSV, Time-series | Multiple cities (Chicago, Helsinki, Macau) |
| **Vehicle Detection & Tracking Data** | Computer Vision datasets (Kaggle, ArXiv) | Real-time vehicle detection results, YOLOv8 models, pedestrian tracking, traffic flow video analysis | Video, Coordinates, Classifications | Traffic camera footage samples |
| **Bangkok Traffic Data** | Bangkok Metropolitan Administration (BMA), OTP | 127 identified congestion points, traffic flow speeds, area traffic control (ATC) system data, BRT and feeder bus information | Structured, Geospatial | Bangkok specific (2023-2025) |
| **Weather and Environmental Data** | NASA, NOAA, Weather API | Temperature, precipitation, visibility, wind conditions; impacts on traffic behavior | Numerical, Time-series | Global coverage including Thailand |
| **Google Maps & TomTom API Data** | Google Maps, TomTom | Real-time travel times, traffic flow speed, route alternative analysis (requires API keys and subscription) | JSON, Real-time | Global coverage including Thailand |
| **Urban Traffic Flow Dataset** | Kaggle (Recent 2024) | Preprocessed urban traffic data with temporal, spatial, and categorical features designed for traffic prediction | CSV, Structured | Multi-city dataset |
| **Public Transport Dataset (Finland)** | Kaggle / TrafficSense Project | Mobile positioning data, activity recognition, public transit trips, train schedules, real-time position samples | CSV, GPS traces | Helsinki/Finland sample |

### 3.2 Primary Datasets Selected for Analysis

**Selected Dataset 1: US Accidents Dataset (Kaggle)**
- **Justification:** Although US-based, this is the largest and most comprehensive publicly available accident dataset (2.8M+ records). It contains detailed attributes (location, weather, severity, road type, time) transferable to Bangkok analysis through similar feature engineering. The methodology and feature engineering approaches are directly applicable to Thai road accident analysis.
- **Usage:** Provides templates for accident pattern analysis, correlation with traffic congestion, and hotspot identification

**Selected Dataset 2: Bangkok Traffic Congestion Index (CEIC/TrafficIndex)**
- **Justification:** Provides authentic Bangkok-specific time-series data with daily granularity from 2019-2025. Essential for understanding real congestion patterns in the project's geographic focus area. Available historical data enables trend analysis and pattern recognition.
- **Usage:** Primary dataset for temporal pattern analysis, baseline metrics, and validating predictive models

**Selected Dataset 3: OpenStreetMap Road Network (Bangkok)**
- **Justification:** Provides complete, free, and up-to-date road network topology for Bangkok. Includes road classifications, intersections, connectivity—essential for spatial analysis. Crowd-sourced data regularly updated by community.
- **Usage:** Foundation for spatial analysis, route optimization algorithms, and infrastructure impact assessment

**Selected Dataset 4: Public Transit Ridership Data**
- **Justification:** Similar structure to datasets available from Bangkok Mass Transit System (BTS), Metropolitan Rapid Transit (MRT), and Bangkok Omnibus Public Company Limited (BMTA). Reference datasets from other cities provide methodology templates.
- **Usage:** Analyze public transit efficiency, identify underutilized routes, support route optimization recommendations

**Selected Dataset 5: Computer Vision Traffic Data (YOLOv8 Models)**
- **Justification:** Demonstrates modern vehicle detection technology applicable to Bangkok's traffic camera infrastructure. Real-time detection capabilities support ATC system analysis recommended by BMA.
- **Usage:** Proof-of-concept for integrating computer vision with traffic management systems

### 3.3 Data Quality Assessment

| Quality Dimension | Assessment | Pass/Fail | Explanation & Mitigation Strategy |
|---|---|---|---|
| **Completeness** | PASS | ✓ | Bangkok Congestion Index: 1,682 observations (2019-2023); US Accidents: 2.8M+ records with minimal gaps. OpenStreetMap: 99%+ road coverage. **Mitigation:** For missing transit data, interpolation methods will be applied; traffic sensors provide redundant coverage |
| **Relevance** | PASS | ✓ | All datasets directly address research questions: traffic patterns, accidents, transit efficiency, infrastructure impact. Bangkok-specific data ensures local applicability; US accident patterns transfer via similar features. **Mitigation:** Data fusion ensures multi-perspective analysis |
| **Granularity/Resolution** | PASS | ✓ | Bangkok data: Daily measurements (sufficient for trend analysis). Accident data: Individual incident level (enables spatial clustering). Traffic flow: Real-time capable via APIs. Road network: Segment-level detail. **Mitigation:** Temporal aggregation strategies defined for different analyses (hourly, daily, weekly) |
| **Timeliness/Currency** | PASS | ✓ | Bangkok Congestion Index updated daily through Nov 2025 (current as of project kickoff). US Accidents 2016-2021 (5-year historical dataset adequate for pattern validation). OpenStreetMap regularly updated by community. **Mitigation:** Real-time APIs will be incorporated for live prediction validation; historical data sufficient for model training |
| **Data Consistency** | PASS | ✓ | Bangkok Index: Consistent methodology (TCI metric); US Accidents: Standardized schema across 49 states. OSM: Validated by community governance. **Mitigation:** Data validation pipeline will check for outliers (±3σ rule); format standardization applied during ETL |
| **Accuracy & Validity** | PASS | ✓ | Bangkok data: Validated by government agencies (CEIC, OTP). US Accidents: Peer-reviewed in academic publications. OSM: Community-validated geographic accuracy. **Mitigation:** Cross-validation with multiple sources (Google Maps, TomTom); anomaly detection algorithms for statistical outliers |

**Overall Assessment:** ✅ All datasets meet quality thresholds for capstone-level analysis. Data is sufficient for answering research questions, developing predictive models, and generating recommendations.

---

## 4. Expected Impact and Relevance

### 4.1 Expected Insights

This capstone project expects to generate the following key insights:

1. **Temporal Congestion Patterns:** Identification of precise rush-hour windows, day-of-week variations, seasonal trends, and special event impacts on traffic. Expected to reveal that 17:00-18:00 is peak congestion; Saturday/Sunday show 30-40% lower congestion; special events (Songkran, Chinese New Year) cause 50%+ congestion increases.

2. **Spatial Hotspot Mapping:** GIS-based identification of the most congested roads, intersections, and zones in Bangkok. Expected to confirm Vibhavadi Rangsit Road (150,000+ vehicles/day) and Sukhumvit areas as primary congestion zones; identification of 15-20 secondary hotspots for targeted intervention.

3. **Accident-Congestion Correlations:** Discovery of relationships between accident frequency/severity and congestion levels. Expected to reveal that accidents increase congestion by 40-60% in affected zones; weather conditions (rain) correlate with 25% increase in accident rates and subsequent congestion cascades.

4. **Public Transit Efficiency Gaps:** Identification of underutilized transit routes, capacity mismatches, and opportunities for ridership growth through optimization. Expected to show 20-30% of bus seats are empty during off-peak; BTS/MRT capture only 20-25% of total trips despite higher efficiency.

5. **Predictive Capability:** Validated machine learning models capable of predicting congestion 15-60 minutes in advance with 75-85% accuracy. Expected models: LSTM for time-series, XGBoost for classification, k-means for route clustering.

6. **Infrastructure Recommendations:** Data-driven identification of infrastructure improvements (signal timing optimization, lane reallocation, corridor priority) that would reduce congestion by 15-25% based on simulated scenarios.

### 4.2 Real-World Impact and Contribution to SDGs

**Impact on SDG 11 (Sustainable Cities and Communities):**

- **Immediate Impact:** Recommendations for Bangkok authorities can reduce daily congestion-related emissions by an estimated 5-8% (saving 5-8 million baht in fuel daily). Improved traffic flow enhances air quality in high-congestion zones by reducing particulate matter and NOx emissions.
- **Medium-term Impact:** Enhanced public transit data enables service improvements increasing ridership by 10-15%; BMA implementation of proposed route optimizations reduces average commute time by 10-15 minutes during peak hours.
- **Long-term Impact:** Decision-support dashboard enables data-driven urban planning; sustainable transportation policies achieve SDG 11 targets for increased transit access and reduced transport-related emissions.

**Impact on SDG 9 (Industry, Innovation and Infrastructure):**

- **Technological Innovation:** Demonstrates application of AI/ML, computer vision, and big data analytics to urban infrastructure challenges—creating replicable model for other Thai cities (Chiang Mai, Phuket, Pattaya).
- **Infrastructure Optimization:** Provides evidence-based approach to prioritizing infrastructure investments (signal upgrades, corridor improvements) based on data rather than intuition, improving ROI on public spending.
- **Capacity Building:** Project deliverables (methodology, code, models) create knowledge transfer to BMA and transportation authorities for ongoing optimization.

**Impact on SDG 13 (Climate Action):**

- **Emission Reduction:** Optimized traffic flow alone reduces vehicular emissions by 5-8% (each 10% reduction in congestion = 5-7% emission reduction). Public transit promotion reduces CO2 equivalent by 15-20kg per diverted car trip.
- **Climate Resilience:** Analysis of weather-traffic correlations informs climate adaptation strategies for Bangkok's increasingly severe flood and weather events.

**Stakeholder Benefits:**

- **Bangkok Metropolitan Administration:** Data-driven decision support, prioritized investment roadmap, validated KPIs for measuring policy effectiveness
- **General Public:** Reduced commute times, improved air quality, more affordable/accessible transit options, enhanced road safety
- **Transportation Operators (BTS, MRT, BMTA):** Route optimization data, demand forecasting, resource allocation guidance
- **Urban Planners & Policy Makers:** Evidence-based recommendations for sustainable urban development aligned with Thailand's 20-Year National Strategy
- **Academic Community:** Replicable methodology for urban traffic analysis, demonstration of data science application to SDGs, foundation for future research

---

## 5. Preliminary Analysis Plan

### 5.1 Data Processing Pipeline

1. **Data Acquisition & Integration**
   - Download/API calls to traffic, accident, weather, transit data sources
   - Standardize formats (convert shapefiles, APIs, CSVs to unified schema)
   - Temporal alignment (ensure all timestamps on consistent timezone/frequency)

2. **Data Cleaning & Validation**
   - Remove duplicates, invalid records (±3σ outlier detection)
   - Handle missing values (interpolation for time-series, mode for categorical)
   - Geocoding and spatial validation for location-based records

3. **Feature Engineering**
   - Temporal features: hour, day-of-week, season, holidays, events
   - Spatial features: zone clustering, proximity to major intersections, road type
   - Domain features: weather impact, accident severity clustering, transit frequency

### 5.2 Analytical Methods

- **Exploratory Data Analysis:** Time-series plots, heatmaps (congestion by hour/day), spatial clustering
- **Statistical Analysis:** Correlation analysis (accidents vs. congestion), ANOVA (comparing zones/times)
- **Predictive Modeling:** LSTM networks (time-series), XGBoost (classification), ARIMA (baseline)
- **Optimization:** Genetic algorithms for route optimization, simulation models for infrastructure scenarios
- **Geospatial Analysis:** Hotspot mapping (Kernel Density Estimation), network analysis (centrality measures)

---

## 6. Timeline and Deliverables

### 6.1 Project Phases

| Phase | Duration | Key Activities | Deliverables |
|---|---|---|---|
| Data Collection & Integration | Week 1-2 | Download datasets, API setup, initial cleaning | Integrated database, data dictionary |
| Exploratory Analysis | Week 3-4 | Statistical analysis, visualization, pattern discovery | EDA report, preliminary findings |
| Model Development | Week 5-7 | Feature engineering, model training/tuning, validation | Trained models, performance metrics |
| Route Optimization | Week 7-8 | Algorithm implementation, scenario analysis | Optimization results, recommended routes |
| Dashboard & Recommendations | Week 9-10 | Tool development, visualization, policy recommendations | Interactive dashboard, final recommendations |
| Documentation & Presentation | Week 11-12 | Report writing, presentation preparation | Final report, presentation slides |

### 6.2 Expected Deliverables

1. **Technical Deliverables:** Integrated database, machine learning models (Jupyter notebooks), optimization algorithms, interactive dashboard/web application
2. **Analytical Deliverables:** EDA report, predictive model documentation, validation results, optimization recommendations
3. **Strategic Deliverables:** Final capstone report, policy recommendations briefing, presentation slides, methodology documentation for replication

---

## 7. Team Responsibilities and Skills

- **Project Lead (Data Engineering):** Database architecture, ETL pipeline development, data quality management
- **Data Analysis & Visualization:** Statistical analysis, visualization design, dashboard development
- **ML Specialist:** Model selection/training, hyperparameter tuning, prediction validation
- **Transit Systems Specialist:** Domain knowledge, stakeholder engagement, impact assessment
- **Software Developer:** Backend systems, API integration, application deployment

**Technical Skills Required:** Python (Pandas, Scikit-learn, TensorFlow), SQL, GIS tools, Tableau/Power BI, Git version control
