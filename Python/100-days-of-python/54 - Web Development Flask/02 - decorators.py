import time

def function_decorator(function):
    def wrapper():
        print("decorator")
        time.sleep(2)
        function()
    return wrapper

@function_decorator
def calc():
    print("Calc")

calc()

wrapped = function_decorator(calc)
wrapped()
