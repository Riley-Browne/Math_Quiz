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
                                        font=button_font, bg="#FF9933")
        self.subtraction_button.grid(row=5, column=0, padx=65, pady=5, sticky="ew")
        # Multiplication (row 6)
        self.multiplication_button = Button(self.start_frame, text="Multiplication",
                                        font=button_font, bg="#FF9933")
        self.multiplication_button.grid(row=6, column=0, padx=65, pady=5, sticky="ew")
        # Division (row 7)
        self.division_button = Button(self.start_frame, text="Division",
                                        font=button_font, bg="#FF9933")
        self.division_button.grid(row=7, column=0, padx=65, pady=5, sticky="ew")
        # Help Button (row 8)
        self.help_button = Button(self.start_frame, text="Help",
                                        font=button_font, bg="#FF9933")
        self.help_button.grid(row=8, column=0, padx=65, pady=5, sticky="w")
        # Quit Button (row 8)
        self.quit_button = Button(self.start_frame, text="Quit",
                                        font=button_font, bg="#FF9933")
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
            if minimum_value < 0 or maximum_value < 0:
                self.error_label.config(text="Please enter an amount greater than 0 (no text / decimals)")    

            # If no errors found, make error_label empty to make previous error message dissaper
            if minimum_value < maximum_value:
                 self.error_label.config(text="")
                

        except ValueError: 
            has_errors = "yes"
            self.error_label.config(text="Please enter an amount greater than 0 (no text / decimals)")
            

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()
