"""
In this exercise you will simulate 1,000 rolls of two dice.
Begin by writing a function that simulates rolling a pair of six-sided dice.
Your function will not take any parameters.
It will return the total that was rolled on two dice as its only result.

Write a main program that uses your function to simulate rolling two six-sided
dice 1,000 times. As your program runs, it should count the number of times that each
total occurs. Then it should display a table that summarizes this data. Express the
frequency for each total as a percentage of the total number of rolls.
Sample output is shown below.

TOTAL | SIMULATED PERCENT
  2   |   2.90           
  3   |   6.90           
  4   |   9.40           
  5   |   11.90          
  6   |   14.20          
  7   |   14.20          
  8   |   15.00          
  9   |   10.50          
  10  |   7.90           
  11  |   4.50           
  12  |   2.60           
"""

#importing random module
import random

#defining r=the function for the total dice generator
def dice():
  total = random.randint(1,6) + random.randint(1,6)
  return total

#defining the main function
def main():

  #initiating number of times the dice is generated as 0
  times = 0

  #initiating the count dictionary
  #containing the number of times each total number is pulled
  simulate_dict = {2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0,
                   8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}

  #condition for simulation to continue
  while times < 1000:
    times += 1
    
    #what happens while condition is true
    #rollout another dice and find its total
    rollout = dice()

    #then update the count in the dictionary
    simulate_dict.update({rollout: (simulate_dict[rollout] + 1)})

  #printing output
  print("TOTAL     SIMULATE PERCENT")
  for x, y in simulate_dict.items():
    
    #y/10 = (y/1000 * 10) - for getting the frequency of each total as a percent
    print("%2d %12.2f" % (x, (y/10)), end="")
    print()

#activating main function
main()