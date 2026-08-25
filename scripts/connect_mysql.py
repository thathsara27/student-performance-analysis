from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("SQL1227@")
engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost/student_performance')

print(engine)