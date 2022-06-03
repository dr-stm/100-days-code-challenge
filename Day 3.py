# **CHALLENGE DAY 3**

# Task 1

If you have 3 straws, possibly of differing lengths, it may or may not be possible to lay them down so that they form a triangle when their ends are touching.

For example, if all of the straws have a length of 6 inches. then one can easily construct an equilateral triangle using them. However, if one straw is 6 inches long, while the other two are each only 2 inches long, then a triangle cannot be formed.

In general, if any one length is greater than or equal to the sum of the other two then the lengths cannot be used to form a triangle. Otherwise they can form a triangle.


Write a function that determines whether or not three lengths can form a triangle. The function will take 3 parameters and return a Boolean result.

In addition, write a program that reads 3 lengths from the user and demonstrates the behaviour of this function

***Method 1***
"""

try:  #using try to prevent the program from crashing

#calling user to enter three numbers respectively 
  side1 = int(input("Enter a length number: "))
  side2 = int(input("Enter another length number: "))
  side3 = int(input("and the last length number: "))

  if side1 <= 0 or side2 <= 0 or side3 <= 0:  #filtering out negative numbers and 0
    print("Please enter a positive number")
  elif side1 >= side2 + side3: #specifying conditions that disqualifies an actual triangle formation
    print(False)
  else:
    print(True)
except:
  print("Please enter a valid number") #output to print if a non-number is entered

"""***Method 2***"""

try:  #using try to prevent the program from crashing

#calling user to enter three numbers respectively
#and filtering out non-positive numbers per entry
  side1 = int(input("Enter a length number: "))
  if side1 <= 0:
    print("Please enter a positive number")
  else:
    side2 = int(input("Enter another length number: "))
    if side2 <= 0:
      print("Please enter a positive number")
    else:
      side3 = int(input("and the last length number: "))
      if side3 <= 0:
        print("Please enter a positive number")
      else:
        if side1 >= side2 + side3:  #initiating triangle conditions after confirming that all entries are positive numbers
          print(False)
        else:
          print(True)
except:
  print("Please enter a valid number")  #output to print if a non-number is entered


"""## Task 2

A particular retailer is having a 60 percent off sale on a variety of discontinued products.

The retailer would like to help its customers determine the reduced price of the merchandise by having a printed discount table on the shelf that shows the original prices and the prices after the discount has been applied.

Write a program that uses a loop to generate this table, showing the original price, the discount amount, and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95.

Ensure that the discount amounts and the new prices are rounded to 2 decimal places when they are displayed.
"""

original_price_list = [4.95, 9.95, 14.95, 19.95, 24.95] #the list of the original prices
discounted_price_list = []  #initiating the list of the discounted price per item in original list
new_price_list = []  #initiating the list of the final price after removing discounted prices per item

#using for loop to iterate and apply discounts on each original price list item
for price in original_price_list:
  discounted_price = price * 0.6
  new_price = price * 0.4

#using append to add each price to its respective list
  discounted_price_list.append(discounted_price)
  new_price_list.append(new_price)

#rounding off items in the new lists to two decimal points
discounted_price_list = [round(x,2) for x in discounted_price_list]
new_price_list = [round(x,2) for x in new_price_list]

#printing outputs with space in between them
print("Original price list: ", original_price_list)
print("\n")
print("Discounted price list: ", discounted_price_list)
print("\n")
print("New price list: ", new_price_list)
