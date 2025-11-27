# Model Development

**Phase 3: Model Training and Development**

This directory contains trained models, hyperparameter tuning results, and model checkpoints.

---

## 📁 Directory Structure

```
02_Model_Development/
├── README.md                    ← You are here
├── Trained_Models/              ← Saved model artifacts
│   ├── lstm_traffic_model.h5
│   ├── xgboost_traffic_model.pkl
│   └── arima_traffic_model.pkl
├── Hyperparameter_Tuning/       ← Tuning results
│   ├── tuning_results.csv
│   └── best_params.yaml
└── Model_Checkpoints/           ← Training checkpoints
    └── .gitkeep
```

---

## 🤖 Models to Train

| Model | File Format | Status |
|-------|-------------|--------|
| LSTM | `.h5` (Keras) | ⬜ To Do |
| XGBoost | `.pkl` (pickle) | ⬜ To Do |
| ARIMA | `.pkl` (pickle) | ⬜ To Do |
| Random Forest | `.pkl` (pickle) | ⬜ To Do |

---

## 📊 Training Workflow

1. Load preprocessed data from T2
2. Create train/val/test splits (60/20/20)
3. Apply feature engineering
4. Train each model
5. Save trained model artifacts
6. Log training metrics

---

## 🔧 Hyperparameter Tuning

See `Hyperparameter_Tuning/` for:
- Grid search results
- Random search results
- Bayesian optimization results
- Best parameters for each model

---

**Last Updated:** November 27, 2025
