# -*- coding: utf-8 -*-
"""Day 19

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u4nMepple2_vcWJYUDL5t5ZScYfpeSKy

# **CHALLENGE DAY 19**



# Task 1

Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n.

The sum of the first n positive integers can be computed using the formula:
sum = (n)(n + 1)/2
"""

#METHOD 1

#using try/except to prevent program from crashing
try:

  #calling user to enter a figure
  user = int(input("Please enter a single natural number (1 and above) to see the the sum of all numbers from 1 to that number: "))

  #ensuring that only natural numbers are selected
  if user < 1:
    print("Please enter a valid natural number from 1 and above")

  #defining the formula for calculation
  else:
    sum_integers = (user * (user + 1))/2

  #printing output
  print(f"The sum of all integers from 1 to this number is {int(sum_integers)}")

except ValueError:
  print("Please enter a valid natural number from 1 and above")

#METHOD 2

#using try/except to prevent program from crashing
try:

  #calling user to enter a figure
  user1 = int(input("Please enter a single natural number (1 and above) to see the the sum of all numbers from 1 to that number: "))

  #ensuring that only natural numbers are selected
  if user1 < 1:
    print("Please enter a valid natural number from 1 and above")

  #defining the formula for calculation
  else:
    sum_integers1 = sum(range(1, user1+1))

  #output
  print(f"The sum of all integers from 1 to this number is {sum_integers1}")

except ValueError:
  print("Please enter a valid natural number from 1 and above")




"""# Task 2

Write a program that reads an integer from the user.

Then your program should display a message indicating whether the integer is even or odd.
"""

#using try/except to prevent program from crashing
try:

  #calling user to enter a figure
  user2 = int(input("Please enter a number: "))

  #defining conditions for even and odd numbers
  if user2 % 2 == 0:
    print("The number you entered({}) number is an even number.".format(user2))
  else:
    print("The number you entered({}) number is an odd number.".format(user2))

except ValueError:
  print("Please enter a valid number")





"""# Task 3

A univariate quadratic function has the form f (x) = ax^2 + bx + c, where a, b and c are constants, and a is non-zero.

The roots of a quadratic function can be found by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0.

A quadratic function may have 0, 1 or 2 real roots.
These roots can be computed using the quadratic formula, shown below:


> root = [−b ± √(b^2 − 4ac)] / 2a


The portion of the expression under the square root sign is called the discriminant.

If the discriminant is negative then the quadratic equation does not have any real roots.

If the discriminant is 0, then the equation has one real root.

Otherwise the equation has two real roots, and the expression must be evaluated twice, once using a plus sign, and once using a minus sign, when computing the numerator.

Write a program that computes the real roots of a quadratic function.

Your program should begin by prompting the user for the values of a, b and c. 

Then it should display a message indicating the number of real roots, along with the values of the real roots (if any).
"""

#importing math module to be used for squareroot function
import math

#using try/except to prevent program from crashing
try:
  #calling user to enter the first number
  a = int(input("Please enter the value of 'a': "))

  #ensuring that the first number 'a' is not 0
  if a == 0:
    print("'a' cannot be 0, please enter another number")
  
  #continuing with valid entries of a, and calling user to enter remaining numbers
  else:
    b = int(input("Please enter the value of 'b': "))
    c = int(input("Please enter the value of 'c': "))

    #determining the discriminant
    discriminant = (b**2) - (4*a*c)

    #printing outputs and calculating roots according to discriminant value
    if discriminant < 0:
      print(f"\nYou entered {a}, {b}, {c}, and the quadratic equation is f(x) = {a}x^2 + {b}x + {c}\n")
      print(f"Based on these numbers, and a discriminant of {discriminant}, there is no real root")

    elif discriminant == 0:
      root = -b/2*a
      print(f"\nYou entered {a}, {b}, {c}, and the quadratic equation is f(x) = {a}x^2 + {b}x + {c}\n")
      print(f"Based on these numbers, and a discriminant of {discriminant}, there is only one real root and that is {root:.2f}")
  
    else:
      sqr_discriminant = math.sqrt(discriminant)
      root = (-b + (sqr_discriminant)) / (2*a)
      print(f"\nYou entered {a}, {b}, {c}, and the quadratic equation is f(x) = {a}x^2 + {b}x + {c}\n")
      print(f"Based on these numbers, and a discriminant of {discriminant}, there are two  real roots and they are {root:.2f} and -{root:.2f}")

except:
  print("Please enter a valid number")