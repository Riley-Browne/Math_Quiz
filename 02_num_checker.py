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

        # Initial Instructions (row 1)
        self.math_instructions = Label(self.start_frame, font="Arial 10 italic",
                                        text ="Please enter a minimum and maximum number "
                                        "and select what mode you wish to use for the quiz.",
                                        wrap=275, justify=CENTER, padx=10, pady=10)
        self.math_instructions.grid(row=1)

        # Minimum Box Heading (row 2)
        self.minimum_label = Label(self.start_frame, text="Minimum",
                                   font="Arial 10 bold")
        self.minimum_label.grid(row=2, sticky="w", padx=37.5)

        # Maximum Box Heading (row 2)
        self.maximum_label = Label(self.start_frame, text="Maximum",
                                   font="Arial 10 bold")
        self.maximum_label.grid(row=2, sticky="e", padx=37.5)

        # Minimum Entry Text Box (row 3)
        self.minimum_entry = Entry(self.start_frame, font="Arial 10 italic")   
        self.minimum_entry.grid(row=3, sticky="w", pady=5)

        # Maximum Entry Text Box (row 3)
        self.maximum_entry = Entry(self.start_frame, font="Arial 10 italic")   
        self.maximum_entry.grid(row=3, sticky="e", pady=5)

        # Addition Button (row 4)
        self.addition_button = Button(self.start_frame, text="Addition",
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

    def num_checker (self):
        
        error_back = "#ffafaf"
        try:
            print("hurb")
        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter an amount greater than 0 (no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
        else:
            print="No Error"


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()
