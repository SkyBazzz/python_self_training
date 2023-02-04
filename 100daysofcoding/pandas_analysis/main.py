import csv
from typing import List

import pandas

with open("weather_data.csv", mode="r") as data_file:
    weather_data = csv.reader(data_file)
    temperatures = list()
    [temperatures.append(int(row[1])) for row in weather_data if row[1] != "temp"]
    # print(temperatures)

data = pandas.read_csv("weather_data.csv")
temperatures: List[int] = data["temp"].to_list()
avg_temp = sum(temperatures) / len(temperatures)
# print(f"Mean value is {data['temp'].mean()}")
# print(f"Max value is {data['temp'].max()}")
# print(f"Median value is {data['temp'].median()}")
# print(f"Median value is {data.temp.median()}")
# print(data)
# print(data[data.temp == 15].day)

# Download data from https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

squirrels_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = list(set(squirrels_data["Primary Fur Color"].to_list()))[1:]
data_dict = {
    "Fur Color": fur_colors,
    "Count": [len(squirrels_data[squirrels_data["Primary Fur Color"] == color]) for color in fur_colors],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_squirrels.csv")
