
# get template
with open("./input/letters/starting_letter.txt") as file:
    template = file.read()
    print(template)

# get names
with open("./input/names/invited_names.txt") as file:
    contents = file.read()
    names = contents.split("\n")
    print(names)

# generate letters
path = "./output/ReadyToSend/Letter_for_"
for name in names:
    contents = template.replace("[name]", name)
    file = open(path + name, mode="w")
    file.write(contents)
    file.close()

for name in names:
    stripped_name = name.strip()
    new_letter = contents.replace("[name]", name)
    with open(f"./output/ReadyToSend/{stripped_name}.txt", mode="w") as file:
        file.write(new_letter)

