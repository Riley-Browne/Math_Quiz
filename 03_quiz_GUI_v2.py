from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Quiz:

    def __init__(self):

        operation = "+"
        num_questions = 5

        self.Correct_Ans = IntVar()

        # GUI Frame
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()

        # Question Label to show user what question they're on (row 1)
        self.number_label = Label(self.quiz_frame, text="Press 'next' to start", font="Arial 10 italic", wraplength=250)
        self.number_label.grid(row=1)

        # Label for generated question (row 2)
        self.question_label = Label(self.quiz_frame, text="", font="Arial 15 italic", wraplength=250)
        self.question_label.grid(row=2)


        # Answer Box for user to enter answer (row 3)
        self.answer_entry = Entry(self.quiz_frame, font="Arial 10")   
        self.answer_entry.grid(row=3, column=0) 

        # Answer Entry Box Frame
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=4)

        # Next Button (row 5)
        self.next_button = Button(self.button_frame, text="Next",
                                        font="Arial 10", bg="#FF9933", command=lambda: self.question_generator(operation))
        self.next_button.grid(row=0, column=0, padx=5, pady=5)

        self.check_button = Button(self.button_frame, text="Check",
                                        font="Arial 10", bg="#FF9933", command=self.check_question)
        self.check_button.grid(row=0, column=1, padx=5, pady=5)

        # Quit Button (row 4)
        self.quit_button = Button(self.button_frame, text="Quit",
                                        font="Arial 10", bg="#FF9933", 
                                        command=partial(self.close_quiz))
        self.quit_button.grid(row=1, columnspan=2, padx=30, pady=5)



    def question_generator(self, operation):
        
        # Get minimum and Maximum numbers from user (will be set variables until components have been combined)
        minimum_amount = 1
        maximum_amount = 10

        num_2 = random.randint(minimum_amount, maximum_amount)

        num_1 = random.randint(minimum_amount, maximum_amount)

        operation = "+"

        if operation == "+":
            num_3 = num_2 + num_1

        question = "{} {} {}".format(num_2, operation, num_1)
        self.question_label.config(text=question)
        question_answer = eval(question)
        self.Correct_Ans.set(question_answer)
        
    def check_question(self):
        print("you asked to check the questions")
        user_answer = int(self.answer_entry.get())
        actual_answer = self.Correct_Ans.get()

        print("user answer print", user_answer)
        print("correct answer", actual_answer)

        if user_answer == actual_answer:
            print("yay")
        else:
            print("oops")


    # Allows the quit button to shut down the GUI
    def close_quiz(self):
        quit()

   




        

    
        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Quiz()
    root.mainloop()
