from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Quiz:

    def __init__(self):
        
        # GUI Frame
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()

        # Question Label to show user what question they're on (row 1)
        self.question_label = Label(self.quiz_frame, text="{} out of 10", font="Arial 10 italic", wraplength=250)
        self.question_label.grid(row=1)

        # Label for generated question (row 2)
        self.gen_ques_label = Label(self.quiz_frame, text="{} out of 10", font="Arial 10 italic", wraplength=250)
        self.gen_ques_label.grid(row=2)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Quiz()
    root.mainloop()
