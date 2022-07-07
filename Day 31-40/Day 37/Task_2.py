"""
TASK 2

Write a function that takes a string of characters as its first parameter, and the width of
the terminal in characters as its second parameter. Your function should return a new
string that consists of the original string and the correct number of leading spaces
so that the original string will appear centered within the provided width when it is
printed. Do not add any characters to the end of the string. Include a main program
that demonstrates your function.
"""

#specifying a given width
width = 50

#defining the function that will return a centered version of the string
def center(user_string, width):

  #for texts greater than the given width
  if width <len(user_string):
    return user_string

  else:

    #deducting the required spaces to come before the text
    spaces = (width - len(user_string)) // 2

    #adding those number of spaces before the text
    result = (" " * spaces) + user_string

    #returning result
    return result

def main():

  #sample print outs
  print(center("I am a woman", width))
  print(center("By", width))
  print(center("DR. STM", width))
  print(center("This is to know how much the centered text will accommodate", width))

main()
