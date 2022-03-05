# Love calculator - "".lower() "".count('a')
print("-----------------------")
trueLove = "true love"
name1 = "Angela" # input("whats your name")
name2 = "Damiena" # input("whats their name")
combinedName = (name1 + name2).lower()
t = combinedName.count("t")
r = combinedName.count("r")
u = combinedName.count("u")
e = combinedName.count("e")
true = t + r + u + e

l = combinedName.count("l")
o = combinedName.count("o")
v = combinedName.count("v")
e = combinedName.count("e")
love = l + o + v + e

loveScore = int(str(true) + str(love))
if (loveScore < 10) or (loveScore > 90):
  print(f"Your love score is {loveScore}, you go together like coke and menthos")
elif (loveScore >= 40 and loveScore <= 50):
  print(f"Your score is {loveScore}. You are alright together")
else:
  print(f"Your score is {loveScore}")

