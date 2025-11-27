# Technical Reference

## 1. System Requirements

### Hardware
- CPU: Multi-core processor (4+ cores recommended)
- RAM: 16GB minimum
- GPU: CUDA-compatible (optional, for LSTM)

### Software
- Python 3.9+
- TensorFlow 2.10+
- XGBoost 1.7+
- scikit-learn 1.2+

---

## 2. Data Specifications

### Input Data Format

| Field | Type | Description |
|-------|------|-------------|
| date | datetime | Observation date |
| congestion_index | float | Target variable (0-100) |
| temperature | float | Temperature in Celsius |
| rainfall | float | Rainfall in mm |
| is_weekend | int | Weekend flag (0/1) |

### Feature Engineering Output

- Lag features: `{target}_lag_{1,7,14,30}`
- Rolling features: `{target}_rolling_{mean,std,min,max}_{7,14,30}`
- Cyclical features: `{col}_sin`, `{col}_cos`

---

## 3. Model Specifications

### 3.1 LSTM Architecture

```
Input → LSTM(64) → Dropout(0.2) → LSTM(32) → Dropout(0.2) → Dense(1)
```

### 3.2 XGBoost Configuration

```python
{
    'objective': 'reg:squarederror',
    'n_estimators': 100,
    'max_depth': 6,
    'learning_rate': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8
}
```

---

## 4. API Reference

### modeling.py

| Function | Parameters | Returns |
|----------|------------|---------|
| `train_xgboost_model` | X_train, y_train, config | model, info |
| `train_lstm_model` | X_train, y_train, config | model, history |
| `train_arima_model` | y_train, order | model, info |

### evaluation.py

| Function | Parameters | Returns |
|----------|------------|---------|
| `calculate_all_metrics` | y_true, y_pred | dict |
| `compare_models` | models, X_test, y_test | DataFrame |
| `generate_evaluation_report` | model_name, y_true, y_pred | str |

---

## 5. File Structure

```
T3/
├── 02_Data/Processed/       # Engineered features
├── 02_Model_Development/    # Trained models
├── 05_Scripts/              # Python modules
├── 06_Notebooks/            # Jupyter notebooks
├── 07_Documentation/        # This documentation
├── 08_Configuration/        # Config files
└── 09_Results/              # Output results
```

---

**Document Version:** 1.0  
**Last Updated:** November 27, 2025
