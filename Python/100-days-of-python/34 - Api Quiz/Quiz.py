from typing import List
from Question import Question

class Quiz:

    def __init__(self, p_questions:List[Question]):
        self.questions = p_questions
        self.index = 0
        pass

    def answer(self, p_answer):
        return self.questions[self.index].answer == p_answer

    def has_more_questions(self) -> bool:
        print(self.index, len(self.questions) - 1)
        return self.index < (len(self.questions) - 1)

    def next_question(self) -> Question:
        question = self.questions[self.index]
        self.index+=1
        return question