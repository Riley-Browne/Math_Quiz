from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Quiz main screen GUI..
        self.start_frame = Frame(width=300, height=300,
                                     pady=10)
        self.start_frame.grid()

        # Temperature conversion heading (row 0)
        self.math_quiz_label = Label(self.start_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

        # Help button (row 1)
        self.help_button = Button(self.start_frame, text="help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="To enter in your desired numbers, pick your minimum and maximum numbers"
                                          "(no decimals or words) and select one of the 4 quiz modes.)")


class Help:
    def __init__(self, partner):

        # disabled help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Setup GUI Frame
        self.help_frame = Frame(self.help_box)
        self.help_frame.grid()

        # Setup Help heading (row 0)
        self.how_heading = Label(self.help_box, text="How to use the quiz",
                                 font="arial 10 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_box, text="",
                               justify=LEFT, width=40, wrap=250)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_box, text="Dismiss", width=10,
                                  font="arial 10 bold", 
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal..
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()

