# **CHALLENGE DAY 2**

From yesterday’s task, we unrealistically assumed that your salary didn’t change. But you are a Havard graduate, and clearly you are going to be worth more to your company over time! So we are going to build on your solution to yesterday’s task by factoring in a raise every six months. 

In day2.py, copy your solution to day1.py (as we are going to reuse much of that machinery). 

Modify your program to include the following 

1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage) 

2. After the 6th month, increase your salary by that percentage. Do the same after the 12th month, the 18th month, and so on. 

Write a program to calculate how many months it will take you save up enough money for a down payment. Like before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). Have the user enter the following variables: 

1. The starting annual salary (annual_salary) 
2. The percentage of salary to be saved (portion_saved) 
3. The cost of your dream home (total_cost) 
4. 4. The semi¬annual salary raise (semi_annual_raise) 

Hints To help you get started, here is a rough outline of the stages you should probably follow in writing your code: ● Retrieve user input. ● Initialize some state variables. You should decide what information you need. Be sure to be careful about values that represent annual amounts and those that represent monthly amounts. ● Be careful about when you increase your salary – this should only happen after the 6th, 12 th, 18 th month, and so on. Try different inputs and see how quickly or slowly you can save enough for a down payment. 

Please make your program print results in the format shown in the test cases below. 

Test Case 1 >>> Enter your starting annual salary: 120000 

Enter the percent of your salary to save, as a decimal: .05 

Enter the cost of your dream home: 500000 

Enter the semi¬annual raise, as a decimal: .03 

Number of months: 142 >>> 

Test Case 2 >>> 

Enter your starting annual salary: 80000 

Enter the percent of your salary to save, as a decimal: .1 

Enter the cost of your dream home: 800000 

Enter the semi¬annual raise, as a decimal: .03 

Number of months: 159 >>>
"""

annual_salary = float(input("Please enter your annual salary: ")) #asking user for annual salary

portion_saved = float(input("Please enter the portion of your salary that you want to save,\
please enter this as a decimal for example, 10% is 0.1: ")) #asking user for intended portion to be saved

total_cost = float(input("Please enter the cost of your dream house: ")) #asking user for cost of the intended house

semi_annual_raise = float(input("Please enter the percent raise of your salary every six months,\
please enter this as a decimal for example, 10% is 0.1: "))


portion_down_payment = 0.25 * total_cost #defining calculation for minimum payment for the house
r = 0.04                                 #defining the interest rate on investment
current_savings = 0                      #defining the starting amount of savings
monthly_salary = annual_salary/12        #calculating the monthly salary from the annual salary
# portion_saved = portion_saved * monthly_salary #updating the portion saved using the entered intended proportion

months = 0                                #defining the starting duration

#using conditionals to define for final duration to generate desired savings

while current_savings < portion_down_payment:
    current_savings += (annual_salary/12)*portion_saved + current_savings*(r/12)
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise


# #calling the print output (result)
print("Number of months: {}".format(months))
