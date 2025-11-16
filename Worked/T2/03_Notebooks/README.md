# Notebooks Directory

## Overview
Jupyter notebooks for exploratory data analysis, data preprocessing, feature engineering, and model development.

## Notebook Organization

### Execution Order

**Phase 1: Data Exploration**
- `01_Data_Exploration.ipynb` - Initial data loading and overview

**Phase 2: Data Cleaning**
- `02_Data_Cleaning.ipynb` - Data quality assessment and cleaning

**Phase 3: Exploratory Analysis**
- `03_EDA.ipynb` - Statistical analysis and visualization

**Phase 4: Feature Engineering**
- `04_Feature_Engineering.ipynb` - Feature creation and selection

**Phase 5: Modeling**
- `05_Modeling.ipynb` - Model development and training
- `06_Model_Evaluation.ipynb` (optional) - Detailed model comparison

## Notebook Template Structure

Each notebook should follow this structure:

```
1. Project Context & Objectives
   - Brief description of analysis goals
   - Input data sources
   - Expected outputs

2. Setup & Configuration
   - Required imports
   - Configuration loading
   - Logger initialization
   - Random seed setting

3. Data Loading
   - Load data from sources
   - Display dataset info
   - Show sample records

4. [Main Analysis Content]
   - Section-specific analysis steps

5. Summary & Conclusions
   - Key findings recap
   - Outputs saved
   - Next steps
```

## Notebook Descriptions

### 01_Data_Exploration.ipynb
**Purpose:** Load and examine datasets for the first time

**Key Sections:**
- Data source documentation
- Load raw data from files/APIs
- Display basic statistics (shape, dtypes, memory usage)
- Check for missing values and duplicates
- Show data samples
- Identify data quality issues

**Outputs:**
- Data quality assessment report
- Initial data exploration plots
- Recommendations for cleaning

### 02_Data_Cleaning.ipynb
**Purpose:** Clean and prepare data for analysis

**Key Sections:**
- Remove/handle duplicates
- Address missing values
- Fix data types
- Detect and handle outliers
- Merge/align multiple datasets
- Temporal alignment (timezone, frequency)
- Save cleaned dataset

**Outputs:**
- Cleaned processed dataset
- Data cleaning report
- Transformation documentation

### 03_EDA.ipynb
**Purpose:** Exploratory Data Analysis - understand patterns and relationships

**Key Sections:**
- Univariate analysis (distributions, summaries)
- Bivariate analysis (correlations, relationships)
- Multivariate analysis (patterns, clusters)
- Temporal analysis (trends, seasonality)
- Spatial analysis (geographic patterns)
- Statistical testing
- Insights summary

**Outputs:**
- EDA visualizations (histograms, heatmaps, scatter plots)
- Statistical test results
- EDA report with findings

### 04_Feature_Engineering.ipynb
**Purpose:** Create and select features for modeling

**Key Sections:**
- Feature brainstorming
- Temporal features (hour, day, month, season, holidays)
- Spatial features (coordinates, clusters, proximity)
- Lagged features (past values)
- Rolling statistics
- Domain-specific features
- Feature selection/filtering
- Normalization/scaling
- Final feature dataset creation

**Outputs:**
- Feature-engineered dataset
- Feature importance analysis
- Feature documentation

### 05_Modeling.ipynb
**Purpose:** Develop and train machine learning models

**Key Sections:**
- Data splitting (train/val/test)
- Baseline models (simple average, ARIMA, Random Forest)
- Advanced models (XGBoost, LSTM, etc.)
- Hyperparameter tuning
- Cross-validation
- Performance evaluation
- Model comparison
- Best model selection

**Outputs:**
- Trained models (saved to 05_Models/)
- Performance metrics
- Prediction results
- Model comparison report

### 06_Model_Evaluation.ipynb (Optional)
**Purpose:** Detailed evaluation and analysis of best models

**Key Sections:**
- Detailed performance metrics
- Error analysis
- Feature importance analysis
- Sensitivity analysis
- Prediction intervals
- Edge case analysis

**Outputs:**
- Detailed evaluation report
- Diagnostic plots
- Recommendations for improvement

## Best Practices

### Code Style
- Clear, descriptive variable names
- Meaningful function names
- Comments for complex logic
- Docstrings for custom functions
- Consistent indentation (4 spaces)

### Data Handling
- Never modify original data in-place
- Document all transformations
- Save intermediate results
- Use descriptive variable names

### Visualization
- Large, readable fonts
- Clear titles and labels
- Consistent color schemes
- Legend when appropriate
- Grid for readability

### Documentation
- Markdown headers for sections
- Explanation of analysis goals
- Interpretation of results
- Summary at the end
- Save figures with descriptive names

### Notebook Execution
- Notebooks should be runnable end-to-end
- No hardcoded paths (use config)
- No external dependencies without import statements
- Clear error handling
- Reproducible with fixed random seed

## Required Setup

### Before Running Notebooks
```bash
# Navigate to project root
cd /Volumes/T9/Documents/CPE/Y3-TR1/CPE312/Capstone\ Project/Worked

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r 08_Configuration/requirements.txt

# Start Jupyter
jupyter notebook
```

### Notebook Configuration Cell
Every notebook should start with this configuration:

```python
# ============================================================================
# SETUP & CONFIGURATION
# ============================================================================

# System imports
import os
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Data & scientific computing
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 6)

# Project utilities
sys.path.append('../04_Scripts')
from utils import setup_logger, get_data_paths, load_config, get_timestamp

# Configure project
logger = setup_logger('notebook', level='INFO')
config = load_config('../08_Configuration/config.yaml')
paths = get_data_paths()

# Set random seed for reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

logger.info(f"Notebook started at {get_timestamp()}")
logger.info(f"Data paths configured: {paths}")
```

## Troubleshooting

### Common Issues
1. **Import errors:** Ensure all packages installed with `pip install -r requirements.txt`
2. **Path errors:** Use relative paths or `get_data_paths()` from utils
3. **Memory issues:** Use `reduce_memory_usage()` for large dataframes
4. **Random results:** Set seed at beginning: `np.random.seed(42)`

### Debugging
- Use `print()` or logging for debugging
- Check data shapes and dtypes frequently
- Save intermediate results for inspection
- Run notebook cells individually for troubleshooting

## File Management

### Saving Outputs
```python
# Save figures with timestamp
fig.savefig(
    f'../06_Results/Figures/analysis_plot_{get_date_string()}.png',
    dpi=300,
    bbox_inches='tight'
)

# Save data
df.to_csv(f'../02_Data/Processed/my_data_{get_date_string()}.csv', index=False)

# Save models
import joblib
joblib.dump(model, f'../05_Models/trained_models/my_model_{get_date_string()}.pkl')
```

### Cleanup
- Remove large temporary outputs before committing
- Archive old notebook versions if needed
- Keep current version in main notebooks directory

## Related Files
- **Configuration:** `../08_Configuration/`
- **Scripts:** `../04_Scripts/`
- **Results:** `../06_Results/`
- **Models:** `../05_Models/`

---

**Last Updated:** November 16, 2025
**Notebook Maintainer:** Data Science Team

