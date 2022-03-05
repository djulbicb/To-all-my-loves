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