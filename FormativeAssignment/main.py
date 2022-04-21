"""Menu code for the formative assignment"""

import os
import sys
import BinaryConverter
import TrigFunctions
import math


def cls(): 
    """Clear the screen"""
    os.system('cls' if os.name=='nt' else 'clear')


def determineIfStringOrInt(value):
    """Determine if the value is a string or an integer or a float"""

    try:
        int(value)
        return "int"
    except ValueError:
        try:
            float(value)
            return "float"
        except ValueError:
            return "string"


"""
    if isinstance(value, str):
        return "string"
    elif isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    else:
        return "unknown"
"""

def mainMenu():
    """Generate a main selection menu"""

    try:
        print("Would you like to convert some values to binary? (Press 1)")
        print("Would you like to use the trig functions? (Press 2)")
        print("Would you like to exit the program? (Press 3)")
        
        selection = int(input("Please select an option: "))

    except ValueError:
        print("Please enter a valid option.")
        cls()


    if selection == 1:
        binaryConverter()

    elif selection == 2:
        trigFunctions()

    elif selection == 3:
        print("Exiting the program...")
        sys.exit()


def binaryConverter():
    """Convert a given input to binary"""

    #Using determineIfStringOrInt
    print("Please enter a number to convert to binary: ")
    input_value = input()
    input_type = determineIfStringOrInt(input_value)

    if input_type == "string":
        print(BinaryConverter.stringToBinary(input_value))
        input()

    elif input_type == "int":
        print(BinaryConverter.toBinary(int(input_value)))
        input()

    elif input_type == "float":
        print(BinaryConverter.floatToBinary(float(input_value)))
        input()


def trigFunctions():
    """Perform a trig function on a given input"""
    
    print("Please enter a number to perform trig functions on: ")
    input_value = input()
    input_type = determineIfStringOrInt(input_value)

    if input_type == "string":
        print("Please enter a valid number.")
        cls()

    elif input_type == "int" or input_type == "float":
        print(TrigFunctions.cosecant(float(input_value)))
        print(TrigFunctions.secant(float(input_value)))
        print(TrigFunctions.cotangent(float(input_value)))
        print(TrigFunctions.inverse_cosecant(float(input_value)))
        print(TrigFunctions.inverse_secant(float(input_value)))
        print(TrigFunctions.inverse_cotangent(float(input_value)))
        input()


if __name__ == "__main__":
    while True:
        cls()
        mainMenu()

