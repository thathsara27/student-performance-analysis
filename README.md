# Student Performance Analysis 🎓

## Overview
This project analyzes factors that affect student exam performance using a dataset of 6,607 students. 
The goal is to identify key patterns and relationships between factors such as attendance, study hours, 
parental involvement, and exam scores. The project also includes a simple prediction model to predict 
a student's exam score based on key factors.

## Technologies Used
- **Python** — Data cleaning, analysis, and visualization (Pandas, Matplotlib, Seaborn)
- **MySQL** — Storing and querying the cleaned dataset
- **Scikit-learn** — Building the prediction model
- **Power BI** — Interactive dashboard for data visualization
- **Git & GitHub** — Version control and project management

## Dataset
- **Source:** [Student Performance Factors - Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)
- **Size:** 6,607 students, 20 columns
- **Features:** Attendance, Hours Studied, Previous Scores, Parental Involvement, 
Access to Resources, Teacher Quality, Family Income, Gender, and more
- **Target:** Exam Score

## Project Questions
1. What factors affect student performance the most?
2. Does attendance affect exam results?
3. What is the relationship between study time and grades?
4. Does gender affect exam performance?
5. How does parental involvement influence results?

## Project Structure
```
Student Performance Factors/
|-- data/ # Raw and cleaned datasets
|-- scripts/ # Python scripts for cleaning and loading
|-- sql/ # SQL analysis queries
|-- visualizations/ # Charts and visualization scripts
|-- models/ # Prediction model
|-- README.md
```

## Key Findings
- **Attendance** has the strongest correlation with exam score (r = 0.58) — students with 85%+ 
attendance averaged 69.69 vs 64.21 for those under 70%
- **Study hours** is the second strongest factor (r = 0.45) — students studying 20+ hours averaged 
68.32 vs 63.82 for those under 10 hours
- **Gender** has virtually no effect on exam performance (Female: 67.24, Male: 67.23)
- **Parental involvement** shows a clear gradient — High: 68.09, Medium: 67.10, Low: 66.36
- **Sleep hours and physical activity** have almost no correlation with exam scores

## Prediction Model
A **Linear Regression** model was built to predict exam scores using 4 features:
- Attendance, Hours Studied, Previous Scores, Tutoring Sessions

| Metric | Value |
|---|---|
| Mean Absolute Error (MAE) | 1.27 |
| R² Score | 0.64 |

The model predicts exam scores within **1.27 points** on average.

## Power BI Dashboard
An interactive dashboard was built with 2 pages:
- **Page 1:** Overview — Attendance, Gender, Study Hours, Parental Involvement vs Exam Score + KPI cards
- **Page 2:** Detailed Analysis — Access to Resources, Motivation Level, Family Income, Teacher Quality vs Exam Score

## Setup Instructions
1. Clone the repository: git clone https://github.com/thathsara27/student-performance-analysis.git
2. Install dependencies: pip install pandas sqlalchemy mysql-connector-python matplotlib seaborn scikit-learn
3. Run `scripts/clean.py` to generate the cleaned dataset
4. Run `scripts/load_to_mysql.py` to load data into MySQL
5. Run `visualizations/visualize.py` to generate charts
6. Run `models/predict.py` to train and evaluate the prediction model
7. Open `student_performance_dashboard.pbix` in Power BI Desktop