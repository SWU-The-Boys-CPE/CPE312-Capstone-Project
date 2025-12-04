
# Srisupang Thewsuwan
## November 2024

1

---

# Outline

- Executive Summary
- Introduction
- Methodology
- Results
- Conclusion
- Appendix

2

---

# Executive Summary

- อธิบายภาพรวมของวิธีการทั้งหมด และผลลัพธ์จากการศึกษา

3

---

# Introduction

- The task involved gathering data on SpaceX to create dashboards and predict whether the first stage of the Falcon 9 will be reused, ultimately determining launch costs.

4

---

# Section 1: Methodology

5

---

# Methodology Overview

- Data collection methodology:
  - SpaceX launch data using an API, specifically the SpaceX REST API, to predict rocket landing attempts
  - Perform data wrangling
  - Additional API calls to gather specific information for each ID.
  - Filtering, Handling Missing Values, One-Hot encoding.
- Perform exploratory data analysis (EDA) using visualization
- Perform predictive analysis using classification models

6

---

# Data Collection

- The API provides data on past launches, including rocket details, payloads, and landing outcomes, accessible through the endpoint `api.spacexdata.com/v4/launches/past`.
- Data is retrieved using a GET request with the requests library, and the response is in JSON format, which can be converted into a dataframe using the `json_normalize` function.

7

---

# Data Collection – SpaceX API

- Place your flowchart of SpaceX API calls here
- Present your data collection with SpaceX REST calls using key phrases and flowcharts
- Add the GitHub URL of the completed SpaceX API calls notebook (must include completed code cell and outcome cell), as an external reference and peer-review purpose

8

---

# Data Wrangling

- Describe how data were processed
- You need to present your data wrangling process using key phrases and flowcharts
- Add the GitHub URL of your completed data wrangling related notebooks, as an external reference and peer-review purpose

9

---

# EDA with Data Visualization

- Summarize what charts were plotted and why you used those charts
- Add the GitHub URL of your completed EDA with data visualization notebook, as an external reference and peer-review purpose

10

---

# Predictive Analysis (Classification)

- Summarize how you built, evaluated, improved, and found the best performing classification model
- You need present your model development process using key phrases and flowchart
- Add the GitHub URL of your completed predictive analysis lab, as an external reference and peer-review purpose

11

---

# Section 2: Results

- Exploratory data analysis results
- Interactive analytics demo in screenshots
- Predictive analysis results

12

---

# Insights drawn from EDA

13

---

# Payload vs. Orbit Type

- Show a scatter point of payload vs. orbit type
- Show the screenshot of the scatter plot with explanations

14

---

# Launch Success Yearly Trend

- Show a line chart of yearly average success rate
- Show the screenshot of the scatter plot with explanations

15

---

# All Launch Site Names

- Find the names of the unique launch sites
- Present your query result with a short explanation here

16

---

# Total Payload Mass

- Calculate the total payload carried by boosters from NASA
- Present your query result with a short explanation here

17

---

# First Successful Ground Landing Date

- Find the dates of the first successful landing outcome on ground pad
- Present your query result with a short explanation here

18

---

# Section 3: Predictive Analysis Results

19

---

# Classification Accuracy

- Visualize the built model accuracy for all built classification models, in a bar chart
- Find which model has the highest classification accuracy

20

---

# Confusion Matrix

- Show the confusion matrix of the best performing model with an explanation

21

---

# Conclusions

- Point 1
- Point 2
- Point 3
- Point 4
- ...

22

---

# Appendix

- Include any relevant assets like Python code snippets, SQL queries, charts, Notebook outputs, or data sets that you may have created during this project

23

---

# Thank You!

24
