# Bangkok Traffic Flow Optimization - T2: Data Collection, Cleaning & EDA

**Phase 2: Data Preparation and Exploratory Analysis**

**Duration:** 1 week (Week 2)  
**Status:** 🔜 In Progress  
**Last Updated:** November 16, 2025

---

## 📋 Quick Navigation

| Section | Purpose | Go To |
|---------|---------|-------|
| **Getting Started** | New to this project? | ↓ Below |
| **Project Overview** | What is T2? | [Project Overview](#-project-overview) |
| **Directory Structure** | Where are things? | [Directory Structure](#-directory-structure) |
| **Key Documents** | What should I read? | [Key Documents](#-key-documents) |
| **Your Role** | What do I need to do? | [Your Role](#-your-role) |
| **How to Use This** | Code & scripts | [How to Use](#-how-to-use-this-phase) |
| **Deliverables** | What needs to be done? | [Deliverables](#-deliverables) |
| **Daily Tasks** | Today's work | [Week 2 Checklist](05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md) |

---

## 🎯 Project Overview

### What is T2?

**T2** is Phase 2 of the Bangkok Traffic Flow Optimization capstone project. This phase focuses on:

✅ **Data Collection** - Gathering data from multiple sources  
✅ **Data Cleaning** - Handling missing values, outliers, duplicates  
✅ **Data Integration** - Combining multiple datasets  
✅ **Exploratory Data Analysis (EDA)** - Understanding data patterns and relationships  
✅ **Quality Assurance** - Ensuring 90%+ data quality  

### T2 Deliverables

By the end of Phase 2, we will have:

| # | Deliverable | Description | Owner |
|---|-------------|-------------|-------|
| 1 | **Cleaned Datasets** | 5 datasets processed and validated | Data Analyst |
| 2 | **Data Quality Report** | Assessment of completeness, validity, consistency | Data Analyst |
| 3 | **EDA Notebook** | Exploratory analysis with visualizations | Data Analyst |
| 4 | **Findings Document** | Initial insights, patterns, anomalies | Data Scientist |
| 5 | **Feature Engineering** | New features created from raw data | Data Scientist |
| 6 | **Preprocessed Data** | Ready for modeling | Both |

---

## 📂 Directory Structure

```
Worked/T2/
│
├── 📄 README.md                                 ← You are here
│
├── 📂 01_Project_Definition/
│   ├── 📄 README.md
│   ├── 📄 Project_Charter.md                   ⭐⭐⭐ Project details
│   └── 📄 10Traffic-Transport-Capstone.md
│
├── 📂 02_Data/
│   ├── 📄 README.md                            ⭐⭐ Data inventory
│   ├── 📁 Raw/                                 ← Add original datasets here
│   ├── 📁 Processed/                           ← Cleaned data goes here
│   └── 📁 External/                            ← Reference data
│
├── 📂 03_Notebooks/
│   ├── 📄 README.md
│   ├── 📓 01_Data_Exploration.ipynb            🔜 To create Week 2
│   ├── 📓 02_Data_Cleaning.ipynb               🔜 To create Week 2
│   ├── 📓 03_EDA.ipynb                         🔜 To create Week 3
│   ├── 📓 04_Feature_Engineering.ipynb         🔜 To create Week 4
│   └── 📓 05_Modeling.ipynb                    (Future)
│
├── 📂 04_Scripts/                              ✅ Ready to use
│   ├── 📄 README.md
│   ├── 🐍 utils.py                             Helper functions
│   ├── 🐍 data_loader.py                       Load & process data
│   ├── 🐍 preprocessing.py                     Bangkok-specific cleaning
│   └── 🐍 visualization.py                     Plotting functions
│
├── 📂 05_Documentation/
│   ├── 📄 README.md
│   ├── 📂 01_Getting_Started/
│   │   ├── 01_QUICK_START.md                   ⭐⭐⭐ 5-minute setup
│   │   └── 02_DOCUMENT_INDEX.md
│   ├── 📂 02_Project_Setup/
│   │   ├── 01_PROJECT_SETUP_COMPLETE.md
│   │   └── 02_PROJECT_MAP.md
│   ├── 📂 03_Technical_Docs/
│   │   ├── 01_Methodology.md                   ⭐⭐⭐ How we work
│   │   ├── 02_Data_Dictionary.md               ⭐⭐⭐ Data definitions
│   │   └── 03_EDA_Findings.md                  (Update in Week 3)
│   └── 📂 04_Weekly_Progress/
│       ├── 01_PROJECT_STATUS.md                ⭐⭐⭐ Track progress
│       └── 02_Week02_Checklist.md              ⭐⭐⭐ Daily tasks
│
├── 📂 06_Configuration/
│   ├── 📄 README.md
│   ├── 📄 config.yaml
│   ├── 📄 requirements.txt
│   └── 📄 .env.example
│
└── 📂 07_Results/
    ├── 📄 README.md
    ├── 📁 Figures/                             ← Save visualizations here
    ├── 📁 Reports/                             ← Save analysis reports here
    └── 📁 Presentations/                       (Future)

```

**Key Locations:**
- 📥 **Add Raw Data:** `02_Data/Raw/`
- 📤 **Save Cleaned Data:** `02_Data/Processed/`
- 💻 **Use Code:** `04_Scripts/`
- 📊 **Save Figures:** `07_Results/Figures/`
- 📝 **Save Reports:** `07_Results/Reports/`

---

## 📚 Key Documents

### Essential Reading (Required)

| Document | Purpose | Read Time | Priority |
|----------|---------|-----------|----------|
| [QUICK_START.md](05_Documentation/01_Getting_Started/01_QUICK_START.md) | 5-minute setup guide | 5 min | 🔴 URGENT |
| [Week02_Checklist.md](05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md) | This week's tasks | 10 min | 🔴 URGENT |
| [Data_Dictionary.md](05_Documentation/03_Technical_Docs/02_Data_Dictionary.md) | Data definitions | 20 min | ⭐⭐⭐ |
| [Project_Charter.md](01_Project_Definition/Project_Charter.md) | Project scope & goals | 20 min | ⭐⭐⭐ |

### Reference Documents

| Document | Purpose | Use When |
|----------|---------|----------|
| [Methodology.md](05_Documentation/03_Technical_Docs/01_Methodology.md) | Research methodology | Understanding our approach |
| [PROJECT_STATUS.md](05_Documentation/04_Weekly_Progress/01_PROJECT_STATUS.md) | Progress tracking | Weekly updates |
| [DOCUMENT_INDEX.md](05_Documentation/01_Getting_Started/02_DOCUMENT_INDEX.md) | Master index | Finding any document |
| [02_Data/README.md](02_Data/README.md) | Data inventory | Data questions |

---

## 👥 Your Role

### If You're the Data Analyst (วีร์กวิน นาคนิธิชัยรัชต์)

**Your Focus:** Data Collection, Cleaning, Quality Assessment

**T2 Tasks:**
1. ✅ Download and organize all 5 datasets
2. ✅ Perform data quality assessment
3. ✅ Clean missing values and handle outliers
4. ✅ Check for duplicates and inconsistencies
5. ✅ Validate data types and formats
6. ✅ Create initial EDA visualizations
7. ✅ Write data quality report

**Key Files to Use:**
- `04_Scripts/data_loader.py` - Load data
- `04_Scripts/preprocessing.py` - Clean Bangkok-specific data
- `04_Scripts/visualization.py` - Create charts
- `05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md` - Task list

**Deliverables:**
- Clean CSV files in `02_Data/Processed/`
- `01_Data_Exploration.ipynb` notebook
- `02_Data_Cleaning.ipynb` notebook
- Data quality report

---

### If You're the Data Scientist (คามิน สุรขจร)

**Your Focus:** Data Analysis, Pattern Discovery, Feature Engineering Planning

**T2 Tasks:**
1. ✅ Analyze cleaned datasets for patterns
2. ✅ Perform statistical testing
3. ✅ Identify key insights and anomalies
4. ✅ Plan feature engineering approach
5. ✅ Document initial findings
6. ✅ Create analysis reports

**Key Files to Use:**
- `04_Scripts/preprocessing.py` - Understand features
- `04_Scripts/visualization.py` - Create analysis charts
- `05_Documentation/03_Technical_Docs/01_Methodology.md` - Methodology
- `05_Documentation/03_Technical_Docs/02_Data_Dictionary.md` - Data reference

**Deliverables:**
- `03_EDA.ipynb` notebook with findings
- Statistical analysis report
- Feature engineering plan
- EDA findings document

---

### If You're the Project Manager (นิติภูมิ โพธิชัย)

**Your Focus:** Coordination, Progress Tracking, Team Support

**T2 Tasks:**
1. ✅ Assign daily tasks to team members
2. ✅ Track progress using checklists
3. ✅ Update status reports
4. ✅ Resolve blockers
5. ✅ Ensure deliverables on schedule
6. ✅ Prepare weekly status report

**Key Files to Use:**
- `05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md` - Task list
- `05_Documentation/04_Weekly_Progress/01_PROJECT_STATUS.md` - Status tracking
- `01_Project_Definition/Project_Charter.md` - Project overview

**Deliverables:**
- Weekly status updates
- Task completion tracking
- Team coordination

---

### If You're the Technical Lead (กฤตภาส อิ่มทั่ว)

**Your Focus:** Code Quality, Architecture, Technical Oversight

**T2 Tasks:**
1. ✅ Code review for all modules used
2. ✅ Ensure reproducibility
3. ✅ Monitor data quality
4. ✅ QA testing
5. ✅ Technical documentation

**Key Files to Use:**
- `04_Scripts/` - All Python modules
- `05_Documentation/03_Technical_Docs/01_Methodology.md` - Methods
- `06_Configuration/requirements.txt` - Dependencies

**Deliverables:**
- Code review feedback
- QA testing reports
- Reproducibility verification

---

## 🛠️ How to Use This Phase

### Step 1: Setup Your Environment

**Time:** 5 minutes

```bash
# 1. Navigate to project
cd /Volumes/T9/Documents/CPE/Y3-TR1/CPE312/Capstone\ Project/Worked/T2

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate

# 4. Install dependencies
pip install -r 06_Configuration/requirements.txt
```

**Verify:**
```bash
python3 -c "import pandas; import numpy; print('✅ Ready!')"
```

---

### Step 2: Load and Explore Data

**Location:** Start with [QUICK_START.md](05_Documentation/01_Getting_Started/01_QUICK_START.md)

**Example:**
```python
from scripts.data_loader import load_csv_data
from scripts.preprocessing import preprocess_traffic_data

# Load Bangkok traffic data
df = load_csv_data('02_Data/Raw/bangkok_traffic.csv')

# Clean it
df_clean = preprocess_traffic_data(df)

# Check quality
print(df_clean.info())
print(df_clean.describe())
```

---

### Step 3: Perform Quality Assessment

**Checklist from [Week02_Checklist.md](05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md):**

- [ ] Check for missing values
- [ ] Identify outliers
- [ ] Find duplicates
- [ ] Validate data types
- [ ] Check data ranges
- [ ] Document quality issues

**Code Template:**
```python
from scripts.data_loader import detect_outliers, handle_missing_values

# Check missing
print(f"Missing: {df.isnull().sum()}")

# Handle missing
df_filled = handle_missing_values(df)

# Detect outliers
outliers = detect_outliers(df_filled, 'congestion_index')
print(f"Outliers found: {len(outliers)}")
```

---

### Step 4: Create Visualizations

**Use:** `04_Scripts/visualization.py`

**Examples:**
```python
from scripts.visualization import (
    plot_congestion_distribution,
    plot_temporal_heatmap,
    plot_seasonal_patterns
)

# Exploratory visualizations
plot_congestion_distribution(df_clean['congestion_index'])
plot_temporal_heatmap(df_clean)
plot_seasonal_patterns(df_clean)
```

**Save Figures:**
```bash
# Figures go to:
07_Results/Figures/
```

---

### Step 5: Document Findings

**Create Notebooks:**
1. `03_Notebooks/01_Data_Exploration.ipynb`
2. `03_Notebooks/02_Data_Cleaning.ipynb`
3. `03_Notebooks/03_EDA.ipynb`

**Include in Each:**
- Data loading
- Quality checks
- Cleaning steps
- Visualizations
- Key findings
- Assumptions

---

## 📋 Deliverables

### Phase 2 Deliverables Checklist

**Data Deliverables:**
- [ ] Bangkok traffic data (cleaned, 90%+ quality)
- [ ] US accidents data (cleaned, methodology transferred)
- [ ] Weather data (cleaned, integrated)
- [ ] Transit ridership data (cleaned)
- [ ] OpenStreetMap data (processed)

**Analysis Deliverables:**
- [ ] Data quality assessment report
- [ ] Initial EDA report with findings
- [ ] Statistical summary statistics
- [ ] 15+ exploratory visualizations
- [ ] Anomalies and issues documented

**Code Deliverables:**
- [ ] `01_Data_Exploration.ipynb` - Data loading and initial look
- [ ] `02_Data_Cleaning.ipynb` - Cleaning steps and decisions
- [ ] `03_EDA.ipynb` - Exploratory analysis and insights
- [ ] All notebooks reproducible and well-documented

**Documentation Deliverables:**
- [ ] Updated [Data_Dictionary.md](05_Documentation/03_Technical_Docs/02_Data_Dictionary.md)
- [ ] Updated [PROJECT_STATUS.md](05_Documentation/04_Weekly_Progress/01_PROJECT_STATUS.md)
- [ ] Updated [EDA_Findings.md](05_Documentation/03_Technical_Docs/03_EDA_Findings.md)

---

## 📊 Daily Workflow

### Monday - Friday Schedule

**9:00 AM - 9:30 AM:**
- Team standup
- Review day's tasks from [Week02_Checklist.md](05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md)
- Clarify blockers

**9:30 AM - 12:30 PM:**
- Work on assigned tasks
- Data cleaning, analysis
- Notebook development

**12:30 PM - 1:30 PM:**
- Lunch break

**1:30 PM - 5:00 PM:**
- Continue task work
- Create visualizations
- Write documentation

**5:00 PM - 5:30 PM:**
- Update project status
- Commit code to Git
- Document daily progress

**Friday 4:00 PM - 5:00 PM:**
- Weekly review meeting
- Discuss findings
- Plan next week

---

## 🎓 Quick Learning Resources

### New to This Project?

1. **Start Here** (5 minutes)
   - Read this README (you're doing it!)

2. **Get Setup** (5 minutes)
   - Follow [QUICK_START.md](05_Documentation/01_Getting_Started/01_QUICK_START.md)

3. **Understand the Data** (20 minutes)
   - Read [Data_Dictionary.md](05_Documentation/03_Technical_Docs/02_Data_Dictionary.md)

4. **Get the Tasks** (10 minutes)
   - Read [Week02_Checklist.md](05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md)

5. **Start Coding** (15 minutes)
   - Try examples from [04_Scripts/README.md](04_Scripts/README.md)

**Total:** ~55 minutes to be productive!

---

## 🔗 Important Links

### Daily Use
- 📅 [Week 2 Checklist](05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md) - Today's tasks
- 📊 [Project Status](05_Documentation/04_Weekly_Progress/01_PROJECT_STATUS.md) - Progress tracking
- 🗺️ [Project Map](05_Documentation/02_Project_Setup/02_PROJECT_MAP.md) - Navigation guide

### Reference
- 📖 [Data Dictionary](05_Documentation/03_Technical_Docs/02_Data_Dictionary.md) - Data definitions
- 🔬 [Methodology](05_Documentation/03_Technical_Docs/01_Methodology.md) - How we work
- 📋 [Document Index](05_Documentation/01_Getting_Started/02_DOCUMENT_INDEX.md) - Master index

### Code & Setup
- 🚀 [Quick Start](05_Documentation/01_Getting_Started/01_QUICK_START.md) - 5-minute setup
- 🐍 [Scripts](04_Scripts/) - Python modules
- ⚙️ [Configuration](06_Configuration/) - Setup files

---

## ✅ Success Criteria

### By End of Week 2

- [ ] All 5 datasets downloaded and organized
- [ ] Data quality assessment complete (90%+ target)
- [ ] Data cleaning completed
- [ ] Initial EDA performed
- [ ] 15+ visualizations created
- [ ] Findings documented
- [ ] Team agrees on quality

### By End of Week 4

- [ ] Feature engineering completed
- [ ] All notebooks created and reproducible
- [ ] Statistical analysis complete
- [ ] Patterns and insights identified
- [ ] Next phase (modeling) prepared
- [ ] All documentation updated

---

## 🆘 Getting Help

### If You Have Questions

**About the data:**
→ Check [Data_Dictionary.md](05_Documentation/03_Technical_Docs/02_Data_Dictionary.md)  
→ Ask Data Analyst (วีร์กวิน)

**About coding:**
→ Check [04_Scripts/README.md](04_Scripts/README.md)  
→ Ask Technical Lead (กฤตภาส)

**About tasks:**
→ Check [Week02_Checklist.md](05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md)  
→ Ask Project Manager (นิติภูมิ)

**About methodology:**
→ Check [Methodology.md](05_Documentation/03_Technical_Docs/01_Methodology.md)  
→ Ask Data Scientist (คามิน)

**Can't find what you need:**
→ Check [DOCUMENT_INDEX.md](05_Documentation/01_Getting_Started/02_DOCUMENT_INDEX.md)

---

## 🔄 Version Control

### Commit Guidelines

**Commit often (daily):**
```bash
git add .
git commit -m "T2: Data cleaning - handle Bangkok traffic missing values"
```

**Meaningful messages:**
- `T2: Data cleaning - task description`
- `T2: EDA - visualization for congestion patterns`
- `T2: Documentation - update data dictionary`

### What Goes in Git

✅ **DO commit:**
- Code (Python scripts)
- Notebooks (Jupyter)
- Documentation (Markdown)
- Configuration (YAML, TXT)

❌ **DON'T commit:**
- Raw data files (use .gitignore)
- Large CSV files
- Generated plots
- Cache files

---

## 📞 Team Contacts

| Role | Name | Student ID | Responsibility |
|------|------|-----------|-----------------|
| **Project Manager** | นิติภูมิ โพธิชัย | 66109010194 | Coordination, tracking |
| **Data Analyst** | วีร์กวิน นาคนิธิชัยรัชต์ | 66109010201 | Data cleaning, EDA |
| **Data Scientist** | คามิน สุรขจร | 66109010322 | Analysis, insights |
| **Software Engineer** | ยศวีร์ พิมพ์รัฐเกษม | 66109010455 | Code, visualizations |
| **Technical Lead** | กฤตภาส อิ่มทั่ว | 66109010180 | QA, architecture |

---

## 📈 Progress Tracking

### Phase 2 Timeline

```
Week 2: Data Collection & Cleaning
├── Mon-Tue: Download all datasets
├── Wed-Thu: Initial cleaning & quality check
└── Fri: Review & planning

Week 3: EDA & Analysis
├── Mon-Wed: Exploratory analysis
├── Thu: Create visualizations
└── Fri: Document findings

Week 4: Feature Engineering & Prep
├── Mon-Tue: Feature engineering
├── Wed: Final data validation
└── Thu-Fri: Handoff to modeling phase
```

**Track progress in:** [PROJECT_STATUS.md](05_Documentation/04_Weekly_Progress/01_PROJECT_STATUS.md)

---

## 🎯 Next Steps

### Right Now
1. ✅ Read this README (complete!)
2. ⬜ Read [QUICK_START.md](05_Documentation/01_Getting_Started/01_QUICK_START.md)
3. ⬜ Setup your environment
4. ⬜ Download datasets

### This Week
1. ⬜ Review [Data_Dictionary.md](05_Documentation/03_Technical_Docs/02_Data_Dictionary.md)
2. ⬜ Follow [Week02_Checklist.md](05_Documentation/04_Weekly_Progress/02_Week02_Checklist.md)
3. ⬜ Start `01_Data_Exploration.ipynb`
4. ⬜ Begin data cleaning

### This Month
1. ⬜ Complete all EDA
2. ⬜ Create findings report
3. ⬜ Plan feature engineering
4. ⬜ Hand off to modeling team

---

## 📚 Additional Resources

### For Bangkok Data
- [Bangkok OpenStreetMap](https://www.openstreetmap.org/relation/2053698)
- [Bangkok Metropolitan Administration](https://www.bma.go.th/)
- [Thailand's Smart City Initiative](https://www.depa.or.th/)

### For Data Analysis
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)

### For EDA Best Practices
- "Exploratory Data Analysis" by John Tukey
- "[Best Practices for Data EDA](https://github.com/)" - check team resources
- [Kaggle EDA Examples](https://www.kaggle.com/)

---

## 📄 Document History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Nov 16, 2025 | Initial README created | Tech Team |
| - | - | - | - |

---

## ✨ Final Notes

**Remember:**
- 📚 Documentation is your friend - keep reading!
- 👥 Ask questions early and often
- 💾 Commit code frequently
- 📊 Update status regularly
- 🎯 Focus on quality over speed
- 🚀 One task at a time, stay focused

**You've got this! Good luck with T2! 🎉**

---

**Last Updated:** November 16, 2025

**Status:** Ready for Phase 2 Work

**Questions?** Ask your team lead or check the [Document Index](05_Documentation/01_Getting_Started/02_DOCUMENT_INDEX.md)
