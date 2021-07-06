from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Export:
    def __init__(self, partner, game_history, all_game_stats):

        # Disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font='arial 14 bold', pady=10)
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the "
                                                         "box below and press the Save button to save your calculation "
                                                         "history to a text file.", justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=2, pady=10)

        # Error label
        self.save_error_label = Label(self.export_frame, font="arial 12 bold", text="", fg='red', justify=LEFT,
                                      wrap=250)
        self.save_error_label.grid(row=3)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="arial 14 bold",
                                    justify=CENTER)
        self.filename_entry.grid(row=4, pady=10)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", font="Arial 15 bold",
                                  bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, game_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Export()
    root.mainloop()
