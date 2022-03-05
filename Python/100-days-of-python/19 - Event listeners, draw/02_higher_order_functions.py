# Higher order function je kada se funkcija prosledi kao parametar
def add(num1, num2):
    return num1 + num2

def calculate(num1, num2, func):
    return func(num1, num2)

x = calculate(2,3,add)
print(x)