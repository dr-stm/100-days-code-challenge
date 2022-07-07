"""
TASK 5

In a particular jurisdiction, older license plates consist of three letters followed by
three numbers. When all of the license plates following that pattern had been used,
the format was changed to four numbers followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate.
"""

#importing relevant modules for the task
from random import randint
import string
from random import choice

#defining first function for the style of the license
def license_style():
  #randomly generating the length of the characters of each style
  style_length = randint(6,7)

  #assigning style to both lengths
  if style_length == 6:
    return "old"

  else:
    return "new"


#defining  second function for generating the license based on the license style
def license_gen(style):

  #initiating the final license
  license = ""

  #generating the lists from where to select the letters and numbers
  alph = list(string.ascii_uppercase)
  num = list(range(0,10))

  #generating for old license style
  if style == "old":
    
    #adding the fist 3 characters which are letters
    while len(license) < 3:
      license_alph = choice(alph)
      license += license_alph

    #and the last 3 characters which are numbers
    while len(license) < 6:
      license_num = str(choice(num))
      license += license_num

  #and for new license style
  else:

    #adding the first four characters which are numbers
    while len(license) < 4:
      license_num = str(choice(num))
      license += license_num

    #and the last 3 characters which are letters
    while len(license) < 7:
      license_alph = choice(alph)
      license += license_alph

  #returning the finally generated license
  return license

#initiating the main function
def main():
  #storing the first function in a variable
  style = license_style()
  
  #activating the first function, to generate the license style
  style

  #randomly generating the license from the style
  gen_license = license_gen(style)

  #printing output
  print(f"The license plate is '{gen_license}' and the style is {style}.")

#activating the main function
main()
