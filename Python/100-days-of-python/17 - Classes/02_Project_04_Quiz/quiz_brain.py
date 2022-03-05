class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_question_answer):
        if correct_question_answer.lower() == user_answer.lower():
            self.score += 1
            print(f"You got it right. Your current score is {self.score}/{len(self.question_list)}")
        else:
            print("That is wrong")
        print(f"Correct answer was {correct_question_answer}. Your current score is {self.score}/{len(self.question_list)}")


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} {current_question.question} (True/False)")
        self.check_answer(user_answer, current_question.answer)
        print("\n")


