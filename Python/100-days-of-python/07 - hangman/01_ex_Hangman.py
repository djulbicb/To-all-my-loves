stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
import art
from replit import clear

endOfGame = False
badAttempsLeft = 6
words = ["bee", "storm", "rome", "pompeii", "athena"]
chosenWord = random.choice(words);

print(art.logo)
print(f"Picked word is {chosenWord}")

letters = []
for i in range(0, len(chosenWord)):
  letters.append("_")

while not endOfGame :
  print(stages[badAttempsLeft])
  print(letters)
  guess = input("Guess a letter: ").lower()
  clear()
  correct = False
  for i in range(len(chosenWord)):
    iter = chosenWord[i]
    if iter == guess:
      letters[i] = iter
      correct = True

  if correct == False:
      badAttempsLeft -= 1
      print(f"Bad. Attempts left {badAttempsLeft}")

  if "_" not in letters or badAttempsLeft <= 0:
    endOfGame = True

if "_" in letters:
  print("You lose. Word was " + chosenWord)
else:
  print("You win " + chosenWord)



