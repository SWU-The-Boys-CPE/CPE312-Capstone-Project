"""
Modeling Module for Bangkok Traffic Flow Optimization Project

This module provides functions for training traffic prediction models
including LSTM, XGBoost, ARIMA, and Random Forest.

Author: Data Science Team
Date: November 2025
"""

import numpy as np
import pandas as pd
import pickle
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any, Union

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# DATA PREPARATION
# ============================================================================

def create_sequences(
    data: np.ndarray,
    sequence_length: int = 7,
    target_col_idx: int = 0
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create sequences for LSTM training.
    
    Args:
        data: Feature array of shape (n_samples, n_features)
        sequence_length: Number of time steps in each sequence
        target_col_idx: Index of target column
    
    Returns:
        Tuple of (X, y) where X has shape (n_samples, sequence_length, n_features)
    """
    X, y = [], []
    
    for i in range(sequence_length, len(data)):
        X.append(data[i-sequence_length:i])
        y.append(data[i, target_col_idx])
    
    return np.array(X), np.array(y)


def temporal_train_test_split(
    df: pd.DataFrame,
    date_col: str = 'date',
    train_ratio: float = 0.6,
    val_ratio: float = 0.2,
    test_ratio: float = 0.2
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Split data temporally for time-series modeling.
    
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
    
    logger.info(f"Split sizes - Train: {len(train_df)}, Val: {len(val_df)}, Test: {len(test_df)}")
    
    return train_df, val_df, test_df


# ============================================================================
# LSTM MODEL
# ============================================================================

def build_lstm_model(
    input_shape: Tuple[int, int],
    units_layer1: int = 64,
    units_layer2: int = 32,
    dropout: float = 0.2,
    learning_rate: float = 0.001
) -> Any:
    """
    Build LSTM model architecture.
    
    Args:
        input_shape: Shape of input (sequence_length, n_features)
        units_layer1: Units in first LSTM layer
        units_layer2: Units in second LSTM layer
        dropout: Dropout rate
        learning_rate: Learning rate for optimizer
    
    Returns:
        Compiled Keras model
    """
    try:
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import LSTM, Dense, Dropout
        from tensorflow.keras.optimizers import Adam
    except ImportError:
        logger.error("TensorFlow not installed. Install with: pip install tensorflow")
        raise
    
    model = Sequential([
        LSTM(units_layer1, return_sequences=True, input_shape=input_shape),
        Dropout(dropout),
        LSTM(units_layer2),
        Dropout(dropout),
        Dense(1)
    ])
    
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])
    
    logger.info(f"Built LSTM model with input shape {input_shape}")
    return model


def train_lstm_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    config: Optional[Dict] = None,
    save_path: Optional[str] = None
) -> Tuple[Any, Dict]:
    """
    Train LSTM model for traffic prediction.
    
    Args:
        X_train: Training features
        y_train: Training targets
        X_val: Validation features
        y_val: Validation targets
        config: Model configuration dictionary
        save_path: Path to save trained model
    
    Returns:
        Tuple of (trained_model, training_history)
    """
    try:
        from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
    except ImportError:
        logger.error("TensorFlow not installed")
        raise
    
    # Default configuration
    default_config = {
        'units_layer1': 64,
        'units_layer2': 32,
        'dropout': 0.2,
        'learning_rate': 0.001,
        'epochs': 100,
        'batch_size': 32
    }
    
    if config:
        default_config.update(config)
    config = default_config
    
    # Build model
    input_shape = (X_train.shape[1], X_train.shape[2])
    model = build_lstm_model(
        input_shape=input_shape,
        units_layer1=config['units_layer1'],
        units_layer2=config['units_layer2'],
        dropout=config['dropout'],
        learning_rate=config['learning_rate']
    )
    
    # Callbacks
    callbacks = [
        EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True,
            verbose=1
        ),
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5,
            verbose=1
        )
    ]
    
    # Train
    logger.info("Starting LSTM training...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=config['epochs'],
        batch_size=config['batch_size'],
        callbacks=callbacks,
        verbose=1
    )
    
    # Save model
    if save_path:
        model.save(save_path)
        logger.info(f"Model saved to {save_path}")
    
    return model, history.history


# ============================================================================
# XGBOOST MODEL
# ============================================================================

def train_xgboost_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: Optional[np.ndarray] = None,
    y_val: Optional[np.ndarray] = None,
    config: Optional[Dict] = None,
    save_path: Optional[str] = None
) -> Tuple[Any, Dict]:
    """
    Train XGBoost model for traffic prediction.
    
    Args:
        X_train: Training features
        y_train: Training targets
        X_val: Validation features (optional)
        y_val: Validation targets (optional)
        config: Model configuration dictionary
        save_path: Path to save trained model
    
    Returns:
        Tuple of (trained_model, training_info)
    """
    try:
        import xgboost as xgb
    except ImportError:
        logger.error("XGBoost not installed. Install with: pip install xgboost")
        raise
    
    # Default configuration
    default_config = {
        'n_estimators': 100,
        'max_depth': 6,
        'learning_rate': 0.1,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'min_child_weight': 1,
        'gamma': 0,
        'reg_alpha': 0,
        'reg_lambda': 1,
        'random_state': 42,
        'n_jobs': -1
    }
    
    if config:
        default_config.update(config)
    config = default_config
    
    # Create model
    model = xgb.XGBRegressor(
        n_estimators=config['n_estimators'],
        max_depth=config['max_depth'],
        learning_rate=config['learning_rate'],
        subsample=config['subsample'],
        colsample_bytree=config['colsample_bytree'],
        min_child_weight=config['min_child_weight'],
        gamma=config['gamma'],
        reg_alpha=config['reg_alpha'],
        reg_lambda=config['reg_lambda'],
        random_state=config['random_state'],
        n_jobs=config['n_jobs'],
        objective='reg:squarederror'
    )
    
    # Train
    logger.info("Starting XGBoost training...")
    
    if X_val is not None and y_val is not None:
        model.fit(
            X_train, y_train,
            eval_set=[(X_val, y_val)],
            verbose=True
        )
    else:
        model.fit(X_train, y_train)
    
    # Get feature importance
    importance = model.feature_importances_
    
    # Save model
    if save_path:
        with open(save_path, 'wb') as f:
            pickle.dump(model, f)
        logger.info(f"Model saved to {save_path}")
    
    training_info = {
        'feature_importance': importance,
        'config': config
    }
    
    return model, training_info


# ============================================================================
# ARIMA MODEL
# ============================================================================

def train_arima_model(
    y_train: np.ndarray,
    order: Tuple[int, int, int] = (1, 1, 1),
    seasonal_order: Optional[Tuple[int, int, int, int]] = None,
    save_path: Optional[str] = None
) -> Tuple[Any, Dict]:
    """
    Train ARIMA/SARIMA model for traffic prediction.
    
    Args:
        y_train: Training target series
        order: ARIMA order (p, d, q)
        seasonal_order: Seasonal order (P, D, Q, s) or None
        save_path: Path to save trained model
    
    Returns:
        Tuple of (trained_model, training_info)
    """
    try:
        from statsmodels.tsa.arima.model import ARIMA
        from statsmodels.tsa.statespace.sarimax import SARIMAX
    except ImportError:
        logger.error("Statsmodels not installed. Install with: pip install statsmodels")
        raise
    
    logger.info(f"Training ARIMA model with order={order}, seasonal={seasonal_order}")
    
    if seasonal_order:
        # Use SARIMAX for seasonal model
        model = SARIMAX(
            y_train,
            order=order,
            seasonal_order=seasonal_order,
            enforce_stationarity=True,
            enforce_invertibility=True
        )
    else:
        # Use regular ARIMA
        model = ARIMA(y_train, order=order)
    
    # Fit model
    fitted_model = model.fit()
    
    logger.info(f"ARIMA AIC: {fitted_model.aic:.2f}")
    
    # Save model
    if save_path:
        with open(save_path, 'wb') as f:
            pickle.dump(fitted_model, f)
        logger.info(f"Model saved to {save_path}")
    
    training_info = {
        'aic': fitted_model.aic,
        'bic': fitted_model.bic,
        'order': order,
        'seasonal_order': seasonal_order
    }
    
    return fitted_model, training_info


# ============================================================================
# RANDOM FOREST MODEL
# ============================================================================

def train_random_forest_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    config: Optional[Dict] = None,
    save_path: Optional[str] = None
) -> Tuple[Any, Dict]:
    """
    Train Random Forest model for traffic prediction.
    
    Args:
        X_train: Training features
        y_train: Training targets
        config: Model configuration dictionary
        save_path: Path to save trained model
    
    Returns:
        Tuple of (trained_model, training_info)
    """
    from sklearn.ensemble import RandomForestRegressor
    
    # Default configuration
    default_config = {
        'n_estimators': 100,
        'max_depth': 15,
        'min_samples_split': 5,
        'min_samples_leaf': 2,
        'max_features': 'sqrt',
        'bootstrap': True,
        'random_state': 42,
        'n_jobs': -1
    }
    
    if config:
        default_config.update(config)
    config = default_config
    
    # Create and train model
    logger.info("Starting Random Forest training...")
    model = RandomForestRegressor(**config)
    model.fit(X_train, y_train)
    
    # Get feature importance
    importance = model.feature_importances_
    
    # Save model
    if save_path:
        with open(save_path, 'wb') as f:
            pickle.dump(model, f)
        logger.info(f"Model saved to {save_path}")
    
    training_info = {
        'feature_importance': importance,
        'config': config
    }
    
    return model, training_info


# ============================================================================
# BASELINE MODELS
# ============================================================================

def naive_forecast(y_true: np.ndarray) -> np.ndarray:
    """
    Naive forecast: predict tomorrow = today.
    
    Args:
        y_true: Actual values
    
    Returns:
        Predictions (shifted by 1)
    """
    return np.concatenate([[y_true[0]], y_true[:-1]])


def mean_forecast(y_train: np.ndarray, n_predict: int) -> np.ndarray:
    """
    Mean forecast: predict = historical mean.
    
    Args:
        y_train: Training values
        n_predict: Number of predictions
    
    Returns:
        Array of mean predictions
    """
    return np.full(n_predict, np.mean(y_train))


def seasonal_naive_forecast(
    y_true: np.ndarray,
    season_length: int = 7
) -> np.ndarray:
    """
    Seasonal naive: predict = same day last week.
    
    Args:
        y_true: Actual values
        season_length: Season length (7 for weekly)
    
    Returns:
        Predictions
    """
    predictions = np.zeros(len(y_true))
    predictions[:season_length] = y_true[:season_length]
    predictions[season_length:] = y_true[:-season_length]
    return predictions


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    logger.info("Modeling module loaded successfully")
    
    # Example usage
    print("""
    Example Usage:
    --------------
    from modeling import train_xgboost_model, train_lstm_model
    
    # Train XGBoost
    model, info = train_xgboost_model(X_train, y_train, X_val, y_val)
    
    # Train LSTM
    model, history = train_lstm_model(X_train, y_train, X_val, y_val)
    """)
