from tkinter import *
from Quiz import *

THEME_COLOR = "#375362"


# Self postaje property i dostupno je spolja
class UI:
    question: None
    score: int = 0

    def __init__(self, quiz_brain: Quiz):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR,
                                                     font=('Ariel', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.press_Accept)
        self.true_button.grid(row=2, column=1)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.press_Wrong)
        self.false_button.grid(row=2, column=0)

        self.show_next_question()

        self.window.mainloop()

    def press_Accept(self):
        print("Accept")
        if self.quiz.answer(True):
            print("Correct True")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.show_next_question)
        pass

    def press_Wrong(self):
        print("Wrong")
        if self.quiz.answer(False):
            print("Correct False")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.canvas.after(1000, self.show_next_question)
        pass

    def show_next_question(self):
        if self.quiz.has_more_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.question.question)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz done :3")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
