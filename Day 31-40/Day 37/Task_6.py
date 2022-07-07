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

#checking the password as a whole using the parameters from the previously checked components
def check(password):

  if len(password) >= 8:
    leng = True

  else:
    leng = False

  #checking each item in the password
  for x in password:
    #if item is a digit, return true and stop looping
    if x.isdigit():
      digt = True
      break

    else:
      digt = False

    #checking each item in the password
  for x in password:
    #if item is an uppercase, return true and stop looping
    if x.isupper():
      upp = True
      break

    else:
      upp = False

  #checking each item in the password
  for x in password:
    #if item is an uppercase, return true and stop looping
    if x.islower():
      low = True
      break

    else:
      low = False
  
  #good password can only be true when all those conditions are true
  if leng and digt and upp  and low:
    return True
  else:
    return False

#initiating main function
def main():
  #asking user to enter password
  password = input("Enter the password you want to check: ").strip()

  crosscheck = check(password)

  #activating the function
  crosscheck

  #printing output
  if crosscheck:
    print("\nThe password you entered is good.")

  else:
    print("\nThe password is bad.")

#activating main function
if __name__ == "__main__":
  main()