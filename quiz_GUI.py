from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Quiz:
    
    # GUI Frame
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()
    # Question Label to show user what question they're on
    self.error_label = Label(self.start_frame, text="",
                                font="Arial 10 italic", wraplength=250, fg="red")
        self.error_label.grid(row=1)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Quiz(root)
    root.mainloop()
