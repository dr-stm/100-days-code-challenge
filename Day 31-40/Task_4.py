"""
TASK 4

Write a function that generates a random password. The password should have a
random length of between 7 and 10 characters.

Each character should be randomly selected from positions 33 to 126 in the ASCII table.

Your function will not take any parameters.
It will return the randomly generated password as its only result.

Display the randomly generated password in your file’s main program. Your main
program should only run when your solution has not been imported into another file.

Hint: You will probably find the chr function helpful when completing this
exercise. Detailed information about this function is available online.
"""

#importing randint from random module for generation of random integers from a given range
from random import randint

#defining the function
def password():

  #intiating the result to be generated
  result = ""

  #condition for the result to be populated
  while len(result) < randint(7,10):

    #generating a random character between 33 and 126 from the ASCII table
    char = chr(randint(33,126))

    #updating the result variable with the randomly generated char
    result += char

  #returning final result
  return result


#defining main function
def main():

  #storing the password function in a variable
  pword = password()

  #printing putput
  print(f"The random password is: {pword}")
  print(f"The length of the password is {len(pword)}")

#activating main function
if __name__ == "__main__":
  main()