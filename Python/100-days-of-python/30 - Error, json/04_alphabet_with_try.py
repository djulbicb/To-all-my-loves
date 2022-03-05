import pandas

data = pandas.read_csv("alphabet.txt")
phonetic = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic)

word = input("Enter a word: ").upper()
try:
    output_list = [phonetic[letter] for letter in word]
except KeyError:
    print("only letters allowed")
else:
    print(output_list)
