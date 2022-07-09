"""
Write a program that computes the perimeter of a polygon. Begin by reading the x
and y values for the first point on the perimeter of the polygon from the user. Then
continue reading pairs of x and y values until the user enters a blank line for the
x-coordinate. Each time you read an additional coordinate you should compute the
distance to the previous point and add it to the perimeter. When a blank line is entered
for the x-coordinate your program should add the distance from the last point back
to the first point to the perimeter. Then it should display the total perimeter. Sample
input and output is shown below, with user input shown in bold:
Enter the x part of the coordinate: 0
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 1
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 0
Enter the y part of the coordinate: 1
Enter the x part of the coordinate: (blank to quit):
The perimeter of that polygon is 3.414213562373095
"""

#formula for distance between two points is equivalent to the hypotenuse formula in the Pythagoras theorem:
#√[(x₂ - x₁)² + (y₂ - y₁)²]

#importing math module for squareroot needed in the task
import math

#initiating the perimeter
perimeter = 0

#using try/except for preventing the program from crashing if non-numeric input is entered
try:
  #asking user to enter the coordinates of the first point
  x1 = float(input("Enter the x-coordinate of the first point: "))
  y1 = float(input("Enter the y-coordinate of the first point: "))

  #storing the first coordinates in a different variable that will be used at last
  first_x = x1
  first_y = y1

  #collecting the second coordinates
  x2 = float(input("Enter the x-coordinate of the second point: "))
  y2 = float(input("Enter the y-coordinate of the second point: "))

  #updating the perimeter with the distance between the 2 points provided
  perimeter += (math.sqrt(((x2-x1)**2) + ((y2-y1)**2)))

  #now saving the second coordinates as the first so that ...
  # ... new set of coordinates can be collected for the calculation
  x1 = x2
  y1 = y2

  #collecting new coordinates (if blank is entered the program ends)
  x2 = input("Enter the x-coordinate of the other point (blank to quit): ")
  while x2 != "":
    #y is collected if blank is not entered
    y2 = float(input("Enter the corresponding y-coordinate: "))

    #perimeter is updated by the distance between the new point and the previous point
    perimeter += math.sqrt(((float(x2)-x1)**2) + ((y2-y1)**2))

    #storing the new points as the old coordinates now
    x1 = float(x2)
    y1 = y2

    #and asking for new points to be entered (if blank, the program is ended)
    x2 = input("Enter the x-coordinate of the other point (blank to quit): ")

  #if blank is entered, the program ends by ...
  # ...calculating the distance between the last and the first points
  perimeter += math.sqrt(((first_x-x1)**2) + ((first_y-y1)**2))

  #printing output
  print(f"\nThe perimeter of the polygon is {perimeter}")

#printing error message for non-numeric input at any point
except ValueError:
  print("You have entered an invalid input. Enter a numeric value.")