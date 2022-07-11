"""
Write a python program to read three numbers (a,b,c) and check how many numbers between "a" and "b" are divisible by "c"
"""

#using try/except to prevent program from crashing if non-numeric input is entered
try:

  #asking user to enter the numbers
  a = int(input("Enter any number: "))
  b = int(input("Enter another number: "))
  c = int(input("Enter your last number: "))

  #condition if the second number is greater
  if b > a:
    for num in range(a, b + 1):
      if num % c == 0:
        print(num)
  
  #condition if the first number is greater
  elif a > b:
    for num in range(b, a + 1):
      if num % c == 0:
        print(num)
  
  #both numbers are equal then, no range can be created from the two
  else:
    print("please input different numbers in your first two entries")

except ValueError:
  print("Please enter a valid numeric input")