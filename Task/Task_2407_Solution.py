import mysql.connector as connection
import csv
import logging

logging.basicConfig(filename='logg.log', level=logging.DEBUG)

try:
    logging.info('Connecting Mysql Database')
    db = connection.connect(host='localhost',user='root',passwd='admin02')
    cursor = db.cursor()
except Exception as e:
    logging.error(e)


cursor.execute('create database if not exists Mysql_Exercise')

logging.info('Performing task 1 and 2 creating tables and bulk load')

try:
    logging.info('Creating Table for Attribute Dataset')
    s = 'create table if not exists mysql_exercise.attribute_data (Dress_id int ,Style varchar(30) ,' \
        'Price varchar(30),' \
        ' Rating decimal (2,1),' \
        'Size varchar(30),' \
        'Season varchar(30),' \
        'Neckline varchar(30),' \
        'SleeveLength varchar(30), ' \
        'Waiseline varchar(30),' \
        'Material varchar(30),' \
        ' FabricType varchar(30),' \
        ' Decoration varchar(30) ,' \
        ' PatternType varchar(30),' \
        ' Recommendation int)'
    cursor.execute(s)

except Exception as e:
    logging.error(e)

try:
    logging.info('Creating Table for Dress Sales')
    s1 = 'create table if not exists mysql_exercise.Dress_Sales(dress_id int , \
        `29/8/2013` int ,  \
        `31/8/2013` int , \
        `2/9/2013` int , \
        `4/9/2013` int , \
        `6/9/2013` int, \
        `8/9/2013` int, \
        `10/9/2013` int , \
        `12/9/2013` int , \
        `14/9/2013` int , \
         `16/9/2013` int , \
        `18/9/2013` int ,  \
        `20/9/2013` int , \
        `22/9/2013` int , \
        `24/9/2013` int ,\
        `26/9/2013` int , \
        `28/9/2013` int , \
        `30/9/2013` int , \
        `2/10/2013` int , \
        `4/10/2013` int , \
         `6/10/2013` int , \
        `8/10/2013` int , \
        `10/10/2013` int , \
         `12/10/2013` int) '


    cursor.execute(s1)

except Exception as e:
    logging.error(e)


try:
    logging.info('Inserting Data into Table attribute_data')
    with open("Attribute DataSetc.csv") as csv_file:
        csvfile = csv.reader(csv_file,delimiter=',')
        all_values = []
        for row in csvfile:
            value =(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
            all_values.append(value)

    query = "insert into mysql_exercise.attribute_data (`Dress_ID`, \
            `Style`, \
            `Price`, \
            `Rating`, \
            `Size`, \
            `Season`, \
            `NeckLine`, \
            `SleeveLength`, \
            `waiseline`, \
            `Material`, \
            `FabricType`, \
            `Decoration`, \
            `PatternType`, \
            `Recommendation`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cursor.executemany(query,all_values)
    db.commit()

except Exception as e:
    logging.error(e)


# cursor.execute("LOAD DATA INFILE '\Dress Salesc.csv' INTO TABLE dress_sales,'
#                'FIELDS TERMINATED BY `,`,'
#                'ENCLOSED BY '"' ,'
#                "LINES TERMINATED BY `\r\n`,"
#                'IGNORE 1 LINES'")

try:
    logging.info('Inserting Data into Table dress_sales')
    with open("Dress Salesc.csv") as csv_file1:
        csvfile1 = csv.reader(csv_file1,delimiter=',')
        all_values1 = []
        for row in csvfile1:
            value1 =(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23])
            all_values1.append(value1)

    query1 = "insert into mysql_exercise.dress_sales (dress_id  , \
         `29/8/2013`  ,  \
         `31/8/2013` , \
         `2/9/2013`  , \
         `4/9/2013`  , \
         `6/9/2013` , \
         `8/9/2013` , \
        `10/9/2013` , \
         `12/9/2013`  , \
        `14/9/2013`  , \
          `16/9/2013`  , \
        `18/9/2013`  ,  \
        `20/9/2013`  , \
        `22/9/2013`  , \
        `24/9/2013`  ,\
        `26/9/2013`  , \
        `28/9/2013`  , \
        `30/9/2013`  , \
        `2/10/2013`  , \
        `4/10/2013`  , \
        `6/10/2013`  , \
        `8/10/2013`  , \
        `10/10/2013` , \
         `12/10/2013`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cursor.executemany(query1,all_values1)
    db.commit()
except Exception as e:
    logging.error(e)
