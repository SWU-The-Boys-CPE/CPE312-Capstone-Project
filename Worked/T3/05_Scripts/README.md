# Scripts

**Phase 3: Model Development Scripts**

This directory contains Python scripts for modeling, evaluation, and feature engineering.

---

## 📁 Contents

| File | Purpose | Key Functions |
|------|---------|---------------|
| `modeling.py` | Model training | `train_linear_regression`, `train_xgboost`, `train_random_forest` |
| `evaluation.py` | Performance metrics | `calculate_metrics`, `evaluate_model` |
| `model_utils.py` | Helper functions | `save_model`, `load_model` |
| `feature_engineering.py` | Feature creation | `create_lag_features`, `create_rolling_features` |
| `hyperparameter_tuning.py` | Parameter optimization | `tune_xgboost`, `tune_random_forest` |
| `test_suite.py` | Unit tests | Model validation tests |

---

## 🔧 Usage

```python
# Import from T3 scripts
import sys
sys.path.append('../05_Scripts')

from modeling import train_xgboost_model
from evaluation import calculate_all_metrics
from feature_engineering import create_model_features
```

---

## 📦 Dependencies

See `../08_Configuration/requirements.txt`

---

## 📊 Model Results

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Random Forest | 0.81 | 0.63 | 0.9645 |
| Linear Regression | 2.06 | 1.96 | 0.7742 |
| XGBoost | 2.22 | 1.95 | 0.7359 |

---

**Last Updated:** November 28, 2025
