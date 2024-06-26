#!/usr/bin/python3

#Calculator App
# This is version 2 that also has history using a list

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

def main():
    """Main program loop hanfling user input, exits with 'Q'"""
    solutions_history = [] # List storing calculation history

    while True:
        print("Select Operand")
        print("1. Addition\n"
                "2. Subtraction \n"
                "3.  Multiplication \n"
                "4. Division \n"
                "Q. Quit")
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
                print("Error: INvalid input, Please enter numbers only.")
        else:
            print("Invalid selection. Please eneter a number (1-4) or 'Q' to quit.")

                # Print calculation history after each operation
        if solutions_history:
            print("\n Solutins History")
            for entry in solutions_history:
                print(entry)

if __name__ == "__main__":
    main()
