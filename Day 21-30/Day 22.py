# -*- coding: utf-8 -*-
"""Day 22

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q5R_pbshYR2SfBiArBMYacGw0dvvQTEj
"""

"""
TASK 1
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG).
In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100km).

Use your research skills to determine how to convert from MPG to L/100km.

Then create a program that reads a value from the user in American units
and displays the equivalent fuel efficiency in Canadian units.
"""

#1MPG = 235.215 Litres/100km https://www.omnicalculator.com/conversion/fueld-economy-converter

#using try/except to prevent program from crashing if a wrong value is entered
try:

  #calling user to enter the fuel efficiency in American units
  mpg = float(input("Please enter the fuel efficiency value: "))

  #ensuring that only natural numbers are entered
  if mpg <= 0:
    print("Please enter a valid number")

  else:
    
    #defining the formula for conversion to Canadian unit
    l_100km = 235.215 * mpg

    #printing output
    print(f"\n{mpg} mpg = {l_100km:.2f} L/100km")

except ValueError:
  print("Please enter a valid number")

"""
TASK 2
In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.
Hint: Because the 0 marks the end of the input it should not be included in the average.
"""

#using try/except to prevent program from crashing if a wrong value is entered
try:

  #calling user to enter the numbers
  user = float(input("Enter numbers to see the average (enter 0 to end): "))
  num_list = []   #intiating a list to house the entered numbers

  #ensuring that 0 is not the first number
  if user == 0:
    print("0 cannot be your first entry.")
  
  else:
    while user != 0:    #giving condition for entry to stop
      num_list.append(user)   #adding entered number to the initiated list
      user = float(input("Enter numbers to see the average (enter 0 to end): "))  #continuing entry

    avg = sum(num_list)/len(num_list)   #calculating the average

    #printing output
    print(f"\nYou have entered the following numbers: {num_list}")
    print(f"\nThe average of the numbers is {avg}")
except ValueError:
  print("Please enter a valid number")

"""
TASK 3
Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.
"""


#PYTHAGORAS THEOREM:
#Given a right-angled triangle, the square of the length of the longest side (a)
#is equal to the sum of the square of other sides (b & c)
#a^2 = b^2 + c^2


#importing squareroot function from math module
from math import sqrt

#defining function for calculating the longest side based on the theory
def hyp(opp,adj):
  hypotenuse = sqrt((opp**2) + (adj**2))
  return hypotenuse

#defining main function for initiating the program
def main():

  #using try/except to prevent program from crashing if a wrong value is entered
  try:
    print("Let us find the length of the longest side of a right-angled triangle\n")
    opp = float(input("Enter the length of the opposite side of the triangle in cm: "))
    if opp <= 0:  #ensuring that only natural numbers are entered
      print("Please enter a valid length")
    else:
      adj = float(input("Enter the length of the adjacent side of the triangle in cm: "))
      if adj <= 0:    #ensuring that only natural numbers are entered
        print("Please enter a valid length")
      else:

        hypotenuse = hyp(opp,adj)   #activating the function and printing output
        print(f"\nVoila, the length of the longest side of this triangle is {hypotenuse:.2f} cm")
  
  except ValueError:
    print("Please enter a valid number")
  
main()