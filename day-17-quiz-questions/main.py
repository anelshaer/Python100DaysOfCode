from data import  question_data
from question_model import Question
from quiz_brain import QuizBrain

def questions_bank(list_questions_data):
    question_bank = []
    for question_data in list_questions_data:
        question_object = Question(question_data['question'], 
            question_data['correct_answer'])

        question_bank.append(question_object)
    return question_bank


quiz_brain = QuizBrain(questions_bank(question_data))

while quiz_brain.still_has_question():
    quiz_brain.next_question()

quiz_brain.print_results()