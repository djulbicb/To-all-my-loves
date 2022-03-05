# Pizza delivery
print("-----------------------")
print("Welcome to Python Pizza")
size = "S" # input("What size do you want S M L")
optPepperoni = "Y" # input(you want pepperoni Y N)
optCheese = "Y" # input("Want extra cheese Y N")

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if optPepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if optCheese == "Y":
  bill += 1

print(f"Your bill for pizza is {bill}")