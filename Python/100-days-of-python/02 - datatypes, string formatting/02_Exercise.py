# print(len(1234)) # TypeError

# We need to learn about datatypes
# String

print("Hello"[1]) # subscripting, pulling out character
print("123" + "456") # konkatenacija stringa

# Integer - whole numbers
print(123 + 456)
num = 120_456_777
print(num)

# Float 
3.145798

# Boolean - to respond accordingly
True
False

num_char = 10
print(type(num_char)) # class int

# type casting, type changing
num_char = 10
new_num_char = str(10)
print(type(new_num_char)) # class str
print(type(int("10"))) # class int
print(type(123.5)) # class float
print(70 + float("100.5"))

# Assigment - enter two digit number
inp = input("Enter two digits: ");
first = int(inp[0]);
second = int(inp[1]);
res = first + second;
msg = str(first) + " + " + str(second) + " = " + str(res)
print(msg)

3+5
7-4
3*2
print(type(6/3)) # class float, not int
3**2 # exponent

# PEMDAS
# () ** * / + -
# thony
# 3*3 + 3/3 - 3

# BIM Calculator
height = float(input("Enter height in m: "));
weight = float(input("Enter weight in kg: "));
bmi = weight / (height ** 2);
print(int(bmi));
print(round(bmi));
print(round(bmi, 2));
print(4/2); # uvek vraca float rezultat
print(8 // 3); # automatski radi floor. Cak vraca integer

# shorthand
result = 4/2
result /= 2
print(result)
# User scores a point
score = 0;
score += 1
print("Your score is " + str(score));
#f-string
print(f"Your score is {score} and some other var {bmi}")

# Life calculator
age = int(input("What is your current age? "));
dayInYear = 365;
weekInYear = 52;
monthInYear = 12;

cDayInYear = age * dayInYear;
cWeekInYear = age * weekInYear; 
cMonthInYear = age * monthInYear; 

maxAge = 90;
maxDayInYear = maxAge * dayInYear;
maxWeekInYear = maxAge * weekInYear; 
maxMonthInYear = maxAge * monthInYear; 

print(f"Currently you have {maxAge - age} years left, {maxDayInYear - cDayInYear} days left, {maxMonthInYear - cMonthInYear} month left, {maxWeekInYear - cWeekInYear} weeks left.")
# Currently you have 58 years left, 21170 days left, 696 month left, 3016 weeks left.


# 
print("Welcome to the tip calculator")
totalBill = float(input("What was the total bill?: "))
tipPercentage = int(input("How much tip? 10% 12% 15%: "))
peopleCount = int(input("How many people split: "))
billPerPerson = (totalBill + (totalBill * tipPercentage / 100)) / peopleCount
fAmount = round(billPerPerson, 2)
fAmount = "{:.2f}".format(billPerPerson)
print(f"Each person should pay ${fAmount}")

