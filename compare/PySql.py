import pandas as pd
from sqlalchemy import create_engine
import pymysql

df = pd.read_excel('prince.xlsx')
cnx = create_engine('mysql+pymysql://prince:kirad@localhost/exceldb') 
df.to_sql('exceltable', if_exists='append', con=cnx, index=False)



