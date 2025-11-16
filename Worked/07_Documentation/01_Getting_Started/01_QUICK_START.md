# 🚀 Quick Start Guide - Bangkok Traffic Analysis Project

**Get started in 5 minutes!**

---

## 📦 1. Environment Setup (2 minutes)

```bash
# Navigate to project
cd "/Volumes/T9/Documents/CPE/Y3-TR1/CPE312/Capstone Project/Worked"

# Create virtual environment
python3.9 -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r 08_Configuration/requirements.txt

# Verify installation
python -c "import pandas, numpy, sklearn; print('✅ All packages installed!')"
```

---

## 📊 2. Data Setup (2 minutes)

```bash
# Create data directories
mkdir -p 02_Data/Raw
mkdir -p 02_Data/Processed

# Download datasets (see sources below)
# 1. Bangkok Traffic: https://www.trafficindex.org/
# 2. US Accidents: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents
# 3. Weather: NOAA API
# 4. OpenStreetMap: https://www.openstreetmap.org/export

# Place downloaded files in 02_Data/Raw/
```

**Expected files in `02_Data/Raw/`:**
- `bangkok_traffic_2019_2025.csv`
- `us_accidents.csv`
- `bangkok_weather.csv`
- `bangkok_osm_roads.geojson`
- `transit_ridership.csv`

---

## 🔧 3. Configuration (1 minute)

```bash
# Copy environment template
cp 08_Configuration/.env.example 08_Configuration/.env

# Edit with your API keys (optional for Week 2)
# nano 08_Configuration/.env
```

---

## 🧪 4. Test Your Setup (1 minute)

### Quick Test Script
Create a test file: `test_setup.py`

```python
#!/usr/bin/env python3
"""Quick setup verification"""

import sys
sys.path.append('04_Scripts')

from utils import setup_logger, load_config
from data_loader import load_csv_data, check_data_quality
import pandas as pd
import numpy as np

# Test 1: Logging
logger = setup_logger('test')
logger.info("✅ Logger working!")

# Test 2: Config
config = load_config('08_Configuration/config.yaml')
logger.info(f"✅ Config loaded: {len(config)} sections")

# Test 3: Create sample data
sample_data = pd.DataFrame({
    'date': pd.date_range('2019-01-01', periods=100),
    'congestion_index': np.random.uniform(20, 80, 100),
    'temperature': np.random.uniform(25, 38, 100)
})

# Test 4: Data quality check
quality_report = check_data_quality(
    sample_data,
    required_columns=['date', 'congestion_index'],
    max_missing_pct=10.0
)

print("\n" + "="*50)
print("✅ ALL TESTS PASSED!")
print("="*50)
print(f"Quality Report:\n{quality_report}")
```

Run test:
```bash
python test_setup.py
```

Expected output:
```
✅ Logger working!
✅ Config loaded: X sections
==================================================
✅ ALL TESTS PASSED!
==================================================
Quality Report:
{'total_rows': 100, 'total_columns': 3, ...}
```

---

## 📚 5. Your First Analysis (5 minutes)

### Load and Explore Bangkok Traffic Data

Create: `first_analysis.py`

```python
#!/usr/bin/env python3
"""First quick analysis of Bangkok traffic data"""

import sys
sys.path.append('04_Scripts')

import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_csv_data, create_temporal_features
from visualization import plot_congestion_distribution, plot_time_series

# Load data
print("📊 Loading Bangkok traffic data...")
df = load_csv_data('02_Data/Raw/bangkok_traffic_2019_2025.csv')

print(f"✅ Loaded {len(df)} records")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
print(f"\nFirst 5 rows:\n{df.head()}")

# Basic statistics
print("\n📈 Basic Statistics:")
print(df['congestion_index'].describe())

# Create temporal features
print("\n🕐 Creating temporal features...")
df = create_temporal_features(df, date_column='date')

# Visualization 1: Distribution
print("\n📊 Creating congestion distribution plot...")
plot_congestion_distribution(
    df['congestion_index'],
    title='Bangkok Traffic Congestion Distribution (2019-2025)',
    save_path='06_Results/Figures/congestion_distribution.png'
)
print("✅ Saved: 06_Results/Figures/congestion_distribution.png")

# Visualization 2: Time series
print("\n📈 Creating time series plot...")
plot_time_series(
    df,
    date_col='date',
    value_col='congestion_index',
    title='Bangkok Traffic Congestion Over Time',
    save_path='06_Results/Figures/time_series.png'
)
print("✅ Saved: 06_Results/Figures/time_series.png")

print("\n" + "="*50)
print("🎉 First analysis complete!")
print("="*50)
print("\nNext steps:")
print("1. Check 06_Results/Figures/ for your plots")
print("2. Review 07_Documentation/Week02_Checklist.md")
print("3. Start cleaning other datasets")
```

Run:
```bash
python first_analysis.py
```

---

## 📖 Essential Files to Read First

### Must Read (15 minutes total)
1. **README.md** (5 min) - Project overview
2. **PROJECT_SETUP_COMPLETE.md** (5 min) - What's been done
3. **Week02_Checklist.md** (5 min) - Your tasks this week

### Reference When Needed
4. **Project_Charter.md** - Full project details
5. **Methodology.md** - Research methods
6. **PROJECT_STATUS.md** - Current status

---

## 🎯 Week 2 Priorities (In Order)

### Day 1 (Monday) - Data Acquisition
- [ ] Download all 5 primary datasets
- [ ] Place in `02_Data/Raw/`
- [ ] Verify file integrity

### Day 2 (Tuesday) - Initial Cleaning
- [ ] Clean Bangkok Traffic data
- [ ] Clean US Accidents data
- [ ] Document issues found

### Day 3 (Wednesday) - More Cleaning
- [ ] Clean Weather data
- [ ] Process OSM road network
- [ ] Start transit data

### Day 4 (Thursday) - Integration
- [ ] Merge datasets (traffic + weather)
- [ ] Validate integrated dataset
- [ ] Check alignment

### Day 5 (Friday) - Initial EDA
- [ ] Generate 10+ visualizations
- [ ] Calculate descriptive statistics
- [ ] Draft EDA report

### Weekend - Finalize
- [ ] Complete EDA report
- [ ] Quality assessment
- [ ] Update PROJECT_STATUS.md

---

## 💡 Useful Commands

### Data Quality Check
```python
from scripts.data_loader import load_csv_data, check_data_quality

df = load_csv_data('02_Data/Raw/your_file.csv')
report = check_data_quality(df, required_columns=['col1', 'col2'])
print(report)
```

### Quick Visualization
```python
from scripts.visualization import plot_congestion_distribution

plot_congestion_distribution(
    df['congestion_index'],
    save_path='06_Results/Figures/test.png'
)
```

### Preprocessing Pipeline
```python
from scripts.preprocessing import preprocess_traffic_data

df_clean = preprocess_traffic_data(
    df,
    date_col='date',
    congestion_col='congestion_index'
)
```

### Logging
```python
from scripts.utils import setup_logger

logger = setup_logger('my_analysis')
logger.info("Starting analysis...")
logger.warning("Warning message")
logger.error("Error message")
```

---

## 🆘 Troubleshooting

### Issue: Import errors
**Solution:**
```python
import sys
sys.path.append('04_Scripts')
```

### Issue: Missing packages
**Solution:**
```bash
pip install -r 08_Configuration/requirements.txt
```

### Issue: Data file not found
**Solution:**
- Check file is in `02_Data/Raw/`
- Check filename spelling
- Use absolute path if needed

### Issue: Permission denied
**Solution:**
```bash
chmod +x your_script.py
```

---

## 📞 Quick Links

- **Data Sources:** See `02_Data/README.md`
- **Code Examples:** See `04_Scripts/` modules
- **Week 2 Tasks:** See `07_Documentation/Week02_Checklist.md`
- **Project Status:** See `07_Documentation/PROJECT_STATUS.md`

---

## ✅ Checklist: Am I Ready?

Before starting Week 2 work, verify:

- [ ] Python 3.9+ installed
- [ ] Virtual environment activated
- [ ] All packages installed (`pip list` shows 45+ packages)
- [ ] Project structure exists (8 directories)
- [ ] Configuration files in place
- [ ] Read README.md
- [ ] Read PROJECT_SETUP_COMPLETE.md
- [ ] Read Week02_Checklist.md
- [ ] Test script runs successfully

**All checked?** → You're ready! 🚀

---

## 🎓 Learning Resources

### Python Data Science
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

### Machine Learning
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)

### Time Series
- [Statsmodels Time Series](https://www.statsmodels.org/stable/tsa.html)
- [ARIMA Guide](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)

### Geospatial
- [GeoPandas Documentation](https://geopandas.org/)
- [Folium Quickstart](https://python-visualization.github.io/folium/)

---

**Last Updated:** November 16, 2025

**Team:** SWU - The Boys CPE

**Need help?** Check `PROJECT_SETUP_COMPLETE.md` or ask your team! 🤝
