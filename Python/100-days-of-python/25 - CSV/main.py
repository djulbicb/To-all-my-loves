# Vanilla read
with open("weather-data.csv") as file:
    data = file.readlines()
    print(data)


# CSV reader built in
import csv

temperatures = []
with open("weather-data.csv") as file:
    data = csv.reader(file)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
print(temperatures) # so much fluff


# Pandas
# za brzu obradu csv podataka
import pandas

data = pandas.read_csv("weather-data.csv")
# get data. Case sensitive
temp = data["temp"]
temp = data.temp

print(type(data), type(temp))
# Dataframe and Series. Dataframe je ceo sheet. Series je kolona

data_dict = data.to_dict()
print(data_dict)

# Average of temperature
temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
print(temp_list, average)
# ili jos lakse
print(data["temp"].mean())  # izracuna prosecnu vrednost
print(data["temp"].max())   # izracuna max

# Ged Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Create dataframe from scratch, generated in python
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [10, 12, 9]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("path.csv")