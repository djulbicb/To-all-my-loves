from tkinter import *

def clicked():
    miles = float(inpMiles.get())
    km = round(miles * 1.689)
    lblKmOut["text"] = km
    lblKmOut.config(text=km)

window = Tk()
pad = 5
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)

lblIsEqual = Label(text="is equal to", padx=pad, pady=pad)
lblIsEqual.grid(row=1, column=0)

btnCalc = Button(text="Calculate", padx=pad, pady=pad, command=clicked)
btnCalc.grid(row=3, column=1)

inpMiles = Entry()
inpMiles.grid(row=0, column=1)

lblMiles = Label(text="Miles", padx=pad, pady=pad)
lblMiles.grid(row=0, column=3)

lblKmOut = Label(text="_", padx=pad, pady=pad)
lblKmOut.grid(row=1, column=1)

lblKm = Label(text="Km", padx=pad, pady=pad)
lblKm.grid(row=1, column=3)

window.mainloop()

