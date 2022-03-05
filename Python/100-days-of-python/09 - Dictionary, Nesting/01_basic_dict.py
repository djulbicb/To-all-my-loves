# empty dict
dict = {}
# init dict
dict = {
  "test1" : "Some test1 value",
  "test2" : "Some test2 value",
  "test3" : "Some test3 value"
}

# get value
print (dict["test2"])
# set value
dict["test2"] = "Changed value"
print (dict["test2"])

print(dict) # printuje kao da je recnik

# da se isprazni
# dict = {}

# Iteracija
for key in dict:
  print(key) # test1, test2, test3
  print(dict[key])

# if exists
if "test1" in dict:
  print("Yes")
if "test1" not in dict:
  print("Yes")
