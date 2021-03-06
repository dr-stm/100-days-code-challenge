# -*- coding: utf-8 -*-
"""Day 30

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1deZ0Afro1EotvEWthaV9UgE80I3XUgtk
"""

"""
TASK 1

When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.
In 2001, Canada, the United Kingdom and the United States adopted the following formula
for computing the wind chill index. Within the formula Ta is the
air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used with temperatures in
degrees Fahrenheit and wind speeds in miles per hour.

WCI = 13.12 + 0.6215Ta − 11.37V^0.16 + 0.3965TaV^0.16

Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer.
The wind chill index is only considered valid for temperatures less than or
equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per hour.
"""

#using try/except to prevent program from crashing if non-numerical values are entered
try:

  #calling user to enter air temperature
  Ta = float(input("Enter the air temperature in ℃ (valid values are less than or equal to 10℃): "))
  
  #filtering out non-valid air temperature ranges
  if Ta > 10:
    print("\nPlease enter a valid air temperature - valid values are less than or equal to 10℃")

  #for valid air temperature ranges
  else:

    #calling user to enter wind speed
    V = float(input("Enter the wind speed in km/hr (valid values are more than or equal to 4.8km/hr): "))

    #filtering out non-valid wind speeds
    if V < 4.8:
      print("\nPlease enter a valid wind speed - valid values are more than or equal to 4.8km/hr")

    #for valid wind speeds
    else:

      #computing wind chill index using the given formula  
      WCI = 13.12 + (0.6215*Ta) - (11.37*(V**0.16)) + (0.3965*Ta*(V**0.16))

      #printing output
      print(f"\nThe wind chill index is {int(WCI)}")

#error message for non-numeric inputs
except ValueError:
  print("Please enter a valid numerical input.")

"""
TASK 2

A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:

area = (n × s^2)/(4 × tan (pi/n))

Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.
"""
#importing math module for the tangent function and pi
import math

#using try/except to prevent program from crashing if non-numeric inputs are entered
try:

  #calling user to enter length and number of the sides
  s = float(input("Enter the length of a side of the polygon: "))
  n = float(input("Enter the number of sides of the polygon: "))

  #filtering out non-valid entries, since the length cannot be negative
  #and polygon shape can be formed from 3 sides and above
  if s <= 0 or n <= 2:
    print("\nPlease enter a valid side/number of sides")
    print("Length can only be positive and number of sides can only be 3 and above")

  else:
    #computing the area for valid entries
    area = (n * s**2)/(4 * math.tan(math.pi/n))

    #printing output
    print(f"\nThe area of this regular polygon is {area:.2f}")

#error message
except ValueError:
  print("Please enter a valid numeric input")

"""
TASK 3

The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314J/molK , and T is the
temperature in degrees Kelvin.
Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit.
Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
multiply it by 59 and then add 273.15 to it.
"""

#using try/except to prevent program from crashing if non-numeric inputs are entered
try:

  #calling user to enter pressure, volume and temperature
  P = float(input("Enter the pressure in Pascals: "))
  V = float(input("Enter the volume in litres: "))
  R = 8.314
  T = float(input("Enter the temperature in ℃: ")) + 273.15

  #filtering out non-realistic entries (assuming pressure to be absolute)
  if P <= 0 or V <= 0:
    print("Pressure or Volume can only be positive numbers, please supply valid entries")
  
  #for valid entries
  else:
    #formula for numbers of mole
    n = (P * V)/(R * T)

    #printing output
    print(f"\nThe amount of substances in your supplied entries are {n:.2f} moles.")

#error message
except:
  print("Please enter a valid numeric input")