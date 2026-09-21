# Juan Cardenas
# 9/20/2026
# Module 2.2 Assignment
# Purpose: To capture debugging activity of a program that contains at least one function.

# First, I will create a function that converts miles to kilometers.
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

# Next, I will ask the user to input the number of miles driven while using Try/Except blocks for potential incorrect input by the user.
while True:
    try:
        miles = float(input("Enter the number of miles driven: "))
        # the if/else statements will account for the user inputing a negative number.
        if miles < 0:
            print("Miles cannot be negative. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please try again.")

# This is where the program will call to the function.
kilometers = miles_to_kilometers(miles)

# Once the function runs and determines the value of kilometers, the program will display the total miles and the kilometers.
print('Here is the total miles driven in miles and kilometers:')
print(f"Miles: {miles}")
print(f"Kilometers: {kilometers:.2f}")