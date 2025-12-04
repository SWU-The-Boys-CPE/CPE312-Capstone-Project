# Limitations

**Project:** Bangkok Traffic Congestion Index Prediction  
**Date:** November 28, 2025

---

## 1. Data Limitations

### 1.1 Temporal Granularity

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Daily data only (not hourly) | Cannot predict rush-hour spikes | Future work: collect hourly data |
| Historical only (no real-time) | Cannot validate live predictions | Use recent holdout; recommend real-time integration |
| Limited samples (351 days) | May limit complex model performance | Focus on feature engineering |

### 1.2 Geographic Coverage

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Bangkok-specific data | Limited generalizability | Focus on methodology; document context |
| City-wide aggregation | No spatial resolution | Future work: zone-level data |

### 1.3 Data Completeness

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Missing transit ridership | Incomplete multimodal analysis | Use proxy features; document as limitation |
| Limited weather granularity | May miss micro-weather events | Aggregate to daily averages |
| No special events data | Cannot predict event-driven spikes | Future work: add event calendar |

---

## 2. Model Limitations

### 2.1 Linear Regression (Best Model)

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Assumes linear relationships | May miss non-linear patterns | Feature engineering captures non-linearity |
| Sensitive to outliers | Extreme values affect predictions | Data cleaning; robust scaling |
| No uncertainty quantification | Point predictions only | Future: confidence intervals |

### 2.2 XGBoost (Second Best)

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Slight overfitting observed | 8.4% train-test gap | Regularization applied |
| Less interpretable than Linear | Harder to explain to stakeholders | SHAP values for interpretation |

### 2.3 Random Forest (Best R²)

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Less interpretable | Harder to explain individual predictions | Use SHAP values |
| Larger model size | More memory for deployment | Acceptable trade-off for accuracy |
| Slower inference | Slightly more computation | Still fast enough for daily predictions |

---

## 3. Analysis Limitations

### 3.1 Causation vs Correlation

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Cannot establish causation | Temperature correlation ≠ causation | Clear language; focus on associations |
| Confounding variables | Other factors may influence | Document uncertainty |

### 3.2 Scope Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| No rush-hour breakdown | Cannot optimize specific hours | Future work with hourly data |
| No route-level data | Cannot identify bottlenecks | City-wide TCI only |

---

## 4. Production Deployment Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Requires weather forecast | Prediction depends on weather API | Integrate weather forecast service |
| Daily update cycle | Not real-time | Acceptable for daily planning |
| Model drift risk | Performance may degrade | Recommend monthly retraining |

---

## 5. Recommendations for Future Work

1. **Collect hourly data** for rush-hour predictions
2. **Add zone-level** spatial resolution
3. **Include special events** (holidays, festivals, protests)
4. **Integrate real-time** weather API
5. **Implement model monitoring** for drift detection

---

## 6. Honest Assessment

**What this project CAN do:**
- Predict daily TCI with R² = 0.9645 ✅
- All three models exceed R² > 0.70 target ✅
- Provide interpretable predictions via Linear Regression ✅
- Support data-driven traffic planning ✅

**What this project CANNOT do:**
- Predict rush-hour spikes (hourly data needed)
- Identify specific road bottlenecks (no spatial data)
- Establish causal relationships (correlation only)
- Account for unprecedented events (protests, disasters)

---

**Last Updated:** November 28, 2025
