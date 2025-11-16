"""
Utility Functions for Capstone Project
Provides common helper functions for data processing, logging, and configuration
"""

import os
import logging
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, Union


# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

def setup_logger(
    name: str,
    log_file: Optional[str] = None,
    level: str = "INFO"
) -> logging.Logger:
    """
    Configure and return a logger instance.
    
    Args:
        name: Logger name (typically __name__)
        log_file: Optional path to log file
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        Configured logger instance
    
    Example:
        >>> logger = setup_logger(__name__, "logs/app.log")
        >>> logger.info("Starting analysis")
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, level.upper()))
    
    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


# ============================================================================
# CONFIGURATION MANAGEMENT
# ============================================================================

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from YAML or JSON file.
    
    Args:
        config_path: Path to configuration file
    
    Returns:
        Configuration dictionary
    
    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If file format not supported
    """
    config_path = Path(config_path)
    
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        if config_path.suffix == '.yaml' or config_path.suffix == '.yml':
            config = yaml.safe_load(f)
        elif config_path.suffix == '.json':
            config = json.load(f)
        else:
            raise ValueError(f"Unsupported config format: {config_path.suffix}")
    
    return config


def save_config(config: Dict[str, Any], output_path: str) -> None:
    """
    Save configuration to YAML file.
    
    Args:
        config: Configuration dictionary
        output_path: Output file path
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)


# ============================================================================
# PATH MANAGEMENT
# ============================================================================

def get_project_root() -> Path:
    """
    Get the root directory of the project.
    
    Returns:
        Path object pointing to project root
    """
    return Path(__file__).parent.parent


def ensure_directory_exists(path: Union[str, Path]) -> Path:
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Directory path
    
    Returns:
        Path object
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_data_paths() -> Dict[str, Path]:
    """
    Get paths to all data directories.
    
    Returns:
        Dictionary with data directory paths
    """
    root = get_project_root()
    return {
        'raw': root / '02_Data' / 'Raw',
        'processed': root / '02_Data' / 'Processed',
        'external': root / '02_Data' / 'External',
        'models': root / '05_Models',
        'results': root / '06_Results',
        'notebooks': root / '03_Notebooks',
        'scripts': root / '04_Scripts',
        'docs': root / '07_Documentation',
    }


# ============================================================================
# FILE MANAGEMENT
# ============================================================================

def get_latest_file(directory: Union[str, Path], pattern: str = "*") -> Optional[Path]:
    """
    Get the most recently modified file in a directory.
    
    Args:
        directory: Directory to search
        pattern: File pattern to match (e.g., "*.csv")
    
    Returns:
        Path to latest file or None if no files found
    """
    directory = Path(directory)
    files = sorted(
        directory.glob(pattern),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )
    return files[0] if files else None


def list_files(
    directory: Union[str, Path],
    extension: str = "*",
    recursive: bool = False
) -> list:
    """
    List files in a directory with optional filtering.
    
    Args:
        directory: Directory path
        extension: File extension filter (e.g., ".csv")
        recursive: Search recursively
    
    Returns:
        List of matching file paths
    """
    directory = Path(directory)
    pattern = f"**/*{extension}" if recursive else f"*{extension}"
    return sorted(directory.glob(pattern))


# ============================================================================
# TIME & DATE UTILITIES
# ============================================================================

def get_timestamp() -> str:
    """
    Get current timestamp in standard format.
    
    Returns:
        Timestamp string (YYYY-MM-DD HH:MM:SS)
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_date_string() -> str:
    """
    Get current date string.
    
    Returns:
        Date string (YYYY-MM-DD)
    """
    return datetime.now().strftime("%Y-%m-%d")


# ============================================================================
# DATA VALIDATION
# ============================================================================

def validate_dataframe(df, required_columns: list) -> tuple[bool, list]:
    """
    Validate that a dataframe has required columns.
    
    Args:
        df: Pandas DataFrame to validate
        required_columns: List of required column names
    
    Returns:
        Tuple of (is_valid, missing_columns)
    """
    missing = [col for col in required_columns if col not in df.columns]
    return len(missing) == 0, missing


def check_data_quality(df, min_completeness: float = 0.90) -> Dict[str, Any]:
    """
    Assess data quality metrics for a dataframe.
    
    Args:
        df: Pandas DataFrame
        min_completeness: Minimum acceptable completeness ratio
    
    Returns:
        Dictionary with quality metrics
    """
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()
    completeness = (total_cells - missing_cells) / total_cells
    
    quality = {
        'rows': df.shape[0],
        'columns': df.shape[1],
        'total_cells': total_cells,
        'missing_cells': missing_cells,
        'completeness': completeness,
        'passes_quality': completeness >= min_completeness,
        'missing_by_column': df.isnull().sum().to_dict()
    }
    
    return quality


# ============================================================================
# METRICS & STATISTICS
# ============================================================================

def calculate_rmse(y_true, y_pred) -> float:
    """Calculate Root Mean Squared Error."""
    import numpy as np
    return np.sqrt(np.mean((y_true - y_pred) ** 2))


def calculate_mae(y_true, y_pred) -> float:
    """Calculate Mean Absolute Error."""
    import numpy as np
    return np.mean(np.abs(y_true - y_pred))


def calculate_mape(y_true, y_pred) -> float:
    """Calculate Mean Absolute Percentage Error."""
    import numpy as np
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


# ============================================================================
# ENVIRONMENT SETUP
# ============================================================================

def load_environment_variables(env_file: str = ".env") -> None:
    """
    Load environment variables from .env file.
    
    Args:
        env_file: Path to .env file
    """
    from dotenv import load_dotenv
    load_dotenv(env_file)


def get_env_variable(
    name: str,
    default: Optional[str] = None,
    required: bool = False
) -> Optional[str]:
    """
    Get environment variable safely.
    
    Args:
        name: Variable name
        default: Default value if not found
        required: Raise error if not found
    
    Returns:
        Environment variable value
    
    Raises:
        ValueError: If required variable not found
    """
    value = os.getenv(name, default)
    
    if required and value is None:
        raise ValueError(f"Required environment variable not found: {name}")
    
    return value


# ============================================================================
# MEMORY & PERFORMANCE
# ============================================================================

def get_memory_usage() -> Dict[str, float]:
    """
    Get current memory usage statistics.
    
    Returns:
        Dictionary with memory usage info in MB
    """
    import psutil
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    
    return {
        'rss_mb': memory_info.rss / 1024 / 1024,
        'vms_mb': memory_info.vms / 1024 / 1024,
    }


def reduce_memory_usage(df, verbose: bool = True) -> object:
    """
    Reduce dataframe memory usage by optimizing dtypes.
    
    Args:
        df: Pandas DataFrame
        verbose: Print memory reduction stats
    
    Returns:
        DataFrame with optimized dtypes
    """
    import pandas as pd
    
    initial_memory = df.memory_usage(deep=True).sum() / 1024 ** 2
    
    for col in df.columns:
        col_type = df[col].dtype
        
        if col_type != 'object':
            c_min = df[col].min()
            c_max = df[col].max()
            
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
    
    final_memory = df.memory_usage(deep=True).sum() / 1024 ** 2
    
    if verbose:
        print(f"Memory usage: {initial_memory:.2f}MB -> {final_memory:.2f}MB "
              f"({100*(1 - final_memory/initial_memory):.1f}% reduction)")
    
    return df


if __name__ == "__main__":
    # Test utilities
    logger = setup_logger("test_utils")
    logger.info("Utility functions loaded successfully")
    
    print(f"Project root: {get_project_root()}")
    print(f"Data paths: {get_data_paths()}")
    print(f"Current timestamp: {get_timestamp()}")
