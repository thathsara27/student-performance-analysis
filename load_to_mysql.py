import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("SQL1227@")
engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost/student_performance')

df = pd.read_csv('student_performance_clean.csv')

df.to_sql('students', engine, if_exists='replace', index=False)

print("Done. Rows loaded:", len(df))