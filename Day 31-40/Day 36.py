# -*- coding: utf-8 -*-
"""Day 36

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CO0OpIYqA0y1cRDlnOmvXhmX0DFW7kFR
"""

"""
TASK 1

Words like first, second and third are referred to as ordinal numbers. In this exercise,
you will write a function that takes an integer as its only parameter and returns a
string containing the appropriate English ordinal number as its only result. Your
function must handle the integers between 1 and 12 (inclusive). It should return an
empty string if a value outside of this range is provided as a parameter. Include a
main program that demonstrates your function by displaying each integer from 1 to
12 and its ordinal number. Your main program should only run when your file has
not been imported into another program.
"""

#defining the function
def ordinal(user_num):

  #dictionary containing the numbers and their ordinal versions
  ordinal_dict = {1: "first", 2: "second", 3: "third",
   4: "fourth", 5: "fifth", 6: "sixth",
   7: "seventh", 8: "eighth", 9: "ninth",
   10: "tenth", 11: "eleventh", 12: "twelfth"}

  #returning values for numbers in the dictionary
  if user_num in ordinal_dict.keys():
    return ordinal_dict[user_num]

  #else, empty string for entries outside 1-12
  else:
    return " "

#initiating progrma with main function
def main():

  #using try/except to prevent program from crashing if non-numeric input is entered
  try:

    #asking user to enter a number
    user_num = int(input("Enter an integer between 1 and 12: "))

    #activating the function
    print(ordinal(user_num))

  #error message for non-numeric inputs
  except ValueError:
    print("Enter a valid number")

#activating main function
if __name__ == "__main__":
  main()

"""
TASK 2

Write a function that takes three numbers as parameters, and returns the median value
of those parameters as its result. Include a main program that reads three values from
the user and displays their median.
Hint: The median value is the middle of the three values when they are sorted
into ascending order. It can be found using if statements, or with a little bit of
mathematical creativity.
"""

#defining function with the three numbers as the parameters
def median(x, y, z):

  #creating a sorted list from the numbers
  numbers = sorted([x, y, z])

  #returning the middle value
  return numbers[1]


#initiating main function
def main():

  #using try/except to prevent program from crashing if non-numeric input is entered
  try:

    #calling user to enter the three numbers
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    z = float(input("Enter the last number: "))

    #printing out the middle number
    print(median(x, y, z))

  #error message for non-numeric inputs
  except ValueError:
    print("Enter a valid number")

#activating main function
main()