## Srisupang Thewsuwan
November 2024
2
• Executive Summary
• Introduction
• Methodology
• Results
• Conclusion
• Appendix
Outline
3
• อธิบายภาพรวมของวิธีการทั้งหมด และผลลัพธ์จากการศึกษา
Executive Summary
Introduction
• The task involved gathering data
on SpaceX to create dashboards
and predict whether the first
stage of the Falcon 9 will be
reused, ultimately determining
launch costs.
45
Section 1
6
Executive Summary
• Data collection methodology:
• SpaceX launch data using an API, specifically the SpaceX REST API, to predict
rocket landing attempts
• Perform data wrangling
• additional API calls to gather specific information for each ID.
• Filtering, Handling Missing Values One-Hot encoding.
```
• Perform exploratory data analysis (EDA) using visualization
```
• Perform predictive analysis using classification models
Methodology
7
• The API provides data on past launches, including rocket details, payloads, and landing outcomes, accessible
through the endpoint api.spacexdata.com/v4/launches/past.
• Data is retrieved using a GET request with the requests library, and the response is in JSON format, which can be
converted into a dataframe using the json_normalize function.
Data Collection
8
Place your flowchart of SpaceX API calls
here
• Present your data collection with
SpaceX REST calls using key
phrases and flowcharts
• Add the GitHub URL of the
completed SpaceX API calls
```
notebook (must include completed
```
```
code cell and outcome cell), as an
```
external reference and peer-review
purpose
Data Collection – SpaceX API
9
• Describe how data were processed
• You need to present your data wrangling process using key phrases
and flowcharts
• Add the GitHub URL of your completed data wrangling related
notebooks, as an external reference and peer-review purpose
Data Wrangling
10
• Summarize what charts were plotted and why you used those charts
• Add the GitHub URL of your completed EDA with data visualization notebook,
as an external reference and peer-review purpose
EDA with Data Visualization
11
• Summarize how you built, evaluated, improved, and found the best
performing classification model
• You need present your model development process using key phrases and
flowchart
• Add the GitHub URL of your completed predictive analysis lab, as an external
reference and peer-review purpose
```
Predictive Analysis (Classification)
```
• Exploratory data analysis results
• Interactive analytics demo in screenshots
• Predictive analysis results
12
Results
Section 2
14
• Show a scatter point of
payload vs. orbit type
• Show the screenshot of the
scatter plot with
explanations
Payload vs. Orbit Type
15
• Show a line chart of yearly
average success rate
• Show the screenshot of the
scatter plot with
explanations
Launch Success Yearly Trend
16
• Find the names of the unique launch sites
• Present your query result with a short explanation here
All Launch Site Names
17
• Calculate the total payload carried by boosters from NASA
• Present your query result with a short explanation here
Total Payload Mass
18
• Find the dates of the first successful landing outcome on ground pad
• Present your query result with a short explanation here
First Successful Ground Landing Date
Section 3
20
• Visualize the built model accuracy for all
built classification models, in a bar chart
• Find which model has the highest
classification accuracy
Classification Accuracy
21
• Show the confusion matrix of the best performing model with an
explanation
Confusion Matrix
22
• Point 1
• Point 2
• Point 3
• Point 4
• …
Conclusions
23
• Include any relevant assets like Python code snippets, SQL queries, charts, Notebook
outputs, or data sets that you may have created during this project
Appendix