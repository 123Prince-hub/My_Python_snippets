import pandas as pd
from sqlalchemy import create_engine
import pymysql


A = pd.DataFrame(columns=('fname', 'lname', 'number', 'email'))
B = pd.read_excel('right file.xlsx', header=0, skiprows=range(1, 1000000))
C = pd.read_csv('two.csv', header=0, skiprows=range(1, 1000000))


if A.equals(B) or A.equals(C):
    df = pd.read_excel('right file.xlsx') 
    df['address'] = request.user
    print(df) #ye code usme dal ke chalaok
    cnx = create_engine('mysql+pymysql://prince:kirad@localhost/exceldb') 
    df.to_sql('exceltable', if_exists='append', con=cnx, index=False)
    
    
else:
    print('This is wrong file')




# import numpy as np
# cnx = create_engine('mysql+pymysql://prince:kirad@localhost/exceldb') 
# df.to_sql('exceltable', if_exists='append', con=cnx, index=False)
# df = pd.read_excel('right file.xlsx')
# df['UserId'] = [1, 45, 78, 69]
# print(df.head)