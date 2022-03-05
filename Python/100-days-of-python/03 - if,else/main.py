# conditional
if True:
  print("True")
else:
  print("False")

# Operatori
# > >= < <= == != %

# Even or not even
print("-----------------------")
num = 21
modulo = num%2
if modulo == 0:
  print("Its even")
else:
  print("Its not even")

# Leap year
print("-----------------------")
year = 2500
if (year % 4 == 0):
  if (year % 100 == 0):
    if (year % 400 == 0):
      print(f"{year} is leap year")
    else:
      print(f"{year} is not leap year")
  else:
    print(f"{year} is leap year")
else:
  print(f"{year} is not leap year")

# Logical operators
print("-----------------------")
a = 12
if a>10 and a<13:
  print("AND")
elif a>10 or a<13:
  print("OR")
elif not a>15:
  print("NOT")
else:
  print("nope")

print("-----------------------")
print("Through strugle and flex you become better coder")

