from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):   


        # GUI Frame
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Buttons go here...
        button_font = "Arial 12 bold"

        #  Quiz Heading(row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz",
                                font="Arial 20 bold")
        self.math_quiz_label.grid(row=0)

        #Error Label(row 1)
        self.error_label = Label(self.start_frame, text="",
                                font="Arial 10 italic", wraplength=250, fg="red")
        self.error_label.grid(row=1)

        # Minimum Box Heading (row 2)
        self.minimum_label = Label(self.start_frame, text="Minimum",
                                   font="Arial 10 bold")
        self.minimum_label.grid(row=2, sticky="w", padx=37.5)

        # Maximum Box Heading (row 2)
        self.maximum_label = Label(self.start_frame, text="Maximum",
                                   font="Arial 10 bold")
        self.maximum_label.grid(row=2, sticky="e", padx=37.5)

        # Max and Min Entry Box Frame
        self.test_frame = Frame(self.start_frame)
        self.test_frame.grid()

        # Minimum Entry Text Box (row 3)
        self.minimum_entry = Entry(self.test_frame, font="Arial 10 italic")   
        self.minimum_entry.grid(row=3, column=0)

        # Maximum Entry Text Box (row 3)
        self.maximum_entry = Entry(self.test_frame, font="Arial 10 italic")   
        self.maximum_entry.grid(row=3, column=1)

        # Addition Button (row 4)
        self.addition_button = Button(self.start_frame, text="Addition", command=lambda: self.num_checker("+"),
                               font=button_font, bg="#FF9933")
        self.addition_button.grid(row=4, column=0, padx=65, pady=5, sticky="ew")
        # Subtraction Button (row 5)
        self.subtraction_button = Button(self.start_frame, text="Subtraction",
                                        font=button_font, bg="#FF9933", command=lambda: self.to_quiz(2))
        self.subtraction_button.grid(row=5, column=0, padx=65, pady=5, sticky="ew")
        # Multiplication (row 6)
        self.multiplication_button = Button(self.start_frame, text="Multiplication",
                                        font=button_font, bg="#FF9933",command=lambda: self.to_quiz(3))
        self.multiplication_button.grid(row=6, column=0, padx=65, pady=5, sticky="ew")
        # Division (row 7)
        self.division_button = Button(self.start_frame, text="Division",
                                        font=button_font, bg="#FF9933", command=lambda: self.to_quiz(4))
        self.division_button.grid(row=7, column=0, padx=65, pady=5, sticky="ew")
        # Help Button (row 8)
        self.help_button = Button(self.start_frame, text="Help",
                                        font=button_font, bg="#FF9933")
        self.help_button.grid(row=8, column=0, padx=65, pady=5, sticky="w")
        # Quit Button (row 8)
        self.quit_button = Button(self.start_frame, text="Quit",
                                        font=button_font, bg="#FF9933", command=partial(self.close_start))
        self.quit_button.grid(row=8, column=0, padx=65, pady=5, sticky="e")

    # checks entry boxes to see whether values are valid or not
    def num_checker (self, operation):
        
        error_back = "#ffafaf"
        error_feedback = "no errors"

        try:
            minimum_value = self.minimum_entry.get()
            maximum_value = self.maximum_entry.get()
            minimum_value = int(minimum_value)
            maximum_value = int(maximum_value)

            # checks to see whether the minimum value is lower than maximum value
            if minimum_value > maximum_value:
                self.error_label.config(text="Please enter a minimum number lower than your maximum number")   
    
            # If number is lower than 0, prints error
            elif minimum_value < 0 or maximum_value < 0:
                self.error_label.config(text="Please enter an amount greater than 0 (no text / decimals)")    

            # If no errors found, make error_label empty to make previous error message dissaper
            if minimum_value < maximum_value:
                 self.error_label.config(text="")
                 self.to_quiz(operation, minimum_value, maximum_value)
                 
        except ValueError: 
            has_errors = "yes"
            self.error_label.config(text="Please enter an amount greater than 0 (no text / decimals)")
    
    def to_quiz (self, operation, min_val, max_val):
       
        # Get minimum and maximum amount
        Quiz(operation, min_val, max_val)

    # Allows the quit button to shut down the GUI
    def close_start(self):
        quit()

class Quiz:

    def __init__(self, operation, min_val, max_val):
        
        self.operator = StringVar()
        self.operator.set(operation)

        # operation = "+", "-", "*", "/"
        num_questions = 10

        self.Correct_Ans = IntVar()

        self.quiz_box = Toplevel()

        # GUI Frame
        self.quiz_frame = Frame(self.quiz_box, padx=10, pady=10)
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

        self.check_button.config(state=DISABLED)

        # Quit Button (row 4)
        self.quit_button = Button(self.button_frame, text="Quit",
                                        font="Arial 10", bg="#FF9933", 
                                        command=partial(self.close_quiz))
        self.quit_button.grid(row=1, columnspan=2, padx=30, pady=5)

        # Label for generated question (row 5)
        self.answer_label = Label(self.quiz_frame, text="", font="Arial 10", wraplength=250, )
        self.answer_label.grid(row=5)



    def question_generator(self, operation):
        
        # Get minimum and Maximum numbers from user (will be set variables until components have been combined)
        minimum_amount = 1
        maximum_amount = 10
        
        self.next_button.config(state=DISABLED)
        self.check_button.config(state=NORMAL)
        self.answer_entry.config(state=NORMAL)
        self.answer_label.config(text="")
        self.answer_entry.delete(0, 'end')


        num_2 = random.randint(minimum_amount, maximum_amount)

        num_1 = random.randint(minimum_amount, maximum_amount)

        operation = self.operator.get()

        if operation == "+":
            num_3 = num_2 + num_1
     
        elif operation == "-":
            num_3 = num_2 - num_1

        elif operation == "/":
            num_3 = num_2 / num_1
        
        if operation == "*":
            num_3 = num_2 * num_1

        question = "{} {} {}".format(num_2, operation, num_1)
        self.question_label.config(text=question)
        question_answer = eval(question)
        self.Correct_Ans.set(question_answer)

    # allows user to check whether their answer was correct
    def check_question(self):
        print("you asked to check the questions")

        user_answer = self.answer_entry.get()
        
        try:
            user_answer = int(user_answer)
        
        except ValueError:
            self.answer_label.config(text="Please enter in the answer (no text)", fg="red")
    

        actual_answer = self.Correct_Ans.get()
        self.next_button.config(state=NORMAL)
        self.check_button.config(state=DISABLED)
        self.answer_entry.config(state=DISABLED)

        print("user answer print", user_answer)
        print("correct answer", actual_answer)

        # If user enters in the correct answer, print response and 
        # disable the text box to prevent changes to the answer
        if user_answer == actual_answer:
            self.answer_label.config(text="Congratulations, you got {}".format(user_answer), fg="green")
            self.answer_entry.config(state=DISABLED)
        else:
             self.answer_label.config(text="Unfortunately, you got {} and not {}".format(user_answer, actual_answer), fg="red")
             self.answer_entry.config(state=DISABLED)

   
    # Allows the quit button to shut down the GUI
    def close_quiz(self):
        quit()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()
