# import csv, pandas

# with open("Day_25_Pandas/weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("Day_25_Pandas/weather_data.csv")

data_dict = data.to_dict()

# print(data[data.temp == data.temp.max()])
monday= data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

