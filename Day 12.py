"""
Write a function named precedence that returns an integer representing the precedence of a mathematical operator.
A string containing the operator will be passed to the function as its only parameter.
Your function should return 1 for + and -, 2 for * and /, and 3 for ˆ.
If the string passed to the function is not one of these operators then the function should return -1.
Include a main program that reads an operator from the user and either displays the operator’s precedence or an error message indicating that the input was not an operator.
Your main program should only run when the file containing your solution has not been imported into another program.
In this exercise, along with others that appear later in the book, we will use ˆ to represent exponentiation.
Using ˆ instead of Python’s choice of ** will make these exercises easier because an operator will always be a single character.
"""

def precedence(operator):

    operator_list = ["+", "-", "*", "/", "^", "%"]
    
    if len(operator) != 1:
        print("Please enter only one maths operator")
    else:

        if operator in operator_list:

            if operator == "+" or operator == "-":
                return 1
            elif operator == "*" or operator == "/":
                return 2
            elif operator == "^":
                return 3
            else:
                return -1
        else:
            return "This is not an operator"

def main():
    operator = input("Please enter a maths operator: ")
    print(precedence(operator))
main()