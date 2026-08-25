import pandas as pd

df = pd.read_csv('StudentPerformanceFactors.csv')

# Fill missing values in these 3 columns with the mode
for col in ['Teacher_Quality', 'Parental_Education_Level', 'Distance_from_Home']:
    df[col] = df[col].fillna(df[col].mode()[0])

# Cap the one outlier at 100
df['Exam_Score'] = df['Exam_Score'].clip(upper=100)

df.to_csv('student_performance_clean.csv', index=False)
# Confirm it worked
print(df.isnull().sum().sum()) 
print(df['Exam_Score'].max())

