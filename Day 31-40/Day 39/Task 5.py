"""
Write a program that displays a temperature conversion table for degrees Celsius and
degrees Fahrenheit. The table should include rows for all temperatures between 0
and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
headings on your columns. The formula for converting between degrees Celsius and
degrees Fahrenheit can be found on the internet.
"""

#formula for converting from degrees Celsius to degrees Fahrenheit is: °F = (°C × 9/5) + 32

#printing the header
print("CELSIUS(°C)\tFAHRENHEIT(°F)")

#looping through every tenth between 0 and 100
for celsius in range(0,101,10):

  #generating the Fahrenheit equivalent
  fahrenheit = (celsius * (9/5)) + 32
  
  #formatting and printing output
  print(f"{celsius:6.2f} {fahrenheit:18.2f}", end="")
  print()