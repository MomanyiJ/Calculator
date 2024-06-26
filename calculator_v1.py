#!/usr/bin/python3

#calculator program

#define all operators/functions

# addition

def addition(n1, n2):
    """Adds two numbers and retuns the result"""
    return n1 + n2

#subtraction

def subtraction(n1, n2):
    """Subtracts two numbers and returns the result"""
    return n1-n2

#Multiplication

def multiplication(n1, n2):
    """Multiplies two numbers and returns the result"""
    return n1*n2

#Division

def division(n1,n2):
    """Divides two numbers and returns the results/ Handles division by zero"""
    if n2 == 0:
        print("Cannot divide by zero!")
        return None
    return n1/n2

while True:
    # List out options for the calculator
    print("Select Operand")
    print("1.Addition\n"
            "2.Subtraction\n"
            "3.Multiplication\n"
            "4.Division\n"
            "5.Press Q to quit\n")
    
    selection = input("Select operation: ")

    if selection.upper() == 'Q':
        print("Bye Bye!")
        break
    elif selection in ('1', '2', '3', '4'): # Checks for valid selections ie 1-4
        try:
            # Valid selection 1,2,3,4 - proceed to number input
            n1 = float(input("Please enter your 1st number: "))
            n2 = float(input("Please enter your 2nd number: "))


            # Make operation as user chooses

            if selection == '1':
                result = addition(n1, n2)
                print(f"Result: {n1} + {n2} = {result}")

            elif selection == '2':
                result = subtraction(n1, n2)
                print(f"Result: {n1} - {n2} = {result}")

            elif selection == '3':
                result = multiplication(n1, n2)
                print(f"Result: {n1} * {n2} = {result}")
            elif selection == '4':
                result = division(n1, n2)
                if result is not None:
                    print(f"Result: {n1} / {n2} = {result}")
            break
        except ValueError:
            print("Error: INvalid input, enter only numbers.")
    else:
        print("Invald selection. Please enter between 1-4 or 'Q' to quit.")
