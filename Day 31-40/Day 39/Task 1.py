"""
TASK 1

Morse code is an encoding scheme that uses dashes and dots to represent numbers
and letters. In this exercise, you will write a program that uses a dictionary to store
the mapping from letters and numbers to Morse code. Use a period to represent a dot,
and a hyphen to represent a dash. The mapping from letters and numbers to dashes
and dots is shown in Table 6.1.
Your program should read a message from the user. Then it should translate each
letter and number in the message to Morse code, leaving a space between each
sequence of dashes and dots. Your program should ignore any characters that are not
letters or numbers. The Morse code for Hello, World! is shown below:
.... . .-.. .-.. --- .-- --- .-. .-.. -..
(see folder for Table)

Morse code was originally developed in the nineteenth century for use over
telegraph wires. It is still used today, over 160 years after it was first created.
"""

#defining the morse dictionary
morse_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
              "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
              "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
              "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
              "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."}

# asking user to enter input
word = input("Enter a text: ").upper()

#looping through each item of the entered input
for item in word:
  
  #looping that item through the morse dictionary
  for x, y in morse_dict.items():
    
    #condition for printing the dictionary value
    if item == x:
      
      #print output
      print(y + " ", end="")