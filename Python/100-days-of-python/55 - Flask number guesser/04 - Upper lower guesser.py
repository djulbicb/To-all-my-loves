from flask import Flask
import random

app = Flask(__name__)
number:int = -1;
@app.route("/")
def start_game():
    global number
    number = random.randint(1, 10)
    print(number)
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:guesse>")
def guesse(guesse:number):
    global number

    print(number, guesse)
    if (number == -1):
        return "<h1'>First start the game</h1>"
    if number == guesse:
        number = random.randint(1, 10)
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif number > guesse:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif number < guesse:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)


# SOLUTION 2
from flask import Flask
from random import randint

app = Flask(__name__)

winner_number = randint(0, 9)


def checker_decorator(fn):
    def wrap(number):
        if int(number) == winner_number:
            return fn(number)
        elif int(number) < winner_number:
            return '<h1>Too low!</h1>' \
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" height="200">'
        else:
            return '<h1>Too high!</h1>' \
                   '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" height="200">'

    return wrap


@app.route('/')
def greetings():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" height="200">'


@app.route('/<number>')
@checker_decorator
def congratulations(number):
    return f'<h1>Correct! The chosen number was:{number}</h1>' \
           f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" height="200">'


if __name__ == "__main__":
    app.run(debug=True)