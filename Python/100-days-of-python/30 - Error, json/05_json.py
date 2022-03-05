import json
# write     - json.dump()
# read      - json.load()
# update    - json.update() # ja ovo nemam

data = {
    "key" : "value",
    "array" : ["Pear", 1, True],
    "obj" : {
        "key" : "value"
    }
}
# Write
with open("json.json", "w") as file:
    json.dump(data, file, indent=4)

with open("json.json") as file:
    data = json.load(file)
    print(data, data["key"]) # ucita kao mapu





