# Juan Cardenas
# 9/13/2026
# Module 1.3 Assignment
# Purpose: To count down the number of bottles of beer on the wall and remind the user to buy more.

# First, I will define the function that counts down the bottles and displays the remaining number.
def countdown(bottles):
    while bottles >= 1:
        if bottles == 1:
            print("1 bottle of beer on the wall")
        else:
            print(bottles, "bottles of beer on the wall")
        bottles = bottles - 1

# Next, I will get the number of bottles from the user and validate their input using a while loop.
while True:
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))

        if bottles < 1:
            print("Error: Please enter a whole number greater than 0.")
        else:
            break

    except ValueError:
        print("Error: Please enter a whole number.")

# Then, I will run the countdown function.
countdown(bottles)

# Lastly, I will remind the user to buy more beer.
print("Time to buy more beer!")