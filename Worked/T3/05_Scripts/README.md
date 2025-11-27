# Scripts

**Phase 3: Model Development Scripts**

This directory contains Python scripts for modeling, evaluation, and feature engineering.

---

## 📁 Contents

| File | Purpose | Key Functions |
|------|---------|---------------|
| `modeling.py` | Model training | `train_lstm`, `train_xgboost`, `train_arima` |
| `evaluation.py` | Performance metrics | `calculate_metrics`, `cross_validate` |
| `model_utils.py` | Helper functions | `save_model`, `load_model` |
| `feature_engineering.py` | Feature creation | `create_features`, `create_sequences` |

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

**Last Updated:** November 27, 2025
