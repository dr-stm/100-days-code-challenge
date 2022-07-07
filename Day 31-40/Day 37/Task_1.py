"""
TASK 1

The Twelve Days of Christmas is a repetitive song that describes an increasingly
long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on
the first day. A new gift is added to the collection on each additional day, and then
the complete collection is sent. The first three verses of the song are shown below.
The complete lyrics are available on the internet.

On the first day of Christmas
my true love sent to me:
A partridge in a pear tree.

On the second day of Christmas
my true love sent to me:
Two turtle doves,
And a partridge in a pear tree.

On the third day of Christmas
my true love sent to me:
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

Your task is to write a program that displays the complete lyrics for The Twelve
Days of Christmas. Write a function that takes the verse number as its only parameter
and displays the specified verse of the song. Then call that function 12 times with
integers that increase from 1 to 12.
Each item that is sent to the recipient in the song should only appear once in your
program, with the possible exception of the partridge. It may appear twice if that
helps you handle the difference between “A partridge in a pear tree” in the first verse
and “And a partridge in a pear tree” in the subsequent verses.

"""

#defining the function for returning the ordinal version of the entered numbers
def ordinal(user_num):

  #dictionary containing the numbers and their ordinal versions
  ordinal_dict = {1: "first", 2: "second", 3: "third",
                  4: "fourth", 5: "fifth", 6: "sixth",
                  7: "seventh", 8: "eighth", 9: "ninth",
                  10: "tenth", 11: "eleventh", 12: "twelfth"}

  #returning values for numbers in the dictionary
  if user_num in ordinal_dict.keys():
    return ordinal_dict[user_num]

  #else, empty string for entries outside 1-12
  else:
    return " "

#defining the function for the respective gifts
def gifts(ordinal_num):

  #dictionary for the given gifts
  gifts_dict = {"first" : "A patridge in a pear tree",
                "second" : "Two turtle doves",
                "third" : "Three french hens",
                "fourth" : "Four calling birds",
                "fifth" : "Five gold rings",
                "sixth" : "Six geese a-laying",
                "seventh" : "Seven swans a-swimming",
                "eighth" : "Eight maids are milking",
                "ninth" : "Nine ladies dancing",
                "tenth" : "Ten lords a-leaping",
                "eleventh" : "Eleven pipers piping",
                "twelfth" : "Twelve drummers drumming"}

  #returning the exact gift for a selected number
  if ordinal_num in gifts_dict.keys():
    return gifts_dict[ordinal_num]

#initiating progrma with main function
def main():

  #using try/except to prevent program from crashing if non-numeric input is entered
  try:

    #asking user to enter a number
    user_num = int(input("Enter an integer between 1 and 12: "))      

    #activating the function for the ordinal version of the number
    ordinal_num = ordinal(user_num)

    #filtering out numbers outside the valid range
    if user_num not in range(1,13):
      print(ordinal_num)

    #continuing with numbers in valid range
    else:

      #opening message for the gift on a given day
      print(f"\nON THE {ordinal_num.upper()} DAY OF CHRISTMAS, MY TRUE LOVE GAVE TO ME:\n")

      #print output for when entered number is just "one"
      if user_num == 1:
        
        #returning the ordinal version of one
        ordinal(user_num)
        #and printing its gift
        print(gifts(ordinal(user_num)))

      #print for valid entered numbers above 1 (2-12)
      else:

        #using loop to print all valid gifts in the reversed range of that number
        #for example, if 5 is entered, output will return gifts of 5, 4, 3, 2, and 1
        for num in reversed(range(1,user_num+1)):

          #returning the ordinal version of looped number
          ordinal(num)

          #print output if the looped number is 1
          #essence is to be able to add "and" to the last gift which is the gift one
          if num == 1:
            print(f"And {gifts(ordinal(num)).lower()}")

          #print output if the looped number is not 1
          else:
            print(gifts(ordinal(num)))


  #error message for non-numeric inputs
  except ValueError:
    print("Enter a valid number")

#activating main function
if __name__ == "__main__":
  main()
