import pandas as pd
import logging

logging.basicConfig(filename='fitbit.log',level=logging.DEBUG,format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

try:
    logging.info('Reading FitBit in Pandas')
    data = pd.read_csv(r"D:\Python\Inue\All_Tasks\Task_3107\Task1\FitBit data.csv")
    print(data)
except Exception as e:
    logging.error(e)

try:
    logging.info('Converting all datetime To DateTime Stamp')
    print(data.columns)
    #print(data.dtypes)

    data['ActivityDate'] = pd.to_datetime(data['ActivityDate'])

    print(data.dtypes)
except Exception as e:
    logging.error(e)

#logging.info(data)

try:
    logging.info("Getting No of Unique ID's")
    print(data['Id'].nunique())

except Exception as e:
    logging.error(e)


try:
    logging.info("Getting Most Active Id")
    data['TotalActiveMinutes'] = data['VeryActiveMinutes'] + data['FairlyActiveMinutes'] + data['LightlyActiveMinutes']

    df = data.groupby('Id',as_index=False).sum()
    print(df.sort_values('TotalActiveMinutes',ascending=False).iloc[[0]])

except Exception as e:
    logging.error(e)

try:
    logging.info("No of ID's not logged")
    print(len(data[data['TotalActiveMinutes']==0]))
except Exception as e:
    logging.error(e)


try:
    logging.info("Laziest Person on Basis of Calories Burnt")
    print(df[df['Calories']>0].sort_values('Calories',ascending=True).iloc[[0]])

except Exception as e:
    logging.error(e)


try:
    logging.info("No of Healthy Pesron On basis calories burnt")
    print("2250 Calories should be burnt daily for a heathy lifestyle")
    print(data[data['Calories']>2250]['Id'].nunique())

except Exception as e:
    logging.error(e)


try:
    logging.info("5 most Irregular Persons")
    print(df.sort_values('Calories',ascending=True)['Id'].head(5))
except Exception as e:
    logging.error(e)


try:
    logging.info("Third most active Person")
    print(df.sort_values('TotalActiveMinutes',ascending=False).iloc[[2]])
except Exception as e:
    logging.error(e)

try:
    logging.info("Fifth Most Laziest Person")
    print(df[df['Calories']>0].sort_values('Calories',ascending=True).iloc[[4]])
except Exception as e:
    logging.error(e)

try:
    logging.info("Total Accumulative Calories Burnt ")
    print(df[['Id','Calories']])
except Exception as e:
    logging.error(e)