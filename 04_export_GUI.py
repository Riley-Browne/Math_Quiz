from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Export:
    def __init__(self):
        
        # GUI Frame
        self.export_frame = Frame(padx=10, pady=10)
        self.export_frame.grid()

         # Label 
        self.entry_label = Label(self.export_frame, text="File Name:",
                                font="Arial 10 bold")
        self.entry_label.grid(row=0)

        # Entry Text Box for user to enter file name
        self.file_entry = Entry(self.export_frame, font="Arial 10 italic")   
        self.file_entry.grid(row=1, column=0, pady=10)

        # Cancel Button
        self.cancel_button = Button(self.export_frame, text="Cancel", command=self.close_export,
                            font="Arial 10 bold", bg="#FF9933")
        self.cancel_button.grid(row=2, column=0, padx=65, pady=10, sticky="ew")

        # Save Button
        self.save_button_button = Button(self.export_frame, text="Save",
                             font="Arial 10 bold", bg="#FF9933", command=partial(lambda: self.save_history(answered_questions)))
        self.save_button_button.grid(row=3, column=0, padx=65, pady=10, sticky="ew")

    def save_history(self):

        # Regular expression to check filename is valid.
        valid_char = "[A-Za-z0-9_]"
        has_errors = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue
            elif letter == " ":
                problem = "(No spaces allowed)"
            else:
                problem = ("(No {}'s allowed".format(letter))
            has_errors = "yes"
            break

        if filename == "":
            problem = "Can't be blank"
            has_errors = 'yes'

        if has_errors == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # Create file to hold data
            f = open(filename, "w+")

            # Heading for stats
            f.write("Game Statistics\n\n")

            # Game stats
            for round in game_stats:
                f.write(str(round) + "\n")

            # Heading for rounds
            f.write("\nRound Details\n\n")

            # Add new line at the end of each item
            for item in game_history:
                f.write(item + "\n")
            # Closes save window when save is successful
            self.close_export(partner)

    def close_export(self):
        Export.destory()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Export()
    root.mainloop()
