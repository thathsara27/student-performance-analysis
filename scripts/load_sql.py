import pandas as pd
import sqlite3

df = pd.read_csv('student_performance_clean.csv')

conn = sqlite3.connect('student_performance.db')