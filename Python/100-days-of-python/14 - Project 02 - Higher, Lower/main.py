from data import data
from art import logo, vs
import random

print(logo)

def playGame():
  first = random.choice(data)

  keepGoing = True
  score = 0
  while keepGoing:
    second = random.choice(data)
    while (first['name'] == second['name']):
      second = random.choice(data)

    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}");
    print(vs)
    print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}");

    choice = input("Who has more?: 'A' or 'B': ").lower();
    if choice == 'a':
      if (first['follower_count'] > second['follower_count']):
        keepGoing = True
        first = second
        score += 1
      else:
        keepGoing = False
        print("Wrong choice")
    else:
      if (first['follower_count'] < second['follower_count']):
        keepGoing = True
        first = second
        score += 1
      else:
        keepGoing = False
        print("Wrong choice")

    print(f"Score is: {score}")
    print("-----------------")

# MAIN
# ---------------------------------
keepPlay = True
while keepPlay:
  playGame()

  if input("One more game?") == 'N':
    keepPlay = False
print("Bye :)")



