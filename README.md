# Student Performance Analysis 🎓

A data analysis project exploring factors that affect student exam performance.

## Technologies Used
- Python (Pandas, Matplotlib, Seaborn, Scikit-learn)
- MySQL
- Power BI

## Dataset
- Source: [Student Performance Factors - Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)
- 6,607 students, 20 columns

## Project Questions
- What affects student performance?
- Does attendance affect results?
- Relationship between study time and grades
- Gender and demographic analysis

## Project Structure
Student Performance Factors/
├── data/                         # Raw and cleaned datasets
├── scripts/                      # Python scripts for cleaning and loading
├── sql/                          # SQL analysis queries
├── visualizations/               # Charts and visualization scripts
├── models/                       # Prediction model
└── README.md

## Key Findings
- Attendance has the strongest correlation with exam score (r = 0.58)
- Study hours is the second strongest factor (r = 0.45)
- Gender has virtually no effect on exam performance
- Higher parental involvement leads to slightly better scores

## Setup Instructions
1. Install dependencies: `pip install pandas sqlalchemy mysql-connector-python matplotlib seaborn scikit-learn`
2. Run `scripts/clean.py` to generate the cleaned dataset
3. Run `scripts/load_to_mysql.py` to load data into MySQL
4. Run `visualizations/visualize.py` to generate charts