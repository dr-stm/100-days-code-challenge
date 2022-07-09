"""
While the popularity of cheques as a payment method has diminished in recent years,
some companies still issue them to pay employees or vendors. The amount being
paid normally appears on a cheque twice, with one occurrence written using digits,
and the other occurrence written using English words. Repeating the amount in two
different forms makes it much more difficult for an unscrupulous employee or vendor
to modify the amount on the cheque before depositing it.

In this exercise, your task is to create a function that takes an integer between 0 and
999 as its only parameter, and returns a string containing the English words for that
number. For example, if the parameter to the function is 142 then your function should
return “one hundred forty two”. Use one or more dictionaries to implement
your solution rather than large if/elif/else constructs. Include a main program that
reads an integer from the user and displays its value in English words
"""

#defining the function
def word(num):

  #defining the dictionary for the program
  word_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
              7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
              13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
              18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "fourty",
              50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


  #for one-digit and two-digit numbers with straight-forward values in the dictionary
  if num in range(0,21):

    #assessing the key-value pairs in the dictionary
    for x, y in word_dict.items():
      
      #if number is equal to key, it returns the value
      if num == x:
        return y


  #for two digit numbers that need to be derived in other ways
  elif num in range(21,100):

    #assessing the key-value pairs in the dictionary
    for x,y in word_dict.items():
      
      #checking if the number is a multiple of 10, e.g. 30, 40, 70, etc.
      #and returning its corresponding value in the dictionary
      if ((num//10) * 10) == x and (num % 10) == 0:
        return y

      #for two-digit numbers that are not multiples of 10
      #checking the highest multiple of 10 and the last digit so as to print them
      #for example; 33 = 30 + 3 (first check assesses for 30, and the second assesses for 3)
      #and returning corresponding output by concatenating
      elif ((num//10) * 10) == x and (num % 10) in range(1,10):
        return y + "-" + word_dict[num%10]


  #for three digit numbers
  elif num in range(100,1000):
    
    #for numbers in multiples of 100 e.g. 200, 500, etc.
    if num%100 == 0:

      #assessing the key-value pairs in the dictionary
      for x,y in word_dict.items():

        #assessing the first digit of the number
        #and returning output by concatenating
        if num//100 == x:
          return word_dict[num//100] + " hundred"
    
    #for numbers whose remainders are between 1 and 20
    elif num%100 in range(1,21):

      #assessing the key-value pairs in the dictionary
      for x,y in word_dict.items():
        
        #assessing the remainder in the dictionary
        #and returning the output by concatenating
        #first string in the return syntax generates the first digit number
        #last string bears the value of the remainder in the dictionary
        if num%100 == x:
          return word_dict[num//100] + " hundred and " + y

    #for remainders between 21 and 99
    elif num%100 in range(21,100):

      #assessing the key-value pairs in the dictionary
      for x,y in word_dict.items():

        #for three-digit numbers whose remainders are in multiple of 10s
        #i.e. last digit = 0; e.g. 930
        #first condition gets the key value of the remainder in the map
        #second condition confirms that the last digit is 0
        #output returns a concatenation of the first digit and the value of the remainder
        if (((num%100)//10) * 10) == x and ((num%100) % 10) == 0:
          return word_dict[num//100] + " hundred and " + y

        #for three-digit numbers whose remainders are not in multiple of 10s
        #i.e. last digit is not equal to 0; e.g. 937
        #first condition gets the key value of the remainder in the map
        #second condition confirms that the last digit is not 0
        #output returns a concatenation of the first digit and the value of the remainder
        #including the last digit
        elif (((num%100)//10) * 10) == x and ((num%100) % 10) in range(1,10):
          return word_dict[num//100] + " hundred and " + y + "-" + word_dict[(num%100)%10]

  #entries less than 0 or above 999
  else:
    return "Your entry is put of range."

#defining main function
def main():

  #using try/except to prevent program from crashing if a non-integer is entered
  try:

    #calling user to enter number
    num = int(input("Enter an integer between 0 and 999: "))
    
    #activating the function and printing the output
    print(word(num))

  #for non-integer inputs
  except:
    print("Enter a valid number")

#activating the main function
main()