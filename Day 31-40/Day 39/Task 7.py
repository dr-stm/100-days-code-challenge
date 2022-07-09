"""
Exercise 51 included a table that shows the conversion from letter grades to grade
points at a particular academic institution. In this exercise you will compute the
grade point average of an arbitrary number of letter grades entered by the user. The
user will enter a blank line to indicate that all of the grades have been provided. For
example, if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solution to Exercise 51 helpful when completing this exercise.
Your program does not need to do any error checking. It can assume that each value
entered by the user will always be a valid letter grade or a blank line.

THE TABLE
LETTER | GRADE POINTS
A+     |  4.0
A      |  4.0
A-     |  3.7
B+     |  3.3
B      |  3.0
B-     |  2.7
C+     |  2.3
C      |  2.0
C-     |  1.7
D+     |  1.3
D      |  1.0
F      |  0
"""

#asking user to enter letter grade
user_letter_grade = input("Enter the letter grade: ").strip().upper()

#using dictionary to assign grade points to each valid letter grade
grade_dict = {"A+": 4.0, "A": 4.0, "A-": 3.7,
              "B+": 3.3, "B": 3.0, "B-": 2.7,
              "C+": 2.3, "C": 2.0, "C-": 1.7,
              "D+": 1.3, "D": 1.0, "F": 0}

#initiating a list to contain the grade points of the entered grades
grade_list = []

#condition for user to keep entering grades
while user_letter_grade != "":

  #assessing the grade point of each entered grade
  for x, y in grade_dict.items():
    if user_letter_grade == x:

      #adding the grade point to the initiated list
      grade_list.append(y)

      #asking user to enter another grade or enter blank to quit
      user_letter_grade = input("Enter the letter grade (blank to quit): ").strip().upper()

#calculating the average
avg = sum(grade_list)/len(grade_list)

#printing output
print(f"\nThe grade point average is {avg}.")