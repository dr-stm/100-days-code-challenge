# **CHALLENGE DAY 3**

# Task 1

If you have 3 straws, possibly of differing lengths, it may or may not be possible to lay them down so that they form a triangle when their ends are touching.

For example, if all of the straws have a length of 6 inches. then one can easily construct an equilateral triangle using them. However, if one straw is 6 inches long, while the other two are each only 2 inches long, then a triangle cannot be formed.

In general, if any one length is greater than or equal to the sum of the other two then the lengths cannot be used to form a triangle. Otherwise they can form a triangle.


Write a function that determines whether or not three lengths can form a triangle. The function will take 3 parameters and return a Boolean result.

In addition, write a program that reads 3 lengths from the user and demonstrates the behaviour of this function

***Method 1***
"""

try:
  side1 = int(input("Enter a length number: "))
  side2 = int(input("Enter another length number: "))
  side3 = int(input("and the last length number: "))

  if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Please enter a positive number")
  elif side1 >= side2 + side3:
    print(False)
  else:
    print(True)
except:
  print("Please enter a valid number")

"""***Method 2***"""

try:
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
        if side1 >= side2 + side3:
          print(False)
        else:
          print(True)
except:
  print("Please enter a valid number")

"""## Task 2

A particular retailer is having a 60 percent off sale on a variety of discontinued products.

The retailer would like to help its customers determine the reduced price of the merchandise by having a printed discount table on the shelf that shows the original prices and the prices after the discount has been applied.

Write a program that uses a loop to generate this table, showing the original price, the discount amount, and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95.

Ensure that the discount amounts and the new prices are rounded to 2 decimal places when they are displayed.
"""

original_price_list = [4.95, 9.95, 14.95, 19.95, 24.95]
discounted_price_list = []
new_price_list = []

for price in original_price_list:
  discounted_price = price * 0.6
  new_price = price * 0.4

  discounted_price_list.append(discounted_price)
  new_price_list.append(new_price)

discounted_price_list = [round(x,2) for x in discounted_price_list]
new_price_list = [round(x,2) for x in new_price_list]

print("Original price list: ", original_price_list)
print("\n")
print("Discounted price list: ", discounted_price_list)
print("\n")
print("New price list: ", new_price_list)
