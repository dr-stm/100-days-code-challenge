"""
Using your solutions to previous exercises, write a program that generates a random
good password and displays it. Count and display the number of attempts that were
needed before a good password was generated. Structure your solution so that it
imports the functions you wrote previously and then calls them from a function
named main in the file that you create for this exercise
"""

#importing the functions from the respective tasks
from Task_4 import password
from Task_6 import length
from Task_6 import digit
from Task_6 import upper
from Task_6 import lower
from Task_6 import check

#defining the main function to generate a random password and check if it's good or not
def main():

  #storing all functions in a variable
  pword = password()
  leng = length(pword)
  digt = digit(pword)
  upp = upper(pword)
  low = lower(pword)
  crosscheck = check(leng, digt, upp, low)

  #activating the functions
  pword
  leng
  digt
  upp
  low
  crosscheck

  #initiating the number of attempts
  attempts = 1
  
  #condition for a recheck
  while crosscheck == False:
    attempts += 1
    pword
    leng
    digt
    upp
    low
    crosscheck

  #printing output
  print(f"The good password is {pword}")
  print(f"The length of the password is {len(pword)}")
  print(f"It took {attempts} attempt(s) to generate it.")

main()