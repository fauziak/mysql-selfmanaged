import pandas as pd
import os
from sqlalchemy import create_engine

hostname = '34.170.157.57'
os.environ['mysql_username'] = 'fauziak_user'
os.environ['mysql_password'] = 'Mercy2020'
username = os.environ.get('mysql_username')
password = os.environ.get ('mysql_password')
print(username)
print(password)

connection_string = f'mysql+pymysql://{username}:{password}@{hostname}/db'

print(connection_string)
db = create_engine(connection_string) 
query = 'select * from users;'
result = pd.read_sql(query, con=db)
print(result)