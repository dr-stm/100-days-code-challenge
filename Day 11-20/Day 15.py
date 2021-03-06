# -*- coding: utf-8 -*-
"""Day 15

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mrMvWjRpiqavEog5s48hfas09a6pBR0Z

# **CHALLENGE DAY 15**
"""

"""
TASK 1

In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places
"""

# using try/except to prevent the program from crashing if a non-nuerical input is entered
try:
  # calling user to enter inputs
  small_containers = int(input("How many of your containers hold one litre or less: "))
  big_containers = int(input("How many of your containers hold more than one litre: "))

  # generating formula for calculating the refund value
  refund = (0.10 * small_containers) + (0.25 * big_containers)

  # printing output
  print("The refund you get for these containers is ${:.2f}.".format(refund))
except:
  print("Please enter a numerical value")

"""
TASK 2

A Bingo card consists of 5 columns of 5 numbers.
The columns are labeled with the letters B, I, N, G and O.
There are 15 numbers that can appear under each letter.

In particular, the numbers that can appear under the B range from 1 to 15,
the numbers that can appear under the I range from 16 to 30,
the numbers that can appear under the N range from 31 to 45, and so on.

Write a function that creates a random Bingo card and stores it in a dictionary.
The keys will be the letters B, I, N, G and O.
The values will be the lists of five numbers that appear under each letter.

Write a second function that displays the Bingo card with the columns labeled appropriately.
Use these functions to write a program that displays a random Bingo card.
Ensure that the main program only runs when the file containing your solution
has not been imported into another program.

You may be aware that Bingo cards often have a ???free??? space in the middle of
the card. We won???t consider the free space in this exercise.
"""

# importing the "random" module for generating random numbers from the specified range per column
import random

# creating the bingo dictionary with the possible values per column
bingo_dict = {"B": list(range(1,16)),
              "I": list(range(15,31)),
              "N": list(range(30,46)),
              "G": list(range(45,61)),
              "O": list(range(60,71))
              }

#defining function to create the bingo dictionary
def createCard():
  card = {}

  # iterating through the keys of the dictionary which are the bingo columns
  for letter in bingo_dict.keys():
    card[letter] = []     # initiating the list for each column

    while len(card[letter]) != 5:       # giving condition for the iteration task to continue
      num = random.choice(bingo_dict[letter])   # picking random item from the list values of each key
      if num not in card[letter]:       # making sure each number does not appear twice
        card[letter].append(num)        # attaching the randomly selected item to the initiated list

  return card

# defining function for displaying the created card
def displayCard(card):
  print("  B   I   N   G   O")      #printing the column headers of the display output


  # using the for loop to print out each list per column
  for i in range(5):    #iterating through the column headers
    for letter in bingo_dict.keys():     #iterating through index 0-4, since the list items (values) per column header (key) created in the new dictionary are "5"
      print("%3d" %card[letter][i], end=" ")  #printing each iteration value with a 3whitespace prior to each number
    print("")   #printing a whitespace after each iteration round

# defining main program 
def main():
  displayCard(createCard())
if __name__ == "__main__":
  main()
