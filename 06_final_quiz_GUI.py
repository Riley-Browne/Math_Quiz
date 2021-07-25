from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class finish_quiz:
    def __init__(self):

        # GUI Frame
        self.finish_frame = Frame(padx=10, pady=10)
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
    something = finish_quiz()
    root.mainloop()