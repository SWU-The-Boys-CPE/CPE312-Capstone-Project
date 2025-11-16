# 📋 01_Project_Definition - Project Charter & Objectives

## Purpose
This directory contains project definition documents that establish the scope, objectives, research questions, and team structure for the CPE312 Capstone Project.

## 📄 Contents

### Project_Charter.md
**Purpose:** Comprehensive project charter defining project scope and success criteria

**Contains:**
- **Project Identification:** CPE312, SWU-The-Boys-CPE, Nov 16, 2025 - Feb 7, 2026
- **Team Members:** 5 Thai students with names, IDs, and assigned roles
  - นิติภูมิ โพธิชัย (66109010194) - Project Manager
  - วีร์กวิน นาคนิธิชัยรัชต์ (66109010201) - Data Analyst
  - คามิน สุรขจร (66109010322) - Data Scientist
  - ยศวีร์ เพชรรักษ์ (66109010455) - Software Engineer
  - กฤตภาส อิ่มทั่ว (66109010180) - Technical Lead

- **Business Case:** Bangkok traffic optimization
  - Economic impact: 97M THB/day fuel waste
  - Average congestion: 38.88 (0-200 scale)
  - Peak congestion: 162.13 during special events

- **Project Objectives (7 total):**
  1. Reduce congestion 15-25%
  2. Improve transit efficiency 10-15%
  3. Predict congestion 15-60 min ahead
  4. Identify traffic hotspots
  5. Optimize transit routes
  6. Reduce emissions 5-8%
  7. Provide analytical framework for policy makers

- **Research Questions (6 total):**
  1. What are temporal patterns in Bangkok traffic?
  2. What spatial patterns exist across regions?
  3. How do accidents affect traffic flow?
  4. How does public transit affect congestion?
  5. Can we predict congestion 15-60 min ahead?
  6. What route optimization can reduce travel time?

- **Success Criteria:**
  - Data quality: <10% missing values
  - Zero duplicates
  - Model RMSE: <0.80
  - Model MAE: <0.65
  - Model MAPE: <10%
  - Model R²: >0.85

- **Constraints:**
  - Duration: 12 weeks (hard deadline)
  - Scope: 5 primary datasets (defined)
  - Resources: Educational project (limited budget)
  - Purpose: Academic capstone (publication quality)

- **Risks (6 identified):**
  1. Data availability issues
  2. Data quality problems
  3. Model performance gaps
  4. Computational resource constraints
  5. Timeline pressure
  6. Stakeholder engagement challenges

- **Stakeholders:** University, team members, traffic authorities (Thailand), public

- **Timeline:** 7 phases across 12 weeks with detailed milestones

---

## 🎯 Key Information

### Project Scope
- **Type:** Data Science Capstone
- **Domain:** Urban Traffic Flow Optimization
- **Location:** Bangkok Metropolitan Area (Thailand)
- **Scale:** 5 datasets, 2.8M+ accident records, 1,682+ traffic observations

### Datasets Defined
1. Bangkok Traffic Index (2019-2025) - timeseries
2. US Accidents (2.8M records) - geospatial reference
3. OpenStreetMap Road Network - geospatial
4. Weather Data (historical) - timeseries
5. Public Transit Data - timeseries

### Team Roles
- **Project Manager:** นิติภูมิ โพธิชัย
  - Coordinates team activities
  - Tracks timeline and milestones
  - Manages risks and blockers
  
- **Data Analyst:** วีร์กวิน นาคนิธิชัยรัชต์
  - Data collection and validation
  - Quality assurance
  - Statistical analysis

- **Data Scientist:** คามิน สุรขจร
  - Feature engineering
  - Model development
  - Algorithm optimization

- **Software Engineer:** ยศวีร์ เพชรรักษ์
  - Environment setup
  - Code infrastructure
  - Documentation

- **Technical Lead:** กฤตภาส อิ่มทั่ว
  - Architecture oversight
  - Code quality
  - Team guidance

---

## 📅 Project Timeline

**Phase 1: Data Collection** (Week 1-2)
- Collect all 5 datasets
- Validate data sources
- Set up data pipelines

**Phase 2: EDA** (Week 3-4)
- Initial exploration
- Statistical summaries
- Pattern identification

**Phase 3: Preprocessing** (Week 4-5)
- Data cleaning
- Feature engineering
- Data integration

**Phase 4: Modeling** (Week 6-9)
- Train multiple models
- Hyperparameter tuning
- Cross-validation

**Phase 5: Optimization** (Week 8-9)
- Route optimization
- Performance enhancement
- Result refinement

**Phase 6: Dashboard** (Week 9-10)
- Visualization design
- Dashboard development
- Recommendation generation

**Phase 7: Documentation & Presentation** (Week 11-12)
- Final report
- Presentation preparation
- Knowledge transfer

---

## ✅ Related Documents

### In This Directory
- **Project_Charter.md** (15 sections, comprehensive scope definition)

### In 07_Documentation/
- **01_Methodology.md** (11 sections, detailed research approach)
- **02_Data_Dictionary.md** (600 lines, all variable definitions)
- **PROJECT_STATUS.md** (tracking dashboard)

### In 01_Project_Definition/
- **10Traffic-Transport-Capstone.md** (original planning document)

---

## 📊 Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| **Data Quality** | <10% missing | Pending |
| **Zero Duplicates** | 0 duplicates | Pending |
| **Model RMSE** | <0.80 | Pending |
| **Model MAE** | <0.65 | Pending |
| **Model MAPE** | <10% | Pending |
| **Model R²** | >0.85 | Pending |
| **Code Coverage** | >80% | Pending |

---

## 🚀 Next Steps

1. **Week 1 (Complete):** Data collection setup ✅
2. **Week 2 (Current):** Data cleaning and initial EDA
3. **Week 3:** Continue EDA analysis
4. **Week 4:** Preprocessing finalization
5. **Week 6+:** Model development

---

**Last Updated:** November 16, 2025  
**Owner:** Project Manager (นิติภูมิ โพธิชัย)  
**Status:** Active - Week 2  
**Next Review:** End of Week 2
