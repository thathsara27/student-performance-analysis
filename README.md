# Student Performance Analysis 🎓

A data analysis project exploring factors that affect student exam performance.

## Technologies Used
- Python
- Pandas
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
- `explore.py` - Initial data exploration
- `clean.py` - Data cleaning (null handling, outlier removal)
- `load_to_mysql.py` - Load cleaned data into MySQL
- `connect_mysql.py` - MySQL connection setup

## Setup Instructions
1. Install dependencies: `pip install pandas sqlalchemy mysql-connector-python`
2. Run `clean.py` to generate the cleaned dataset
3. Run `load_to_mysql.py` to load data into MySQL