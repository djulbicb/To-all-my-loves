# https://www.youtube.com/watch?v=vmEHCJofslg
# pip install pandas

import pandas
import pandas as pd
from pandas import DataFrame

data: DataFrame = pandas.read_csv("pokemon_data.csv")
# za exel file.             pandas.read_excel("pokemon.data...")
# za tab seperated file     pandas.read_csv("pokemon_data.csv", delimiter='\t')

# pocetak i kraj
print(data.head(2))
print(data.tail(2))

# Print Headers
print(data.columns)

# Read columns
print(data["Name"][0:5])
print(data.Name[0:5])
print(data[["Name", "Type 1", "HP"]][0:3])

print("===>>> Read Each Row")
# Read Each Row
print(data.iloc[1:3])                       # filter by index
print(data.loc[data['Type 1'] == 'Fire'])   # filter by condition

for index, row in data.iterrows():
    print(row.Name, row["Name"])

# Sorting/Describing
data.describe()
# data.sort_values("Name")
data.sort_values(["Type 1", "Name", "HP"], ascending=False)
print(data)

# Generates new column
data["Total"] = data["HP"] + data["Attack"]
print(data)

# Drop column and create in a diff way
data = data.drop(columns=["Total"])
data["Total"] = data.iloc[:, 4:10].sum(axis=1)

# Rearrahge columns
cols = list(data.columns.values)
data = data[cols[0:4] + [cols[-1]] + cols[4:12]]
print(data)
data.to_csv("modified.csv", index=False)
# data.to_excel("modified.exel")
# data.to_csv("modified.csv", index=False, sep="\t")

# Filtering data
data.loc[data["Type 1"] == "Grass"]
new_data:DataFrame = data.loc[(data["Type 1"] == "Grass") & (data["Type 2"] == "Poison") & (data["HP"] > 70)]
new_data.reset_index(drop=True, inplace=True) # by default old indexed are saved
new_data.to_csv("filtered.csv")
print(new_data)

# Filter by string contains
filter_mega = data.loc[data["Name"].str.contains("Mega")]
filter_mega = data.loc[~data["Name"].str.contains("Mega")] # za invert je ~ a ne !
print(filter_mega)

import re
filter_mega = data.loc[data["Name"].str.contains("Fire|Gras", regex=True)]
filter_mega = data.loc[data["Name"].str.contains("Fire|Gras", regex=True, flags=re.I)] # re.I je case insensitive
# sve koji pocinju sa pi
filtered = data.loc[data["Name"].str.contains("^pi[a-z]*", regex=True, flags=re.I)]
print(filtered)

# Conditional changes
# data.loc[data["Type 1" == "Fire", "Type 1"] = "Flamer"
# data.loc[data["Type 1" == "Fire", "Legendary"] = "True" # druga kolona je ona koja ce se promeniti

# Ako je total vece od 500, kolone gen i leg ce imati
data.loc[data["Total"] > 500, ["Generation", "Legendary"]] = "TEST VALUES"
data.loc[data["Total"] > 500, ["Generation", "Legendary"]] = ["Test 1", "Test 2"]


# Agregate statistics (Groupby)
grp = data.groupby(["Type 1"]).mean().sort_values("Defense", ascending=False)
print(data.groupby(["Type 1"]).count())
print(grp)

# Read big files
data = pd.read_csv("modified.csv")
# po 5 redova se cita
for df in pd.read_csv("modified.csv", chunksize=5):
    print("CHUNK")
    print(df)

new_df_with_same_colus = pd.DataFrame(columns=data.columns)
# for df in pd.read_csv("modified.csv", chunksize=5):
    # resource = data.groupby(['Type 1'].count())
    # new_df_with_same_colus = pd.concat([new_df_with_same_colus, results])




# KREIRANJE DATAFRAME
# Preko dict kreiranje
weather = {
    "day": ["1/1/2017", "1/1/2017", "1/1/2017"],
    "temp" : [32, 33, 45],
    "windspeed" : [6, 7, 2]
}
df = pd.DataFrame(weather)
print(df)

# Preko tuples
weather = [
    ("1/1/2017", "1/1/2017", "1/1/2017"),
    (32, 33, 45),
    (6, 7, 2)
]
df = pd.DataFrame(weather, columns=["day", "temperature", "event"])
print(df)

# preko mape
weather = [
    {"day": "1", "temp":2},
    {"day": "1", "temp":2},
    {"day": "1", "temp":2},
]
df = pd.DataFrame(weather)