import mysql.connector as conn
from sqlalchemy import create_engine
import pandas as pd

db = conn.connect(host='localhost',user='root',passwd='admin02')
cursor = db.cursor()

cursor.execute('create database if not exists Superstore')
cursor.execute('use Superstore')

engine = create_engine('mysql+pymysql://root:admin02@localhost:3306/Superstore')

orders_data = pd.read_excel(r"D:\Python\Inue\All_Tasks\Task_3107\task2\Superstore_USA.xlsx")
returns_data = pd.read_excel(r"D:\Python\Inue\All_Tasks\Task_3107\task2\Superstore_USA.xlsx",sheet_name='Returns')
user_data=pd.read_excel(r"D:\Python\Inue\All_Tasks\Task_3107\task2\Superstore_USA.xlsx",sheet_name='Users')

#1. Loading Dataset in SQL
orders_data.to_sql('orders',con=engine)
returns_data.to_sql('returns',con=engine)
user_data.to_sql('users',con=engine)

#4. join orders and returns in sql
join = cursor.execute('select *from orders join returns on orders.OrderId = returns.OrderId')
for i in cursor.fetchall():
     print(i)


# 5. No of unique ID's with sql
cursor.execute('select count(distinct `Customer ID`) from orders')
for i in cursor.fetchall():
     print(i)

#6. Distinct Regions using sql
cursor.execute('select count(distinct `Region`) from users')
for i in cursor.fetchall():
    print(i)

