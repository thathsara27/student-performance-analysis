import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student_performance_clean.csv')

print(df.shape) 

# Chart 1: Attendance vs Exam Score 

# Step 1: Create the attendance bracket column
df['attendance_bracket'] = pd.cut(
    df['Attendance'],
    bins=[0, 69, 84, 100],
    labels=['Under 70%', '70-84%', '85%+']
)

# Step 2: Calculate average exam score per bracket
attendance_avg = df.groupby('attendance_bracket', observed=True)['Exam_Score'].mean().reset_index()

# Step 3: Draw the bar chart
plt.figure(figsize=(8, 5))
sns.barplot(data=attendance_avg, x='attendance_bracket', y='Exam_Score', hue='attendance_bracket', palette='Blues_d', legend=False)
plt.title('Average Exam Score by Attendance Bracket')
plt.xlabel('Attendance Bracket')
plt.ylabel('Average Exam Score')
plt.tight_layout()
plt.savefig('chart1_attendance_vs_score.png')
plt.show()

print("Chart 1 saved.")

# Chart 2: Study Hours vs Exam Score

# Step 1: Draw the scater plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Hours_Studied', y='Exam_Score', alpha=0.3, color='steelblue')
plt.title('Study Hours vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('chart2_studyhours_vs_score.png')
plt.show()

print("Chart 2 saved.")

# Chart 3: Exam Score Distribution by Gender

# Step 1: Draw the box plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Gender', y='Exam_Score', hue='Gender', palette='Set2', legend=False)
plt.title('Exam Score Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('chart3_gender_vs_score.png')
plt.show()

print("Chart 3 saved.")

# Chart 4: Correlation Heatmap 

# Step 1: Select only numeric columns
numeric_df = df.select_dtypes(include='number')

# Step 2: Calculate correlation between all numeric columns
correlation = numeric_df.corr()

# Step 3: Draw the heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('Correlation Heatmap - Student Performance Factors')
plt.tight_layout()
plt.savefig('chart4_correlation_heatmap.png')
plt.show()

print("Chart 4 saved.")