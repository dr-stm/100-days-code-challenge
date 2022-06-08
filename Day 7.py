# -*- coding: utf-8 -*-
"""Day 7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10UYobBVa7JIVKqsDjFcRcVz8g1ndlc51

# **CHALLENGE DAY 7**

# Task 1

A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.

All 3 sides of an equilateral triangle have the same length.

An isosceles triangle has two sides that are the same length, and a third side that is a different length.

If all of the sides have different lengths then the triangle is scalene.

Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.

**METHOD 1**
"""

#using try/except to prevent program from crashing if wrong value is entered
try:
  #asking user to input the lengths
  triangle_side_length1 = int(input("Please enter the length of the first side: "))
  triangle_side_length2 = int(input("Please enter the length of the second side: "))
  triangle_side_length3 = int(input("Please enter the length of the third side: "))

  #using conditionals to assign triangle type
  if triangle_side_length1 == triangle_side_length2 and triangle_side_length1 == triangle_side_length3:
    print("This will make an equilateral triangle")
  elif (triangle_side_length1 == triangle_side_length2 and triangle_side_length1 != triangle_side_length3) or\
  (triangle_side_length2 == triangle_side_length3 and triangle_side_length2 != triangle_side_length1) or\
  (triangle_side_length1 == triangle_side_length3 and triangle_side_length2 != triangle_side_length1):
    print("This will make an isosceles triangle")
  else:
    print("this will make a scalene triangle")
except ValueError:
  print("Please enter a valid number")

"""**METHOD 2**"""

#using try/except to prevent program from crashing if wrong value is entered
try:
  #asking user to input the lengths
  side_length = int(input("Please the enter the side of the triangle: "))
  triangle_sides = [] #initialising the list to contain the triangle sides

  #using conditional statements to repeat program for user to input sides length
  while len(triangle_sides) < 3:
    triangle_sides.append(side_length)
    if len(triangle_sides) >= 3:
      break
    else:
      side_length = int(input("Please the enter the side of the triangle: "))

  #using conditionals to assign triangle type
  print("The length of the triangle sides include: ", triangle_sides)
  if triangle_sides[0] == triangle_sides[1] and triangle_sides[0] == triangle_sides[2]:
    print("This will make an equilateral triangle")
  elif (triangle_sides[0] == triangle_sides[1] and triangle_sides[0] != triangle_sides[2]) or\
  (triangle_sides[1] == triangle_sides[2] and triangle_sides[1] != triangle_sides[0]) or\
  (triangle_sides[0] == triangle_sides[2] and triangle_sides[1] != triangle_sides[0]):
    print("This will make an isosceles triangle")
  else:
    print("this will make a scalene triangle")
except ValueError:
  print("please enter a valid numerical input")