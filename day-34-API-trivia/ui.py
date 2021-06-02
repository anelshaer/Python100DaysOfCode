from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.feedback_background_color = False
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=340, height=380)
        self.label_score = Label(text="Score: 0",
                                 bg=THEME_COLOR,
                                 fg="white",
                                 font=("Arial", 12)
                                 )
        self.label_score.grid(column=1, row=0)
        self.canvas = Canvas(width=300,
                             height=250,
                             bg="white"
                             )
        self.question_text = self.canvas.create_text(
            150, 125, 
            width=280,
            text="Qustion Goes here", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.img_true = PhotoImage(file="images/true.png")
        self.img_false = PhotoImage(file="images/false.png")
        self.button_true = Button(image=self.img_true, command=self.answer_true, highlightthickness=0)
        self.button_true.grid(column=0, row=2)
        self.button_false = Button(image=self.img_false, command=self.answer_false, highlightthickness=0)
        self.button_false.grid(column=1, row=2)
        self.next_question()
        self.window.mainloop()

    
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def check_answer(self, answer):
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)        

    def answer_true(self):
        self.check_answer("True")
    
    def answer_false(self):
        self.check_answer("False")
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(self.canvas, bg="red")
        self.window.after(900, self.clear_feedback)
    
    def clear_feedback(self):
        self.canvas.config(self.canvas, bg="white")
        self.next_question()
