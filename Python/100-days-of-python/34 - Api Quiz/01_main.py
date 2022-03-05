from Ui import *
from Quiz import *
from Data import results
import html

questions = []
for qr in results:
    q = Question(html.unescape(qr["question"]), bool(qr["correct_answer"]))
    questions.append(q)

quiz = Quiz(questions)
ui = UI(quiz)
