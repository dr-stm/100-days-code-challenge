# -*- coding: utf-8 -*-
"""Day 8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/186VzjpNkiXafGFj-pNT4lsw15TbGDF-c

# **CHALLENGE DAY 8**

# Task 1

Positions on a chess board are identified by a letter and a number.

The letter identifies the column, while the number identifies the row, as shown below:


![image.png](data:image/png;base64,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)


Write a program that reads a position from the user.

Use an if statement to determine if the column begins with a black square or a white square.

Then use modular arithmetic to report the color of the square in that row.

For example, if the user enters a1 then your program should report that the square is black. If the user enters d5 then your program should report that the square is white.

Your program may assume that a valid position will always be entered. It does not need to perform any error checking
"""

# asking user to enter input
chess_coordinate = input("Please enter the coordinate label: ")

black_start_columns = ["a", "c", "e", "g"]

if chess_coordinate[0] in black_start_columns:
  print("The column starts with black")
else:
  print("The column starts with white")

# specifying dictionary to use for conversion of the first character in the input
column_dict = {"a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", "g":"7", "h":"8"}

# specifying the column as a number by replacing the first character of the input ...
# with the dictionary value and then converting back to integer.
# Dictionary was not specified as integer because the replace function requires the ...
# second argument to be a string
col = int(chess_coordinate[0].replace(chess_coordinate[0],\
                                   column_dict.get(chess_coordinate[0])))

# specifying the row of the cell from the entry and converting to integer for arithmetric purposes
row = int(chess_coordinate[1])

# using arithmetric to prime for the conditional statement
# this is because when you add up the row_index and the column_index of the chess board
# index will be based on natural numbers only; cells with even numbers will be coloured black
# while the odd numbered cells are coloured white
cell_position = col + row

# specifying the conditionals and output to be printed
if cell_position % 2 == 0:
  print("The coordinate is black")
else:
  print("The coordinate is white")