"""
TASK 2

In a Canadian postal code, the first, third and fifth characters are letters while the
second, fourth and sixth characters are numbers. The province can be determined
from the first character of a postal code, as shown in the following table. No valid
postal codes currently begin with D, F, I, O, Q, U, W, or Z.

PROVINCE                  |   FIRST CHARACTER(S)
Newfoundland              |   A
Nova Scotia               |   B
Prince Edward Island      |   C
New Brunswick             |   E
Quebec                    |   G, H and J
Ontario                   |   K, L, M, N and P
Manitoba                  |   R
Saskatchewan              |   S
Alberta                   |   T
British Columbia          |   V
Nunavut                   |   X
Northwest Territories     |   X
Yukon                     |   Y

The second character in a postal code identifies whether the address is rural or
urban. If that character is a 0 then the address is rural. Otherwise it is urban.

Create a program that reads a postal code from the user and displays the province
associated with it, along with whether the address is urban or rural. For example,
if the user enters T2N 1N4 then your program should indicate that the postal code
is for an urban address in Alberta. If the user enters X0A 1B2 then your program
should indicate that the postal code is for a rural address in Nunavut or Northwest
Territories. Use a dictionary to map from the first character of the postal code to the
province name. Display a meaningful error message if the postal code begins with
an invalid character.
"""

#asking user to enter a postal code
postal_code = input("Enter a postal code: ").strip().upper()

#putting the invalid first characters in a list
invalid_first_char = ["D", "F", "I", "O", "Q", "U", "W", "Z"]

#setting a dictionary for the provinces and their respective first characters
postal_code_dict = {"Newfoundland": "A", "Nova Scotia": "B", "Prince Edward Island": "C",
                    "New Brunswick": "E", "Quebec": ["G", "H", "J"],
                    "Ontario": ["K", "L", "M", "N" "P"], "Manitoba": "R", "Saskatchewan": "S",
                    "Alberta": "T", "British Columbia": "V", "Nunavut": "X",
                    "Northwest Territories": "X", "Yukon": "Y"}

#filtering out invalid entries
if postal_code[0].isalpha() and postal_code[1].isdigit():

  #filtering out valid entries that started with invalid first characters
  if postal_code[0] in invalid_first_char:
    print("No valid postal code starts with this letter, enter a valid postal code")
  
  #determining respective provinces and areas for remaining entries
  else:
    #first print output
    print("\nTHE PROVINCE AND AREA OF THE CODE YOU ENTERED IS: ")

    #initiating a list to house the assessed provinces
    province_list = []

    #assessing the provinces and appending to the list
    for x, y in postal_code_dict.items():
      if postal_code[0] in y:
        province_list.append(x)

    #assessing the area of the postal code
    for z in range(0,10):
      if postal_code[1] == 0:
        zone = "Rural"
      else:
        zone = "Urban"
    
    #printing outputs
    
    #printing output for potal codes with first character corresponding to only one province
    if len(province_list) == 1:
      print(province_list[0])

      #printing out the area
      print(zone)

    #for first character corresponding to more than one province
    else:
      for x in province_list:

        #output for items before the last item in the province list
        if x != province_list[-1]:
          print(x, end="")
          print(" or ", end = "")

        #output for the last item
        else:
          print(x)

      #printing out the area
      print(zone)

#print output for non-valid entries
else:
  print("Enter a valid postal code")