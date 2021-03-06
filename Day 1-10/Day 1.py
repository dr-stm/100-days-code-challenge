# **CHALENGE DAY 1**

# 1

Create a program to check whether a number is positive or negative or 0.

If the number is positive, print "The number is positive"
If the number is negative, print "The number is negative"
(and) If the number is 0, print "The number is 0"
"""

#using try to prevent the program to crash
try:
    num = int(input("Please enter any number: ")) #calling the user to enter any number
    
    #defining conditional actions for the program
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is 0")

#defining program output if the user inputs a wrong entry
except:
    print("This is not a number, please a valid number")

"""# 2

You have graduated from Havard and now have a great job! You move to New York and decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area, you realize you are going to have to save for several years before you can afford to make the down payment on a house. In Part A, we are going to determine how long it will take you to save enough money to make the down payment given the following assumptions:

1. Call the cost of your dream home total_cost.
2. Call the portion of the cost needed for a down payment portion_down_payment. For simplicity, assume that portion_down_payment = 0.25 (25%).
3. Call the amount that you have saved thus far current_savings. You start with a current savings of $0. 
4. Assume that you invest your current savings wisely, with an annual return of r (in other words, at the end of each month, you receive an additional current_savings*r/12 funds to put into your savings – the 12 is because r is an annual rate). Assume that your investments earn a return of r = 0.04 (4%).
5. Assume your annual salary is annual_salary.
6. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that portion_saved. This variable should be in decimal form (i.e. 0.1 for 10%). 
7. At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary (annual salary / 12).

Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats. 

Your program should ask the user to enter the following variables:
1. The starting annual salary (annual_salary)
2. The portion of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)

Hint:

Try different inputs and see how long it takes to save for a down payment. 

Please make your program print results in the format shown in the test cases below. 

Test Case 1 
>>>
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183 


>>>

Test Case 2 
>>>
Enter your annual salary: 80000 
Enter the percent of your salary to save, as a decimal: .15
Enter the cost of your dream home: 500000
Number of months: 105
>>>
"""

annual_salary = float(input("Please enter your annual salary: ")) #asking user for annual salary

portion_saved = float(input("Please enter the portion of your salary that you want to save,\
please enter this as a decimal for example, 10% is 0.1: ")) #asking user for intended portion to be saved

total_cost = float(input("Please enter the cost of your dream house: ")) #asking user for cost of the intended house


portion_down_payment = 0.25 * total_cost #defining calculation for minimum payment for the house
r = 0.04                                 #defining the interest rate on investment
current_savings = 0                      #defining the starting amount of savings
monthly_salary = annual_salary/12        #calculating the monthly salary from the annual salary
portion_saved = portion_saved * monthly_salary #updating the portion saved using the entered intended proportion

months = 0                                #defining the starting duration

#using conditionals to define for final duration to generate desired savings
while current_savings <= portion_down_payment:
    months += 1
    monthly_investment_return = current_savings * r / 12
    current_savings += monthly_investment_return + portion_saved

#calling the print output (result)
print("Number of months: {}".format(months))
