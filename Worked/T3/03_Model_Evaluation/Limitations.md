# Limitations

**Project:** Bangkok Traffic Flow Optimization  
**Date:** November 27, 2025

---

## 1. Data Limitations

### 1.1 Temporal Granularity

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Daily data only (not hourly) | Cannot predict 15-min spikes | Use hourly proxies; state as limitation |
| Historical only (no real-time) | Cannot validate live predictions | Use recent holdout; recommend real-time integration |

### 1.2 Geographic Coverage

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Bangkok-specific data | Limited generalizability | Focus on methodology; document context |
| US accidents for methodology | Transferability concerns | Use as methodology template, not direct predictions |

### 1.3 Data Completeness

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Missing transit ridership | Incomplete multimodal analysis | Use proxy features; document as limitation |
| Limited weather granularity | May miss micro-weather events | Aggregate to daily; use categorical |
| Gaps during COVID (2020) | Unusual traffic patterns | Consider excluding or flagging |

---

## 2. Model Limitations

### 2.1 LSTM

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Black-box nature | Difficult to explain predictions | Use SHAP values; attention mechanisms |
| Data hungry | May underperform with 1,682 samples | Use transfer learning; ensemble |
| Long training time | Limited hyperparameter exploration | Use early stopping; cloud resources |

### 2.2 XGBoost

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| May overfit | Poor generalization | Regularization; cross-validation |
| Sequential patterns | Doesn't capture time dependencies | Add lag features; compare with LSTM |

### 2.3 ARIMA

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Stationarity assumption | May miss non-linear patterns | Differencing; combine with ML |
| Univariate focus | Cannot use exogenous features | Use SARIMAX; document limitation |

---

## 3. Analysis Limitations

### 3.1 Causation vs Correlation

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Cannot establish causation | Policy recommendations are suggestive | Clear language; focus on associations |
| Confounding variables | Relationships may be spurious | Consider domain knowledge; multiple analyses |

### 3.2 External Factors

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| COVID-19 impact | Unusual 2020-2021 patterns | Flag period; consider exclusion |
| Special events (protests) | Extreme outliers | Include event features; document |
| Infrastructure changes | May affect predictions | Include infrastructure features |

---

## 4. Generalizability Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Bangkok-specific | May not apply to other cities | Document context; focus on methodology |
| Time period (2019-2025) | May not reflect future | Recommend regular retraining |
| Thai holidays | Culture-specific patterns | Document holiday effects |

---

## 5. Recommendations

1. **Acquire real-time data** for production deployment
2. **Implement regular model retraining** (monthly/quarterly)
3. **Conduct A/B testing** before full deployment
4. **Monitor model drift** over time
5. **Document uncertainty** in predictions

---

## 6. Honest Assessment

**What this project CAN do:**
- Predict daily congestion trends with reasonable accuracy
- Identify important features affecting congestion
- Provide methodology template for Bangkok authorities
- Support data-driven decision making

**What this project CANNOT do:**
- Guarantee real-time predictions without live data
- Establish causal relationships
- Replace domain expert judgment
- Account for unprecedented events

---

**Last Updated:** November 27, 2025
