# Write a program that determines the name of a shape from its number of sides. 

# Read the number of sides from the user and then report the appropriate name as part of a meaningful message.
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides. 

# If a number of sides outside of this range is entered
# then your program should display an appropriate error message.


def shape(x):
    if x == 3:
        return "triangle"
    elif x == 4:
        return "quadrangle"
    elif x == 5:
        return "pentagon"
    elif x == 6:
        return "hexagon"
    elif x == 7:
        return "heptagon"
    elif x == 8:
        return "octagon"
    elif x == 9:
        return "nonagon"
    elif x == 10:
        return "decagon"
    else:
        return "not recorded because this number is outside the stipulated range"

x = int(input("please enter the number of sides of the shape to determine its name (hint: the number should be between 3 and 10):"))

print("The name of the shape is {}".format(shape(x)))