# ⚙️ 08_Configuration - Project Configuration & Environment

## Purpose
This directory contains all configuration files, environment variables, and dependency specifications needed to run the project.

## 📄 Contents

### 1. requirements.txt (62 packages)
**Purpose:** Python package dependencies and versions

**Install Command:**
```bash
pip install -r 08_Configuration/requirements.txt
```

**Package Categories:**

**Core Data Processing & Analysis** (4 packages)
- pandas==2.1.3
- numpy==1.26.2
- scipy==1.11.4
- scikit-learn==1.3.2

**Visualization** (4 packages)
- matplotlib==3.8.2
- seaborn==0.13.0
- plotly==5.17.0
- folium==0.14.0

**Machine Learning & Deep Learning** (4 packages)
- tensorflow==2.14.0
- torch==2.1.1
- xgboost==2.0.3
- lightgbm==4.0.0

**Time Series & Forecasting** (3 packages)
- statsmodels==0.14.0
- pmdarima==2.0.4
- prophet==1.1.5

**Geospatial Analysis** (3 packages)
- geopandas==0.14.0
- shapely==2.0.1
- pyproj==3.6.1

**Data Quality & Validation** (2 packages)
- great-expectations==0.18.10
- pandasvalidation==0.1.0

**Interactive Dashboards** (3 packages)
- streamlit==1.28.1
- dash==2.14.1
- plotly-express==5.17.0

**Utilities & Development** (13 packages)
- python-dotenv==1.0.0
- pyyaml==6.0.1
- tqdm==4.66.1
- jupyter==1.0.0
- jupyterlab==4.0.9
- ipython==8.17.2
- notebook==7.0.6
- ipywidgets==8.1.1
- black==23.11.0
- flake8==6.1.0
- pylint==3.0.2
- pytest==7.4.3
- pytest-cov==4.1.0

**API & Web** (2 packages)
- requests==2.31.0
- aiohttp==3.9.1

**Documentation** (2 packages)
- sphinx==7.2.6
- sphinx-rtd-theme==2.0.0

**Optimization & Performance** (2 packages)
- numba==0.58.1
- bottleneck==1.3.7

**Date/Time Handling** (2 packages)
- pytz==2023.3
- python-dateutil==2.8.2

**Version Control** (1 package)
- gitpython==3.1.40

**Total:** 62 packages across 16 categories

---

### 2. config.yaml (200+ lines)
**Purpose:** Central configuration for all project settings

**Key Sections:**

**Project Metadata**
```yaml
project:
  name: "CPE312 Capstone - Traffic Flow Optimization"
  version: "1.0"
  created: "2025-11-16"
  duration_weeks: 12
```

**Paths Configuration**
- raw_data: ./02_Data/Raw
- processed_data: ./02_Data/Processed
- external_data: ./02_Data/External
- notebooks: ./03_Notebooks
- scripts: ./04_Scripts
- models: ./05_Models
- results: ./06_Results
- documentation: ./07_Documentation
- configs: ./08_Configuration
- logs: ./logs

**Data Configuration**
- 5 datasets defined (Bangkok Traffic, US Accidents, OSM, Weather, Transit)
- Sources, frequency, years documented
- Status tracking for each dataset

**Processing Configuration**
- Data cleaning parameters:
  - Remove duplicates: true
  - Missing value handling: interpolation (limit: 7)
  - Outlier detection: IQR method (multiplier: 1.5)

- Feature engineering:
  - Temporal features: hour, day, month, season, holiday
  - Spatial features: district, area_cluster
  - Derived features: lags, rolling averages

- Normalization:
  - Method: StandardScaler (or MinMaxScaler/Robust)
  - Applied to: congestion_index, volume, temperature, precipitation

**Modeling Configuration**
- Data splits: Train (60%), Validation (20%), Test (20%)
- Temporal split: true (for time-series)
- Random seed: 42 (reproducibility)

- Models configured:
  - LSTM (neural network)
  - XGBoost (gradient boosting)
  - Random Forest (ensemble)
  - ARIMA (time-series)

**Validation Configuration**
- Quality gates:
  - Data completeness: >90%
  - Model accuracy: >75%
  - Code coverage: >80%

**Schedule**
- 6 phases over 12 weeks:
  1. Data Collection & Integration (2 weeks)
  2. Exploratory Data Analysis (2 weeks)
  3. Data Preprocessing (2 weeks)
  4. Modeling & Validation (4 weeks)
  5. Route Optimization (2 weeks)
  6. Dashboard & Recommendations (2 weeks)
  7. Documentation & Presentation (1 week)

---

### 3. .env.example
**Purpose:** Template for environment variables

**Sample Variables:**
```
# API Keys
GOOGLE_MAPS_API_KEY=your_key_here
OPENWEATHER_API_KEY=your_key_here
KAGGLE_API_KEY=your_key_here

# Database
DATABASE_URL=postgresql://user:password@localhost/dbname

# Flask/Web Settings
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

# AWS Credentials (if using cloud)
AWS_ACCESS_KEY_ID=your_key_here
AWS_SECRET_ACCESS_KEY=your_secret_here

# Logging Level
LOG_LEVEL=INFO

# Model Parameters
MODEL_RANDOM_SEED=42
USE_GPU=True
```

**Usage:**
1. Copy to `.env` (not tracked by git)
2. Fill in actual values
3. Load with `python-dotenv` in code

---

## 🔧 Setup Instructions

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### 2. Install Dependencies
```bash
pip install --upgrade pip
pip install -r 08_Configuration/requirements.txt
```

### 3. Setup Environment Variables
```bash
cp 08_Configuration/.env.example .env
# Edit .env with your values
```

### 4. Verify Installation
```bash
python3 -c "import pandas; import numpy; import tensorflow; print('✅ All packages installed')"
```

---

## 📊 Configuration Best Practices

### ✅ Implemented
- **YAML Format:** Human-readable configuration
- **Path Centralization:** All paths in one place
- **Version Pinning:** Exact versions for reproducibility
- **Environment Separation:** .env for secrets
- **Documentation:** All settings documented with comments
- **Category Organization:** Packages grouped logically
- **Quality Gates:** Acceptance criteria defined
- **Schedule:** Detailed timeline in config
- **Validation:** Data quality thresholds set

### ✅ Security
- `.env` file in `.gitignore` (secrets not tracked)
- API keys in environment variables only
- No credentials in requirements.txt
- `.env.example` as template (safe to share)

### ✅ Reproducibility
- Exact package versions specified
- Random seed set to 42
- Data splits defined
- Train/val/test ratios documented
- Processing parameters centralized
- Feature engineering steps documented

---

## 🚀 Quick Reference

### Install Everything
```bash
source venv/bin/activate
pip install -r 08_Configuration/requirements.txt
```

### Load Configuration in Code
```python
import yaml
from pathlib import Path

def load_config():
    config_path = Path('08_Configuration/config.yaml')
    with open(config_path) as f:
        return yaml.safe_load(f)

config = load_config()
raw_data_path = config['paths']['raw_data']
```

### Access Environment Variables
```python
import os
from dotenv import load_dotenv

load_dotenv('08_Configuration/.env')
api_key = os.getenv('GOOGLE_MAPS_API_KEY')
```

### Check Package Versions
```bash
pip list | grep -E "pandas|numpy|tensorflow"
```

---

## 📋 Configuration Checklist

### Before Running Analysis
- [ ] Virtual environment created
- [ ] All packages installed (requirements.txt)
- [ ] .env file created from .env.example
- [ ] API keys filled in .env (if needed)
- [ ] config.yaml reviewed for your setup
- [ ] Paths created (02_Data/Raw, etc.)

### Before Each Run
- [ ] Virtual environment activated
- [ ] `.env` loaded (python-dotenv)
- [ ] config.yaml settings verified
- [ ] Log level appropriate
- [ ] GPU setting correct (if applicable)

### Quality Assurance
- [ ] requirements.txt versions fixed
- [ ] Random seed = 42 for reproducibility
- [ ] All paths relative (portable)
- [ ] Credentials in .env (not in code)
- [ ] Configuration documented

---

## 🔄 Updating Configuration

### Adding a New Package
```bash
# Install the package
pip install package_name==version

# Add to requirements.txt (manually or use):
pip freeze | grep package_name >> 08_Configuration/requirements.txt
```

### Changing Model Parameters
Edit `config.yaml` under `modeling.models[]` section:
```yaml
- name: "LSTM"
  hyperparameters:
    units: [64, 32]  # Change here
    epochs: 100      # Change here
```

### Adding New Paths
Add to `config.yaml` `paths:` section:
```yaml
paths:
  new_path: "./09_NewDirectory"
```

---

## 📊 Statistics

| Item | Count | Status |
|------|-------|--------|
| Python Packages | 62 | ✅ Documented |
| Configuration Sections | 15 | ✅ Complete |
| Environment Variables | 10+ | ✅ Template |
| Paths Defined | 10 | ✅ Documented |
| Models Configured | 4 | ✅ Hyperparams set |
| Data Quality Gates | 3 | ✅ Defined |
| Phases Scheduled | 7 | ✅ Documented |

---

## 🎯 Key Configuration Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Random Seed | 42 | Reproducibility |
| Train/Val/Test | 60/20/20 | Standard split |
| Temporal Split | true | Time-series aware |
| Data Completeness | >90% | Quality threshold |
| Model RMSE Target | <0.80 | Success criterion |
| Outlier Detection | IQR 1.5 | Standard method |
| Missing Value Limit | 7 | Max consecutive NaN |
| Figure DPI | 300 | Publication quality |

---

## ⚡ Performance Settings

```yaml
performance:
  num_workers: 4        # Parallel processing
  use_gpu: true         # GPU acceleration
  memory_limit_gb: 8    # RAM budget
```

Adjust based on your hardware:
- **Laptop:** num_workers=2, memory_limit_gb=4
- **Workstation:** num_workers=8, memory_limit_gb=16
- **Server:** num_workers=16+, memory_limit_gb=32+

---

## 🔗 Related Files

### Main Configuration
- config.yaml (main settings)
- requirements.txt (Python packages)
- .env.example (environment template)

### Usage
- 03_Notebooks/01_Data_Exploration.ipynb
- 04_Scripts/utils.py (load_config function)
- 08_Configuration/.gitignore (doesn't track .env)

### Documentation
- 07_Documentation/README.md (references config)
- 01_Project_Definition/Project_Charter.md (scope)

---

**Last Updated:** November 16, 2025  
**Status:** ✅ Complete  
**Version:** 1.0  
**Owner:** Software Engineer (ยศวีร์ เพชรรักษ์)  

**To Get Started:**
```bash
cd "/Volumes/T9/Documents/CPE/Y3-TR1/CPE312/Capstone Project/Worked"
source venv/bin/activate
pip install -r 08_Configuration/requirements.txt
# You're ready to go! 🚀
```
