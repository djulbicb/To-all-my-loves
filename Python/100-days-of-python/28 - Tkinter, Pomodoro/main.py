from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
# Ovo nece raditi jer se radi u GUI. Stoga tkinter ima svoj sistem window.after
# import time
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        title.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="WORK", fg=GREEN)
        count_down(work_sec)

def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if (count_sec < 10):
        # count_sec = "0" + str(count_sec)
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if (count > 0):
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "y "
        check_marks.config(text=mark)

def reset_timer():
    print("RESET")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")

    title.config(text="Timer")
    check_marks.config(text="")

    global reps
    reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# window.after(1000, count_down, 10) # treci parametar je inf positional argument

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
#
# count_down(5)

btn_start = Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.grid(column=0, row=2)

reset_start = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_start.grid(column=2, row=2)

check_marks = Label(text="y", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()