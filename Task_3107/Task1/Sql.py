import pandas as pd
import mysql.connector as connection
from sqlalchemy import create_engine
import pymysql

db = connection.connect(host='localhost',user='root',passwd='admin02')
print(db)

cursor  = db.cursor()


cursor.execute('create database if not exists FitBitData')
cursor.execute('use FitBitData')

engine = create_engine('mysql+pymysql://root:admin02@localhost:3306/FitBitdata')

fitbit = pd.read_csv(r"D:\Python\Inue\All_Tasks\Task_3107\Task1\FitBit data.csv")

fitbit.to_sql('FitBitData',con=engine)

