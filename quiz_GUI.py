from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Quiz:

    def __init__(self):
        
        # GUI Frame
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()

        # Question Label to show user what question they're on (row 1)
        self.number_label = Label(self.quiz_frame, text="[] out of 10", font="Arial 10 italic", wraplength=250)
        self.number_label.grid(row=1)

        # Label for generated question (row 2)
        self.question_label = Label(self.quiz_frame, text="", font="Arial 15 italic", wraplength=250)
        self.question_label.grid(row=2)

        # Answer Entry Box Frame
        self.answer_frame = Frame(self.quiz_frame)
        self.answer_frame.grid()

        # Answer Box for user to enter answer (row 3)
        self.answer_entry = Entry(self.answer_frame, font="Arial 10")   
        self.answer_entry.grid(row=3, column=0)

        # Answer Entry Box Frame
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid()

        # Quit Button (row 4)
        self.quit_button = Button(self.button_frame, text="Quit",
                                        font="Arial 10", bg="#FF9933", 
                                        command=partial(self.close_quiz))
        self.quit_button.grid(row=4, column=0, padx=30, pady=5, sticky="w")
        # Next Button (row 5)
        self.next_button = Button(self.button_frame, text="Next",
                                        font="Arial 10", bg="#FF9933")
        self.next_button.grid(row=4, column=1, padx=30, pady=5, sticky="e")

    # Allows the quit button to shut down the GUI
    def close_quiz(self):
        quit()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Quiz()
    root.mainloop()
