# -*- coding: utf-8 -*-
"""Day 35

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WqREjHH9YwrnobuNEzuj2DxG8mxF_Zdw
"""



"""
TASK 1

The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare.

YEAR    |   ANIMAL
2000    |   Dragon
2001    |   Snake
2002    |   Horse
2003    |   Sheep
2004    |   Monkey
2005    |   Rooster
2006    |   Dog
2007    |   Pig
2008    |   Rat
2009    |   Ox
2010    |   Tiger
2011    |   Hare

Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table.
"""

#using try/except to prevent the program from crashing if a non-numerical input is entered
try:

  #calling user to enter input
  year = int(input("Enter the year: "))


  #filtering out negative entries
  if year < 0:
    print("\nYear cannot be less than 0.")

  #specifying conditions for each of the years
  else:
    if year % 12 == 8:
      animal = "Dragon"

    elif year % 12 == 9:
      animal = "Snake"

    elif year % 12 == 10:
      animal = "Horse"

    elif year % 12 == 11:
      animal = "Sheep"

    elif year % 12 == 0:
      animal = "Monkey"

    elif year % 12 == 1:
      animal = "Rooster"

    elif year % 12 == 2:
      animal = "Dog"

    elif year % 12 == 3:
      animal = "Pig"

    elif year % 12 == 4:
      animal = "Rat"

    elif year % 12 == 5:
      animal = "Ox"

    elif year % 12 == 6:
      animal = "Tiger"

    elif year % 12 == 7:
      animal = "Hare"

    #print output
    print(f"\nThe Chinese zodiac animal of this year is {animal}.")

#error message for non-numeric input
except ValueError:
  print("Enter a numerical input")



"""
TASK 2

The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors:

MAGNITUDE             |   DESCRIPTOR
Less than 2.0         |   Micro
2.0 to less than 3.0  |   Very minor
3.0 to less than 4.0  |   Minor
4.0 to less than 5.0  |   Light
5.0 to less than 6.0  |   Moderate
6.0 to less than 7.0  |   Strong
7.0 to less than 8.0  |   Major
8.0 to less than 10.0 |   Great
10.0 or more          |   Meteoric

Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.
"""

#using try/except to prevent the program from crashng if a non-numeric input is entered
try:

  #calling user to enter the magnitude
  magnitude = float(input("Enter the magnitude: "))

  #using conditionals to generate the respective desciptors of the given magnitudes
  if magnitude < 2.0:
    descriptor = "micro"

  elif magnitude >= 2.0 and magnitude < 3.0:
    descriptor = "very minor"

  elif magnitude >= 3.0 and magnitude < 4.0:
    descriptor = "minor"

  elif magnitude >= 4.0 and magnitude < 5.0:
    descriptor = "light"

  elif magnitude >= 5.0 and magnitude < 6.0:
    descriptor = "moderate"

  elif magnitude >= 6.0 and magnitude < 7.0:
    descriptor = "strong"

  elif magnitude >= 7.0 and magnitude < 8.0:
    descriptor = "major"

  elif magnitude >= 8.0 and magnitude < 10.0:
    descriptor = "great"

  else:
    descriptor = "meteoric"

  #print output
  print(f"\nA magnitude of {magnitude} is considered to be {descriptor}.")

#error message for non-numeric input
except ValueError:
  print("Enter a valid numeric input")



"""
TASK 3

At a particular university, letter grades are mapped to grade points in the following
manner:

LETTER | GRADE POINTS
A+     |  4.0
A      |  4.0
A???     |  3.7
B+     |  3.3
B      |  3.0
B???     |  2.7
C+     |  2.3
C      |  2.0
C???     |  1.7
D+     |  1.3
D      |  1.0
F      |  0

Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
that your program generates an appropriate error message if the user enters an invalid
letter grade.
"""

#defininf a list of valid letter grades
letter_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]

#asking user to enter letter grade
user_letter_grade = input("Enter the letter grade: ").strip().upper()

#filtering out invalid entries
if user_letter_grade not in letter_grades:
  print("Enter a valid letter grade")

else:

  #using conditionals to assign grade points to each valid letter grade
  if user_letter_grade == "A+":
    grade_points = 4.0

  elif user_letter_grade == "A":
    grade_points = 4.0

  elif user_letter_grade == "A-":
    grade_points = 3.7

  elif user_letter_grade == "B+":
    grade_points = 3.3

  elif user_letter_grade == "B":
    grade_points = 3.0

  elif user_letter_grade == "B-":
    grade_points = 2.7

  elif user_letter_grade == "C+":
    grade_points = 2.3

  elif user_letter_grade == "C":
    grade_points = 2.0

  elif user_letter_grade == "C-":
    grade_points = 1.7

  elif user_letter_grade == "D+":
    grade_points = 1.3

  elif user_letter_grade == "D":
    grade_points = 1.0

  else:
    grade_points = 0

  #print output
  print(f"\nThe grade point for {user_letter_grade} is {grade_points}")

    
    
"""
TASK 4

In the previous exercise you created a program that converts a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ for a 4.0 (or greater) grade point average.
"""

#using try/except to prevent the program from crashing id a non-numeric input is entered
try:

  #asking user to enter the grade point
  user_grade_point = float(input("Enter a grade point: "))

  #using conditionals to assign letter grades to entered point
  if user_grade_point <= 0:
    letter_grade = "F"

  elif user_grade_point > 0 and user_grade_point <= 1.0:
    letter_grade = "D"

  elif user_grade_point > 1.0 and user_grade_point <= 1.3:
    letter_grade = "D+"

  elif user_grade_point > 1.3 and user_grade_point <= 1.7:
    letter_grade = "C-"

  elif user_grade_point > 1.7 and user_grade_point <= 2.0:
    letter_grade = "C"

  elif user_grade_point > 2.0 and user_grade_point <= 2.3:
    letter_grade = "C+"

  elif user_grade_point > 2.3 and user_grade_point <= 2.7:
    letter_grade = "B-"

  elif user_grade_point > 2.7 and user_grade_point <= 3.0:
    letter_grade = "B"

  elif user_grade_point > 3.0 and user_grade_point <= 3.3:
    letter_grade = "B+"

  elif user_grade_point > 3.3 and user_grade_point <= 3.7:
    letter_grade = "A-"

  elif user_grade_point > 3.7 and user_grade_point < 4.0:
    letter_grade = "A"

  else:
    letter_grade = "A+"

  #printing output
  print(f"\nThe letter grade of {user_grade_point} is {letter_grade}.")

#error message for non-numeric input
except ValueError:
  print("Enter a numerical input")



"""
TASK 5

The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

COLOR   |   WAVELENGTH (nm)
Violet  |   380 to less than 450
Blue    |   450 to less than 495
Green   |   495 to less than 570
Yellow  |   570 to less than 590
Orange  |   590 to less than 620
Red     |   620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
"""

#using try/except to prevent program from crashing
try:

  #asking user to enter the wavelength
  wavelength = float(input("Enter the wavelength: "))

  #using conditionals to asisgn colours to the visible spectrum
  #and to assign an output to wavelengths outside the visible spectrum range
  if wavelength >= 380 and wavelength <450:
    colour = "violet"

  elif wavelength >= 450 and wavelength < 495:
    colour = "blue"

  elif wavelength >= 495 and wavelength < 570:
    colour = "green"

  elif wavelength >= 570 and wavelength < 590:
    colour = "yellow"

  elif wavelength >= 590 and wavelength < 620:
    colour = "orange"

  elif wavelength >= 620 and wavelength <= 750:
    colour = "red"

  else:
    colour = "outside the visible spectrum"

  #print output
  print(f"\nThe colour of {wavelength}nm wavelength is {colour}.")

#error message for non-numeric input
except ValueError:
  print("Enter a valid numeric input")



"""
TASK 6

Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

NAME                |   FREQUENCY RANGE (Hz)
Radio waves         |   Less than 3 ?? 10^9
Microwaves          |   3 ?? 10^9 to less than 3 ?? 10^12
Infrared light      |   3 ?? 10^12 to less than 4.3 ?? 10^14
Visible light       |   4.3 ?? 10^14 to less than 7.5 ?? 10^14
Ultraviolet light   |   7.5 ?? 10^14 to less than 3 ?? 10^17
X-rays              |   3 ?? 10^17 to less than 3 ?? 10^19
Gamma rays          |   3 ?? 10^19 or more

Write a program that reads the frequency of the radiation from the user and displays
the appropriate name.
"""

#using try/except to prevent message from crashing if a non-numeric input is entered
try:

  #asking user to enter frequency
  frequency = float(input("Enter the frequency: "))

  #using conditionals to assign names
  if frequency < (3 * (10**9)):
    name = "radio waves"

  elif frequency >= (3 * (10**9)) and frequency < (3 * (10**12)):
    name = "microwaves"

  elif frequency >= (3 * (10**12)) and frequency < (4.3 * (10**14)):
    name = "infrared light"

  elif frequency >= (4.3 * (10**14)) and frequency < (7.5 * (10**14)):
    name = "visible light"

  elif frequency >= (7.5 * (10**14)) and frequency < (3 * (10**17)):
    name = "ultraviolet light"

  elif frequency >= (3 * (10**17)) and frequency < (3 * (10**19)):
    name = "X-rays"

  else:
    name = "gamma rays"

  #printing output
  print(f"\n{frequency}Hz corresponds to {name}.")

#error message for non-numeric inputs
except:
  print("Enter a valid numeric input")



"""
TASK 7

A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. 

Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each.

All cell phone bills include an additional charge of $0.44 to support 911 call centers,
and the entire bill (including the 911 charge) is subject to 5 percent sales tax.

Write a program that reads the number of minutes and text messages used in a
month from the user.

Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount.

Only display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.

"""

#using try/except to prevent program from crashing if non-numeric input is entered
try:

  #calling user to enter the number of minutes and sms used in the month
  minutes = float(input("Enter the number of minutes you used this month: "))
  sms = int(input("Enter the number of messages sent this month: "))

  #initiating all base figures and the main charge at the base conditions
  base_minutes = 50
  base_sms = 50
  base_charge = 15.00
  main_charge = 15.00

  #raising additional charge for each minute above 50
  if minutes > 50:
    additional_minutes_charge = 0.25 * (minutes - base_minutes)
  else:
    additional_minutes_charge = 0

  #raising additional charge for each sms above 50
  if sms > 50:
    additional_sms_charge = 0.15 * (sms - base_sms)
  else:
    additional_sms_charge = 0

  #generating the main charge after factoring in additional minutes and/or sms charge(s)
  main_charge += (additional_sms_charge + additional_minutes_charge)

  #adding in the fee to support 911
  charge_and_911 = main_charge + 0.44

  #generating the 5% sales tax
  tax = 0.05 * charge_and_911

  #and generating the final charge after adding in tax
  final_charge = tax + charge_and_911


  #printing outputs
  #and using conditionals to control when to print the respective additional charges
  print(f"\nBase charge: ${base_charge:.2f}")

  if additional_minutes_charge != 0:
    print(f"\nAdditional minutes charge: ${additional_minutes_charge:.2f}")

  if additional_sms_charge != 0:
    print(f"\nAdditional text message charge: ${additional_sms_charge:.2f}")

  print(f"\nMain charge: ${main_charge:.2f}")
  print(f"\nCharge with 911 fee of $0.44 included: ${charge_and_911:.2f}")
  print(f"\nTax (5%): ${tax:.2f}")
  print(f"\nFinal charge: ${final_charge:.2f}")

#error message for non-numeric input
except ValueError:
  print("Enter a valid numeric input")



"""
TASK 8

Most years have 365 days. However, the time required for the Earth to orbit the Sun
is actually slightly more than that. As a result, an extra day, February 29, is included
in some years to correct for this difference. Such years are referred to as leap years.
The rules for determining whether or not a year is a leap year follow:

??? Any year that is divisible by 400 is a leap year.
??? Of the remaining years, any year that is divisible by 100 is not a leap year.
??? Of the remaining years, any year that is divisible by 4 is a leap year.
??? All other years are not leap years.

Write a program that reads a year from the user and displays a message indicating
whether or not it is a leap year.
"""

#using try/except to prevent program from crashing if a non-numeric input is entered
try:

  #asking user to enter the year
  user_year = int(input("Enter the year: "))


  #testing the given conditions and assigning leap year as boolean value

  #testing the first given condition
  if user_year % 400 == 0:
    leap_year = True

  else:

    #tesing the second condition
    if user_year % 100 == 0:
      leap_year = False

    else:

      #and the third condition
      if user_year % 4 == 0:
        leap_year = True

      #and the last condition
      else:
        leap_year = False

  #printing output based on bool value
  if leap_year:   #print out for leap_year == True
    print(f"\n{user_year} is a leap year.")

  else:     #print out for leap_year == False
    print(f"\n{user_year} is NOT a leap year.")

#error message for non-numeric inputs
except ValueError:
  print("Enter a valid year in numbers")



"""
TASK 9

Write a program that reads a date from the user and computes its immediate successor.

For example, if the user enters values that represent 2013-11-18 then your program
should display a message indicating that the day immediately after 2013-11-18 is
2013-11-19.

If the user enters values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01.

If the user enters values that represent 2013-12-31
then the program should indicate that the next day is 2014-01-01.

The date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years.
"""

#importing datetime function
import datetime

#using try/except to prevent program from crashing if an invalid date is entered
try:

  #calling user to enter date
  d = int(input("Enter the day: "))
  m = int(input("Enter the month: "))
  y = int(input("Enter the year: "))
     
 
 #raising the given date and the next date
  given_date = datetime.date(y, m, d) 
  next_day = given_date + datetime.timedelta(days=1) 

  #print output
  print(f"\nThe given date is {given_date} and the next day is {next_day}.") 

#error message for invalid date entries
except ValueError:
  print("Please enter a valid date!")



"""
TASK 10

In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three numbers.

When all of the license plates following that pattern had been used,
the format was changed to four numbers followed by three uppercase letters.

Write a program that begins by reading a string of characters from the user.

Then your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate.

Your program should display an appropriate message if the string entered by the user
is not valid for either style of license plate
"""

#asking user to enter the license plate identifier
license = input("Enter the license plate identifier: ").strip()

#for old styled plates
if len(license) == 6:
  
  #selecting valid old styles
  if license[0:3].isupper() and license[3:6].isdigit():
    print("This is an old license plate style")

  #non-valid old styles
  else:
    print("This is not a valid license plate number!")

#for new styled plates
elif len(license) == 7:
  
  #selecting valid new styles
  if license[0:4].isdigit() and license[4:7].isupper():
    print("This is a new license plate style")

  #non-valid new styles
  else:
    print("This is not a valid license plate number!")

#non-valid license plate
else:
  print("This is not a valid license plate number!")



"""
TASK 11

A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
between 1 and 36 are used to number the black spaces.
Many different bets can be placed in roulette. We will only consider the following
subset of them in this exercise:
??? Single number (1 to 36, 0, or 00)
??? Red versus Black
??? Odd versus Even (Note that 0 and 00 do not pay out for even)
??? 1 to 18 versus 19 to 36
Write a program that simulates a spin of a roulette wheel by using Python???s random
number generator. Display the number that was selected and all of the bets that must
be payed. For example, if 13 is selected then your program should display:
The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18
If the simulation results in 0 or 00 then your program should display Pay 0 or
Pay 00 without any further output.
"""

#importing random module for the game
import random

#defining lists for each colour
green = ["0", "00"]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [i for i in list(range(1,37)) if i not in red]

#generating the bet
bet = random.randint(0,37)

#displaying generated bet
print("BET:", bet)

#pay out put for 0
if bet == 0 or bet == 00:
  print("\npay",bet)

#pay outputs for other bets
else:

  #single number display
  print("\npay",bet)

  #red versus black display
  if bet in red:
    print("pay red")

  elif bet in black:
    print("pay black")

  #odd versus even display
  if bet != 0:
    if bet % 2 == 0:
      print("pay even")
    else:
      print("pay odd")

  #1 to 18 vs 19 to 36 display
  if bet in range(1,19):
    print("pay 1 to 18")
  elif bet in range(19,37):
    print("pay 19 to 36")
