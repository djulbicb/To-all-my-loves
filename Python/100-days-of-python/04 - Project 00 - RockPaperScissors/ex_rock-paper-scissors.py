# Choices
import hands
choices = ["rock", "paper", "scissors"]
user = "rock"
userPic = ""
pc = random.choice(choices)
pcPic = ""

# Assign graphic to choices
if (user == "rock"):
  userPic = hands.rock
elif (user == "paper"):
  userPic = hands.paper
else:
  userPic = hands.scissors

if (pc == "rock"):
  pcPic = hands.rock
elif (pc == "paper"):
  pcPic = hands.paper
else:
  pcPic = hands.scissors

print(f"User choice:\n{userPic}")
print(f"Pc choice:\n{pcPic}")

if (user == pc):
  print("Its a tie.")
elif (
      (user == "rock" and pc == "scissors")
  or  (user == "scissors" and pc == "papper")
  or  (user == "paper" and pc == "rock")
  ):
  print(f"Winner is user")
else:
  winner = "pc"
  print(f"Winner is PC")