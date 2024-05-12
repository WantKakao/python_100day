# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data["condition"])
# print(data.condition)
# print(data_dict["condition"])
# print(data_dict.condition)

# temp_list = data["temp"].to_list()
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
#
# print(max(temp_list))
# print(data["temp"].max())
#
# print(data["condition"])

# print(data[data.day == "Monday"].temp)
# print(type(data[data.day == "Monday"].temp))
# print(int(data[data.day == "Monday"].temp) * 9/5 + 32)
# print(int(data[data.day == "Monday"].temp.iloc[0]) * 9/5 + 32)
# print(data[data.temp == data.temp.max()])

data_dict = {
    "students": ["Yuna", "Wonyoung", "Jiwoo"],
    "scores": ["100", "98", "95"]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")