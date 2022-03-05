import pandas

data = pandas.read_csv("data.txt")
alphabet = {value.letter:value.code for (key,value) in data.iterrows()}
print(alphabet)

word = "Bojan" #input("Enter a word")
for letter in word:
    print(letter)

output = [alphabet[letter.upper()] for letter in word]
print(output)
