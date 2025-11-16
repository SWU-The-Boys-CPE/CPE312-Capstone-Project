# Data Dictionary

**Project:** Urban Traffic Flow Optimization and Public Transit Efficiency Analysis in Bangkok Metropolitan Area

**Version:** 1.0

**Last Updated:** November 16, 2025

---

## Table of Contents

1. [Bangkok Traffic Congestion Index](#1-bangkok-traffic-congestion-index)
2. [US Accidents Dataset](#2-us-accidents-dataset)
3. [OpenStreetMap Road Network](#3-openstreetmap-road-network)
4. [Weather and Environmental Data](#4-weather-and-environmental-data)
5. [Public Transit Ridership Data](#5-public-transit-ridership-data)
6. [Engineered Features](#6-engineered-features)
7. [Data Types and Formats](#7-data-types-and-formats)
8. [Missing Value Codes](#8-missing-value-codes)

---

## 1. Bangkok Traffic Congestion Index

**Source:** CEIC Data / TrafficIndex.org

**File:** `bangkok_traffic_2019_2025.csv`

**Records:** 1,682+ observations

**Date Range:** January 1, 2019 - November 16, 2025

### Variables

| Variable Name | Data Type | Description | Valid Range | Missing Values | Notes |
|--------------|-----------|-------------|-------------|----------------|-------|
| `date` | Date | Observation date | 2019-01-01 to 2025-11-16 | 0% | Format: YYYY-MM-DD |
| `congestion_index` | Float | Traffic congestion index | 0.0 - 200.0 | < 2% | Higher = more congested |
| `time_of_day` | String | Time period | 'morning', 'afternoon', 'evening', 'night' | 0% | 4 categories |
| `region` | String | Bangkok region | 'central', 'north', 'south', 'east', 'west' | 0% | 5 regions |
| `day_of_week` | Integer | Day of week | 0-6 | 0% | 0=Monday, 6=Sunday |
| `is_weekend` | Boolean | Weekend indicator | 0, 1 | 0% | 1=Saturday/Sunday |
| `is_holiday` | Boolean | Thai holiday indicator | 0, 1 | 0% | Based on Thai calendar |

### Summary Statistics
- **Mean congestion_index:** 38.88
- **Median congestion_index:** 35.20
- **Std Dev:** 18.45
- **Historical Peak:** 162.13 (Special event)
- **Typical Range:** 20.0 - 80.0
- **Peak Hours:** 17:00-18:00 (avg 65.3)
- **Off-Peak Hours:** 02:00-05:00 (avg 15.8)

### Known Issues
- 2 days missing data (Jan 15, 2020 and May 3, 2021) - public holidays
- Outliers > 150 during special events (royal ceremonies, major protests)
- Regional data availability varies (central has most coverage)

---

## 2. US Accidents Dataset

**Source:** Kaggle - Sobhan Moosavi et al.

**File:** `us_accidents.csv`

**Records:** 2,845,342 (2016-2021)

**Purpose:** Methodology reference for Bangkok accident analysis

### Core Variables (49 total, key variables listed)

| Variable Name | Data Type | Description | Valid Range | Missing Values | Notes |
|--------------|-----------|-------------|-------------|----------------|-------|
| `ID` | String | Unique accident identifier | - | 0% | Format: A-XXXXXXX |
| `Severity` | Integer | Accident severity | 1-4 | 0% | 1=minor, 4=severe |
| `Start_Time` | Datetime | Accident start time | 2016-2021 | 0% | UTC timezone |
| `End_Time` | Datetime | Accident end time | 2016-2021 | 0% | Duration varies |
| `Start_Lat` | Float | Latitude | -90 to 90 | 0% | WGS84 |
| `Start_Lng` | Float | Longitude | -180 to 180 | 0% | WGS84 |
| `Distance(mi)` | Float | Affected road length | 0.0 - 50.0 | 1.2% | Miles |
| `Temperature(F)` | Float | Temperature | -40 to 120 | 5.8% | Fahrenheit |
| `Humidity(%)` | Float | Humidity percentage | 0 - 100 | 5.3% | Percent |
| `Pressure(in)` | Float | Atmospheric pressure | 25 - 35 | 5.5% | Inches Hg |
| `Visibility(mi)` | Float | Visibility distance | 0 - 10 | 6.2% | Miles |
| `Wind_Speed(mph)` | Float | Wind speed | 0 - 100 | 7.1% | MPH |
| `Precipitation(in)` | Float | Precipitation amount | 0 - 10 | 8.5% | Inches |
| `Weather_Condition` | String | Weather description | Various | 3.2% | 120+ categories |
| `Amenity` | Boolean | Nearby amenity | 0, 1 | 0% | Gas, restaurant, etc. |
| `Crossing` | Boolean | Near crossing | 0, 1 | 0% | Pedestrian crossing |
| `Junction` | Boolean | Near junction | 0, 1 | 0% | Intersection |
| `Traffic_Signal` | Boolean | Near traffic signal | 0, 1 | 0% | Signal presence |
| `Sunrise_Sunset` | String | Day/night | 'Day', 'Night' | 0.5% | 2 categories |
| `Civil_Twilight` | String | Light condition | 'Day', 'Night' | 0.5% | 2 categories |
| `Weather_Timestamp` | Datetime | Weather record time | 2016-2021 | 5.5% | UTC |

### Severity Levels
- **1:** Minor impact (< 10 min delay)
- **2:** Moderate impact (10-30 min delay)
- **3:** Significant impact (30-60 min delay)
- **4:** Severe impact (> 60 min delay)

### Usage Notes
- **For Bangkok Analysis:** Use methodology and feature engineering approaches
- **Not Direct Use:** Geographic data is US-specific
- **Lessons Learned:** Weather correlation, time-of-day patterns, severity classification

---

## 3. OpenStreetMap Road Network

**Source:** OpenStreetMap (OSM)

**File:** `bangkok_osm_roads.geojson`

**Format:** GeoJSON / Shapefile

**Coverage:** Bangkok Metropolitan Area (13.5-13.95°N, 100.3-100.9°E)

### Geometry Fields

| Field Name | Data Type | Description | Valid Range | Notes |
|------------|-----------|-------------|-------------|-------|
| `geometry` | LineString | Road geometry | WGS84 coordinates | GeoJSON format |
| `osm_id` | Integer | OSM identifier | - | Unique ID |
| `name` | String | Road name | - | Thai and English |
| `name:th` | String | Thai road name | - | Thai script |
| `name:en` | String | English road name | - | Transliteration |

### Attribute Fields

| Field Name | Data Type | Description | Valid Values | Notes |
|------------|-----------|-------------|--------------|-------|
| `highway` | String | Road type | 'motorway', 'trunk', 'primary', 'secondary', 'tertiary', 'residential', 'service' | OSM classification |
| `lanes` | Integer | Number of lanes | 1-12 | Often missing |
| `maxspeed` | Integer | Speed limit (km/h) | 20-120 | Often missing |
| `oneway` | String | One-way indicator | 'yes', 'no', '-1' | Direction |
| `surface` | String | Road surface | 'asphalt', 'concrete', 'unpaved' | Often missing |
| `width` | Float | Road width (m) | 2.0-30.0 | Often missing |
| `bridge` | String | Bridge indicator | 'yes', 'no' | Bridge presence |
| `tunnel` | String | Tunnel indicator | 'yes', 'no' | Tunnel presence |
| `ref` | String | Road reference | 'Route 1', 'AH1' | Highway numbers |

### Road Type Classification

**Major Roads (High Priority):**
- **motorway:** Expressways, tollways (e.g., Chalerm Mahanakhon Expressway)
- **trunk:** Important non-motorway roads (e.g., Vibhavadi Rangsit Road)
- **primary:** Major roads connecting districts (e.g., Sukhumvit Road)

**Minor Roads (Medium Priority):**
- **secondary:** District-level connectors
- **tertiary:** Sub-district roads

**Local Roads (Low Priority):**
- **residential:** Neighborhood streets
- **service:** Service roads, parking aisles

### Completeness
- **Major roads:** ~95% complete
- **Minor roads:** ~80% complete
- **Attributes (lanes, speed):** ~40% complete
- **Road names:** ~85% complete

---

## 4. Weather and Environmental Data

**Source:** NOAA, NASA Weather APIs

**File:** `bangkok_weather.csv`

**Records:** Daily observations (2019-2025)

**Coverage:** Bangkok Meteorological Station (13.7563°N, 100.5018°E)

### Variables

| Variable Name | Data Type | Description | Valid Range | Missing Values | Notes |
|--------------|-----------|-------------|-------------|----------------|-------|
| `date` | Date | Observation date | 2019-2025 | 0% | Daily data |
| `temp_avg` | Float | Average temperature (°C) | 15.0 - 42.0 | < 1% | Daily average |
| `temp_min` | Float | Minimum temperature (°C) | 12.0 - 35.0 | < 1% | Daily minimum |
| `temp_max` | Float | Maximum temperature (°C) | 20.0 - 45.0 | < 1% | Daily maximum |
| `humidity_avg` | Float | Average humidity (%) | 30.0 - 100.0 | 2% | Daily average |
| `precipitation` | Float | Precipitation (mm) | 0.0 - 250.0 | 3% | Daily total |
| `wind_speed_avg` | Float | Average wind speed (km/h) | 0.0 - 50.0 | 5% | Daily average |
| `wind_direction` | String | Wind direction | 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW' | 6% | 8 directions |
| `pressure` | Float | Atmospheric pressure (hPa) | 1005 - 1020 | 2% | Sea level |
| `visibility` | Float | Visibility (km) | 0.5 - 20.0 | 8% | Daily average |
| `cloud_cover` | Integer | Cloud cover (oktas) | 0 - 8 | 10% | 0=clear, 8=overcast |
| `weather_condition` | String | Weather description | See categories below | 1% | Primary condition |

### Weather Condition Categories
- `clear`: Clear sky
- `partly_cloudy`: Partly cloudy
- `cloudy`: Overcast
- `rain`: Light to moderate rain
- `heavy_rain`: Heavy rain
- `thunderstorm`: Thunderstorms
- `fog`: Fog/mist
- `haze`: Haze/smoke (pollution)

### Bangkok Climate Context
- **Hot Season (Dry):** March-May (avg 32-35°C)
- **Rainy Season:** June-October (avg 28-30°C, frequent rain)
- **Cool Season:** November-February (avg 25-28°C)
- **Typical Precipitation:** 1,500 mm/year
- **Peak Rain Month:** September (~300 mm)

---

## 5. Public Transit Ridership Data

**Source:** Bangkok BMA/BTS/MRT (pending) + Reference datasets

**File:** `transit_ridership.csv`

**Status:** Partially available (using reference data)

### Variables (Planned)

| Variable Name | Data Type | Description | Valid Range | Missing Values | Notes |
|--------------|-----------|-------------|-------------|----------------|-------|
| `datetime` | Datetime | Entry timestamp | 2019-2025 | TBD | Hourly aggregates |
| `station_id` | String | Station identifier | - | 0% | BTS/MRT codes |
| `station_name` | String | Station name | - | 0% | Thai and English |
| `line_id` | String | Transit line | 'BTS_Sukhumvit', 'BTS_Silom', 'MRT_Blue', 'MRT_Purple' | 0% | 4+ lines |
| `entry_count` | Integer | Passenger entries | 0 - 50,000 | TBD | Hourly entries |
| `exit_count` | Integer | Passenger exits | 0 - 50,000 | TBD | Hourly exits |
| `day_of_week` | Integer | Day of week | 0-6 | 0% | 0=Monday |
| `hour` | Integer | Hour of day | 0-23 | 0% | 24-hour format |
| `is_weekend` | Boolean | Weekend indicator | 0, 1 | 0% | Saturday/Sunday |
| `is_holiday` | Boolean | Holiday indicator | 0, 1 | 0% | Thai holidays |

### Reference Dataset (Chicago/Helsinki)
Used for methodology and feature engineering while awaiting Bangkok data approval

---

## 6. Engineered Features

**Created during preprocessing and feature engineering**

### Temporal Features

| Feature Name | Data Type | Description | Formula/Logic |
|-------------|-----------|-------------|---------------|
| `year` | Integer | Year | Extracted from date |
| `month` | Integer | Month (1-12) | Extracted from date |
| `day` | Integer | Day of month | Extracted from date |
| `hour` | Integer | Hour (0-23) | Extracted from datetime |
| `dayofweek` | Integer | Day of week (0-6) | 0=Monday |
| `week_of_year` | Integer | Week number | ISO week |
| `quarter` | Integer | Quarter (1-4) | Jan-Mar=Q1, etc. |
| `is_weekend` | Boolean | Weekend flag | 1 if Sat/Sun |
| `is_holiday` | Boolean | Thai holiday flag | Based on calendar |
| `season` | String | Thai season | 'dry', 'rainy', 'cool' |
| `is_morning_rush` | Boolean | Morning peak (7-9 AM) | 1 if hour in [7,8,9] |
| `is_evening_rush` | Boolean | Evening peak (5-7 PM) | 1 if hour in [17,18,19] |
| `is_rush_hour` | Boolean | Any rush hour | morning OR evening |

### Lag Features

| Feature Name | Data Type | Description | Formula |
|-------------|-----------|-------------|---------|
| `congestion_lag_1` | Float | Yesterday's congestion | shift(1) |
| `congestion_lag_7` | Float | Last week same day | shift(7) |
| `congestion_lag_14` | Float | 2 weeks ago | shift(14) |
| `congestion_lag_30` | Float | 1 month ago | shift(30) |

### Rolling Window Features

| Feature Name | Data Type | Description | Window |
|-------------|-----------|-------------|--------|
| `congestion_rolling_mean_7` | Float | 7-day avg congestion | 7 days |
| `congestion_rolling_std_7` | Float | 7-day volatility | 7 days |
| `congestion_rolling_min_7` | Float | 7-day minimum | 7 days |
| `congestion_rolling_max_7` | Float | 7-day maximum | 7 days |
| `congestion_rolling_mean_30` | Float | 30-day avg | 30 days |
| `congestion_rolling_std_30` | Float | 30-day volatility | 30 days |

### Spatial Features

| Feature Name | Data Type | Description | Method |
|-------------|-----------|-------------|--------|
| `district` | String | Bangkok district | Geocoding |
| `road_type` | String | Road classification | OSM join |
| `dist_to_major_intersection` | Float | Distance to major junction (km) | Haversine |
| `near_bts_station` | Boolean | Within 500m of BTS | Buffer |
| `near_mrt_station` | Boolean | Within 500m of MRT | Buffer |

### Interaction Features

| Feature Name | Data Type | Description | Formula |
|-------------|-----------|-------------|---------|
| `weekend_x_month` | Integer | Weekend-month interaction | is_weekend * month |
| `rain_x_rush_hour` | Integer | Rain during rush | (weather=='rain') * is_rush_hour |
| `season_x_dayofweek` | String | Season-day combination | f"{season}_{dayofweek}" |

---

## 7. Data Types and Formats

### Date and Time Formats
- **Date:** YYYY-MM-DD (ISO 8601)
- **Datetime:** YYYY-MM-DD HH:MM:SS (24-hour, UTC+7 for Bangkok)
- **Time:** HH:MM:SS (24-hour)
- **Timezone:** UTC+7 (Bangkok, Thailand)

### Coordinate System
- **CRS:** WGS84 (EPSG:4326)
- **Latitude:** Decimal degrees (-90 to 90)
- **Longitude:** Decimal degrees (-180 to 180)
- **Bangkok Bounds:** 13.5-13.95°N, 100.3-100.9°E

### Numeric Formats
- **Float:** Decimal precision to 2 places (e.g., 38.88)
- **Integer:** Whole numbers (e.g., 42)
- **Percentage:** 0-100 scale (e.g., 75.5%)

### String Formats
- **Categorical:** Lowercase, underscore-separated (e.g., 'morning_rush')
- **Names:** Title case (e.g., 'Sukhumvit Road')
- **IDs:** Uppercase with hyphens (e.g., 'BTS-N8')

---

## 8. Missing Value Codes

### Explicit Codes
- **-999:** Missing or unavailable
- **NaN:** Not a Number (float variables)
- **None:** Missing object (Python)
- **'':** Empty string (text variables)

### Implicit Missing
- **0.0:** May indicate missing for some variables (check context)
- **'Unknown':** Explicit unknown category

### Imputation Methods Used
- **Time-series:** Linear interpolation (max 7-day gap)
- **Categorical:** Mode imputation or 'Unknown' category
- **Numerical (non-time):** Median imputation
- **High missingness (>20%):** Dropped or indicator variable added

---

## Data Versioning

### Version Control
- **Raw Data:** Never modified, dated filename (e.g., `bangkok_traffic_20191115.csv`)
- **Processed Data:** Version in filename (e.g., `bangkok_traffic_cleaned_v1.csv`)
- **Date Format:** YYYYMMDD

### Change Log
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-16 | Initial data dictionary | Team |
| - | - | - | - |

---

## Notes and Conventions

### General
- All numeric variables use metric system (km, °C, mm) unless specified
- All dates/times in Bangkok timezone (UTC+7)
- Categorical variables are case-sensitive
- IDs are immutable and unique

### Bangkok-Specific
- **Thai Holidays:** Include Songkran (Apr 13-15), King's Birthday (Dec 5), etc.
- **Seasons:** Based on Thailand Met Department definitions
- **Districts:** 50 districts in Bangkok Metropolitan Area
- **Major Roads:** Focus on Vibhavadi Rangsit, Sukhumvit, Rama IV, Ratchadaphisek

### Quality Thresholds
- **Missing values:** < 10% acceptable
- **Outliers:** Flag but retain for time-series
- **Duplicates:** Remove all
- **Temporal gaps:** Interpolate max 7 days

---

**Document Owner:** Data Analysis Team

**Review Frequency:** Weekly during data collection phase

**Last Reviewed:** November 16, 2025

**Next Review:** November 23, 2025
