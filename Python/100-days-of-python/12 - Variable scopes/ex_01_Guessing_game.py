# Guessing game
# https://pythontutor.com/visualize.html#mode=display
print("------------GUESSING GAME--------------")
import random

guesse = "GUESSING GAME"

def getAction():
  ask = True
  actions = ["easy", "hard", "exit"]
  while(ask):
    action = input("Pick 'easy', 'hard' or 'exit': ")
    if (action in actions):
      ask = False
      return action
    else:
      print("Wrong option")

def playGame(maxGuesse):
  keepGoing = True
  pickedNumber = random.randint(0, 100)

  while keepGoing:
    userGuesse = int(input("Pick your number: "))
    if userGuesse > pickedNumber:
      print("Too high. Try again")
      maxGuesse -= 1
    elif userGuesse < pickedNumber:
      print("Too low. Try again")
      maxGuesse -= 1
    elif userGuesse == pickedNumber:
      print("Correct: You win")
      keepGoing = False

    if maxGuesse <= 0:
      keepGoing = False
      print(f"No win. Try again. Number was {pickedNumber}")

# MAIN
# ----------------------------------
keepGoing = True
while keepGoing:
  print("---------------------------")
  print(f"Welcome to {guesse}")

  action = getAction();
  if action == "easy":
    playGame(10)
  elif action == "hard":
    playGame(5)
  elif action == "exit":
    keepGoing = False
    print("exit")