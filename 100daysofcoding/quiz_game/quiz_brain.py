from typing import List

from question_model import Question


class QuizBrain:
    def __init__(self, question_list: List) -> None:
        self.question_number = 0
        self.question_list: List[Question] = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

        if not self.still_has_questions():
            self.print_result()

    def print_result(self):
        print("You have finished the quiz")
        print(f"Your final score is {self.score}/{self.question_number}.")

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer: str, question_answer: str) -> None:
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("You got it")
        else:
            print("That's wrong")
        print(f"The correct answer was {question_answer.lower()}")
        print(f"Your current score is {self.score}/{self.question_number}.\n")
