# Trained Models Directory

This directory stores trained model artifacts.

## Expected Files

| File | Model | Format | Size (est.) |
|------|-------|--------|-------------|
| `lstm_traffic_model.h5` | LSTM | Keras HDF5 | ~5-10 MB |
| `xgboost_traffic_model.pkl` | XGBoost | Pickle | ~1-5 MB |
| `arima_traffic_model.pkl` | ARIMA | Pickle | <1 MB |
| `rf_traffic_model.pkl` | Random Forest | Pickle | ~10-50 MB |

## Loading Models

```python
# LSTM
from tensorflow.keras.models import load_model
lstm_model = load_model('lstm_traffic_model.h5')

# XGBoost
import pickle
with open('xgboost_traffic_model.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

# ARIMA
with open('arima_traffic_model.pkl', 'rb') as f:
    arima_model = pickle.load(f)
```

## Version Control

- Models are NOT tracked in git (too large)
- Add to `.gitignore`
- Document model versions in training logs

---

**Last Updated:** November 27, 2025
