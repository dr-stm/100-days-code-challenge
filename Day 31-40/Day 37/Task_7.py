"""
TASK 7

Using your solutions to previous exercises, write a program that generates a random
good password and displays it. Count and display the number of attempts that were
needed before a good password was generated. Structure your solution so that it
imports the functions you wrote previously and then calls them from a function
named main in the file that you create for this exercise
"""

#importing the functions from the respective tasks
from Task_4 import password
from Task_6 import check

#defining the main function to generate a random password and check if it's good or not
def main():

  #activating the functions
  password()
  check(password())

  #initiating the number of attempts
  attempts = 1
  
  #condition for a recheck
  while check(password()) == False:
    attempts += 1
    password()
    check(password())

  #printing output
  print(f"The good password is {password()}")
  print(f"The length of the password is {len(password())}")
  print(f"It took {attempts} attempt(s) to generate it.")

main()