# Read
# -------------------------------------
# Open and read file
file = open("text.txt")
print(file.read())
file.close()

# da ne bi rucno zatvarao file moze ovako
# kao try-catch resource
with open("text.txt") as file:
    contents = file.read()
    print(contents)

# Write, by default is read-only
# -------------------------------------
with open("text.txt", mode="w") as file:
    file.write("New text")

with open("text.txt", mode="a") as file:
    file.write("\nNew text append")

with open("new_file.txt", mode="a") as file:
    file.write("If doesnt exist, it will create it")


# Methods
# file.readlines() - read all lines. Imace \n na kraju pa moze strip()
# "text banana".replace("banana", "apple")
# "    banana    ".strip() - kao trim()
