import pandas as pd 
from sqlalchemy import create_engine
conn_string='postgresql://postgres:admin@localhost/db1'
db=create_engine(conn_string)
conn=db.connect()

df=pd.read_csv('C:\Users\HP\OneDrive\Desktop\SQL IHUB\paintings.zip\artist')