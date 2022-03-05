# Declare a function
# -------------------------------------------------------------
def my_function():
  print("Hello")
  print("Sunny")
my_function()

# argument i parametar
# -------------------------------------------------------------
# parametar je naziv ulazne informacije tipa name, location...
# argument je konkretna informacija koja ulazi Bojan, Berlin
# poslednji parametar je sa default vrednoscu
def function(name, location, test=110):
    print(f"Hello {name}")
    print(f"Welcome to {location}")
    print(f"{test}")

# Argumenti mogu da se proslede na osnovu pozicije i nazive
# positional vs keyword argument
function("Bojan", "Berlin")
function(location="Amsterdam", name="Bojan")

# Output parametri
# -------------------------------------------------------------
# function with outputs
def function(param):
  return param + str(1)

# function with multiple outputs
def function(param):
  return param + str(1), 456

firstOut, secondOut = function("s")
print(firstOut)

# example
def formatName (fName, lName):
  if (fName == "" or lName == ""):
    return "" # "You didnt provide valid inputs"

  return f"{fName.title()} {lName.title()}"

formated = formatName("bojan", "djulbic")
print(formated)

"""
Ovo se koristi kao multiline koment ali nije docstring jer nije u metodi. Ne preporucuje se, bolje vise #
"""
def isLeap(year):
  """This is docstring:
  Returns boolean if year is leaf"""
  if year%4 == 0:
    if year%100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True

  return False

def daysInMonth(year, month):
  if month > 12 or month < 1:
    return "Invalid month"
  if year < 0:
    return "Invalid year"

  if isLeap(year) and month == 2:
    return 29
  else:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month -1 ]

print(daysInMonth(2003,2))

# Arguments with default values
##########################################
def func (a=1, b=2, c=3):
    print (a, b, c)
func(b = 5) # 1 5 3

# Varargs arguments
##########################################
def add (*args) :
    print(args)
    sum = 0
    for n in args:
        sum += n
    print(sum)
add(10, 20, 30, 40, 50) # (10, 20, 30, 40, 50) <class 'tuple'>

# Method arguments datatype
# To se zove TypeHints
##########################################
def check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
def greet(name:str) -> str:
    return "Hello " + name