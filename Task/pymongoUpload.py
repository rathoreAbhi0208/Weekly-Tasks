import json
import logging

import pymongo
import reading_task


client = pymongo.MongoClient("mongodb+srv://Abhi:abhi02@cluster0.ozaps66.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['DataTask']
collection = database['AttributeData']

try:
    logging.info('Performing task 5...stroing json file into mogoDB ')
    with open (r"D:\Python\Inue\Task\attribute_jsn.json") as file:
        file_data = json.load(file)

    collection.insert_one(file_data)

except Exception as e:
    logging.error(e)
