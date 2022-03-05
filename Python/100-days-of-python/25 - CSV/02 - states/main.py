from turtle import Turtle, Screen
# turtle dozvoljava samo gif slike

def clicked(x, y):
    print(x, y)

class State:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

from turtle import Turtle
import pandas

FONT = ("Courier", 12, "normal")
states = {}
guesses_states = []

# Read all states
csv = pandas.read_csv("50_states.csv")
for row in csv.iterrows():
    states[row[1].state.lower()] = State(name=row[1].state, x=row[1].x, y=row[1].y)
print(states)

# Window setup
turtle = Turtle()
screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.onscreenclick(clicked)

# Game loop
def print_missed_countries():
    data_dict = []
    print(guesses_states)
    for name in states:
        if name not in guesses_states:
            data_dict.append(name)

    pandas.DataFrame(data_dict).to_csv("missed.csv")
    pass


while len(guesses_states) < 50:
    answer = screen.textinput(f"States {len(guesses_states)}/50", "Name a state: ")
    if answer is None or answer.lower() == "exit":
        print_missed_countries()
        break

    answer = answer.lower()
    if answer in states:
        guesses_states.append(answer)
        state = states[answer]
        turtle.goto((state.x, state.y))
        turtle.write(f"{state.name}", align="left", font=FONT)

screen.mainloop()
