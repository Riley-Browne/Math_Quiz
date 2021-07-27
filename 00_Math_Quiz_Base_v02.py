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
                                        font=button_font, bg="#FF9933", command=lambda: self.num_checker("-"))
        self.subtraction_button.grid(row=5, column=0, padx=65, pady=5, sticky="ew")
        # Multiplication (row 6)
        self.multiplication_button = Button(self.start_frame, text="Multiplication",
                                        font=button_font, bg="#FF9933",command=lambda: self.num_checker("*"))
        self.multiplication_button.grid(row=6, column=0, padx=65, pady=5, sticky="ew")
        # Division (row 7)
        self.division_button = Button(self.start_frame, text="Division",
                                        font=button_font, bg="#FF9933", command=lambda: self.num_checker("/"))
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

             # If numbers are equal to each other, print error
            elif minimum_value == maximum_value:
                self.error_label.config(text="Please make a minimum and a maximum number that are not equal")   

            # If no errors found, make error_label empty to make previous error message dissaper
            if minimum_value < maximum_value:
                self.error_label.config(text="")
                self.to_quiz(operation, minimum_value, maximum_value)

        except ValueError: 
            has_errors = "yes"
            self.error_label.config(text="Please enter an amount greater than 0 (no text / decimals)")
    
    def to_quiz (self, operation, minimum_value , maximum_value):
       
        # minimum_value = min_val 
        # maximum_value = max_val

        print("minimum value", minimum_value)
        print("maximum value", maximum_value)

        # Get minimum and maximum amount
        Quiz(operation, minimum_value, maximum_value)

    # Allows the quit button to shut down the GUI
    def close_start(self):
        quit()

class Quiz:

    def __init__(self, operation, minimum_entry, maximum_entry):
        
        self.operator = StringVar()
        self.operator.set(operation)

        # operation = "+", "-", "*", "/"
        
        #  Number of quesitons in the quiz
        num_questions = 10

        # Starting questions 
        self.asked_questions = IntVar()
        self.asked_questions.set(1)

        self.Correct_Ans = IntVar()

        self.minimum = IntVar()
        self.minimum.set(minimum_entry)

        self.maximum = IntVar()
        self.maximum.set(maximum_entry)

        self.question_asked = StringVar()

        self.question_history_list = []

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

        self.question_results = self.answer_entry.get()

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
        
        how_many = self.asked_questions.get()
        how_many += 1
        self.asked_questions.get()
        if how_many == 11:
            print("It is working, quiz over")
            self.next_button.config(state=DISABLED)
            finish_quiz(self.question_results)
            

            # configure stuff etc, think mystery box when you ran out of money

        else:
        
            # Get minimum and Maximum numbers from user (will be set variables until components have been combined)
            minimum_amount = self.minimum.get()
            maximum_amount = self.maximum.get()
            
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
            self.question_asked.set(question)


            self.question_label.config(text=question)
            question_answer = eval(question)
            self.Correct_Ans.set(question_answer)

            answered_question = self.answer_entry.get()
            user_list = "{} {} {} = {}".format(num_2, operation, num_1, answered_question)
            
    # allows user to check whether their answer was correct
    def check_question(self):
        print("you asked to check the questions")

        user_answer = self.answer_entry.get()
        
        try:

            how_many = self.asked_questions.get()
            how_many += 1
            self.asked_questions.set(how_many)

            user_answer = int(user_answer)
            actual_answer = self.Correct_Ans.get()
            self.next_button.config(state=NORMAL)
            self.check_button.config(state=DISABLED)
            self.answer_entry.config(state=DISABLED)

            print("quesitons asked, how many", how_many)

            # If user enters in the correct answer, print response and 
            # disable the text box to prevent changes to the answer
            if user_answer == actual_answer:
                self.answer_label.config(text="Congratulations, you got {}".format(user_answer), fg="green")
                self.answer_entry.config(state=DISABLED)

                result = "correct"

                num_right = self.Correct_Ans.get()
                num_right += 1
                self.Correct_Ans.set(num_right)
 
            else:
                self.answer_label.config(text="Unfortunately, you got {} and not {}".format(user_answer, actual_answer), fg="red")
                self.answer_entry.config(state=DISABLED)

                result = "incorrect"

            # add question and answer to list...
            question_for_history = self.question_asked.get()

            question_answer = "{} = {} | {}".format(question_for_history, user_answer, result)
            print("we asked", question_answer)
            print()

            self.question_history_list.append(question_answer)
            print(self.question_history_list)

        except ValueError:
            self.answer_label.config(text="Please enter in the answer (no text)", fg="red")

    # Allows the quit button to shut down the GUI
    def close_quiz(self):
        quit()

class finish_quiz():
    def __init__(self, question_results):


        self.finish_box = Toplevel()
        # GUI Frame
        self.finish_frame = Frame(self.finish_box, padx=10, pady=10)
        self.finish_frame.grid()
    
        # Label for user to see how many they got right and wrong
        self.math_quiz_label = Label(self.finish_frame, text="Congratulations for completing the quiz!", font="Arial 10 bold")
        self.math_quiz_label.grid(row=0)

        self.sub_quiz_label = Label(self.finish_frame, text="You can now export your results or quit",
                                    font="Arial 8 italic")
        self.sub_quiz_label.grid(row=1)

        self.save_button = Button(self.finish_frame, text="Save",
                             font="Arial 10 bold", bg="#FF9933")
        self.save_button.grid(row=2, column=0, padx=65, pady=10)

        self.quit_button = Button(self.finish_frame, text="Quit",
                             font="Arial 10 bold", bg="#FF9933", command=partial(self.close_finished))
        self.quit_button.grid(row=3, column=0, padx=65, pady=10)
    
    # Allows the quit button to shut down the GUI
    def close_finished(self):
        quit()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()
