import pandas as pd
df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
count_df = pd.DataFrame(df.groupby(['Primary Fur Color']).size())
count_df.columns =[['Count']]
print(count_df)
count_df.to_csv('count.csv')








# data = pd.read_csv('weather_data.csv')
# print(type(data['temp']))
# temp_list= data['temp'].to_list()
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data[data['temp']==data['temp'].max()])

# monday= data[data.day=='Monday']
# print((monday.temp*9/5)+32)
# data_dict = {
#     "students":["Harsh","Max","Ram"],
#     "scores":[50,50,50]
# }
# df = pd.DataFrame(data_dict)
# print(df)
# df.to_csv('df.csv')
