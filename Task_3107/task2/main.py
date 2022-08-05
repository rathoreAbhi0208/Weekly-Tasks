import pandas as pd
import xlrd

# 1. Loading Datasets in Pandas
orders_data = pd.read_excel(r"D:\Python\Inue\All_Tasks\Task_3107\task2\Superstore_USA.xlsx",sheet_name='Orders')
returns_data = pd.read_excel(r"D:\Python\Inue\All_Tasks\Task_3107\task2\Superstore_USA.xlsx",sheet_name='Returns')
user_data=pd.read_excel(r"D:\Python\Inue\All_Tasks\Task_3107\task2\Superstore_USA.xlsx",sheet_name='Users')

#4. Join orders and returns in pandas
order_returns = pd.merge(orders_data,returns_data)
print(order_returns['Order ID'])

#3. How many Returns Received with product ID
print(order_returns[(order_returns['Status']=='Returned')]['Order ID'])

#5. No of Unique ID's
print(orders_data['Customer ID'].nunique())

#6. No of regions with Managers
print(user_data)
print(orders_data['Region'].nunique())

#7. differnet shipement mode that we have and what is a percentage usablity of all the shipment mode with respect to dataset
ship_modes = orders_data['Ship Mode'].value_counts()
total_ship = orders_data['Ship Mode'].value_counts().sum()
print(( (ship_modes) / (total_ship) *100 ).to_frame())

#8. new coulmn and try to find our a diffrence between order date and shipment date
orders_data['Diff_Date'] = orders_data['Ship Date'] - orders_data['Order Date']

#9. which order id we have shipment duration more than 10 days
print(orders_data[orders_data['Diff_Date'].dt.components['days']>15])

#11. Group by region and find out which region is more profitable
print(orders_data.groupby(['Region'])['Profit'].aggregate('count').reset_index().sort_values("Profit",ascending = True))

#13.list of unique postal code
print(orders_data['Postal Code'].unique())

#14. customer segement is more profitalble find it out
print(orders_data.groupby(['Customer Segment'])['Profit'].aggregate('count'))

#15. try to find out the 10th most loss making product catagory
print(orders_data[orders_data['Profit']<0].sort_values('Profit',ascending=True).head(10))