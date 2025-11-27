"""
Hyperparameter Tuning Module for Bangkok Traffic Flow Optimization Project

This module provides advanced hyperparameter tuning and model optimization
to achieve production-quality model performance (R² > 0.75).

Author: Data Science Team
Date: November 2025
"""

import numpy as np
import pandas as pd
import logging
from typing import Dict, List, Tuple, Optional, Any, Callable
from pathlib import Path
import pickle
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import TimeSeriesSplit, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import make_scorer, mean_squared_error, r2_score, mean_absolute_error

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# CUSTOM SCORERS
# ============================================================================

def rmse_scorer(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Calculate negative RMSE (for sklearn maximization)."""
    return -np.sqrt(mean_squared_error(y_true, y_pred))

def mape_scorer(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Calculate negative MAPE (for sklearn maximization)."""
    mask = y_true != 0
    if not np.any(mask):
        return 0
    return -np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100


# ============================================================================
# HYPERPARAMETER GRIDS
# ============================================================================

def get_xgboost_param_grid(search_type: str = 'grid') -> Dict[str, Any]:
    """
    Get XGBoost hyperparameter search space.
    
    Args:
        search_type: 'grid' for GridSearchCV, 'random' for RandomizedSearchCV
    
    Returns:
        Parameter grid dictionary
    """
    if search_type == 'grid':
        return {
            'n_estimators': [100, 200, 300],
            'max_depth': [4, 6, 8, 10],
            'learning_rate': [0.01, 0.05, 0.1],
            'subsample': [0.7, 0.8, 0.9],
            'colsample_bytree': [0.7, 0.8, 0.9],
            'min_child_weight': [1, 3, 5],
            'gamma': [0, 0.1, 0.2],
            'reg_alpha': [0, 0.1, 1],
            'reg_lambda': [0.5, 1, 2]
        }
    else:  # random search - wider ranges
        from scipy.stats import uniform, randint
        return {
            'n_estimators': randint(100, 500),
            'max_depth': randint(3, 12),
            'learning_rate': uniform(0.01, 0.19),
            'subsample': uniform(0.6, 0.4),
            'colsample_bytree': uniform(0.6, 0.4),
            'min_child_weight': randint(1, 10),
            'gamma': uniform(0, 0.5),
            'reg_alpha': uniform(0, 2),
            'reg_lambda': uniform(0.5, 3)
        }


def get_random_forest_param_grid(search_type: str = 'grid') -> Dict[str, Any]:
    """
    Get Random Forest hyperparameter search space.
    
    Args:
        search_type: 'grid' or 'random'
    
    Returns:
        Parameter grid dictionary
    """
    if search_type == 'grid':
        return {
            'n_estimators': [100, 200, 300, 500],
            'max_depth': [10, 15, 20, 25, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'max_features': ['sqrt', 'log2', 0.3, 0.5],
            'bootstrap': [True, False]
        }
    else:
        from scipy.stats import uniform, randint
        return {
            'n_estimators': randint(100, 600),
            'max_depth': randint(5, 30),
            'min_samples_split': randint(2, 20),
            'min_samples_leaf': randint(1, 10),
            'max_features': ['sqrt', 'log2', 0.3, 0.5, 0.7],
            'bootstrap': [True, False]
        }


def get_gradient_boosting_param_grid(search_type: str = 'grid') -> Dict[str, Any]:
    """
    Get Gradient Boosting hyperparameter search space.
    
    Args:
        search_type: 'grid' or 'random'
    
    Returns:
        Parameter grid dictionary
    """
    if search_type == 'grid':
        return {
            'n_estimators': [100, 200, 300],
            'max_depth': [3, 4, 5, 6],
            'learning_rate': [0.01, 0.05, 0.1],
            'subsample': [0.7, 0.8, 0.9],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'max_features': ['sqrt', 'log2', 0.5]
        }
    else:
        from scipy.stats import uniform, randint
        return {
            'n_estimators': randint(100, 400),
            'max_depth': randint(3, 10),
            'learning_rate': uniform(0.01, 0.19),
            'subsample': uniform(0.6, 0.4),
            'min_samples_split': randint(2, 20),
            'min_samples_leaf': randint(1, 10),
            'max_features': ['sqrt', 'log2', 0.3, 0.5, 0.7]
        }


# ============================================================================
# TIME SERIES CROSS-VALIDATION
# ============================================================================

def create_time_series_cv(
    n_splits: int = 5,
    gap: int = 0,
    test_size: Optional[int] = None
) -> TimeSeriesSplit:
    """
    Create TimeSeriesSplit cross-validator.
    
    Args:
        n_splits: Number of splits
        gap: Gap between train and test
        test_size: Size of test set (optional)
    
    Returns:
        TimeSeriesSplit object
    """
    return TimeSeriesSplit(n_splits=n_splits, gap=gap, test_size=test_size)


# ============================================================================
# HYPERPARAMETER TUNING
# ============================================================================

def tune_xgboost(
    X_train: np.ndarray,
    y_train: np.ndarray,
    search_type: str = 'random',
    n_iter: int = 50,
    cv: int = 5,
    scoring: str = 'neg_root_mean_squared_error',
    n_jobs: int = -1,
    verbose: int = 1
) -> Tuple[Any, Dict[str, Any]]:
    """
    Tune XGBoost hyperparameters using cross-validation.
    
    Args:
        X_train: Training features
        y_train: Training targets
        search_type: 'grid' or 'random'
        n_iter: Number of iterations for random search
        cv: Number of CV folds
        scoring: Scoring metric
        n_jobs: Number of parallel jobs
        verbose: Verbosity level
    
    Returns:
        Tuple of (best_model, tuning_results)
    """
    try:
        import xgboost as xgb
    except ImportError:
        raise ImportError("XGBoost not installed. Run: pip install xgboost")
    
    logger.info("Starting XGBoost hyperparameter tuning...")
    
    # Base model
    base_model = xgb.XGBRegressor(
        objective='reg:squarederror',
        random_state=42,
        n_jobs=n_jobs
    )
    
    # Parameter grid
    param_grid = get_xgboost_param_grid(search_type)
    
    # Time series CV
    tscv = create_time_series_cv(n_splits=cv)
    
    # Search
    if search_type == 'grid':
        search = GridSearchCV(
            base_model,
            param_grid,
            cv=tscv,
            scoring=scoring,
            n_jobs=n_jobs,
            verbose=verbose,
            refit=True
        )
    else:
        search = RandomizedSearchCV(
            base_model,
            param_grid,
            n_iter=n_iter,
            cv=tscv,
            scoring=scoring,
            n_jobs=n_jobs,
            verbose=verbose,
            refit=True,
            random_state=42
        )
    
    # Fit
    search.fit(X_train, y_train)
    
    # Results
    results = {
        'best_params': search.best_params_,
        'best_score': -search.best_score_,  # Convert back to positive RMSE
        'cv_results': pd.DataFrame(search.cv_results_),
        'n_candidates': len(search.cv_results_['mean_test_score'])
    }
    
    logger.info(f"Best XGBoost RMSE: {results['best_score']:.4f}")
    logger.info(f"Best params: {results['best_params']}")
    
    return search.best_estimator_, results


def tune_random_forest(
    X_train: np.ndarray,
    y_train: np.ndarray,
    search_type: str = 'random',
    n_iter: int = 50,
    cv: int = 5,
    scoring: str = 'neg_root_mean_squared_error',
    n_jobs: int = -1,
    verbose: int = 1
) -> Tuple[Any, Dict[str, Any]]:
    """
    Tune Random Forest hyperparameters using cross-validation.
    
    Args:
        X_train: Training features
        y_train: Training targets
        search_type: 'grid' or 'random'
        n_iter: Number of iterations for random search
        cv: Number of CV folds
        scoring: Scoring metric
        n_jobs: Number of parallel jobs
        verbose: Verbosity level
    
    Returns:
        Tuple of (best_model, tuning_results)
    """
    logger.info("Starting Random Forest hyperparameter tuning...")
    
    # Base model
    base_model = RandomForestRegressor(random_state=42, n_jobs=n_jobs)
    
    # Parameter grid
    param_grid = get_random_forest_param_grid(search_type)
    
    # Time series CV
    tscv = create_time_series_cv(n_splits=cv)
    
    # Search
    if search_type == 'grid':
        search = GridSearchCV(
            base_model,
            param_grid,
            cv=tscv,
            scoring=scoring,
            n_jobs=n_jobs,
            verbose=verbose,
            refit=True
        )
    else:
        search = RandomizedSearchCV(
            base_model,
            param_grid,
            n_iter=n_iter,
            cv=tscv,
            scoring=scoring,
            n_jobs=n_jobs,
            verbose=verbose,
            refit=True,
            random_state=42
        )
    
    # Fit
    search.fit(X_train, y_train)
    
    # Results
    results = {
        'best_params': search.best_params_,
        'best_score': -search.best_score_,
        'cv_results': pd.DataFrame(search.cv_results_),
        'n_candidates': len(search.cv_results_['mean_test_score'])
    }
    
    logger.info(f"Best Random Forest RMSE: {results['best_score']:.4f}")
    logger.info(f"Best params: {results['best_params']}")
    
    return search.best_estimator_, results


def tune_gradient_boosting(
    X_train: np.ndarray,
    y_train: np.ndarray,
    search_type: str = 'random',
    n_iter: int = 50,
    cv: int = 5,
    scoring: str = 'neg_root_mean_squared_error',
    n_jobs: int = -1,
    verbose: int = 1
) -> Tuple[Any, Dict[str, Any]]:
    """
    Tune Gradient Boosting hyperparameters using cross-validation.
    
    Args:
        X_train: Training features
        y_train: Training targets
        search_type: 'grid' or 'random'
        n_iter: Number of iterations for random search
        cv: Number of CV folds
        scoring: Scoring metric
        n_jobs: Number of parallel jobs
        verbose: Verbosity level
    
    Returns:
        Tuple of (best_model, tuning_results)
    """
    logger.info("Starting Gradient Boosting hyperparameter tuning...")
    
    # Base model
    base_model = GradientBoostingRegressor(random_state=42)
    
    # Parameter grid
    param_grid = get_gradient_boosting_param_grid(search_type)
    
    # Time series CV
    tscv = create_time_series_cv(n_splits=cv)
    
    # Search
    if search_type == 'grid':
        search = GridSearchCV(
            base_model,
            param_grid,
            cv=tscv,
            scoring=scoring,
            n_jobs=n_jobs,
            verbose=verbose,
            refit=True
        )
    else:
        search = RandomizedSearchCV(
            base_model,
            param_grid,
            n_iter=n_iter,
            cv=tscv,
            scoring=scoring,
            n_jobs=n_jobs,
            verbose=verbose,
            refit=True,
            random_state=42
        )
    
    # Fit
    search.fit(X_train, y_train)
    
    # Results
    results = {
        'best_params': search.best_params_,
        'best_score': -search.best_score_,
        'cv_results': pd.DataFrame(search.cv_results_),
        'n_candidates': len(search.cv_results_['mean_test_score'])
    }
    
    logger.info(f"Best Gradient Boosting RMSE: {results['best_score']:.4f}")
    logger.info(f"Best params: {results['best_params']}")
    
    return search.best_estimator_, results


# ============================================================================
# ENSEMBLE MODEL
# ============================================================================

class WeightedEnsembleRegressor:
    """
    Weighted ensemble of multiple regressors.
    
    Combines predictions from multiple models using learned or specified weights.
    """
    
    def __init__(
        self,
        models: List[Tuple[str, Any]],
        weights: Optional[List[float]] = None
    ):
        """
        Initialize ensemble.
        
        Args:
            models: List of (name, model) tuples
            weights: Optional weights for each model
        """
        self.models = models
        self.weights = weights
        self.is_fitted = False
    
    def fit(
        self,
        X: np.ndarray,
        y: np.ndarray,
        optimize_weights: bool = True,
        X_val: Optional[np.ndarray] = None,
        y_val: Optional[np.ndarray] = None
    ) -> 'WeightedEnsembleRegressor':
        """
        Fit ensemble models.
        
        Args:
            X: Training features
            y: Training targets
            optimize_weights: Whether to optimize weights on validation set
            X_val: Validation features
            y_val: Validation targets
        
        Returns:
            Self
        """
        logger.info(f"Fitting ensemble with {len(self.models)} models...")
        
        # Fit each model
        for name, model in self.models:
            logger.info(f"  Fitting {name}...")
            model.fit(X, y)
        
        # Optimize weights if requested
        if optimize_weights and X_val is not None and y_val is not None:
            self._optimize_weights(X_val, y_val)
        elif self.weights is None:
            # Equal weights
            self.weights = [1.0 / len(self.models)] * len(self.models)
        
        self.is_fitted = True
        return self
    
    def _optimize_weights(self, X_val: np.ndarray, y_val: np.ndarray):
        """Optimize weights using validation set."""
        from scipy.optimize import minimize
        
        # Get predictions from each model
        predictions = np.column_stack([
            model.predict(X_val) for _, model in self.models
        ])
        
        # Objective: minimize RMSE
        def objective(weights):
            weights = np.array(weights)
            weights = weights / weights.sum()  # Normalize
            ensemble_pred = predictions @ weights
            return np.sqrt(mean_squared_error(y_val, ensemble_pred))
        
        # Initial guess: equal weights
        initial_weights = np.ones(len(self.models)) / len(self.models)
        
        # Constraints: weights sum to 1, all >= 0
        constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
        bounds = [(0, 1)] * len(self.models)
        
        # Optimize
        result = minimize(
            objective,
            initial_weights,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        self.weights = list(result.x)
        logger.info(f"  Optimized weights: {self.weights}")
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions.
        
        Args:
            X: Features
        
        Returns:
            Weighted average predictions
        """
        if not self.is_fitted:
            raise ValueError("Ensemble not fitted. Call fit() first.")
        
        predictions = np.column_stack([
            model.predict(X) for _, model in self.models
        ])
        
        return predictions @ np.array(self.weights)
    
    @property
    def feature_importances_(self) -> np.ndarray:
        """Get weighted average feature importance."""
        importances = []
        for (name, model), weight in zip(self.models, self.weights):
            if hasattr(model, 'feature_importances_'):
                importances.append(model.feature_importances_ * weight)
        
        if importances:
            return np.sum(importances, axis=0)
        return None


# ============================================================================
# FULL TUNING PIPELINE
# ============================================================================

def run_full_tuning_pipeline(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    X_test: np.ndarray,
    y_test: np.ndarray,
    n_iter: int = 30,
    save_dir: Optional[str] = None
) -> Dict[str, Any]:
    """
    Run full hyperparameter tuning pipeline.
    
    Args:
        X_train, y_train: Training data
        X_val, y_val: Validation data
        X_test, y_test: Test data
        n_iter: Number of random search iterations
        save_dir: Directory to save models
    
    Returns:
        Dictionary with all results
    """
    logger.info("=" * 60)
    logger.info("STARTING FULL HYPERPARAMETER TUNING PIPELINE")
    logger.info("=" * 60)
    
    results = {}
    models = {}
    
    # 1. Tune XGBoost
    try:
        xgb_model, xgb_results = tune_xgboost(
            X_train, y_train,
            search_type='random',
            n_iter=n_iter,
            cv=5
        )
        models['xgboost'] = xgb_model
        results['xgboost'] = xgb_results
    except Exception as e:
        logger.error(f"XGBoost tuning failed: {e}")
    
    # 2. Tune Random Forest
    try:
        rf_model, rf_results = tune_random_forest(
            X_train, y_train,
            search_type='random',
            n_iter=n_iter,
            cv=5
        )
        models['random_forest'] = rf_model
        results['random_forest'] = rf_results
    except Exception as e:
        logger.error(f"Random Forest tuning failed: {e}")
    
    # 3. Tune Gradient Boosting
    try:
        gb_model, gb_results = tune_gradient_boosting(
            X_train, y_train,
            search_type='random',
            n_iter=n_iter,
            cv=5
        )
        models['gradient_boosting'] = gb_model
        results['gradient_boosting'] = gb_results
    except Exception as e:
        logger.error(f"Gradient Boosting tuning failed: {e}")
    
    # 4. Create and fit ensemble
    if len(models) >= 2:
        logger.info("\nCreating ensemble model...")
        ensemble = WeightedEnsembleRegressor([
            (name, model) for name, model in models.items()
        ])
        ensemble.fit(X_train, y_train, optimize_weights=True, X_val=X_val, y_val=y_val)
        models['ensemble'] = ensemble
    
    # 5. Evaluate all models on test set
    logger.info("\n" + "=" * 60)
    logger.info("FINAL TEST SET EVALUATION")
    logger.info("=" * 60)
    
    test_results = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        
        metrics = {
            'MAE': mean_absolute_error(y_test, y_pred),
            'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
            'R2': r2_score(y_test, y_pred)
        }
        
        test_results[name] = metrics
        
        status = "✅" if metrics['R2'] >= 0.75 else "⚠️"
        logger.info(f"{name:20s}: RMSE={metrics['RMSE']:.4f}, R²={metrics['R2']:.4f} {status}")
    
    results['test_results'] = test_results
    results['models'] = models
    
    # 6. Save best model
    if save_dir:
        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)
        
        # Find best model
        best_name = min(test_results, key=lambda x: test_results[x]['RMSE'])
        best_model = models[best_name]
        
        with open(save_dir / 'best_model.pkl', 'wb') as f:
            pickle.dump(best_model, f)
        
        # Save all models
        for name, model in models.items():
            if name != 'ensemble':  # Ensemble might have issues with pickle
                with open(save_dir / f'{name}_tuned.pkl', 'wb') as f:
                    pickle.dump(model, f)
        
        logger.info(f"\nModels saved to {save_dir}")
    
    # 7. Summary
    logger.info("\n" + "=" * 60)
    logger.info("TUNING COMPLETE")
    logger.info("=" * 60)
    
    best_name = min(test_results, key=lambda x: test_results[x]['RMSE'])
    best_metrics = test_results[best_name]
    
    logger.info(f"\n🏆 Best Model: {best_name}")
    logger.info(f"   MAE:  {best_metrics['MAE']:.4f}")
    logger.info(f"   RMSE: {best_metrics['RMSE']:.4f}")
    logger.info(f"   R²:   {best_metrics['R2']:.4f}")
    
    return results


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("""
    Hyperparameter Tuning Module
    ============================
    
    This module provides advanced hyperparameter tuning for achieving
    production-quality model performance (R² > 0.75).
    
    Example Usage:
    --------------
    from hyperparameter_tuning import run_full_tuning_pipeline
    
    results = run_full_tuning_pipeline(
        X_train, y_train,
        X_val, y_val,
        X_test, y_test,
        n_iter=50,
        save_dir='models/'
    )
    
    # Access best model
    best_model = results['models']['ensemble']
    
    # Check test performance
    print(results['test_results'])
    """)
