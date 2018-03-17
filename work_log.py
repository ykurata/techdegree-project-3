from task import Task
from datetime import datetime

import csv
import os
import re


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Prints main menu
def main_menu():
    print("Welcome to WORK LOG!\n")
    print("""What would you like to do?\n
             1) Add new entry
             2) Search in existing entry
             3) Quit program
          """)


def user_choice():
    """
    Presents a menu with 3 options and allows the user to choose one.
    Provides the result the user has chosen.
    """
    choice = input("Please select the number of your choice: ")
    clear_screen()
    try:
        # Checks if the number is integer or not
        choice = int(choice)
    except ValueError:
        print("Please enter the number again\n")
        # Returns the main menu
        main_menu()
        user_choice()

    if choice == 1:
        # Writes tasks on the csvfile
        task = Task()
        task.add_task()
        # Returns the main menu
        print("The entry has been added.\n")
        play_again()

    elif choice == 2:
        # Searches entry
        search()

    elif choice == 3:
        # Quits program
        print("See you again!")


def search():
    """
    Presents 6 search options and allows the user to choose one.
    """
    print("Please choose one of the following search options:")
    print("""
    a) Exact Date
    b) Date range
    c) Time spent
    d) Task name or Note
    e) Regex Patern
    f) Return to menu
    """)
    search_choice = input("""
Enter the letter associated with the search you want: """)

    if search_choice == "a":
        clear_screen()
        show_dates()
        play_again()

    elif search_choice == "b":
        clear_screen()
        find_range()
        play_again()

    elif search_choice == "c":
        clear_screen()
        find_time()
        play_again()

    elif search_choice == "d":
        clear_screen()
        find_exact_search()
        play_again()

    elif search_choice == "e":
        clear_screen()
        find_pattern()
        play_again()

    elif search_choice == "f":
        clear_screen()
        main_menu()
        user_choice()

    else:
        clear_screen()
        print("Please enter the letter associated with the search!\n")
        search()


def show_entry(row):
    """Prints the entries"""
    print("""
Here's your entry.\n
Date: {}
Title: {}
Time: {} minutes
Note: {}""".format(row[0], row[1], row[2], row[3]))


def show_dates():
    """Prints the line number and date"""
    print("Here's your date entry \n")
    with open('log.csv') as csvfile:
        reader = csv.reader(csvfile)
        for count, row in enumerate(reader, 1):
            try:
                dates = '{}. {}'.format(count, row[0])
                print(dates)
            except IndexError:
                clear_screen()
                print("There is no entries.")
                break
        else:
            find_date()

def find_date():
    """
    Shows list of dates, and allows the user to choose one from the list.
    Checks if the number is valid or not.
    Prints the entry.
    """
    date_choice = input("\nEnter the number associated with the date you want: ")
    try:
        date_choice = int(date_choice)
    except ValueError:
        clear_screen()
        print("Invalid number.Try again\n")
        find_date()
    else:
        with open('log.csv') as csvfile:
            reader = csv.reader(csvfile)
            for count, row in enumerate(reader, 1):
                if date_choice == count:
                    clear_screen()
                    show_entry(row)
                    break
            else:
                clear_screen()
                print("No results. Try again\n")
                find_date()


def find_range():
    """
    Allows user to enter the date range.(start date, end date)
    Checks if the dates are valid dates.
    Prints the entry between the start date and end date.
    """

    first_date = input("Enter the start date in MM/DD/YYYY format: ")
    second_date = input("Enter the end date in MM/DD/YYYY format: ")
    try:
        first_date = datetime.strptime(first_date, '%m/%d/%Y')
        second_date = datetime.strptime(second_date, '%m/%d/%Y')
    except ValueError:
        print("\n{} doesn't seem to be a valid date.\n".format(first_date))
        print("\n{} doesn't seem to be a valid date.\n".format(second_date))
        find_range()
    else:
        with open('log.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    if first_date <= datetime.strptime(row[0],
                        '%m/%d/%Y')<= second_date:
                        show_entry(row)
                    else:
                        print("No results.")
                except IndexError:
                    print("\nThere is no entries.")
                    break


def find_time():
    """
    Allows user to enter the number of minutes it took to complete.
    Prints the entry with the time the user took.
    """
    time = input("Enter the time you spent: ")
    with open('log.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                if time == row[2]:
                    clear_screen()
                    show_entry(row)
                    break
            except IndexError:
                print("\nThere is no entries.")
                break
        else:
            clear_screen()
            print("No results. Try again. \n")
            find_time()


def find_exact_search():
    """
    Allows user to enter the name of task or note.
    Prints the entry which is matched with the user input.
    """
    search = input("Enter your task name or note: ")
    with open('log.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                if search in row[1]:
                    clear_screen()
                    show_entry(row)
                    break
                elif search in row[3]:
                    clear_screen()
                    show_entry(row)
                    break
            except IndexError:
                print("\nThere is no entries.")
                break
        else:
            clear_screen()
            print("No results. Try again. \n")
            find_exact_search()


def find_pattern():
    """
    Allows user to enter the regular expression of task or note.
    Prints the entry which is matched with the regular expression.
    """
    regex = input("Enter the regular expression of your Task or Note: ")
    try:
        pattern = re.compile(regex, re.I)
    except re.error:
        print("Invalid regular expression. Try again\n")
    else:
        with open('log.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    if (re.findall(pattern, row[1]) or
                        re.findall(pattern, row[3])):
                        show_entry(row)
                    else:
                        print("No results.")
                except IndexError:
                    print("\nThere is no entries.")


def play_again():
    """Asks user if they want to continue"""
    ask = input("\nDo you want to continue? Enter Y or N: ").lower()

    if ask != "y":
        print("See you again!")
    elif ask == "y":
        clear_screen()
        main_menu()
        user_choice()


if __name__ == '__main__':
    main_menu()
    user_choice()
