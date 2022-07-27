import logging

import mysql.connector as connection
import csv
import pandas as pd
import pymongo
import logging

logging.basicConfig(filename='logg.log', level=logging.DEBUG)

db = connection.connect(host='localhost',user='root',passwd='admin02')
cursor = db.cursor()


cursor.execute('use mysql_exercise')
try:
    logging.info('Performing Task 3 loading table in Pandas DataFrame')
    sql_query1 = pd.read_sql('select * from mysql_exercise.attribute_data',db)
    attribute_data = pd.DataFrame(sql_query1, columns = ['dress_id', 'style', 'price','rating','size','season','neckline',
                                            'sleevelength','waiseline','material','fabrictype','decoration',
                                            'patterntype','recommendation'])
    #print(attribute_data)

    sql_query2 = pd.read_sql('select * from mysql_exercise.dress_sales', db)
    dress_sales = pd.DataFrame(sql_query2, columns = ['dress_id','29/8/2013', '31/8/2013', '2/9/2013','4/9/2013','6/9/2013','8/9/2013','10/9/2013',
                                         '12/9/2013','14/9/2013','16/9/2013','18/9/2013','20/9/2013','22/9/2013','24/9/2013'
                                         ,'26/9/2013','28/9/2013','30/9/2013','2/10/2013','4/10/2013','6/10/2013',
                                         '8/10/2013','10/10/2013','12/10/2013'])
    #print(dress_sales)

except Exception as e:
    logging.error(e)


try:
    logging.info('Performing Task 4 convert to json')
    attribute_data.to_json('attribute_jsn.json')
except Exception as e:
    logging.error(e)


try:
    logging.info('Performing Task 6 ...Left Join')
    left_join = 'select * from mysql_exercise.attribute_data left join mysql_exercise.dress_sales on mysql_exercise.attribute_data.dress_id =  mysql_exercise.dress_sales.dress_id'
    # cursor.execute(left_join)
    # for i in cursor.fetchall():
    #      print(i)
except Exception as e:
    logging.error(e)

try:
    logging.info('Performing Task 7 ....no of Distinct dress ')
    cursor.execute("select count(distinct Dress_id) from attribute_data")
    for i in cursor.fetchall():
        print(i)
except  Exception as e:
    logging.error(e)


try:
    logging.info('Performing Task 8...NO of dresses having rec = 0')
    cursor.execute('select (count(recommendation)) from attribute_data where recommendation = 0')
    print(cursor.fetchall())
except Exception as e:
    logging.error(e)

try:
    logging.info('Performing task 9....Sum of dress sales for each dress id')
    cursor.execute('select dress_id, `29/8/2013` + `31/8/2013` + `2/9/2013` + `4/9/2013` + `6/9/2013` + `8/9/2013` + `10/9/2013` + `12/9/2013` + `14/9/2013` + `16/9/2013` + `18/9/2013` + `20/9/2013` + `22/9/2013` + `24/9/2013` + `26/9/2013` + `28/9/2013` + `30/9/2013` + `2/10/2013` + `4/10/2013` + `6/10/2013` + `8/10/2013` + `10/10/2013` + `12/10/2013` as Total from dress_sales')
    for i in cursor.fetchall():
        print(i)

except Exception as e:
    logging.error(e)

