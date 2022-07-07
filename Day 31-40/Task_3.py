"""
TASK 3

Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. In this exercise, you will write a function that capitalizes
the appropriate characters in a string.

A lowercase “i” should be replaced with an uppercase “I” if it is both preceded and followed by a space.
The first character in the string should also be capitalized,
as well as the first non-space character after a “.”, “!” or “?”.

For example, if the function is provided with the string:

“what time do i have to be there? what’s the address?”

then it should return the string

“What time do I have to be there? What’s the address?”.

Include a main program that reads a string from the user,
capitalizes it using your function, and displays the result.
"""

#defining the function for capitalization
def capitalize(user_text):
  
  #initiating the variable for the final result
  result = ""

  #replacing the first character with its upper version
  user_text[0] = user_text[0].upper()

  #Capitalizing stand-alone "i" by iterating through the index of the remaining characters excluding the last
  for x in range(1,len(user_text)):
    
    #conditions for capitalizing the letter "i"
    if user_text[x] == "i" and (user_text[x - 1] == " ") and (user_text[x + 1] == " "):
      
      #replacing the item in the list with a capitalized version
      user_text[x] = user_text[x].upper()

  #capitalizing non-space characters after punctuations (".", "?", "!")
  for item in user_text:

    #conditions for capitalizing them
    if (item == "." or item == "!" or item == "?") and (user_text.index(item) != -1):

      #replacing the item in the list with a capitalized version
      user_text[user_text.index(item) +2] = user_text[user_text.index(item) +2].upper()

  #joining back the final list items to the initialised string
  for ele in user_text:
    result += ele

  #returning the final result
  return result


#defining main function
def main():

  #calling user to enter a text
  #and storing the text with stripped blank ends in a list variable
  user_text = list(input("Enter a text: ").strip())

  #printing output
  print()
  print("\n", capitalize(user_text))

#activating the main function
main()