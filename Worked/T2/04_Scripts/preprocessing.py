"""
Data Preprocessing Module for Bangkok Traffic Congestion Index Prediction

This module provides functions for preprocessing traffic and weather data
for the Bangkok Traffic Congestion Index Prediction project.

Datasets:
- Bangkok Traffic Congestion Index (daily TCI, 2019-2025)
- Bangkok Weather Data (temperature, humidity, precipitation)
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


# ============================================================================
# TRAFFIC DATA PREPROCESSING
# ============================================================================

def preprocess_traffic_data(
    df: pd.DataFrame,
    datetime_col: str = 'date',
    congestion_col: str = 'congestion_index'
) -> pd.DataFrame:
    """
    Preprocess Bangkok traffic congestion data.
    
    Args:
        df: Raw traffic DataFrame
        datetime_col: Name of datetime column
        congestion_col: Name of congestion index column
    
    Returns:
        Preprocessed DataFrame
    """
    df = df.copy()
    
    # Convert datetime
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    df = df.sort_values(datetime_col)
    
    # Handle missing values (interpolation for time-series)
    if df[congestion_col].isnull().any():
        logger.warning(f"Found {df[congestion_col].isnull().sum()} missing values in {congestion_col}")
        df[congestion_col] = df[congestion_col].interpolate(method='linear', limit=7)
    
    # Remove outliers (keep extreme events but flag them)
    Q1 = df[congestion_col].quantile(0.25)
    Q3 = df[congestion_col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    df['is_outlier'] = (df[congestion_col] < lower_bound) | (df[congestion_col] > upper_bound)
    outlier_count = df['is_outlier'].sum()
    logger.info(f"Identified {outlier_count} outliers in traffic data")
    
    # Create temporal features
    df['year'] = df[datetime_col].dt.year
    df['month'] = df[datetime_col].dt.month
    df['day'] = df[datetime_col].dt.day
    df['dayofweek'] = df[datetime_col].dt.dayofweek
    df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)
    
    # Bangkok holidays (simplified)
    holidays = {
        (1, 1): 'New Year',
        (4, 13): 'Songkran',
        (4, 14): 'Songkran',
        (4, 15): 'Songkran',
        (5, 1): 'Labour Day',
        (12, 5): 'King Birthday',
        (12, 31): 'New Year Eve'
    }
    df['is_holiday'] = df.apply(
        lambda x: (x['month'], x['day']) in holidays,
        axis=1
    ).astype(int)
    
    # Season (Thailand: Dry, Rainy, Cool)
    def get_season(month):
        if month in [3, 4, 5]:
            return 'dry'
        elif month in [6, 7, 8, 9, 10]:
            return 'rainy'
        else:
            return 'cool'
    
    df['season'] = df['month'].apply(get_season)
    
    logger.info(f"Traffic data preprocessed: {df.shape}")
    return df


# ============================================================================
# WEATHER DATA PREPROCESSING
# ============================================================================
def preprocess_accident_data(
    df: pd.DataFrame,
    lat_col: str = 'latitude',
    lon_col: str = 'longitude',
    datetime_col: str = 'datetime',
    bangkok_bounds: Tuple[float, float, float, float] = (13.5, 100.3, 13.95, 100.9)
) -> pd.DataFrame:
    """
    Preprocess accident data (US dataset for methodology, or Bangkok data).
    
    Args:
        df: Raw accident DataFrame
        lat_col: Latitude column name
        lon_col: Longitude column name
        datetime_col: Datetime column name
        bangkok_bounds: (min_lat, min_lon, max_lat, max_lon) for Bangkok
    
    Returns:
        Preprocessed DataFrame
    """
    df = df.copy()
    
    # Convert datetime
    if datetime_col in df.columns:
        df[datetime_col] = pd.to_datetime(df[datetime_col], errors='coerce')
    
    # Validate geographic coordinates
    if lat_col in df.columns and lon_col in df.columns:
        valid_coords = (
            (df[lat_col] >= bangkok_bounds[0]) & 
            (df[lat_col] <= bangkok_bounds[2]) &
            (df[lon_col] >= bangkok_bounds[1]) & 
            (df[lon_col] <= bangkok_bounds[3])
        )
        
        if not valid_coords.all():
            logger.warning(f"Filtering out {(~valid_coords).sum()} records outside Bangkok bounds")
            df = df[valid_coords]
    
    # Handle missing severity (if applicable)
    if 'severity' in df.columns:
        df['severity'] = df['severity'].fillna('Unknown')
    
    # Create temporal features
    if datetime_col in df.columns:
        df['year'] = df[datetime_col].dt.year
        df['month'] = df[datetime_col].dt.month
        df['day'] = df[datetime_col].dt.day
        df['hour'] = df[datetime_col].dt.hour
        df['dayofweek'] = df[datetime_col].dt.dayofweek
        df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)
    
    # Weather condition standardization
    if 'weather_condition' in df.columns:
        weather_mapping = {
            'Clear': 'clear',
            'Cloudy': 'cloudy',
            'Rain': 'rain',
            'Heavy Rain': 'heavy_rain',
            'Fog': 'fog',
            'Snow': 'snow'  # Not applicable to Bangkok but keep for US data
        }
        df['weather_condition'] = df['weather_condition'].map(weather_mapping).fillna('unknown')
    
    logger.info(f"Accident data preprocessed: {df.shape}")
    return df


def preprocess_weather_data(
    df: pd.DataFrame,
    datetime_col: str = 'datetime',
    temp_col: str = 'temperature',
    precip_col: str = 'precipitation'
) -> pd.DataFrame:
    """
    Preprocess weather data.
    
    Args:
        df: Raw weather DataFrame
        datetime_col: Datetime column name
        temp_col: Temperature column name
        precip_col: Precipitation column name
    
    Returns:
        Preprocessed DataFrame
    """
    df = df.copy()
    
    # Convert datetime
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    df = df.sort_values(datetime_col)
    
    # Handle missing temperature (interpolate)
    if df[temp_col].isnull().any():
        df[temp_col] = df[temp_col].interpolate(method='linear', limit=7)
    
    # Handle missing precipitation (fill with 0)
    if precip_col in df.columns:
        df[precip_col] = df[precip_col].fillna(0)
    
    # Validate temperature range for Bangkok (15-42°C typical)
    temp_outliers = (df[temp_col] < 10) | (df[temp_col] > 45)
    if temp_outliers.any():
        logger.warning(f"Found {temp_outliers.sum()} temperature outliers")
        df.loc[temp_outliers, temp_col] = df[temp_col].median()
    
    # Create weather categories
    if precip_col in df.columns:
        df['weather_category'] = pd.cut(
            df[precip_col],
            bins=[-np.inf, 0.1, 10, 35, np.inf],
            labels=['dry', 'light_rain', 'moderate_rain', 'heavy_rain']
        )
    
    logger.info(f"Weather data preprocessed: {df.shape}")
    return df


# ============================================================================
# FEATURE ENGINEERING
# ============================================================================

def create_traffic_features(
    df: pd.DataFrame,
    datetime_col: str = 'date',
    target_col: str = 'congestion_index'
) -> pd.DataFrame:
    """
    Create advanced features for traffic prediction.
    
    Args:
        df: Preprocessed traffic DataFrame
        datetime_col: Datetime column name
        target_col: Target variable column name
    
    Returns:
        DataFrame with engineered features
    """
    df = df.copy()
    
    # Lagged features (previous time periods)
    lags = [1, 7, 14, 30]  # 1 day, 1 week, 2 weeks, 1 month
    for lag in lags:
        df[f'{target_col}_lag_{lag}'] = df[target_col].shift(lag)
    
    # Rolling statistics
    windows = [7, 14, 30]
    for window in windows:
        df[f'{target_col}_rolling_mean_{window}'] = df[target_col].rolling(window=window).mean()
        df[f'{target_col}_rolling_std_{window}'] = df[target_col].rolling(window=window).std()
        df[f'{target_col}_rolling_min_{window}'] = df[target_col].rolling(window=window).min()
        df[f'{target_col}_rolling_max_{window}'] = df[target_col].rolling(window=window).max()
    
    # Day of month features
    if datetime_col in df.columns:
        df['day_of_month'] = df[datetime_col].dt.day
        df['week_of_year'] = df[datetime_col].dt.isocalendar().week
        df['quarter'] = df[datetime_col].dt.quarter
    
    # Interaction features
    if 'is_weekend' in df.columns and 'month' in df.columns:
        df['weekend_x_month'] = df['is_weekend'] * df['month']
    
    logger.info(f"Created traffic features: {df.shape[1]} columns")
    return df


def merge_datasets(
    traffic_df: pd.DataFrame,
    weather_df: Optional[pd.DataFrame] = None,
    accident_df: Optional[pd.DataFrame] = None,
    date_col: str = 'date'
) -> pd.DataFrame:
    """
    Merge traffic, weather, and accident datasets.
    
    Args:
        traffic_df: Traffic DataFrame (base)
        weather_df: Weather DataFrame (optional)
        accident_df: Accident DataFrame (optional)
        date_col: Common date column for merging
    
    Returns:
        Merged DataFrame
    """
    merged_df = traffic_df.copy()
    
    # Merge weather data
    if weather_df is not None:
        logger.info("Merging weather data...")
        weather_df = weather_df.rename(columns={'datetime': date_col})
        merged_df = merged_df.merge(
            weather_df,
            on=date_col,
            how='left',
            suffixes=('', '_weather')
        )
    
    # Aggregate accident data by date
    if accident_df is not None and 'datetime' in accident_df.columns:
        logger.info("Aggregating and merging accident data...")
        accident_df['date'] = pd.to_datetime(accident_df['datetime']).dt.date
        
        accident_agg = accident_df.groupby('date').agg({
            'severity': 'count',  # Count of accidents
            'latitude': 'count'   # Alternative count
        }).rename(columns={
            'severity': 'accident_count',
            'latitude': 'accident_count_alt'
        }).reset_index()
        
        accident_agg['date'] = pd.to_datetime(accident_agg['date'])
        
        merged_df = merged_df.merge(
            accident_agg,
            left_on=date_col,
            right_on='date',
            how='left'
        )
        
        # Fill missing accident counts with 0
        if 'accident_count' in merged_df.columns:
            merged_df['accident_count'] = merged_df['accident_count'].fillna(0)
    
    logger.info(f"Merged dataset shape: {merged_df.shape}")
    return merged_df


# ============================================================================
# DATA SPLITTING
# ============================================================================

def temporal_train_test_split(
    df: pd.DataFrame,
    date_col: str,
    train_ratio: float = 0.6,
    val_ratio: float = 0.2,
    test_ratio: float = 0.2
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Split data temporally (chronologically) for time-series modeling.
    
    Args:
        df: DataFrame to split
        date_col: Date column for sorting
        train_ratio: Training set ratio
        val_ratio: Validation set ratio
        test_ratio: Test set ratio
    
    Returns:
        Tuple of (train_df, val_df, test_df)
    """
    df = df.sort_values(date_col).reset_index(drop=True)
    
    n = len(df)
    train_size = int(n * train_ratio)
    val_size = int(n * val_ratio)
    
    train_df = df.iloc[:train_size]
    val_df = df.iloc[train_size:train_size + val_size]
    test_df = df.iloc[train_size + val_size:]
    
    logger.info(f"Temporal split - Train: {len(train_df)} ({train_ratio:.1%}), "
                f"Val: {len(val_df)} ({val_ratio:.1%}), "
                f"Test: {len(test_df)} ({test_ratio:.1%})")
    
    return train_df, val_df, test_df


# ============================================================================
# NORMALIZATION & SCALING
# ============================================================================

def normalize_features(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    test_df: pd.DataFrame,
    numeric_features: List[str],
    method: str = 'standard'
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, Dict]:
    """
    Normalize numerical features using training set statistics.
    
    Args:
        train_df: Training DataFrame
        val_df: Validation DataFrame
        test_df: Test DataFrame
        numeric_features: List of numerical columns to normalize
        method: 'standard' or 'minmax'
    
    Returns:
        Tuple of (train_df, val_df, test_df, scaler_params)
    """
    train_df = train_df.copy()
    val_df = val_df.copy()
    test_df = test_df.copy()
    
    scaler_params = {}
    
    for col in numeric_features:
        if col not in train_df.columns:
            logger.warning(f"Column {col} not found in training data")
            continue
        
        if method == 'standard':
            mean_val = train_df[col].mean()
            std_val = train_df[col].std()
            
            train_df[col] = (train_df[col] - mean_val) / std_val
            val_df[col] = (val_df[col] - mean_val) / std_val
            test_df[col] = (test_df[col] - mean_val) / std_val
            
            scaler_params[col] = {'mean': mean_val, 'std': std_val, 'method': 'standard'}
        
        elif method == 'minmax':
            min_val = train_df[col].min()
            max_val = train_df[col].max()
            
            train_df[col] = (train_df[col] - min_val) / (max_val - min_val)
            val_df[col] = (val_df[col] - min_val) / (max_val - min_val)
            test_df[col] = (test_df[col] - min_val) / (max_val - min_val)
            
            scaler_params[col] = {'min': min_val, 'max': max_val, 'method': 'minmax'}
    
    logger.info(f"Normalized {len(numeric_features)} features using {method} method")
    
    return train_df, val_df, test_df, scaler_params


# ============================================================================
# ENCODING
# ============================================================================

def encode_categorical_features(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    test_df: pd.DataFrame,
    categorical_features: List[str],
    method: str = 'onehot'
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Encode categorical features.
    
    Args:
        train_df: Training DataFrame
        val_df: Validation DataFrame
        test_df: Test DataFrame
        categorical_features: List of categorical columns
        method: 'onehot' or 'label'
    
    Returns:
        Tuple of (train_df, val_df, test_df)
    """
    train_df = train_df.copy()
    val_df = val_df.copy()
    test_df = test_df.copy()
    
    if method == 'onehot':
        # One-hot encoding
        train_df = pd.get_dummies(train_df, columns=categorical_features, prefix=categorical_features)
        val_df = pd.get_dummies(val_df, columns=categorical_features, prefix=categorical_features)
        test_df = pd.get_dummies(test_df, columns=categorical_features, prefix=categorical_features)
        
        # Align columns
        all_columns = train_df.columns.tolist()
        val_df = val_df.reindex(columns=all_columns, fill_value=0)
        test_df = test_df.reindex(columns=all_columns, fill_value=0)
    
    elif method == 'label':
        # Label encoding
        from sklearn.preprocessing import LabelEncoder
        
        for col in categorical_features:
            if col in train_df.columns:
                le = LabelEncoder()
                train_df[col] = le.fit_transform(train_df[col].astype(str))
                val_df[col] = le.transform(val_df[col].astype(str))
                test_df[col] = le.transform(test_df[col].astype(str))
    
    logger.info(f"Encoded {len(categorical_features)} categorical features using {method}")
    
    return train_df, val_df, test_df


if __name__ == "__main__":
    logger.info("Preprocessing module loaded successfully")
