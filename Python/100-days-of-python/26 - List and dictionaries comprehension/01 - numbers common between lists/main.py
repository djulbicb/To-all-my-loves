def read_file_as_list(file_name) :
    with(open(file_name)) as file:
        contents = file.readlines() # contents.split("\n")
        lines = [int(line) for line in contents]
        return lines

text01 = read_file_as_list("01.txt")
text02 = read_file_as_list("02.txt")

common_numbers = [item for item in text01 if item in text02]
print(f"Common numbers are {common_numbers}.")