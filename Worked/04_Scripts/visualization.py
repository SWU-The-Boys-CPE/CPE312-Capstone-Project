"""
Visualization Module for Traffic Flow Optimization Project

Provides functions for creating professional visualizations of traffic data,
accident patterns, weather impacts, and spatial analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List, Tuple, Dict
import logging

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12

logger = logging.getLogger(__name__)


# ============================================================================
# TRAFFIC VISUALIZATIONS
# ============================================================================

def plot_congestion_distribution(
    df: pd.DataFrame,
    congestion_col: str = 'congestion_index',
    title: str = 'Bangkok Traffic Congestion Index Distribution',
    save_path: Optional[str] = None
) -> None:
    """
    Plot distribution of congestion index.
    
    Args:
        df: DataFrame with congestion data
        congestion_col: Name of congestion column
        title: Plot title
        save_path: Path to save figure (optional)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Histogram
    ax1.hist(df[congestion_col].dropna(), bins=50, edgecolor='black', alpha=0.7)
    ax1.set_xlabel('Congestion Index')
    ax1.set_ylabel('Frequency')
    ax1.set_title(f'{title} - Histogram')
    ax1.axvline(df[congestion_col].mean(), color='red', linestyle='--', 
                linewidth=2, label=f'Mean: {df[congestion_col].mean():.2f}')
    ax1.axvline(df[congestion_col].median(), color='green', linestyle='--',
                linewidth=2, label=f'Median: {df[congestion_col].median():.2f}')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Box plot
    ax2.boxplot(df[congestion_col].dropna(), vert=True)
    ax2.set_ylabel('Congestion Index')
    ax2.set_title(f'{title} - Box Plot')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved plot to {save_path}")
    
    plt.show()


def plot_temporal_heatmap(
    df: pd.DataFrame,
    datetime_col: str = 'date',
    value_col: str = 'congestion_index',
    title: str = 'Traffic Congestion by Hour and Day of Week',
    save_path: Optional[str] = None
) -> None:
    """
    Create heatmap showing congestion by hour and day of week.
    
    Args:
        df: DataFrame with temporal data
        datetime_col: Datetime column name
        value_col: Value column to aggregate
        title: Plot title
        save_path: Path to save figure (optional)
    """
    df = df.copy()
    
    # Extract hour and day of week if not present
    if 'hour' not in df.columns and datetime_col in df.columns:
        df['hour'] = pd.to_datetime(df[datetime_col]).dt.hour
    if 'dayofweek' not in df.columns and datetime_col in df.columns:
        df['dayofweek'] = pd.to_datetime(df[datetime_col]).dt.dayofweek
    
    # Pivot table for heatmap
    pivot_table = df.pivot_table(
        values=value_col,
        index='hour',
        columns='dayofweek',
        aggfunc='mean'
    )
    
    # Day names
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    pivot_table.columns = [day_names[i] for i in pivot_table.columns]
    
    # Create heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(
        pivot_table,
        annot=True,
        fmt='.1f',
        cmap='YlOrRd',
        cbar_kws={'label': 'Average Congestion Index'},
        linewidths=0.5
    )
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=14)
    plt.ylabel('Hour of Day', fontsize=14)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved heatmap to {save_path}")
    
    plt.show()


def plot_time_series(
    df: pd.DataFrame,
    datetime_col: str = 'date',
    value_col: str = 'congestion_index',
    title: str = 'Traffic Congestion Time Series (2019-2025)',
    rolling_window: int = 7,
    save_path: Optional[str] = None
) -> None:
    """
    Plot time series with rolling average.
    
    Args:
        df: DataFrame with time series data
        datetime_col: Datetime column name
        value_col: Value column to plot
        title: Plot title
        rolling_window: Window size for rolling average
        save_path: Path to save figure (optional)
    """
    df = df.copy()
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    df = df.sort_values(datetime_col)
    
    # Calculate rolling average
    df['rolling_avg'] = df[value_col].rolling(window=rolling_window).mean()
    
    plt.figure(figsize=(16, 8))
    
    # Plot raw data
    plt.plot(df[datetime_col], df[value_col], alpha=0.3, color='gray', label='Daily Values')
    
    # Plot rolling average
    plt.plot(df[datetime_col], df['rolling_avg'], color='red', linewidth=2,
             label=f'{rolling_window}-Day Moving Average')
    
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Congestion Index', fontsize=14)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved time series plot to {save_path}")
    
    plt.show()


def plot_seasonal_patterns(
    df: pd.DataFrame,
    datetime_col: str = 'date',
    value_col: str = 'congestion_index',
    title: str = 'Seasonal Traffic Patterns',
    save_path: Optional[str] = None
) -> None:
    """
    Plot seasonal patterns (monthly/quarterly).
    
    Args:
        df: DataFrame with temporal data
        datetime_col: Datetime column name
        value_col: Value column to aggregate
        title: Plot title
        save_path: Path to save figure (optional)
    """
    df = df.copy()
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    df['month'] = df[datetime_col].dt.month
    df['month_name'] = df[datetime_col].dt.month_name()
    
    # Aggregate by month
    monthly_avg = df.groupby('month_name')[value_col].mean().reindex([
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    
    plt.figure(figsize=(14, 8))
    bars = plt.bar(range(12), monthly_avg.values, edgecolor='black', alpha=0.7)
    
    # Color by season (Thailand)
    colors = ['#87CEEB'] * 2 + ['#FFD700'] * 3 + ['#90EE90'] * 5 + ['#87CEEB'] * 2
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.xlabel('Month', fontsize=14)
    plt.ylabel(f'Average {value_col}', fontsize=14)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xticks(range(12), monthly_avg.index, rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    # Add season labels
    plt.text(1, monthly_avg.max() * 0.95, 'Cool Season', fontsize=12, ha='center')
    plt.text(4, monthly_avg.max() * 0.95, 'Dry Season', fontsize=12, ha='center')
    plt.text(8, monthly_avg.max() * 0.95, 'Rainy Season', fontsize=12, ha='center')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved seasonal plot to {save_path}")
    
    plt.show()


def plot_weekday_weekend_comparison(
    df: pd.DataFrame,
    datetime_col: str = 'date',
    value_col: str = 'congestion_index',
    title: str = 'Weekday vs Weekend Traffic Patterns',
    save_path: Optional[str] = None
) -> None:
    """
    Compare weekday vs weekend traffic patterns.
    
    Args:
        df: DataFrame with temporal data
        datetime_col: Datetime column name
        value_col: Value column to compare
        title: Plot title
        save_path: Path to save figure (optional)
    """
    df = df.copy()
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    
    if 'is_weekend' not in df.columns:
        df['is_weekend'] = df[datetime_col].dt.dayofweek.isin([5, 6])
    
    if 'hour' not in df.columns:
        df['hour'] = df[datetime_col].dt.hour
    
    # Aggregate by hour for weekday and weekend
    weekday_pattern = df[~df['is_weekend']].groupby('hour')[value_col].mean()
    weekend_pattern = df[df['is_weekend']].groupby('hour')[value_col].mean()
    
    plt.figure(figsize=(14, 8))
    plt.plot(weekday_pattern.index, weekday_pattern.values, 
             marker='o', linewidth=2, label='Weekday', color='blue')
    plt.plot(weekend_pattern.index, weekend_pattern.values,
             marker='s', linewidth=2, label='Weekend', color='orange')
    
    plt.xlabel('Hour of Day', fontsize=14)
    plt.ylabel(f'Average {value_col}', fontsize=14)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(range(24))
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved weekday-weekend comparison to {save_path}")
    
    plt.show()


# ============================================================================
# CORRELATION & RELATIONSHIP VISUALIZATIONS
# ============================================================================

def plot_correlation_matrix(
    df: pd.DataFrame,
    features: Optional[List[str]] = None,
    title: str = 'Feature Correlation Matrix',
    save_path: Optional[str] = None
) -> None:
    """
    Plot correlation matrix heatmap.
    
    Args:
        df: DataFrame with numerical features
        features: List of features to include (optional, uses all numeric if None)
        title: Plot title
        save_path: Path to save figure (optional)
    """
    if features is None:
        features = df.select_dtypes(include=[np.number]).columns.tolist()
    
    correlation_matrix = df[features].corr()
    
    plt.figure(figsize=(14, 12))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt='.2f',
        cmap='coolwarm',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={'label': 'Correlation Coefficient'}
    )
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved correlation matrix to {save_path}")
    
    plt.show()


def plot_scatter_with_regression(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: Optional[str] = None,
    save_path: Optional[str] = None
) -> None:
    """
    Plot scatter plot with regression line.
    
    Args:
        df: DataFrame
        x_col: X-axis column name
        y_col: Y-axis column name
        title: Plot title (optional)
        save_path: Path to save figure (optional)
    """
    if title is None:
        title = f'{y_col} vs {x_col}'
    
    plt.figure(figsize=(12, 8))
    
    # Scatter plot
    plt.scatter(df[x_col], df[y_col], alpha=0.5, edgecolors='black', linewidth=0.5)
    
    # Regression line
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df[x_col].dropna(), df[y_col].dropna()
    )
    line = slope * df[x_col] + intercept
    plt.plot(df[x_col], line, 'r-', linewidth=2,
             label=f'y = {slope:.2f}x + {intercept:.2f}\nR² = {r_value**2:.3f}')
    
    plt.xlabel(x_col, fontsize=14)
    plt.ylabel(y_col, fontsize=14)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved scatter plot to {save_path}")
    
    plt.show()


# ============================================================================
# ACCIDENT & WEATHER VISUALIZATIONS
# ============================================================================

def plot_weather_impact(
    df: pd.DataFrame,
    weather_col: str = 'weather_condition',
    value_col: str = 'congestion_index',
    title: str = 'Traffic Congestion by Weather Condition',
    save_path: Optional[str] = None
) -> None:
    """
    Plot box plots showing impact of weather on traffic/accidents.
    
    Args:
        df: DataFrame
        weather_col: Weather condition column name
        value_col: Value column to analyze
        title: Plot title
        save_path: Path to save figure (optional)
    """
    plt.figure(figsize=(14, 8))
    
    # Sort by median for better visualization
    order = df.groupby(weather_col)[value_col].median().sort_values().index
    
    sns.boxplot(data=df, x=weather_col, y=value_col, order=order, palette='Set2')
    plt.xlabel('Weather Condition', fontsize=14)
    plt.ylabel(value_col, fontsize=14)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved weather impact plot to {save_path}")
    
    plt.show()


def plot_accident_severity_distribution(
    df: pd.DataFrame,
    severity_col: str = 'severity',
    title: str = 'Accident Severity Distribution',
    save_path: Optional[str] = None
) -> None:
    """
    Plot accident severity distribution.
    
    Args:
        df: DataFrame with accident data
        severity_col: Severity column name
        title: Plot title
        save_path: Path to save figure (optional)
    """
    severity_counts = df[severity_col].value_counts().sort_index()
    
    plt.figure(figsize=(12, 8))
    bars = plt.bar(severity_counts.index, severity_counts.values, 
                   edgecolor='black', alpha=0.7)
    
    # Color code by severity
    colors = ['yellow', 'orange', 'red', 'darkred'][:len(bars)]
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.xlabel('Severity Level', fontsize=14)
    plt.ylabel('Number of Accidents', fontsize=14)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, (idx, val) in enumerate(severity_counts.items()):
        plt.text(i, val, f'{val:,}', ha='center', va='bottom', fontsize=12)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved severity distribution to {save_path}")
    
    plt.show()


# ============================================================================
# MODEL PERFORMANCE VISUALIZATIONS
# ============================================================================

def plot_predictions_vs_actual(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    title: str = 'Predictions vs Actual Values',
    save_path: Optional[str] = None
) -> None:
    """
    Plot predictions vs actual values.
    
    Args:
        y_true: True values
        y_pred: Predicted values
        title: Plot title
        save_path: Path to save figure (optional)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Scatter plot
    ax1.scatter(y_true, y_pred, alpha=0.5, edgecolors='black', linewidth=0.5)
    
    # Perfect prediction line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    ax1.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction')
    
    ax1.set_xlabel('Actual Values', fontsize=14)
    ax1.set_ylabel('Predicted Values', fontsize=14)
    ax1.set_title(f'{title} - Scatter Plot', fontsize=14)
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Residual plot
    residuals = y_true - y_pred
    ax2.scatter(y_pred, residuals, alpha=0.5, edgecolors='black', linewidth=0.5)
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=2)
    ax2.set_xlabel('Predicted Values', fontsize=14)
    ax2.set_ylabel('Residuals', fontsize=14)
    ax2.set_title(f'{title} - Residual Plot', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved predictions plot to {save_path}")
    
    plt.show()


def plot_feature_importance(
    feature_names: List[str],
    importance_scores: np.ndarray,
    title: str = 'Feature Importance',
    top_n: int = 15,
    save_path: Optional[str] = None
) -> None:
    """
    Plot feature importance.
    
    Args:
        feature_names: List of feature names
        importance_scores: Importance scores
        title: Plot title
        top_n: Number of top features to show
        save_path: Path to save figure (optional)
    """
    # Sort by importance
    indices = np.argsort(importance_scores)[-top_n:]
    
    plt.figure(figsize=(12, 10))
    plt.barh(range(len(indices)), importance_scores[indices], align='center', alpha=0.7, edgecolor='black')
    plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
    plt.xlabel('Importance Score', fontsize=14)
    plt.ylabel('Features', fontsize=14)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved feature importance plot to {save_path}")
    
    plt.show()


if __name__ == "__main__":
    logger.info("Visualization module loaded successfully")
