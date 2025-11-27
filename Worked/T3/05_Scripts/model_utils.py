"""
Model Utilities Module for Bangkok Traffic Flow Optimization Project

This module provides utility functions for model saving, loading,
and general model management.

Author: Data Science Team
Date: November 2025
"""

import numpy as np
import pandas as pd
import pickle
import json
import yaml
import logging
from pathlib import Path
from typing import Dict, Any, Optional, Union
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# MODEL SAVING AND LOADING
# ============================================================================

def save_model(
    model: Any,
    filepath: str,
    model_type: str = 'sklearn'
) -> None:
    """
    Save a trained model to file.
    
    Args:
        model: Trained model object
        filepath: Output file path
        model_type: Type of model ('sklearn', 'keras', 'pytorch')
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    if model_type == 'keras':
        # Save Keras model
        model.save(str(filepath))
        logger.info(f"Keras model saved to {filepath}")
    
    elif model_type in ['sklearn', 'xgboost', 'statsmodels']:
        # Save with pickle
        with open(filepath, 'wb') as f:
            pickle.dump(model, f)
        logger.info(f"Model saved to {filepath}")
    
    else:
        raise ValueError(f"Unknown model type: {model_type}")


def load_model(
    filepath: str,
    model_type: str = 'sklearn'
) -> Any:
    """
    Load a trained model from file.
    
    Args:
        filepath: Model file path
        model_type: Type of model ('sklearn', 'keras', 'pytorch')
    
    Returns:
        Loaded model object
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"Model file not found: {filepath}")
    
    if model_type == 'keras':
        from tensorflow.keras.models import load_model as keras_load
        model = keras_load(str(filepath))
        logger.info(f"Keras model loaded from {filepath}")
    
    elif model_type in ['sklearn', 'xgboost', 'statsmodels']:
        with open(filepath, 'rb') as f:
            model = pickle.load(f)
        logger.info(f"Model loaded from {filepath}")
    
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    
    return model


# ============================================================================
# CONFIGURATION MANAGEMENT
# ============================================================================

def save_config(
    config: Dict[str, Any],
    filepath: str
) -> None:
    """
    Save configuration to YAML file.
    
    Args:
        config: Configuration dictionary
        filepath: Output file path
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    logger.info(f"Config saved to {filepath}")


def load_config(filepath: str) -> Dict[str, Any]:
    """
    Load configuration from YAML file.
    
    Args:
        filepath: Config file path
    
    Returns:
        Configuration dictionary
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"Config file not found: {filepath}")
    
    with open(filepath, 'r') as f:
        config = yaml.safe_load(f)
    
    return config


# ============================================================================
# TRAINING HISTORY
# ============================================================================

def save_training_history(
    history: Dict[str, Any],
    filepath: str,
    model_name: str
) -> None:
    """
    Save training history to file.
    
    Args:
        history: Training history dictionary
        filepath: Output file path
        model_name: Name of the model
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Add metadata
    record = {
        'model_name': model_name,
        'timestamp': datetime.now().isoformat(),
        'history': history
    }
    
    with open(filepath, 'w') as f:
        json.dump(record, f, indent=2, default=str)
    
    logger.info(f"Training history saved to {filepath}")


def load_training_history(filepath: str) -> Dict[str, Any]:
    """
    Load training history from file.
    
    Args:
        filepath: History file path
    
    Returns:
        Training history dictionary
    """
    with open(filepath, 'r') as f:
        return json.load(f)


# ============================================================================
# MODEL METADATA
# ============================================================================

def create_model_card(
    model_name: str,
    model_type: str,
    metrics: Dict[str, float],
    hyperparameters: Dict[str, Any],
    training_data_info: Dict[str, Any],
    output_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a model card with metadata.
    
    Args:
        model_name: Name of the model
        model_type: Type of model
        metrics: Evaluation metrics
        hyperparameters: Model hyperparameters
        training_data_info: Information about training data
        output_path: Path to save model card
    
    Returns:
        Model card dictionary
    """
    model_card = {
        'model_name': model_name,
        'model_type': model_type,
        'created_at': datetime.now().isoformat(),
        'version': '1.0.0',
        'metrics': metrics,
        'hyperparameters': hyperparameters,
        'training_data': training_data_info,
        'limitations': [],
        'intended_use': 'Traffic congestion prediction for Bangkok',
        'ethical_considerations': 'Model should not be used for individual tracking'
    }
    
    if output_path:
        with open(output_path, 'w') as f:
            yaml.dump(model_card, f, default_flow_style=False)
        logger.info(f"Model card saved to {output_path}")
    
    return model_card


# ============================================================================
# REPRODUCIBILITY
# ============================================================================

def set_random_seeds(seed: int = 42) -> None:
    """
    Set random seeds for reproducibility.
    
    Args:
        seed: Random seed value
    """
    import random
    
    random.seed(seed)
    np.random.seed(seed)
    
    try:
        import tensorflow as tf
        tf.random.set_seed(seed)
    except ImportError:
        pass
    
    logger.info(f"Random seeds set to {seed}")


def get_reproducibility_info() -> Dict[str, str]:
    """
    Get reproducibility information.
    
    Returns:
        Dictionary with version info
    """
    import sys
    
    info = {
        'python_version': sys.version,
        'numpy_version': np.__version__,
        'pandas_version': pd.__version__,
    }
    
    try:
        import sklearn
        info['sklearn_version'] = sklearn.__version__
    except ImportError:
        pass
    
    try:
        import tensorflow as tf
        info['tensorflow_version'] = tf.__version__
    except ImportError:
        pass
    
    try:
        import xgboost as xgb
        info['xgboost_version'] = xgb.__version__
    except ImportError:
        pass
    
    return info


# ============================================================================
# UTILITIES
# ============================================================================

def get_feature_names(
    model: Any,
    feature_names: Optional[list] = None
) -> list:
    """
    Get feature names from model or provided list.
    
    Args:
        model: Trained model
        feature_names: Optional list of feature names
    
    Returns:
        List of feature names
    """
    if feature_names:
        return feature_names
    
    if hasattr(model, 'feature_names_in_'):
        return list(model.feature_names_in_)
    
    if hasattr(model, 'feature_names'):
        return list(model.feature_names)
    
    return None


def summarize_model(model: Any) -> Dict[str, Any]:
    """
    Get summary information about a model.
    
    Args:
        model: Trained model
    
    Returns:
        Summary dictionary
    """
    summary = {
        'type': type(model).__name__,
        'module': type(model).__module__
    }
    
    if hasattr(model, 'get_params'):
        summary['params'] = model.get_params()
    
    if hasattr(model, 'n_features_in_'):
        summary['n_features'] = model.n_features_in_
    
    if hasattr(model, 'feature_importances_'):
        summary['has_feature_importance'] = True
    
    return summary


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    logger.info("Model utilities module loaded successfully")
    
    # Print reproducibility info
    info = get_reproducibility_info()
    print("\nEnvironment Info:")
    for key, value in info.items():
        print(f"  {key}: {value}")
