# -*- coding: utf-8 -*-
"""Day 29

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x6XYo-VTQ8Zz_sos6lp7xXDz3glhqAFm
"""



"""
TASK 1

When writing out a list of items in English, one normally separates the items with
commas. In addition, the word “and” is normally included before the last item, unless
the list only contains one item. Consider the following four lists:

apples
apples and oranges
apples, oranges and bananas
apples, oranges, bananas and lemons

Write a function that takes a list of strings as its only parameter. Your function
should return a string that contains all of the items in the list formatted in the manner
described previously as its only result. While the examples shown previously only
include lists containing four elements or less, your function should behave correctly
for lists of any length. Include a main program that reads several items from the user,
formats them by calling your function, and then displays the result returned by the
function.
"""

#defining function for formatting a list
def list_format(user_item_list):

  #initiating the string
  user_item_string = " "

  #initiating conditions for more than one entry
  if len(user_item_list) > 1:

    #condition for two entries only
    if len(user_item_list) == 2:
      user_item_list.insert(1, "and")   #inserting "and" between the entries
    
    #condition for three entries and above
    else:
      user_item_list.insert(-1, "and") #inserting "and" between the last two entries
      
      #assessing each item before the last two entries
      for item in user_item_list[:-3]:

        #inserting comma at the end of those assessed entries and ...
        #replacing the original entry in the list with a similar entry that now has a comma
        user_item_list[user_item_list.index(item)] = item + ","

  #joining the formatted entries in the list into a string using join function on the initiated string
  return user_item_string.join(user_item_list)


#defining the main function
def main():
  
  #initiating the list to house all entries
  user_item_list = []
  
  #calling user to enter first entry
  user_item = input("Enter an item (enter dead space to end): ").strip()

  #condition for user to continue entering items
  while user_item != "":

    #adding each added item to the list
    user_item_list.append(user_item)

    #calling user to enter another input if the breaking condition is still not met
    user_item = input("Enter an item (enter dead space to end): ").strip()
  
  #printing output
  print(f"\nThe items are: {list_format(user_item_list)}.")

#activating main function
main()




"""
TASK 2

In order to win the top prize in a particular lottery, one must match all 6 numbers
on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
organizer. Write a program that generates a random selection of 6 numbers for a
lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
Display the numbers in ascending order.
"""

#importing random module for generation of random numbers
import random

#initiating a list to house the selected numbers
lottery_numbers = []

#initiating condition for populating the list
while len(lottery_numbers) != 6:

  #selecting a random number
  x = random.randrange(1,50)

  #ensuring the number is not duplicated by making sure it is not in the list already
  if x not in lottery_numbers:

    #adding the random number that is not already in the list, to the list
    lottery_numbers.append(x)

#printing output
print(f"The randomly selected numbers are {sorted(lottery_numbers)}")




"""
TASK 3

It is possible to compute the area of a triangle when the lengths of all three sides are known.
Let s1, s2 and s3 be the lengths of the sides. Let s = (s1 + s2 + s3)/2.
Then the area of the triangle can be calculated using the following formula:
area = square root of (s × (s − s1) × (s − s2) × (s − s3))
Develop a program that reads the lengths of the sides of a triangle from the user
and displays its area.
"""

#importing math module for the needed square root function
import math

#using try/except to prevent program from crashing if non-numeric input is entered
try:

  #asking user to enter the three sides of the triangle
  s1 = float(input("Enter the length of the first side: "))
  s2 = float(input("Enter the length of the second side: "))
  s3 = float(input("Enter the length of the third side: "))

  #ensuring that only positive numbers are entered, since triangular sides are natural numbers
  if s1 > 0 and s2 > 0 and s3 > 0:
    
    #generating "s" based on given formula
    s = (s1 + s2 + s3)/2

    #generating triangular area based on given formula
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

    #printing output
    print(f"\nThe area of the triangle is {area:.2f}")

  #error message for negative number entries
  else:
    print("\nTriangle sides can only be positive numbered, please enter valid numbers")

#error message for non-numeric entries
except ValueError as err:
  print(f"\nPlease enter a valid number, we {err}")




"""
TASK 4

Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.
"""

try:
  #calling user to enter an integer
  user_num = int(input("Enter a number: "))

  #generating the list of each of the digits by first converting the number to string
  user_num_list = list(str(user_num))

  #changing each of the item of the list from string to integer
  for i in range(len(user_num_list)):
    user_num_list[i] = int(user_num_list[i])

  #printing out the sum of the list which contains the digit
  print(f"\nThe sum of the digits of the number you entered is {sum(user_num_list)}")

#error message for non-numeric entries
except:
  print("Please enter a valid integer")




"""
TASK 5

Python includes a library of functions for working with time, including a function
called asctime in the time module. It reads the current time from the computer’s internal clock
and returns it in a human-readable format. Write a program that displays 
the current time and date. Your program will not require any input from the user.
"""

#importing the mentioned function from the time module
from time import asctime

#printing the current time
asctime()




"""
TASK 6

Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""

#using try/except to prevent program from crashing
try:

  #calling user to enter respective durations
  days = int(input("Enter the number of days: "))
  hours = int(input("Enter the number of hours: "))
  minutes = int(input("Enter the number of minutes: "))
  seconds = int(input("Enter the number of seconds: "))

  #calculating how many seconds in the given duration
  total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

  #printing output
  print(f"\nThe total seconds in this duration is {total_seconds} seconds.")

#error message
except:
  print("Please enter valid numbers only")



"""
TASK 7

In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary.
"""


#using try/except to prevent program from crashing
try:

  #asking user to enter the duration in seconds
  duration = int(input("Enter the duration in seconds: "))

  #using formulas to derive the equivalent time formats in the given seconds
  rev_seconds = duration % 60
  rev_minutes = (duration // 60) % 60
  rev_hours = ((duration // 60) // 60) % 24
  rev_days = duration // (24 * 60 * 60)

  #printing output
  print(f"\nThe equivalent amount of time is {rev_days:d}:{rev_hours:02d}:{rev_minutes:02d}:{rev_seconds:02d}")

#error message
except:
  print("enter a valid number")
