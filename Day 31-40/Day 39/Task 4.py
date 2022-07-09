"""
A particular retailer is having a 60 percent off sale on a variety of discontinued
products. The retailer would like to help its customers determine the reduced price
of the merchandise by having a printed discount table on the shelf that shows the
original prices and the prices after the discount has been applied. Write a program that
uses a loop to generate this table, showing the original price, the discount amount,
and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
that the discount amounts and the new prices are rounded to 2 decimal places when
they are displayed.
"""

#list of the original prices
original_price = [4.95, 9.95, 14.95, 19.95, 24.95]

#printing the header
print("ORIGINAL PRICE\t\tDISCOUNT AMOUNT\t\tNEW PRICE")

#looping through each item in the list
for x in original_price:

  #generating the respective discount amount and new price
  discount_price = 0.6 * x
  new_price = 0.4 * x

  #formatting and printing output
  print(f"{x:10.2f} {discount_price:20.2f} {new_price:24.2f}", end="")
  print()