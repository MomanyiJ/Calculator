#!/usr/bin/python3

#calculator program

#define all operators/functions

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
    
    selection = input("Select operand: ")

    if selection.upper() == 'Q':
        print("Bye Bye!")
        break

    if selection not in ['1', '2', '3', '4']:
        print("Invalid selection")
        continue
    #get input from user
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))


    # Make operation as user chooses

    if selection == '1':
        print(n1, "+",n2,"=",addition(n1,n2))

    elif selection == '2':
        print(n1, "-",n2, "=",subtraction(n1,n2))

    elif selection == '3':
        print(n1,"*","=",multiplication(n1,n2))
    elif selection == '4':
        result = division(n1, n2)
        if result is not None:
            print(n1, "/",n2,"=",division(n1,n2))

