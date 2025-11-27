"""
Evaluation Module for Bangkok Traffic Flow Optimization Project

This module provides functions for evaluating model performance,
including metrics calculation, cross-validation, and comparison.

Author: Data Science Team
Date: November 2025
"""

import numpy as np
import pandas as pd
import logging
from typing import Dict, List, Tuple, Optional, Any, Union
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# EVALUATION METRICS
# ============================================================================

def calculate_mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate Mean Absolute Error.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        MAE value
    """
    return mean_absolute_error(y_true, y_pred)


def calculate_rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate Root Mean Squared Error.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        RMSE value
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))


def calculate_mape(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate Mean Absolute Percentage Error.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        MAPE value (percentage)
    
    Note:
        Returns inf if any y_true values are 0
    """
    # Avoid division by zero
    mask = y_true != 0
    if not np.any(mask):
        logger.warning("All true values are zero, MAPE is undefined")
        return np.inf
    
    return np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100


def calculate_r2(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate R-squared (Coefficient of Determination).
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        R² value
    """
    return r2_score(y_true, y_pred)


def calculate_bias(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate prediction bias (mean error).
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        Bias value (positive = over-prediction)
    """
    return np.mean(y_pred - y_true)


def calculate_directional_accuracy(
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> float:
    """
    Calculate directional accuracy (% correct direction).
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        Directional accuracy (0-100%)
    """
    if len(y_true) < 2:
        return 0.0
    
    true_direction = np.sign(np.diff(y_true))
    pred_direction = np.sign(np.diff(y_pred))
    
    correct = np.sum(true_direction == pred_direction)
    total = len(true_direction)
    
    return (correct / total) * 100


def calculate_all_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> Dict[str, float]:
    """
    Calculate all evaluation metrics.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        Dictionary with all metrics
    """
    metrics = {
        'MAE': calculate_mae(y_true, y_pred),
        'RMSE': calculate_rmse(y_true, y_pred),
        'MAPE': calculate_mape(y_true, y_pred),
        'R2': calculate_r2(y_true, y_pred),
        'Bias': calculate_bias(y_true, y_pred),
        'Directional_Accuracy': calculate_directional_accuracy(y_true, y_pred)
    }
    
    logger.info(f"Metrics calculated - RMSE: {metrics['RMSE']:.4f}, R²: {metrics['R2']:.4f}")
    
    return metrics


# ============================================================================
# CROSS-VALIDATION
# ============================================================================

def time_series_cv_split(
    n_samples: int,
    n_splits: int = 5,
    min_train_size: int = 100
) -> List[Tuple[np.ndarray, np.ndarray]]:
    """
    Generate time-series cross-validation splits.
    
    Args:
        n_samples: Total number of samples
        n_splits: Number of CV splits
        min_train_size: Minimum training size
    
    Returns:
        List of (train_idx, val_idx) tuples
    """
    splits = []
    fold_size = (n_samples - min_train_size) // n_splits
    
    for i in range(n_splits):
        train_end = min_train_size + i * fold_size
        val_end = min(train_end + fold_size, n_samples)
        
        train_idx = np.arange(0, train_end)
        val_idx = np.arange(train_end, val_end)
        
        splits.append((train_idx, val_idx))
    
    return splits


def cross_validate_model(
    model_class: Any,
    X: np.ndarray,
    y: np.ndarray,
    n_splits: int = 5,
    model_params: Optional[Dict] = None
) -> Dict[str, Any]:
    """
    Perform time-series cross-validation.
    
    Args:
        model_class: Model class (sklearn-compatible)
        X: Features
        y: Targets
        n_splits: Number of CV folds
        model_params: Model parameters
    
    Returns:
        Dictionary with CV results
    """
    if model_params is None:
        model_params = {}
    
    splits = time_series_cv_split(len(y), n_splits)
    
    fold_results = []
    
    for i, (train_idx, val_idx) in enumerate(splits):
        X_train, X_val = X[train_idx], X[val_idx]
        y_train, y_val = y[train_idx], y[val_idx]
        
        # Train model
        model = model_class(**model_params)
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_val)
        
        # Calculate metrics
        metrics = calculate_all_metrics(y_val, y_pred)
        metrics['fold'] = i + 1
        fold_results.append(metrics)
        
        logger.info(f"Fold {i+1}/{n_splits} - RMSE: {metrics['RMSE']:.4f}")
    
    # Aggregate results
    results_df = pd.DataFrame(fold_results)
    
    summary = {
        'fold_results': fold_results,
        'mean_RMSE': results_df['RMSE'].mean(),
        'std_RMSE': results_df['RMSE'].std(),
        'mean_MAE': results_df['MAE'].mean(),
        'std_MAE': results_df['MAE'].std(),
        'mean_R2': results_df['R2'].mean(),
        'std_R2': results_df['R2'].std()
    }
    
    logger.info(f"CV Complete - Mean RMSE: {summary['mean_RMSE']:.4f} ± {summary['std_RMSE']:.4f}")
    
    return summary


# ============================================================================
# MODEL COMPARISON
# ============================================================================

def compare_models(
    models: Dict[str, Any],
    X_test: np.ndarray,
    y_test: np.ndarray
) -> pd.DataFrame:
    """
    Compare multiple models on test set.
    
    Args:
        models: Dictionary of {model_name: model_object}
        X_test: Test features
        y_test: Test targets
    
    Returns:
        DataFrame with comparison results
    """
    results = []
    
    for name, model in models.items():
        y_pred = model.predict(X_test)
        metrics = calculate_all_metrics(y_test, y_pred)
        metrics['Model'] = name
        results.append(metrics)
        
        logger.info(f"{name}: RMSE={metrics['RMSE']:.4f}, R²={metrics['R2']:.4f}")
    
    comparison_df = pd.DataFrame(results)
    comparison_df = comparison_df.set_index('Model')
    
    # Rank by RMSE (lower is better)
    comparison_df['RMSE_Rank'] = comparison_df['RMSE'].rank()
    
    return comparison_df.sort_values('RMSE')


def calculate_improvement_over_baseline(
    model_metrics: Dict[str, float],
    baseline_metrics: Dict[str, float]
) -> Dict[str, float]:
    """
    Calculate improvement over baseline.
    
    Args:
        model_metrics: Metrics from trained model
        baseline_metrics: Metrics from baseline
    
    Returns:
        Dictionary with improvement percentages
    """
    improvements = {}
    
    for metric in ['MAE', 'RMSE', 'MAPE']:
        if metric in model_metrics and metric in baseline_metrics:
            baseline_val = baseline_metrics[metric]
            model_val = model_metrics[metric]
            
            if baseline_val != 0:
                improvement = ((baseline_val - model_val) / baseline_val) * 100
                improvements[f'{metric}_improvement_%'] = improvement
    
    if 'R2' in model_metrics and 'R2' in baseline_metrics:
        improvements['R2_improvement'] = model_metrics['R2'] - baseline_metrics['R2']
    
    return improvements


# ============================================================================
# EVALUATION REPORTING
# ============================================================================

def generate_evaluation_report(
    model_name: str,
    y_true: np.ndarray,
    y_pred: np.ndarray,
    output_path: Optional[str] = None
) -> str:
    """
    Generate detailed evaluation report.
    
    Args:
        model_name: Name of the model
        y_true: Actual values
        y_pred: Predicted values
        output_path: Path to save report (optional)
    
    Returns:
        Report as string
    """
    metrics = calculate_all_metrics(y_true, y_pred)
    
    report = f"""
================================================================================
MODEL EVALUATION REPORT
================================================================================

Model: {model_name}
Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

--------------------------------------------------------------------------------
PERFORMANCE METRICS
--------------------------------------------------------------------------------

| Metric                | Value          | Target    | Status  |
|-----------------------|----------------|-----------|---------|
| MAE                   | {metrics['MAE']:.4f}         | < 5.0     | {'✅' if metrics['MAE'] < 5.0 else '⚠️'} |
| RMSE                  | {metrics['RMSE']:.4f}        | < 8.0     | {'✅' if metrics['RMSE'] < 8.0 else '⚠️'} |
| MAPE                  | {metrics['MAPE']:.2f}%       | < 15%     | {'✅' if metrics['MAPE'] < 15 else '⚠️'} |
| R²                    | {metrics['R2']:.4f}         | > 0.75    | {'✅' if metrics['R2'] > 0.75 else '⚠️'} |
| Directional Accuracy  | {metrics['Directional_Accuracy']:.2f}%   | > 70%     | {'✅' if metrics['Directional_Accuracy'] > 70 else '⚠️'} |
| Bias                  | {metrics['Bias']:.4f}        | ≈ 0       | {'✅' if abs(metrics['Bias']) < 1 else '⚠️'} |

--------------------------------------------------------------------------------
PREDICTION STATISTICS
--------------------------------------------------------------------------------

Actual Values:
  - Mean: {np.mean(y_true):.4f}
  - Std:  {np.std(y_true):.4f}
  - Min:  {np.min(y_true):.4f}
  - Max:  {np.max(y_true):.4f}

Predicted Values:
  - Mean: {np.mean(y_pred):.4f}
  - Std:  {np.std(y_pred):.4f}
  - Min:  {np.min(y_pred):.4f}
  - Max:  {np.max(y_pred):.4f}

Error Distribution:
  - Mean Error: {np.mean(y_pred - y_true):.4f}
  - Error Std:  {np.std(y_pred - y_true):.4f}
  - Max Overestimate: {np.max(y_pred - y_true):.4f}
  - Max Underestimate: {np.min(y_pred - y_true):.4f}

================================================================================
"""
    
    if output_path:
        with open(output_path, 'w') as f:
            f.write(report)
        logger.info(f"Report saved to {output_path}")
    
    return report


def print_metrics_table(results: Dict[str, Dict[str, float]]) -> None:
    """
    Print formatted metrics table.
    
    Args:
        results: Dictionary of {model_name: metrics_dict}
    """
    df = pd.DataFrame(results).T
    df = df.round(4)
    print("\n" + "=" * 70)
    print("MODEL COMPARISON")
    print("=" * 70)
    print(df.to_string())
    print("=" * 70 + "\n")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    logger.info("Evaluation module loaded successfully")
    
    # Example usage
    print("""
    Example Usage:
    --------------
    from evaluation import calculate_all_metrics, compare_models
    
    # Calculate metrics
    metrics = calculate_all_metrics(y_true, y_pred)
    print(f"RMSE: {metrics['RMSE']:.4f}")
    
    # Compare models
    comparison = compare_models({'LSTM': lstm, 'XGBoost': xgb}, X_test, y_test)
    print(comparison)
    """)
