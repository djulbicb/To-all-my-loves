from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# =============================================
# Mechanics
# =============================================
def save():
    website = inpWebsite.get()
    email = inpUsername.get()
    password = inpPassword.get()

    if (len(email) == 0 or len(password) ==0):
        messagebox.showinfo(title="Warning", message="Cant save empty field")
        return

    is_ok = messagebox.askokcancel(title="Saving passwords...", message="Do you want to save")

    if is_ok:
        with open(file="data.txt", mode="a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        clear_input()

def clear_input():
    inpWebsite.delete(0, END)
    inpPassword.delete(0, END)

def generatePassword():
    inpPassword.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(numbers) for _ in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    pasword = "".join(password_list)

    inpPassword.insert(0,pasword)
    pyperclip.copy(pasword)

# =============================================
# UI
# =============================================

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Input: Website
# =============================================
lblWebsite = Label(text="Website:")
lblWebsite.grid(column=0, row=1)
inpWebsite = Entry(width=35)
inpWebsite.grid(column=1, row=1, columnspan=3)

# Input: Username
# =============================================
lblUsername = Label(text="Email/Username:")
lblUsername.grid(column=0, row=2)
inpUsername = Entry(width=35)
inpUsername.grid(column=1, row=2, columnspan=3)
inpUsername.insert(0, "bojan:3")

# Input: Password
# =============================================
lblPassword = Label(text="Password:")
lblPassword.grid(column=0, row=3)
inpPassword = Entry(width=21)
inpPassword.grid(column=1, row=3)
btnPassword = Button(text="Generate Password", command=generatePassword)
btnPassword.grid(row=3, column=2)

# Input: Add
# =============================================
btnAdd = Button(text="Add", width=10, command=save)
btnAdd.grid(row=4, column=1, columnspan=2)

window.mainloop()

