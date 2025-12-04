# Project Charter: Bangkok Traffic Congestion Index Prediction

## Document Information
- **Document Version:** 2.0
- **Date Created:** November 2025
- **Last Updated:** November 2025
- **Status:** Active
- **Owner:** Project Manager

---

## 1. Project Identification

### 1.1 Project Title
**Bangkok Traffic Congestion Index Prediction Using Time-Series Machine Learning**

### 1.2 Project Code
`CPE312-CapstoneProject-Traffic`

### 1.3 Project Duration
- **Start Date:** November 16, 2025
- **End Date:** [Target End Date]
- **Total Duration:** 12 weeks

---

## 2. Business Case & Strategic Alignment

### 2.1 Problem Statement
Bangkok's traffic congestion costs approximately 97 million Thai Baht daily in wasted fuel. The congestion index averages 38.88, with peaks reaching 162.13. Accurate prediction of congestion levels can enable proactive travel planning and traffic management.

### 2.2 Project Vision
To develop machine learning models that accurately predict Bangkok's daily Traffic Congestion Index using historical congestion data and weather features.

### 2.3 Strategic Alignment
- **SDG 11:** Sustainable Cities and Communities (data-driven urban planning)
- **SDG 13:** Climate Action (reducing emissions through better traffic forecasting)

---

## 3. Project Goals & Objectives

### 3.1 Primary Goal
Develop a machine learning model to predict Bangkok's daily Traffic Congestion Index using temporal and weather features.

### 3.2 Specific Objectives

| # | Objective | Success Criteria | Target Completion |
|---|-----------|-----------------|-------------------|
| O1 | Collect and clean traffic & weather data | Complete cleaned dataset with <1% missing values | Week 2 |
| O2 | Perform exploratory data analysis | Identify temporal patterns and weather correlations | Week 4 |
| O3 | Engineer predictive features | Create temporal and weather-based features | Week 5 |
| O4 | Train ML models (RF, XGBoost, Linear) | Successfully train all three models | Week 8 |
| O5 | Evaluate and compare model performance | Select best model with RMSE < 15 | Week 10 |
| O6 | Document methodology & findings | Complete final report and presentation | Week 12 |

---

## 4. Scope Definition

### 4.1 In Scope
- ✅ Bangkok Traffic Congestion Index analysis (2019-2025)
- ✅ Weather data integration (temperature, humidity, precipitation)
- ✅ Temporal feature engineering (day of week, month, holidays)
- ✅ ML model training (Random Forest, XGBoost, Linear Regression)
- ✅ Model evaluation and comparison
- ✅ Final documentation and presentation

### 4.2 Out of Scope
- ❌ Accident pattern analysis
- ❌ Public transit optimization
- ❌ Road network/infrastructure analysis
- ❌ Real-time prediction system deployment
- ❌ Multi-city analysis
- ❌ Route optimization

---

## 5. High-Level Requirements

### 5.1 Data Requirements
- Bangkok Traffic Congestion Index (daily, 2019-2025)
- Bangkok Weather Data (temperature, humidity, precipitation)

### 5.2 Technical Requirements
- **Language:** Python 3.9+
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Tools:** Jupyter Notebook, Git
- **Models:** Random Forest, XGBoost, Linear Regression

### 5.3 Analytical Requirements
- Predictive modeling (Random Forest, XGBoost, Linear Regression)
- Feature importance analysis
- Time-series forecasting with cross-validation
- Model comparison and selection

### 5.4 Deliverable Requirements
- All code must be documented and version controlled
- Notebooks must be reproducible with clear execution paths
- Models must include performance metrics and validation results
- Visualizations must have clear titles, labels, and legends
- Documentation must be comprehensive and accessible

---

## 6. Success Criteria

### 6.1 Quality Metrics
| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Data Quality | ≥90% completeness | Data quality assessment report |
| Model Accuracy | 75-85% for predictions | Cross-validation, test set performance |
| Code Quality | 90%+ PEP 8 compliance | Automated linting checks |
| Documentation | Complete & clear | Technical review checklist |
| Reproducibility | All analyses reproducible | Run from scratch verification |

### 6.2 Project Metrics
| Metric | Target |
|--------|--------|
| On-time delivery | 100% (all deliverables by week 12) |
| Team coordination | Weekly meetings, zero critical issues unresolved |
| Code coverage | 80%+ for utility functions |
| Stakeholder satisfaction | Positive feedback from academic review |

### 6.3 Impact Metrics
| Metric | Target | Basis |
|--------|--------|-------|
| Prediction RMSE | < 15 | Based on TCI range (0-200) |
| Prediction MAE | < 10 | Daily forecast error tolerance |
| Prediction R² | > 0.70 | Strong predictive power |
| Model Interpretability | High | Feature importance analysis |

---

## 7. Key Constraints & Assumptions

### 7.1 Constraints
- **Time:** 12-week duration, fixed academic calendar
- **Budget:** Limited to free/open-source tools and datasets
- **Data:** Limited real-time API access (free tier restrictions)
- **Personnel:** 5-person team with part-time commitment
- **Infrastructure:** Local development machines (no dedicated servers)

### 7.2 Assumptions
- Historical traffic data patterns are predictive of future trends
- Weather data correlates with traffic congestion patterns
- Daily aggregated data is sufficient for prediction
- Team members have required technical skills (or will upskill quickly)
- Stakeholders will be available for feedback and validation
- Data quality issues can be addressed through preprocessing

### 7.3 Dependencies
- External: Availability of datasets (Kaggle, CEIC, OSM)
- Internal: Regular team coordination, timely decision-making
- Technical: Jupyter environment, Python libraries compatibility
- Stakeholder: Academic approval process, any required permissions

---

## 8. Risks & Mitigation

### 8.1 Risk Register

| # | Risk | Probability | Impact | Mitigation Strategy |
|---|------|-------------|--------|-------------------|
| R1 | Data quality issues/gaps | Medium | High | Early data exploration, validation pipeline, handling strategy documented |
| R2 | Model performance below target | Medium | Medium | Ensemble approaches, hyperparameter optimization, baseline comparisons |
| R3 | Scope creep | Medium | High | Strict scope definition, change control process |
| R4 | Team coordination/availability | Low | High | Weekly standups, clear responsibilities, backup assignments |
| R5 | Technical/tool issues | Low | Medium | Early setup testing, documentation, quick resolution protocols |
| R6 | Dataset availability changes | Low | Medium | Backup datasets identified, fallback analysis approaches |

---

## 9. Stakeholders & Communication

### 9.1 Stakeholder Analysis

| Stakeholder | Interest | Influence | Strategy |
|-------------|----------|-----------|----------|
| Academic Advisors | Quality, methodology | High | Regular consultations, documentation |
| BMA/Traffic Authorities | Actionable insights | High | Policy-focused recommendations |
| Team Members | Clear direction, resources | High | Regular meetings, support |
| Students/Peers | Project success, learning | Low | Presentations, knowledge sharing |
| General Public | Impact realization | Low | Report dissemination |

### 9.2 Communication Plan
- **Weekly:** Team standups (1 hour) - status, blockers, coordination
- **Bi-weekly:** Progress reviews - checkpoint validation
- **Monthly:** Stakeholder updates (if applicable)
- **Formal Documentation:** Status reports, meeting notes
- **Version Control:** Git commits with clear messages

---

## 10. Organization & Roles

### 10.1 Project Team

| Role | Team Member | Student ID | Responsibilities |
|------|-------------|-----------|------------------|
| **Project Manager** | นิติภูมิ โพธิชัย | 66109010194 | Overall coordination, timeline management, stakeholder communication, progress tracking |
| **Data Analyst** | วีร์กวิน นาคนิธิชัยรัชต์ | 66109010201 | Data collection, data cleaning, exploratory data analysis (EDA) |
| **Data Scientist** | คามิน สุรขจร | 66109010322 | Statistical analysis, modeling, algorithm development, validation |
| **Visualization & Docs** | ยศวีร์ พิมพ์รัฐเกษม | 66109010455 | Visualizations, dashboards, documentation, report writing, presentation preparation |
| **Technical Lead & QA** | กฤตภาส อิ่มทั่ว | 66109010180 | Code quality assurance, tool setup, technical infrastructure, testing |

### 10.2 Decision Authority
- **Day-to-day decisions:** Technical Lead, Data Scientist
- **Scope decisions:** Project Manager, Technical Lead
- **Quality gates:** Technical Lead with team consensus
- **Escalation:** Project Manager to academic advisors

### 10.3 Support Functions
- **Academic Support:** Course instructors, TA (as needed)
- **Infrastructure:** IT support (university resources)
- **Documentation:** All team members responsible for their areas

---

## 11. Implementation Plan Overview

### 11.1 Phase Breakdown

**Phase 1: Setup & Data (Weeks 1-2)**
- Establish development environment
- Data source identification and download
- Initial data exploration and quality assessment

**Phase 2: Data Preparation & EDA (Weeks 3-5)**
- Data cleaning and standardization
- Exploratory analysis and visualization
- Feature engineering

**Phase 3: Modeling & Analysis (Weeks 6-9)**
- Model development and training (RF, XGBoost, Linear)
- Hyperparameter optimization
- Validation and performance testing
- Feature importance analysis

**Phase 4: Synthesis & Documentation (Weeks 10-12)**
- Results visualization and analysis
- Report writing and findings documentation
- Model interpretation and insights
- Final presentation preparation

---

## 12. Resources & Budget

### 12.1 Technical Resources
- Development machines (5 laptops)
- Cloud storage (optional: AWS/Google Cloud free tier)
- Open-source software stack (no licensing costs)
- University computing resources

### 12.2 Tools & Software
- **Data Processing:** Pandas, NumPy
- **Modeling:** Scikit-learn, XGBoost
- **Visualization:** Matplotlib, Seaborn
- **Version Control:** Git/GitHub
- **Documentation:** Markdown, Jupyter Notebooks

### 12.3 Data Access
- **Free datasets:** Kaggle, CEIC, OpenStreetMap, NASA
- **API access:** Google Maps (limited), TomTom (trial), Weather APIs
- **Local data:** BMA datasets (pending availability)

---

## 13. Change Management

### 13.1 Change Control Process
1. **Identify:** Document proposed change and rationale
2. **Assess:** Evaluate impact on schedule, scope, resources
3. **Approve:** Project Manager & Technical Lead consensus required
4. **Execute:** Update documentation, communicate to team
5. **Monitor:** Track change implementation and impact

### 13.2 Change Thresholds
- Minor (no impact on timeline/scope): Technical Lead approval
- Moderate (minor timeline/scope impact): PM + TL approval
- Major (significant impact): Team consensus required

---

## 14. Quality Assurance & Approval

### 14.1 Quality Gates

| Gate | Timing | Criteria | Owner |
|------|--------|----------|-------|
| Data Quality | Week 2 | 90%+ completeness, validated sources | Data Analyst |
| EDA Approval | Week 4 | Comprehensive analysis, clear findings | Data Scientist |
| Model Validation | Week 8 | 75%+ accuracy, documented methodology | Data Scientist |
| Documentation | Week 11 | Complete, clear, reproducible | Tech Lead |
| Final Review | Week 12 | All deliverables, passing QA checklist | PM + TL |

### 14.2 Sign-off Authority
- **Data & Analysis:** Data Scientist
- **Code Quality:** Technical Lead
- **Overall Project:** Project Manager with advisor approval

---

## 15. Success Factors & Next Steps

### 15.1 Critical Success Factors
1. Data availability and quality
2. Team coordination and communication
3. Technical capability and upskilling
4. Clear scope management
5. Timely decision-making
6. Stakeholder engagement

### 15.2 Immediate Next Steps (Week 1)
- [ ] Team roles finalized and documented
- [ ] Development environment setup completed
- [ ] Data sources confirmed and access established
- [ ] Project timeline detailed in task tracking system
- [ ] Initial team standup and kickoff meeting
- [ ] GitHub repository setup and initial structure

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Technical Lead | | | |
| Academic Advisor | | | |

---

**Document History:**
- v1.0 (Nov 2025): Initial charter created

---

*End of Project Charter*
