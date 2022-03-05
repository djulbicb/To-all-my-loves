from tkinter import *
import pandas
import random
import csv

# COLORS and FONTS
# ========================
BACKGROUND_COLOR = "#B1DDC6"
DARK_GRAY = "#333"
FONT_NAME = "Courier"

# VARS
# ========================
# words_learnt = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['Word', 'Translate'])
words_to_learn = []
words_learnt = []

# LOAD DATA
# ========================
data = pandas.read_csv("data/french_words.csv")
words = {row.word:row.translation for (index, row) in data.iterrows()}

# METHODS
# ========================
def clickRight():
    words_learnt.append([current_word[0], current_word[1]])
    write_csv()
    print("Right")
    start_timer()


def clickWrong():
    words_to_learn.append([current_word[0], current_word[1]])
    write_csv()
    print("Wrong")
    start_timer()


def write_csv():
    file_words_learnt = "words_learnt.csv"
    file_words_to_learn = "words_to_learn.csv"
    fields = ["Word", "Translation"]

    with open(file_words_learnt, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(words_learnt)

    with open(file_words_to_learn, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(words_to_learn)


current_word = None
def start_timer():
    global current_word
    current_word = random.choice(list(words.items()))

    canvas.itemconfig(canvas_text, text=current_word[0])
    ticker(3)


def ticker(count=3):
    if count == 0:
        canvas.itemconfig(canvas_text, text=current_word[1])
        canvas.itemconfig(img_card_front, image="images/card_back.png")
    if count>0:
        window.after(1000, ticker, count - 1)
        print(count)


# UI
# ========================
window = Tk()
window.title("Flash Cards")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

img_card_front = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=img_card_front)

canvas_text = canvas.create_text(390, 250, text="mercredi", fill=DARK_GRAY, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
imgWrong = PhotoImage(file="images/wrong.png")
btnWrong = Button(image=imgWrong, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=clickWrong)
btnWrong.grid(column=0, row=2)
imgRight = PhotoImage(file="images/right.png")
btnYes = Button(image=imgRight, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=clickRight)
btnYes.grid(column=1, row=2)

# Timer
start_timer()

window.mainloop()