# import turtle
# tim = turtle.Turtle()
# tim.write("Some text", font=("Times New Roman", 80, "bold"))

import tkinter

window = tkinter.Tk()
window.title("My window")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
label = tkinter.Label(text="I am label", font=("Ariel", 24, "bold"))
# label.pack(expand=0, side="bottom")
# label.pack()
# Updating elements after creation
label["text"] = "Changed text"
label.config(text="Text from configs")

# from tkinter import *
# Button
def btn_clicked ():
    print("I got clicked")
    label["text"] = "Button Clicked"
    inp = input.get()
    label["text"] = inp
    print(inp)

button = tkinter.Button(text="Click me", command=btn_clicked)
#button.pack() # da se pozicionira

# Entry
input = tkinter.Entry(width=10)
#input.pack()
#input.get() # get value from input

# Pack
# Pack automatski from top to bottom organizuje
# Ne mozes direkt mnogo da utices
# Umesto toga place
# Ako widget nema place ili pack ili grid, nece biti vidljiv

# label.place(x=0, y=0)
# Grid ne moze da se koristi ako se vec koriste pack ili place
label.grid(column=0, row=0)
button.grid(column=1, row=1)
input.grid(column=2, row=2)



# za izvrsavanje prozora
window.mainloop()


# Arguments with default values
def func (a=1, b=2, c=3):
    print (a, b, c)
func(b = 5) # 1 5 3

# Varargs arguments
# takodje zove se unlimeted positional arguments
def add (*args) :
    print(args)
    sum = 0
    for n in args:
        sum += n
    print(sum)
add(10, 20, 30, 40, 50) # (10, 20, 30, 40, 50) <class 'tuple'>

# **kwargs: Double asterix
# to su keyword arguments, unlimited keyword arguments
# Unlimited keywords
# def calculate (**kwargs) :
def calculate (n, **kwargs) :
    print(">>>", kwargs) # {'add': 3, 'multiple': 5}
    for key,value in kwargs.items():
        print(key, value)
calculate(10, add=3, multiple=5)

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"] # baca exception ako nije definisan
        self.make = kw.get("make") # ne baca exception ako nije definisan
        self.sears = kw.get("model")

car = Car(make="Nissan", model="sss")
print(car.make)