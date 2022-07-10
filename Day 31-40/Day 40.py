"""
Write a function that determines how many days there are in a particular month. Your
function will take two parameters: The month as an integer between 1 and 12, and
the year as a four digit integer. Ensure that your function reports the correct number
of days in February for leap years. Include a main program that reads a month and
year from the user and displays the number of days in that month. You may find your
solution to Exercise 57 helpful when solving this problem.
"""

#testing if the year is a leap year
def isLeapYear(year):
  if year % 400 == 0:
    return True
  else:
    if year % 100 == 0:
      return False
    else:
      if year % 4 == 0:
        return True
      else:
        return False

#assigning the respective number of days in each month in a given year (including leap years)
def days_month(year,month):
  days_31 = [1, 3, 5, 7, 8, 10, 12]
  days_30 = [4, 6, 9, 11]

  if month in days_31:
    return 31
  elif month in days_30:
    return 30
  else:
    if isLeapYear(year):
      return 29
    else:
      return 28

#defining main function
def main():

  #using try/except to prevent program from crashing if a non-numeric input is entered
  try:

    #calling user to enter month and year
    month = int(input("Enter the month as a number: "))
    year = int(input("Enter the year (must be a four-digit year): "))

    #filtering out invalid month entries
    if month not in range (1, 13):
      print("Please enter a valid month")

    #for valid month entries
    else:

      #filtering out invalid year entries
      if len(str(year)) != 4:
        print("Please enter a valid four-digit year")

      #for valid year entries
      else:
        #activting leap year check
        isLeapYear(year)
        #and the subsequent check for number of days
        days = days_month(year,month)

        #printing output
        print(f"\nThe number of days in the month and year you entered is {days} days.")

  #error message for non-numeric input
  except ValueError:
    print("Please enter a valid numeric input.")

#activating main function
main()