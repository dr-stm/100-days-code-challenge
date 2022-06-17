# -*- coding: utf-8 -*-
"""Day 16

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RAlMrzuPLB9TfMc85h8PPTQN6wxSv76S

# **CHALLENGE DAY 16**
"""

"""
CHECKING FOR A WINNING CARD
A winning Bingo card contains a line of 5 numbers that have all been called.
Players normally mark the numbers that have been called by crossing them out or marking
them with a Bingo dauber.
In our implementation we will mark that a number has been called 
by replacing it with a 0 in the Bingo card dictionary.

Write a function that takes a dictionary representing a Bingo card as its only parameter.
If the card contains a line of five zeros (vertical, horizontal or diagonal),
then your function should return True, indicating that the card has won.
Otherwise the function should return False.

Create a main program that demonstrates your function by creating several Bingo
cards, displaying them, and indicating whether or not they contain a winning line.

You should demonstrate your function with at least one card with a horizontal line,
at least one card with a vertical line, at least one card with a diagonal line, and at
least one card that has some numbers crossed out but does not contain a winning line.

Hint: Because there are no negative numbers on a Bingo card, finding a line
of 5 zeros is the same problem as finding a line of 5 entries that sum to zero.
You may find the summation problem easier to solve.
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
# the card in this argument is the  bingo card dictionary generated in the function above
def displayCard(card):
  print("  B   I   N   G   O")      #printing the column headers of the display output

  # using the for loop to print out each list per column
  for i in range(5):    # iterating through index 0-4, since the list items (values) per column header (key) created in the new dictionary are "5"
    for letter in bingo_dict.keys():     #iterating through the column headers
      print("%3d" %card[letter][i], end=" ")  #printing each iteration value with a 3whitespace prior to each number
    print("")   #printing a whitespace after each iteration round



# defining function to generate a list of 1-75 but randomly placing the numbers
def generate_draw_list():
  draw_list = random.sample(range(1, 76), 75)
  return draw_list


# defining a function that draws numbers from the game list generated in the immediate function above
# and then if that number is in the bingo card dictionary, it replaces it with 0
# the two arguments represent the bingo card dictionary generated in the first function
# and the randomly placed list generated in the immediate previous function
def draw(card, draw_list):
  number_drawn = draw_list.pop()     #drawing numbers using pop so that it doesn't draw a number twice
  for letter in card:
    for i in range(5):
      if card[letter][i] == number_drawn:
        card[letter][i] = 0       #replacing each drawn number with 0
  return number_drawn


# defining function to check for winning card - vertical, horizontal and diagonal
def check_win(card):

  #default state of win
  win = False
  
  # conditions for win to be true
  if card["B"][0] + card["I"][1] + card["N"][2] + card["G"][3] + card["O"][4] == 0:     #diagonal left to right
    win = True
  elif card["O"][0] + card["G"][1] + card["N"][2] + card["I"][3] + card["B"][4] == 0:   #diagonal right to left
    win = True

  for letter in card:     # vertical win
    if(len(set(card[letter]))==1):
      win = True

  for i in range(5):      # horizontal win
    if card["B"][i] + card["I"][i] + card["N"][i] + card["G"][i] + card["O"][i] == 0:
      win = True
      break

  return win


# defining main program to initiate the game
def main():

  print("\nLet's play bingo!\n")
  card = createCard()   #to create card

  print("Here is your card: ")

  displayCard(card)     #to display original card

  draw_list = generate_draw_list()    #generating list where numbers can be drawn from

  balls_drawn = 0             #initial state of balls drawn in the game
  list_of_drawn_balls = []    #initial state of numbers drawn in the game  

  win = check_win(card)     #initiating the default win state

  print("\nNow let's check how many draws it'll take for you to win\n")

  # inviting user to initiate the program to draw numbers until a BINGO is struck
  progress = input("Press any key to see this or type 'stop' to stop playing: ").strip().lower()

  #exit option if user wishes to abort after viewing cards
  if progress == "stop":
    print("Goodbye, and thank you")
  
  else:
    while win == False:     #until their is a BINGO, this should continue
      number_drawn = draw(card, draw_list)  #actual drawing of numbers from the random 1-75 list
      list_of_drawn_balls.append(number_drawn)    #making a list with the drawn numbers
      balls_drawn += 1      #updating number of balls drawn before a BINGO is eventually gotten
      win = check_win(card)   #rechecking for a BINGO win yet
      #if win is false, it re-enters the loop, else, it follows the instructions below

    else:  
      print("\nYay!!!, you won!\n")
  
    #other print details to make the output interactive
    print("You drew {} balls to win a BINGO".format(balls_drawn))
    print("These are the numbers you have drawn: {}\n".format(sorted(list_of_drawn_balls)))
    print("\nAnd this is what your final card looks like:\n")
    displayCard(card) #prints the final card after the drawn numbers have been replaced with 0 to create BINGO

# main program to initialise the functions
if __name__ == "__main__":
  play = input("\nWould you like to play bingo? (yes/no): ").strip().lower()
  if play == "yes":
    main()
  elif play == "no":
    print("Goodbye, and thank you")
  else:
    print("Please enter a valid answer")
