# Models & Artifacts Directory

## Overview
This directory contains trained machine learning models and model artifacts used in the analysis.

## Subdirectories

### `/checkpoints`
- Intermediate model checkpoints during training
- Useful for resuming training or accessing earlier model versions
- File format: `.h5` (TensorFlow), `.pt` / `.pth` (PyTorch), `.pkl` (scikit-learn)

### `/trained_models`
- Final trained model files ready for inference/prediction
- Best performing models validated on test set
- Named with format: `{model_name}_{metric}_{date}.{extension}`
- Example: `lstm_traffic_prediction_rmse_0.82_2025-11-20.h5`

### `/model_registry.json`
- Central registry of all trained models with metadata
- Tracks: model name, type, performance metrics, training date, hyperparameters
- Updated after each successful model training

## Model Artifact Contents

### Standard Model Metadata
Each model should have associated documentation including:
- **Training dataset info:** Features used, time period, split ratios
- **Hyperparameters:** All settings used during training
- **Performance metrics:** RMSE, MAE, MAPE, R², accuracy, etc.
- **Validation strategy:** Cross-validation folds, test set performance
- **Training history:** Convergence plots, loss curves
- **Preprocessing artifacts:** Scalers, encoders, feature lists

### Preprocessor Objects
- `scalers/`: StandardScaler, MinMaxScaler objects (`.pkl` files)
- `encoders/`: Categorical encoders (OneHotEncoder, LabelEncoder)
- `feature_lists/`: Saved feature names and order for consistency

## Usage Guidelines

### Saving Models
```python
# TensorFlow/Keras
model.save('05_Models/trained_models/lstm_traffic_rmse_0.82_2025-11-20.h5')

# PyTorch
torch.save(model.state_dict(), '05_Models/trained_models/lstm_traffic_2025-11-20.pt')

# Scikit-learn
import joblib
joblib.dump(model, '05_Models/trained_models/xgboost_traffic_2025-11-20.pkl')
```

### Loading Models
```python
# TensorFlow/Keras
from tensorflow import keras
model = keras.models.load_model('05_Models/trained_models/lstm_traffic.h5')

# PyTorch
model = YourModelClass()
model.load_state_dict(torch.load('05_Models/trained_models/lstm_traffic.pt'))

# Scikit-learn
import joblib
model = joblib.load('05_Models/trained_models/xgboost_traffic.pkl')
```

### Model Registry Update
After training a model:
```python
model_registry = {
    "model_name": "LSTM Traffic Prediction",
    "model_type": "neural_network",
    "framework": "tensorflow",
    "file_path": "trained_models/lstm_traffic_rmse_0.82_2025-11-20.h5",
    "training_date": "2025-11-20",
    "performance_metrics": {
        "rmse": 0.82,
        "mae": 0.65,
        "mape": 8.5,
        "r2": 0.92
    },
    "hyperparameters": {
        "units": [64, 32],
        "dropout": 0.2,
        "activation": "relu",
        "epochs": 100,
        "batch_size": 32
    },
    "input_shape": (24, 12),  # (timesteps, features)
    "training_samples": 2000,
    "validation_samples": 400,
    "test_samples": 400
}
```

## Model Version Control

### Naming Convention
- Models should be versioned with date: `{name}_{metric}_{YYYY-MM-DD}.{ext}`
- Keep only best models (1-2 per model type)
- Archive older versions in `checkpoints/archive/`

### Storage Strategy
- Git-ignored: Large model files (>100MB)
- Tracked: Model metadata, hyperparameters, performance logs
- Cloud backup: Important trained models (AWS S3, Google Cloud)

## Performance Baseline

Reference baseline metrics for traffic prediction tasks:
- **Simple Average:** RMSE ~1.2, MAPE ~15%
- **ARIMA:** RMSE ~0.95, MAPE ~12%
- **Random Forest:** RMSE ~0.85, MAPE ~10%
- **XGBoost:** RMSE ~0.78, MAPE ~8.5%
- **LSTM:** RMSE ~0.82, MAPE ~9% (goal: 0.75+ with low variance)

## Related Files
- Training scripts: `../04_Scripts/`
- Training notebooks: `../03_Notebooks/04_Modeling.ipynb`, `05_Modeling.ipynb`
- Results: `../06_Results/`

---

**Last Updated:** November 16, 2025
**Repository:** CPE312-Capstone-Project
