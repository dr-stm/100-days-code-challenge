# -*- coding: utf-8 -*-
"""Day 13
"""

"""
Canada has three national holidays which fall on the same dates each year

JANUARY 1 = New year's day
JULY 1 = Canada day
December 25 = Christmas day

Write a program that reads a month and day from the user.
If the month and day match one of the holidays listed previously then your program should display the holiday’s name.
Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.

Canada has two additional national holidays, Good Friday and Labour Day, whose dates vary from year to year.
There are also numerous provincial and territorial holidays, some of which have fixed dates,
and some of which have variable dates. We will not consider any of these additional holidays in this exercise.
"""

#importing calendar module
import calendar

#creating a list from months' names
months_list = list(calendar.month_name)

#and another list containing the ,onths with fixed date holidays
fixed_date_months = ["January", "July", "December"]

#asking user to enter month
month = input("Please enter the full name of the month: ").title()

#filtering out invalid month name
if month not in months_list:
  print("Please enter the full name of a valid month")
else:
  day = int (input("Please enter the date of the month: ")) #asking user to enter date
  
  #using conditionals to execute task
  if month in months_list:
    if month in fixed_date_months:
      if month == fixed_date_months[0] and day == 1:
        print("New year's day")
      elif month == fixed_date_months[1] and day == 1:
        print("Canada day")
      elif month == fixed_date_months[2] and day == 25:
        print("Christmas day")
      else:
        print("No fixed-date holiday")
    else:
      print("No fixed-date holiday")
  else:
    print("No fixed-date holiday")
