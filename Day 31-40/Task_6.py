"""
TASK 6

In this exercise you will write a function that determines whether or not a password
is good. We will define a good password to be a one that is at least 8 characters
long and contains at least one uppercase letter, at least one lowercase letter, and at
least one number. Your function should return true if the password passed to it as
its only parameter is good. Otherwise it should return false. Include a main program
that reads a password from the user and reports whether or not it is good. Ensure
that your main program only runs when your solution has not been imported into
another file.
"""

#function to check for length of password
def length(password):

  #good length
  if len(password) >= 8:
    return True

  #bad length
  else:
    return False

#function to check if it has a digit
def digit(password):
  #checking each item in the password
  for x in password:
    
    #if item is a digit, return true and stop looping
    if x.isdigit():
      return True
      break

    #else continue checking, if at the end, the loop has not broken, then return false
    else:
      continue
      return False

#checking for uppercase
def upper(password):

  #checking each item in the password
  for x in password:

    #if item is an uppercase, return true and stop looping
    if x.isupper():
      return True
      break

    #else continue checking, if at the end, the loop has not broken, then return false
    else:
      continue
      return False

#checking for lowercase
def lower(password):

  #checking each item in the password
  for x in password:

    #if item is an uppercase, return true and stop looping
    if x.islower():
      return True
      break

    #else continue checking, if at the end, the loop has not broken, then return false
    else:
      continue
      return False

#checking the password as a whole using the parameters from the previously checked components
def check(leng, digt, upp, low):
  #good password can only be true when all those conditions are true
  if leng == True and digt == True and upp == True and low == True:
    return True
  else:
    return False

#initiating main function
def main():
  #asking user to enter password
  password = input("Enter the password you want to check: ").strip()

  #storing all functions in a variable
  leng = length(password)
  digt = digit(password)
  upp = upper(password)
  low = lower(password)
  crosscheck = check(leng, digt, upp, low)

  #activating all the functions
  leng
  digt
  upp
  low
  crosscheck

  #printing output
  if crosscheck:
    print("\nThe password you entered is good.")

  else:
    print("\nThe password you entered is bad.")

#activating main function
if __name__ == "__main__":
  main()