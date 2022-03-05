# Ex: generate password
print("--------------------")
import random
letters = ["a", "b", "c", "d", "e", "f", "g"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "9", "9", "0"]
symbol = ["$", "%", "&"]
lenLetters = 10 # input("How many letters would you like")
lenNumbers = 3 # input("How many numbers would you like")
lenSymbol = 2 # input("How many symbols would you like")

pickedLetters = []
pickedNumbers = []
pickedSymbol = []
for i in range(0, lenLetters):
  if (random.randint(0, 1) == 1):
    pickedLetters.append(random.choice(letters))
  else:
    pickedLetters.append(random.choice(letters).upper())
for i in range(0, lenNumbers):
  pickedNumbers.append(random.choice(numbers))
for i in range(0, lenSymbol):
  pickedSymbol.append(random.choice(symbol))

picked = []
picked.extend(pickedLetters)
picked.extend(pickedNumbers)
picked.extend(pickedSymbol)
print(picked)

result = []
for i in range(0, len(picked)):
  rndIndex = random.randint(0, len(picked) - 1);
  elem = picked.pop(rndIndex)
  result.append(elem)

print(result)
random.shuffle(result) # shuffluje elemente u nizu
print(result)




