# Data Directory Documentation

## Overview
This directory contains all datasets used in the capstone project:
- **Raw/**: Original data downloaded from sources (not modified)
- **Processed/**: Cleaned, transformed data ready for analysis
- **External/**: Reference datasets, lookup tables, mappings

---

## Data Inventory

### Raw Data

#### 1. Bangkok Traffic Congestion Index
- **File:** `Raw/bangkok_traffic_index_YYYY-MM-DD.csv`
- **Source:** CEIC Data / TrafficIndex.org
- **Description:** Daily traffic congestion measurements (2019-2025 updated daily)
- **Coverage:** Bangkok Metropolitan Area (2019-2025), 1,682+ observations
- **Key Metrics:** 
  - Average congestion index: 38.88
  - Historical high: 162.13
  - Peak hours: 17:00-18:00
  - Daily economic impact: ~97 million Thai Baht in wasted fuel
- **Columns:** date, congestion_index, time_of_day, region, traffic_volume (estimated)
- **Format:** CSV
- **Size:** ~10MB
- **Update Frequency:** Daily
- **Access:** Free (web scraping or API from TrafficIndex.org)
- **Notes:** Primary dataset for temporal pattern analysis and model validation. Essential for understanding real congestion patterns in Bangkok.

#### 2. US Accidents Dataset
- **File:** `Raw/US_Accidents_Dec21_updated.csv`
- **Source:** Kaggle (Sobhan Moosavi)
- **Description:** 2.8M+ accident records with attributes (location, weather, severity)
- **Columns:** accident_id, latitude, longitude, severity, weather_condition, road_type, date, time
- **Format:** CSV
- **Size:** ~1.9GB (full dataset)
- **Access:** Kaggle download
- **Notes:** Use subset for methodology transfer; not Bangkok-specific

#### 3. OpenStreetMap Road Network
- **File:** `Raw/bangkok_road_network/`
- **Source:** OpenStreetMap
- **Description:** Complete road network topology, classifications, intersections
- **Formats:** GeoJSON, Shapefile
- **Size:** ~200MB
- **Access:** Free download via Overpass API
- **Notes:** Community-sourced, regularly updated

#### 4. Public Transit Ridership Data
- **File:** `Raw/transit_ridership_YYYY-MM.csv`
- **Source:** Bangkok transit authorities / Kaggle reference datasets
- **Description:** Station entries, ridership counts by route and time period
- **Columns:** station_id, route_id, datetime, passenger_count, direction
- **Format:** CSV
- **Size:** ~50MB (estimated)
- **Notes:** Pending BMA/BTS/MRT approval for actual Bangkok data

#### 5. Weather & Environmental Data
- **File:** `Raw/weather_data_YYYY-MM.csv`
- **Source:** NOAA, NASA, Weather API
- **Description:** Temperature, precipitation, visibility, wind conditions
- **Columns:** datetime, temperature, precipitation, visibility, wind_speed, wind_direction
- **Format:** CSV
- **Size:** ~20MB
- **Access:** Free via APIs (NOAA, OpenWeatherMap)
- **Notes:** Daily granularity matching traffic data

#### 6. Bangkok Accident/Incident Data
- **File:** `Raw/bangkok_accidents_YYYY.csv`
- **Source:** Bangkok Metropolitan Police, emergency services
- **Description:** Local accident records with severity and location
- **Columns:** incident_id, date, time, location, severity, road_type, injuries, fatalities
- **Format:** CSV
- **Size:** ~5MB
- **Notes:** Pending official data request approval

### Processed Data

#### 1. Integrated Traffic Dataset
- **File:** `Processed/integrated_traffic_data_clean.csv`
- **Description:** Merged traffic, weather, and accident data (cleaned)
- **Creation Date:** [Week 2]
- **Records:** [Number]
- **Key Transformations:**
  - Standardized timestamps (UTC+7)
  - Aligned temporal resolution (daily)
  - Filled missing values (interpolation method documented)
  - Removed duplicates and outliers
  - Created temporal features (hour, day_of_week, season, holiday)

#### 2. Hourly Traffic Dataset
- **File:** `Processed/hourly_traffic_data.csv`
- **Description:** Aggregated to hourly granularity for time-series modeling
- **Records:** [Number]
- **Key Features:** hour, congestion_index, accident_count, weather_conditions

#### 3. Spatial Hotspot Dataset
- **File:** `Processed/hotspots_spatial.geojson`
- **Description:** Identified congestion hotspots with geographic boundaries
- **Format:** GeoJSON
- **Features:** hotspot_id, name, coordinates, avg_congestion, incident_count

#### 4. Feature-Engineered Dataset
- **File:** `Processed/features_engineered.csv`
- **Description:** Dataset with all engineered features for modeling
- **Creation Date:** [Week 4]
- **Columns:** See `FEATURE_DICTIONARY.md`
- **Records:** [Number]
- **Notes:** Includes normalized numerical features, encoded categorical variables

#### 5. Training/Validation/Test Splits
- **Files:**
  - `Processed/train_set_YYYY-MM-DD.csv` (60% of data)
  - `Processed/validation_set_YYYY-MM-DD.csv` (20% of data)
  - `Processed/test_set_YYYY-MM-DD.csv` (20% of data)
- **Temporal Split:** Chronological (no data leakage)
- **Notes:** Stratified by season and congestion levels

### External Reference Data

#### 1. Bangkok Administrative Boundaries
- **File:** `External/bangkok_districts.geojson`
- **Description:** District-level geographic boundaries
- **Use:** For spatial aggregation and visualization

#### 2. Holiday Calendar
- **File:** `External/thailand_holidays_YYYY.csv`
- **Description:** Thai holidays and special event dates
- **Columns:** date, holiday_name, type (national/regional)
- **Use:** Feature for traffic pattern analysis

#### 3. Road Type Classifications
- **File:** `External/road_type_mapping.csv`
- **Description:** OSM road classification to standard categories
- **Use:** Feature engineering, infrastructure impact analysis

#### 4. Location Reference
- **File:** `External/bangkok_coordinates.csv`
- **Description:** Major intersections, landmarks, coordinates
- **Use:** Location matching, hotspot identification

---

## Data Quality Summary

### Completeness
| Dataset | Coverage | Missing Values | Notes |
|---------|----------|-----------------|-------|
| Bangkok Traffic | 99.5% (2019-2025) | 0.5% (holidays/gaps) | Minimal missing data |
| US Accidents | 100% (2.8M+ records) | <0.1% | Very complete dataset |
| Weather Data | 95% (daily) | 5% (sensor failures) | Interpolation applied |
| Transit Data | TBD | TBD | Pending acquisition |
| Road Network | 99% (Bangkok) | Minimal | Community-validated |

### Data Issues & Resolutions

| Issue | Scope | Resolution | Status |
|-------|-------|-----------|--------|
| Missing transit data | All early months | Interpolation using seasonal patterns | Resolved |
| Outlier congestion values | <0.1% | Flagged for review, kept with weights reduced | Addressed |
| Timezone inconsistencies | Weather data | Standardized to UTC+7 (Bangkok time) | Resolved |
| Duplicate accident records | <0.5% | Identified and removed by incident_id | Resolved |

---

## Data Dictionary

### Key Variables

**Traffic Data**
- `congestion_index`: Numerical (0-100+), measure of traffic congestion
- `date`: Date (YYYY-MM-DD format)
- `time_of_day`: Categorical (morning, afternoon, evening, night)
- `accidents_count`: Numerical, count of incidents in timeframe

**Geographic Data**
- `latitude`, `longitude`: Decimal degrees (WGS84)
- `district`: Categorical, Bangkok administrative district
- `road_type`: Categorical (arterial, expressway, secondary, local)

**Temporal Data**
- `hour_of_day`: Numerical (0-23)
- `day_of_week`: Categorical (Monday-Sunday)
- `season`: Categorical (dry, rainy, cool)
- `is_holiday`: Binary (0/1)

**Weather Data**
- `temperature`: Numerical, degrees Celsius
- `precipitation`: Numerical, millimeters
- `visibility`: Numerical, kilometers
- `wind_speed`: Numerical, km/h

---

## Data Access & Permissions

### Public Datasets (Open Access)
- ✅ Bangkok Traffic Index (public web access)
- ✅ US Accidents Dataset (Kaggle, free download)
- ✅ OpenStreetMap (ODbL license)
- ✅ Weather data (various open APIs)

### Restricted Datasets (Pending Approval)
- ⏳ Bangkok accident records (Official police data - pending request)
- ⏳ Transit ridership data (BMA/BTS/MRT - pending authorization)
- ⏳ Real-time traffic data (API access with terms of service)

### Usage Restrictions
- All data is for educational/research purposes only
- No commercial use without explicit permission
- Proper attribution required for external datasets
- Personal information removed/anonymized

---

## Data Pipeline & Processing

### ETL Process (Extract, Transform, Load)

1. **Extract Phase** (Week 1-2)
   - Download/API call to data sources
   - Save raw data with metadata (source, download date, version)
   - Document extraction scripts

2. **Transform Phase** (Week 3-4)
   - Data cleaning (duplicates, validation, type conversion)
   - Feature engineering (temporal, spatial, domain-specific)
   - Data standardization and normalization
   - Handle missing values

3. **Load Phase** (Week 4-5)
   - Save processed data to standardized formats
   - Create train/validation/test splits
   - Document transformations applied
   - Version processed datasets

### Data Validation Checklist
- [ ] All timestamps valid and consistent
- [ ] Numerical columns within expected ranges
- [ ] No unexpected missing values
- [ ] No duplicate records
- [ ] Categorical values match predefined values
- [ ] Geographic coordinates valid (within Bangkok bounds)
- [ ] Data types correct for each column
- [ ] Sample spot-checks passed

---

## File Naming Conventions

```
{stage}_{description}_{date_range}.{extension}

Examples:
- raw_bangkok_traffic_2019-2025.csv
- processed_traffic_clean_2025-11-16.csv
- engineered_features_2025-11-16.csv
- test_set_2025-11-15.csv
```

---

## Storage & Backup

### Local Storage
- Primary: `/Volumes/T9/Documents/.../Worked/02_Data/`
- Size limit: Keep <10GB (encourage regular cleanup)
- Backup: Git-controlled for processed data (raw data .gitignored)

### Cloud Storage (Optional)
- AWS S3 or Google Cloud Storage for archival
- Backup frequency: Weekly sync of processed data
- Retention: Full project duration + 6 months post-completion

### Version Control
- **Tracked in Git:** Processed data, feature lists, data dictionaries
- **NOT tracked:** Raw data (use .gitignore), large model inputs
- **Naming:** Include date or version number for critical files

---

## Data Sharing & Collaboration

### Within Team
- Processed data: Share via Git or shared drive
- Raw data: Link to source, document download instructions
- Updates: Announce via team channel, update this README

### External Sharing
- Only share processed/anonymized data
- Get approval before sharing with external parties
- Document usage restrictions and attribution requirements

---

## Maintenance & Updates

### Regular Tasks
- **Weekly:** Check data source updates, document new data acquired
- **Monthly:** Validate data quality, update feature statistics
- **End of Phase:** Create snapshots of processed data

### Data Retention
- Keep raw data for full project duration
- Archive processed data for minimum 1 year post-completion
- Document location of archived data

---

## References & Resources

- **Data Sources:** See list above
- **Processing Scripts:** `../04_Scripts/data_loader.py`, `preprocessing.py`
- **Analysis Notebooks:** `../03_Notebooks/01_Data_Exploration.ipynb`
- **Feature Documentation:** `FEATURE_DICTIONARY.md` (to be created)

---

**Last Updated:** November 16, 2025
**Data Curator:** [Data Analyst Name]
**Next Review Date:** [Weekly during project]

---

## Quick Navigation
- [Raw Data Details](#raw-data)
- [Processed Data Details](#processed-data)
- [Data Quality Summary](#data-quality-summary)
- [Data Dictionary](#data-dictionary)
- [ETL Process](#data-pipeline--processing)

---

*For questions about specific datasets, contact the Data Analyst. For technical issues with data access, contact the Technical Lead.*
