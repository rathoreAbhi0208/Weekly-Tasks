import pymongo
import json
import pandas as pd


client = pymongo.MongoClient("mongodb+srv://Abhi:abhi02@cluster0.ozaps66.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

db = client['FitBit']
collection = db['FitBitData']

df = pd.read_csv(r"D:\Python\Inue\All_Tasks\Task_3107\Task1\FitBit data.csv")

jsn = df.to_json('Fitbitjson.json')

with open(r"D:\Python\Inue\All_Tasks\Task_3107\Task1\Fitbitjson.json") as file:
    file_data = json.load(file)

collection.insert_one(file_data)
