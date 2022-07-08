"""
TASK 2

Write a function named reverseLookup that finds all of the keys in a dictionary
that map to a specific value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from
the dictionary that map to the provided value.
Include a main program that demonstrates the reverseLookup function as part
of your solution to this exercise. Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple
keys, a single key, and no keys. Ensure that your main program only runs when
the file containing your solution to this exercise has not been imported into another
program.
"""

#defining the function
def reverseLookup(dictionary, value):
  
  #initiating the list to house the assessed keys
  keys_list = []

  #looking throught the keys and values of the dictionary
  #once the specified value is spotted in the dictionary
  #its key is added to the keys list
  for x,y in dictionary.items():
    if y == value:
      keys_list.append(x)

  #returning the keys list
  return keys_list

#defining the main function for the program
def main():

  #providing the test dictionary
  test_dict = {"Obi": "male",
                "Ada": "female",
                "John": "male",
                "Cynthia": "female",
                "Ifeanyi": "female",
                "Hillary": "male",
                "Uche": "female"}

  #saving the values to be tested inside variables
  females = reverseLookup(test_dict, "female")
  males = reverseLookup(test_dict, "male")
  transgender = reverseLookup(test_dict, "transgender")

  #printing output
  print("LET'S TEST THE REVERSE LOOKUP FUNCTION\n")
  print(f"\nThe females in the test dictionary are: {females}")
  print("Expected: ['Ada', 'Cynthia', 'Ifeanyi', 'Uche']")
  print(f"\nThe males in the test dictionary are: {males}")
  print("Expected: ['Obi', 'John', 'Hillary']")
  print(f"\nThose who identify as transgenders in the test dictionary are: {transgender}")
  print("Expected: []")

#activating the main function
if __name__ == "__main__":
  main()
