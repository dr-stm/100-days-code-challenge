"""
TASK 1

In the game of Scrabble™, each letter has points associated with it. The total score
of a word is the sum of the scores of its letters. More common letters are worth fewer
points while less common letters are worth more points. The points associated with
each letter are shown below:

One point     | A, E, I, L, N, O, R, S, T and U
Two points    | D and G
Three points  | B, C, M and P
Four points   | F, H, V, W and Y
Five points   | K
Eight points  | J and X
Ten points    | Q and Z

Write a program that computes and displays the Scrabble™ score for a word.
Create a dictionary that maps from letters to point values. Then use the dictionary to
compute the score.
A Scrabble™ board includes some squares that multiply the value of a letter
or the value of an entire word. We will ignore these squares in this exercise
"""

#asking user to enter input
word = input("Enter a word: ").strip().upper()

#defining the function
def score(word):

  #saving the points in a dictionary
  scrabble_dict = {
                  1: ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
                  2: ["D", "G"],
                  3: ["B", "C", "M", "P"],
                  4: ["F", "H", "V", "W", "Y"],
                  5: "K",
                  8: ["J", "X"],
                  10: ["Q", "Z"]
                  }

  #initiating the score
  score = 0

  #looping through each item of the word
  for x in word:
    #searching for that item in the dictionary and assessing its point
    for y, z in scrabble_dict.items():
      if x in z:
        #updating the score with the assessed point value of the item
        score += y

  #returning the final score
  return score

#printing output
print("\nThe socre of the word is:")
print(score(word))
