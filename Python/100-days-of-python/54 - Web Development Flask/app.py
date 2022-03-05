# most popular frameworks are Django and Flask
# App is combo of client, server, database

# Library are tools that can be reused for functionality
# Framework is similar to library. But you call library whenver you want
# Framework is architecture which you follow, and it will call your code

# name of file must not be the same like name of library of framework
# like requests.py, and import request

# Postoji 3 nacina instalacije python stvari.
# preko pip, preko ide, preko context menu

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

# to run flask app
# on Mac
# export FLASK_APP=hello.py
# flask run

# on widnwos
# set FLASK_APP=hello.py
# flask run

# or name the file app.py


# kernel je program koji interfaces with hardware, so its the core
# OS is the shell of kernel.
# This shell can be CLI - command line interface
# And OS - GUI

# RUn code from current file
if __name__ == "__main__":
    app.run()

## __main__  # execute only if script
## __name__ name of method
import random
# print where code is now
print(random.__name__)

# Anotacija/Dekoracija dodaje dodatnu funkcionalnost na vec postojecu
# Funckije su first-class objects. Sto znaci funkcija moze biti proslednjena kao argument
# I napravis novu funkciju koja koristi ovu funkciju
def func():
    pass
def calc(calc_fun, a, b):
    calc_fun(a, b)
calc(func, 5, 10);

# Funkcije se mogu nestovati
def outer_function():
    print("Im outside")

    # samo u okviru outer_function se moze pozvati
    def nested():
        print("Im inside")

# funkcije se mogu vratiti iz druge funkcije
def outer_function():
    print("Im outside")

    # samo u okviru outer_function se moze pozvati
    def nested():
        print("Im inside")

    return nested
inner = outer_function()
inner()


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do