from datetime import datetime

import csv
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Task:
    """
    This class takes user input and writes user input into the csv file.
    Asks user date, title, time spent, and note.
    """
    def add_task(self):
        while True:
            self.date = input("Enter the date in MM/DD/YYYY format: ")
            # Checks if the date is valid or not.
            try:
                self.date = datetime.strptime(self.date, '%m/%d/%Y')
            except ValueError:
                print("\n{} doesn't seem to be a valid date.\n".format(self.date))
            else:
                self.date = self.date.strftime('%m/%d/%Y')
                clear_screen()
                break

        self.title = input("Enter the title of the task: ")
        clear_screen()

        self.time = input("Enter the number of time you spent(minutes): ")
        clear_screen()

        self.note = input("Enter any note(optional): ")
        # Writes on the csvfile
        with open("log.csv", "a") as csvfile:
                taskwriter = csv.writer(csvfile, delimiter=',')
                taskwriter.writerow([self.date, self.title, self.time, self.note])
