from question_model import Question
from data import load_question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
question_data = load_question_data()
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# type hint
# name: str
# name = 12
#
#
# def can_drive(age: int) -> bool:
#     if age > 18:
#         return True
#     else:
#         return 'hi'
#
#
# print(can_drive('hanni'))