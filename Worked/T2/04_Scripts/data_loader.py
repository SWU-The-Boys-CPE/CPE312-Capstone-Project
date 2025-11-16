# Data Processing Script Module

"""
Script for loading, processing, and validating data.
Provides functions for ETL pipeline and data operations.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union
import logging

logger = logging.getLogger(__name__)


# ============================================================================
# DATA LOADING
# ============================================================================

def load_csv_data(
    filepath: Union[str, Path],
    parse_dates: Optional[List[str]] = None,
    **kwargs
) -> pd.DataFrame:
    """
    Load CSV file with standard options.
    
    Args:
        filepath: Path to CSV file
        parse_dates: Columns to parse as datetime
        **kwargs: Additional arguments for pd.read_csv
    
    Returns:
        Loaded DataFrame
    """
    logger.info(f"Loading data from {filepath}")
    
    df = pd.read_csv(filepath, parse_dates=parse_dates, **kwargs)
    
    logger.info(f"Data loaded successfully: {df.shape}")
    return df


def load_multiple_csv_files(
    directory: Union[str, Path],
    pattern: str = "*.csv"
) -> Dict[str, pd.DataFrame]:
    """
    Load multiple CSV files from a directory.
    
    Args:
        directory: Directory containing CSV files
        pattern: File pattern to match (default: all .csv files)
    
    Returns:
        Dictionary with filename (without extension) as key
    """
    directory = Path(directory)
    files = sorted(directory.glob(pattern))
    
    data_dict = {}
    for filepath in files:
        name = filepath.stem
        data_dict[name] = load_csv_data(filepath)
        logger.info(f"Loaded {name}: {data_dict[name].shape}")
    
    return data_dict


# ============================================================================
# DATA VALIDATION
# ============================================================================

def validate_columns(
    df: pd.DataFrame,
    required_columns: List[str],
    raise_error: bool = True
) -> Tuple[bool, List[str]]:
    """
    Validate that DataFrame has required columns.
    
    Args:
        df: DataFrame to validate
        required_columns: List of required column names
        raise_error: Raise error if validation fails
    
    Returns:
        Tuple of (is_valid, missing_columns)
    """
    missing = [col for col in required_columns if col not in df.columns]
    is_valid = len(missing) == 0
    
    if not is_valid and raise_error:
        raise ValueError(f"Missing required columns: {missing}")
    
    return is_valid, missing


def check_missing_values(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate missing value percentages.
    
    Args:
        df: DataFrame to check
    
    Returns:
        Dictionary with column names and missing percentages
    """
    missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
    return missing_pct[missing_pct > 0].to_dict()


def detect_duplicates(
    df: pd.DataFrame,
    subset: Optional[List[str]] = None
) -> pd.DataFrame:
    """
    Identify duplicate rows.
    
    Args:
        df: DataFrame to check
        subset: Columns to consider for duplicates
    
    Returns:
        DataFrame containing duplicate rows
    """
    duplicates = df[df.duplicated(subset=subset, keep=False)]
    logger.info(f"Found {len(duplicates)} duplicate rows")
    return duplicates


# ============================================================================
# DATA CLEANING
# ============================================================================

def handle_missing_values(
    df: pd.DataFrame,
    method: str = 'ffill',
    limit: int = 7,
    numeric_method: str = 'interpolate'
) -> pd.DataFrame:
    """
    Handle missing values in DataFrame.
    
    Args:
        df: DataFrame with missing values
        method: Strategy - 'ffill', 'bfill', 'drop', 'interpolate'
        limit: Maximum consecutive NaN to fill
        numeric_method: Method for numeric columns
    
    Returns:
        DataFrame with handled missing values
    """
    df = df.copy()
    
    if method == 'drop':
        df = df.dropna()
    elif method == 'ffill':
        df = df.fillna(method='ffill', limit=limit)
    elif method == 'bfill':
        df = df.fillna(method='bfill', limit=limit)
    elif method == 'interpolate':
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].interpolate(
            method='linear',
            limit=limit,
            limit_direction='both'
        )
    
    logger.info(f"Missing values handled using {method}")
    return df


def remove_duplicates(
    df: pd.DataFrame,
    subset: Optional[List[str]] = None,
    keep: str = 'first'
) -> pd.DataFrame:
    """
    Remove duplicate rows.
    
    Args:
        df: DataFrame with potential duplicates
        subset: Columns to consider for duplicates
        keep: Which duplicates to keep ('first', 'last', False for all)
    
    Returns:
        DataFrame without duplicates
    """
    n_before = len(df)
    df = df.drop_duplicates(subset=subset, keep=keep)
    n_removed = n_before - len(df)
    
    logger.info(f"Removed {n_removed} duplicate rows")
    return df


def detect_outliers(
    df: pd.DataFrame,
    method: str = 'iqr',
    multiplier: float = 1.5,
    columns: Optional[List[str]] = None
) -> Dict[str, list]:
    """
    Detect outliers using specified method.
    
    Args:
        df: DataFrame to analyze
        method: 'iqr' or 'zscore'
        multiplier: IQR multiplier (1.5 standard)
        columns: Columns to check (default: all numeric)
    
    Returns:
        Dictionary with column names and outlier indices
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    outliers_dict = {}
    
    for col in columns:
        if method == 'iqr':
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - multiplier * IQR
            upper = Q3 + multiplier * IQR
            
            outlier_mask = (df[col] < lower) | (df[col] > upper)
        
        elif method == 'zscore':
            z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
            outlier_mask = z_scores > 3
        
        outliers_dict[col] = df[outlier_mask].index.tolist()
        logger.info(f"Found {len(outliers_dict[col])} outliers in {col}")
    
    return outliers_dict


# ============================================================================
# FEATURE ENGINEERING
# ============================================================================

def create_temporal_features(
    df: pd.DataFrame,
    datetime_col: str,
    features: Optional[List[str]] = None
) -> pd.DataFrame:
    """
    Create temporal features from datetime column.
    
    Args:
        df: DataFrame with datetime column
        datetime_col: Name of datetime column
        features: Which features to create (default: all)
    
    Returns:
        DataFrame with new temporal features
    """
    df = df.copy()
    
    # Ensure datetime
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    
    # Define all possible features
    all_features = {
        'year': lambda x: x.dt.year,
        'month': lambda x: x.dt.month,
        'day': lambda x: x.dt.day,
        'hour': lambda x: x.dt.hour,
        'dayofweek': lambda x: x.dt.dayofweek,
        'quarter': lambda x: x.dt.quarter,
        'is_weekend': lambda x: x.dt.dayofweek.isin([5, 6]).astype(int),
        'is_holiday': lambda x: x.dt.month.isin([1, 4, 5, 12]).astype(int),
    }
    
    if features is None:
        features = list(all_features.keys())
    
    for feature in features:
        if feature in all_features:
            df[feature] = all_features[feature](df[datetime_col])
    
    logger.info(f"Created {len(features)} temporal features")
    return df


def create_lagged_features(
    df: pd.DataFrame,
    column: str,
    lags: List[int]
) -> pd.DataFrame:
    """
    Create lagged features.
    
    Args:
        df: DataFrame
        column: Column to create lags from
        lags: List of lag periods
    
    Returns:
        DataFrame with lagged features
    """
    df = df.copy()
    
    for lag in lags:
        df[f'{column}_lag_{lag}'] = df[column].shift(lag)
    
    logger.info(f"Created {len(lags)} lagged features for {column}")
    return df


# ============================================================================
# DATA NORMALIZATION
# ============================================================================

def normalize_column(
    df: pd.DataFrame,
    columns: List[str],
    method: str = 'minmax',
    save_scaler: bool = False,
    scaler_path: Optional[str] = None
) -> Tuple[pd.DataFrame, Optional[Dict]]:
    """
    Normalize/standardize numerical columns.
    
    Args:
        df: DataFrame to normalize
        columns: Columns to normalize
        method: 'minmax' or 'standard'
        save_scaler: Save scaler parameters
        scaler_path: Path to save scaler
    
    Returns:
        Normalized DataFrame and scaler parameters (optional)
    """
    df = df.copy()
    scaler_params = {}
    
    for col in columns:
        if method == 'minmax':
            min_val = df[col].min()
            max_val = df[col].max()
            df[col] = (df[col] - min_val) / (max_val - min_val)
            scaler_params[col] = {'min': min_val, 'max': max_val, 'method': 'minmax'}
        
        elif method == 'standard':
            mean_val = df[col].mean()
            std_val = df[col].std()
            df[col] = (df[col] - mean_val) / std_val
            scaler_params[col] = {'mean': mean_val, 'std': std_val, 'method': 'standard'}
    
    logger.info(f"Normalized {len(columns)} columns using {method} method")
    
    if save_scaler and scaler_path:
        import json
        with open(scaler_path, 'w') as f:
            json.dump(scaler_params, f)
    
    return df, scaler_params if save_scaler else None


# ============================================================================
# DATA SPLITTING
# ============================================================================

def create_train_test_split(
    df: pd.DataFrame,
    train_ratio: float = 0.6,
    test_ratio: float = 0.2,
    temporal_split: bool = True,
    random_state: int = 42
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Split data into train, validation, and test sets.
    
    Args:
        df: DataFrame to split
        train_ratio: Training set ratio (0-1)
        test_ratio: Test set ratio (0-1)
        temporal_split: Use chronological split (for time series)
        random_state: Random seed
    
    Returns:
        Tuple of (train_df, val_df, test_df)
    """
    val_ratio = 1 - train_ratio - test_ratio
    
    if temporal_split:
        # Chronological split
        n = len(df)
        train_size = int(n * train_ratio)
        val_size = int(n * val_ratio)
        
        train_df = df[:train_size]
        val_df = df[train_size:train_size + val_size]
        test_df = df[train_size + val_size:]
    else:
        # Random split
        train_df = df.sample(frac=train_ratio, random_state=random_state)
        remaining = df.drop(train_df.index)
        val_df = remaining.sample(
            frac=val_ratio / (val_ratio + test_ratio),
            random_state=random_state
        )
        test_df = remaining.drop(val_df.index)
    
    logger.info(f"Data split - Train: {len(train_df)}, "
                f"Val: {len(val_df)}, Test: {len(test_df)}")
    
    return train_df, val_df, test_df


# ============================================================================
# EXPORT & SAVING
# ============================================================================

def save_data(
    df: pd.DataFrame,
    filepath: str,
    format: str = 'csv',
    **kwargs
) -> None:
    """
    Save DataFrame to file.
    
    Args:
        df: DataFrame to save
        filepath: Output file path
        format: 'csv', 'parquet', or 'json'
        **kwargs: Additional arguments for save function
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    
    if format == 'csv':
        df.to_csv(filepath, index=False, **kwargs)
    elif format == 'parquet':
        df.to_parquet(filepath, index=False, **kwargs)
    elif format == 'json':
        df.to_json(filepath, orient='records', **kwargs)
    
    logger.info(f"Data saved to {filepath}")


if __name__ == "__main__":
    # Example usage
    print("Data loading and processing module loaded successfully")
