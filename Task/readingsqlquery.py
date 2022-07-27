import mysql.connector as connection
import pandas as pd

db = connection.connect(host='localhost',user='root',passwd='admin02')
cursor = db.cursor()
print(db)

sql_query1 = pd.read_sql('select * from mysql_exercise.attribute_data_v2',db)

attribute_data_v2 = pd.DataFrame(sql_query1, columns = ['dress_id', 'style', 'price','rating','size','season','neckline',
                                        'sleevelength','waiseline','material','fabrictype','decoration',
                                        'patterntype','recommendation'])

print(attribute_data_v2)