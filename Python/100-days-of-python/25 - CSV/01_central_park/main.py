import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = data[data["Primary Fur Color"] == "Black"]
gray = data[data["Primary Fur Color"] == "Gray"]
cinammon = data[data["Primary Fur Color"] == "Cinnamon"]
print(len(black), len(gray), len(cinammon))

data_dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [len(gray), len(cinammon), len(black)]
}
data = pandas.DataFrame(data_dict)
data.to_csv("output.csv")
print(data)