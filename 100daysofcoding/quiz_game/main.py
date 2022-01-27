from typing import List

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank: List[Question] = list()

# TODO: replace with https://opentdb.com/
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
