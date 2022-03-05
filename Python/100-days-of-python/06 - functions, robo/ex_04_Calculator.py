# Calculator
from art import calculator_logo
print("------------CALCULATOR---------------")

def add(param1, param2):
  return param1 + param2
def subtract(param1, param2):
  return param1 + param2
def multiple(param1, param2):
  return param1 + param2
def divide(param1, param2):
  return param1 + param2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : "multiple",
  "/" : "divide"
}

def calculator():
  print(calculator_logo)
  shouldContinue = True
  param1 = float(input("First param: "))
  while(shouldContinue):
    operationInp = input("Operation + - * /: ")
    operation = operations[operationInp]
    param2 = float(input("Second param: "))

    result = operation(param1, param2)
    print(f"{param1} {operationInp} {param2} = {result}")

    nextStep = input("y - continue with result, n - start new, x - exit: ")
    if (nextStep == "y"):
      param1 = result
    elif (nextStep == "n"):
      shouldContinue = False
      calculator()
    else:
      shouldContinue = False
calculator()
