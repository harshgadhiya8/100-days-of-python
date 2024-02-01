from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for _ in range(0,len(question_data)):
    question  = question_data[_]['text']
    answer = question_data[_]['answer']
    question_bank.append(Question(question,answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is : {quiz.score}/{len(quiz.question_list)}")