"""
Feature Engineering Module for Bangkok Traffic Flow Optimization Project

This module provides functions for creating features for traffic prediction,
including temporal features, lag features, and rolling statistics.

Author: Data Science Team
Date: November 2025
"""

import numpy as np
import pandas as pd
import logging
from typing import Dict, List, Tuple, Optional, Union
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# TEMPORAL FEATURES
# ============================================================================

def create_temporal_features(
    df: pd.DataFrame,
    datetime_col: str = 'date'
) -> pd.DataFrame:
    """
    Create temporal features from datetime column.
    
    Args:
        df: Input DataFrame
        datetime_col: Name of datetime column
    
    Returns:
        DataFrame with temporal features added
    """
    df = df.copy()
    
    # Ensure datetime type
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    
    # Basic temporal features
    df['year'] = df[datetime_col].dt.year
    df['month'] = df[datetime_col].dt.month
    df['day'] = df[datetime_col].dt.day
    df['dayofweek'] = df[datetime_col].dt.dayofweek  # 0=Monday
    df['dayofyear'] = df[datetime_col].dt.dayofyear
    df['weekofyear'] = df[datetime_col].dt.isocalendar().week.astype(int)
    df['quarter'] = df[datetime_col].dt.quarter
    
    # Binary features
    df['is_weekend'] = (df['dayofweek'] >= 5).astype(int)
    df['is_month_start'] = df[datetime_col].dt.is_month_start.astype(int)
    df['is_month_end'] = df[datetime_col].dt.is_month_end.astype(int)
    
    # Thai season (simplified)
    def get_thai_season(month):
        if month in [11, 12, 1, 2]:
            return 'cool'
        elif month in [3, 4, 5]:
            return 'hot'
        else:
            return 'rainy'
    
    df['season'] = df['month'].apply(get_thai_season)
    
    # Thai holidays (major ones)
    thai_holidays = [
        # (month, day): 'holiday_name'
        (1, 1),   # New Year
        (4, 13), (4, 14), (4, 15),  # Songkran
        (5, 1),   # Labour Day
        (12, 5),  # King's Birthday
        (12, 31), # New Year's Eve
    ]
    
    df['is_holiday'] = df.apply(
        lambda x: int((x['month'], x['day']) in thai_holidays),
        axis=1
    )
    
    logger.info(f"Created {12} temporal features")
    
    return df


# ============================================================================
# LAG FEATURES
# ============================================================================

def create_lag_features(
    df: pd.DataFrame,
    target_col: str,
    lag_periods: List[int] = [1, 7, 14, 30]
) -> pd.DataFrame:
    """
    Create lag features for time-series prediction.
    
    Args:
        df: Input DataFrame (must be sorted by date)
        target_col: Target column name
        lag_periods: List of lag periods to create
    
    Returns:
        DataFrame with lag features added
    """
    df = df.copy()
    
    for lag in lag_periods:
        col_name = f'{target_col}_lag_{lag}'
        df[col_name] = df[target_col].shift(lag)
        logger.info(f"Created lag feature: {col_name}")
    
    return df


def create_diff_features(
    df: pd.DataFrame,
    target_col: str,
    diff_periods: List[int] = [1, 7]
) -> pd.DataFrame:
    """
    Create difference features (change from previous period).
    
    Args:
        df: Input DataFrame
        target_col: Target column name
        diff_periods: List of differencing periods
    
    Returns:
        DataFrame with difference features added
    """
    df = df.copy()
    
    for period in diff_periods:
        col_name = f'{target_col}_diff_{period}'
        df[col_name] = df[target_col].diff(period)
        logger.info(f"Created diff feature: {col_name}")
    
    return df


# ============================================================================
# ROLLING WINDOW FEATURES
# ============================================================================

def create_rolling_features(
    df: pd.DataFrame,
    target_col: str,
    windows: List[int] = [7, 14, 30]
) -> pd.DataFrame:
    """
    Create rolling window features (mean, std, min, max).
    
    Args:
        df: Input DataFrame
        target_col: Target column name
        windows: List of window sizes
    
    Returns:
        DataFrame with rolling features added
    """
    df = df.copy()
    
    for window in windows:
        # Rolling mean
        df[f'{target_col}_rolling_mean_{window}'] = (
            df[target_col].rolling(window=window, min_periods=1).mean()
        )
        
        # Rolling std
        df[f'{target_col}_rolling_std_{window}'] = (
            df[target_col].rolling(window=window, min_periods=1).std()
        )
        
        # Rolling min
        df[f'{target_col}_rolling_min_{window}'] = (
            df[target_col].rolling(window=window, min_periods=1).min()
        )
        
        # Rolling max
        df[f'{target_col}_rolling_max_{window}'] = (
            df[target_col].rolling(window=window, min_periods=1).max()
        )
        
        logger.info(f"Created rolling features for window={window}")
    
    return df


def create_ewm_features(
    df: pd.DataFrame,
    target_col: str,
    spans: List[int] = [7, 14, 30]
) -> pd.DataFrame:
    """
    Create exponentially weighted moving average features.
    
    Args:
        df: Input DataFrame
        target_col: Target column name
        spans: List of span values for EWM
    
    Returns:
        DataFrame with EWM features added
    """
    df = df.copy()
    
    for span in spans:
        col_name = f'{target_col}_ewm_{span}'
        df[col_name] = df[target_col].ewm(span=span, adjust=False).mean()
        logger.info(f"Created EWM feature: {col_name}")
    
    return df


# ============================================================================
# INTERACTION FEATURES
# ============================================================================

def create_interaction_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create interaction features between existing columns.
    
    Args:
        df: Input DataFrame
    
    Returns:
        DataFrame with interaction features added
    """
    df = df.copy()
    
    # Weekend x Month interaction
    if 'is_weekend' in df.columns and 'month' in df.columns:
        df['weekend_x_month'] = df['is_weekend'] * df['month']
    
    # Holiday x Dayofweek interaction
    if 'is_holiday' in df.columns and 'dayofweek' in df.columns:
        df['holiday_x_dayofweek'] = df['is_holiday'] * df['dayofweek']
    
    logger.info("Created interaction features")
    
    return df


# ============================================================================
# CYCLICAL FEATURES
# ============================================================================

def create_cyclical_features(
    df: pd.DataFrame,
    col: str,
    max_val: int
) -> pd.DataFrame:
    """
    Create cyclical (sin/cos) encoding for periodic features.
    
    Args:
        df: Input DataFrame
        col: Column to encode
        max_val: Maximum value (e.g., 12 for months, 7 for days)
    
    Returns:
        DataFrame with cyclical features added
    """
    df = df.copy()
    
    df[f'{col}_sin'] = np.sin(2 * np.pi * df[col] / max_val)
    df[f'{col}_cos'] = np.cos(2 * np.pi * df[col] / max_val)
    
    logger.info(f"Created cyclical features for {col}")
    
    return df


# ============================================================================
# MAIN FEATURE ENGINEERING PIPELINE
# ============================================================================

def create_model_features(
    df: pd.DataFrame,
    target_col: str = 'congestion_index',
    datetime_col: str = 'date',
    lag_periods: List[int] = [1, 7, 14, 30],
    rolling_windows: List[int] = [7, 14, 30],
    include_cyclical: bool = True
) -> pd.DataFrame:
    """
    Main feature engineering pipeline.
    
    Args:
        df: Input DataFrame
        target_col: Target column name
        datetime_col: Datetime column name
        lag_periods: Lag periods to create
        rolling_windows: Rolling window sizes
        include_cyclical: Whether to include cyclical encoding
    
    Returns:
        DataFrame with all engineered features
    """
    logger.info("Starting feature engineering pipeline...")
    
    # 1. Temporal features
    df = create_temporal_features(df, datetime_col)
    
    # 2. Lag features
    df = create_lag_features(df, target_col, lag_periods)
    
    # 3. Difference features
    df = create_diff_features(df, target_col, [1, 7])
    
    # 4. Rolling features
    df = create_rolling_features(df, target_col, rolling_windows)
    
    # 5. EWM features
    df = create_ewm_features(df, target_col, [7, 14])
    
    # 6. Interaction features
    df = create_interaction_features(df)
    
    # 7. Cyclical features
    if include_cyclical:
        df = create_cyclical_features(df, 'month', 12)
        df = create_cyclical_features(df, 'dayofweek', 7)
    
    # Drop rows with NaN from lagging
    initial_rows = len(df)
    df = df.dropna()
    dropped_rows = initial_rows - len(df)
    
    logger.info(f"Feature engineering complete. Created {len(df.columns)} features.")
    logger.info(f"Dropped {dropped_rows} rows with NaN values.")
    
    return df


def get_feature_columns(
    df: pd.DataFrame,
    target_col: str = 'congestion_index',
    exclude_cols: List[str] = ['date']
) -> List[str]:
    """
    Get list of feature columns (exclude target and specified columns).
    
    Args:
        df: DataFrame with features
        target_col: Target column to exclude
        exclude_cols: Additional columns to exclude
    
    Returns:
        List of feature column names
    """
    exclude = set(exclude_cols + [target_col])
    features = [col for col in df.columns if col not in exclude]
    return features


def prepare_train_test_data(
    df: pd.DataFrame,
    target_col: str,
    feature_cols: List[str],
    train_ratio: float = 0.8
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Prepare train/test data arrays.
    
    Args:
        df: DataFrame with features
        target_col: Target column
        feature_cols: Feature columns
        train_ratio: Training set ratio
    
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    n = len(df)
    train_size = int(n * train_ratio)
    
    X = df[feature_cols].values
    y = df[target_col].values
    
    X_train = X[:train_size]
    X_test = X[train_size:]
    y_train = y[:train_size]
    y_test = y[train_size:]
    
    logger.info(f"Train size: {len(X_train)}, Test size: {len(X_test)}")
    
    return X_train, X_test, y_train, y_test


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    logger.info("Feature engineering module loaded successfully")
    
    # Example usage
    print("""
    Example Usage:
    --------------
    from feature_engineering import create_model_features, get_feature_columns
    
    # Create features
    df_features = create_model_features(
        df, 
        target_col='congestion_index',
        lag_periods=[1, 7, 14, 30]
    )
    
    # Get feature columns
    feature_cols = get_feature_columns(df_features, target_col='congestion_index')
    print(f"Number of features: {len(feature_cols)}")
    """)
