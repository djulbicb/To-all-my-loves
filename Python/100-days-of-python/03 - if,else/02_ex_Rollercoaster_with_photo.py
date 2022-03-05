# Rollercoaster
print("-----------------------")
print("Welcome to the rollercoaster: ")
height = 120
age = 18
if height >= 120:
  print ("You CAN ride. Wohooo")
  if (age < 12 ):
    print("Ticket is 5$")
  elif (age <= 18):
    print("Ticket is 7$")
  else:
    print("Ticket is 12$")
else:
  print ("You cant ride")

# multiple conditions - Rollercoaster with photo
print("-----------------------")
print("Welcome to the rollercoaster: ")
height = 120
age = 18
bill = 0
if height >= 120:
  print ("You CAN ride. Wohooo")
  if (age < 12 ):
    bill = 5
    print("Ticket is 5$")
  elif (age <= 18):
    bill = 7
    print("Ticket is 7$")
  elif (age >= 45 and age <= 55):
    print("Everything is going to be ok. Have a free ride on us.")
  else:
    bill = 12
    print("Ticket is 12$")

  wantsPhoto = "Y"
  if wantsPhoto == "Y":
    bill += 3

  print(f"Your bill is ${bill}")
else:
  print ("You cant ride")