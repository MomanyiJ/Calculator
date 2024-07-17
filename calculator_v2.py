#!/usr/bin/python3

#Calculator App
# This is version 2 that also has history using a list
import os
def add(num1, num2):
    ''' Adds two numbers and returns result'''
    return num1 + num2

def subtract(num1, num2):
    '''Subtracts two numbers and returns returns result'''
    return num1 - num2

def multiply(num1, num2):
    '''Multiplies two numbers and returns result'''
    return num1 * num2

def divide(num1, num2):
    '''Divides two unumbers and returns result'''
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
def read_history_from_file(calc_history):
    """Reads calculation history and returns a list"""
    calculation_history = []
    if os.path.exists(calc_history):
        try:
            with open(calc_history, 'r') as file:
                for line in file:
                    calculation_history.append(line.strip()) # gets rid of trailing new line
        except IOError:
            print(f"Error reading hidtory from '{calc_history}'.")
    return calculation_history

def write_history_to_file(calc_history, solutions_history):
    """ This writes calculations hstory to the file calc_history"""
    try:
         with open(calc_history, 'w') as file:
             for entry in solutions_history:
                 file.write(f"{entry}\n") #Adds new line fr each entry
    except IOError:
        print(f"Error writing history to: '{calc_history}'.")
        print("Failed to save calculation history, check file permissions")

def main():
    """Main program loop hanfling user input, exits with 'Q'"""
    solutions_history = [] # List storing calculation history

    while True:
        print("Select Operand")
        print("1. Addition\n"
                "2. Subtraction \n"
                "3.  Multiplication \n"
                "4. Division \n"
                "Q. Quit \n"
                "H. Show History")
                
        selection = input("Please Enter your operand ")

        if selection.upper() == "Q":
            print("Bye! Bye!")
            break
        elif selection in ('1', '2', '3', '4'):  #Check for valid digits
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Make operation as user per user's choice

                if selection == '1':
                    result = add(num1, num2)
                    solutions_history.append(f"{num1} + {num2} = {result}")
                    print(f"Result: {num1} + {num2} = {result}")
                elif selection == '2':
                    result = subtract(num1, num2)
                    solutions_history.append(f"{num1} - {num2} = {result}")
                    print(f"Result: {num1} - {num2} = {result}")
                elif selection == '3':
                    result = multiply(num1, num2)
                    solutions_history.append(f"{num1} * {num2} = {result}")
                    print(f"Result: {num1} * {num2} = {result}")
                elif selection == '4':
                    result = divide(num1, num2)
                    if result:
                        solutions_history.append(f"{num1} / {num2} = {result}")
                        print(f"Result: {num1} / {num2} = {result}")
                    else:
                        print("Error: Cannot divide by zero.")
            except ValueError:
                print("Error: Invalid output pplease enter numbers only")
        elif selection.upper() == 'H': 
            # shows calculation history if it exists
            if solutions_history:
                print("\nSolutions History:") #Prints last five calculations
                # slicing the last five elements up to ndex -1
                last_five_calculations = solutions_history[-5:] # this will give the last 5 elements
                for entry in solutions_history:
                    print(entry)
            else:
                print("\nThere is no History")
        else:
            print("Invalid selection. Enter a number between 1-4. Or Q to quit.Or H for History")

if __name__ == "__main__":
    main()
