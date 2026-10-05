# Juan Cardenas
# 10/4/2026
# Module 4.2 Assignment
# Purpose: To practice brownfield development on an existing program that uses data from a CSV file and displays high temperatures in Sitka, Alaska.

# The following changes were made to the original program:
# 1. Added the menu option for Highs, Lows, or Exit, and instructions on how to use it.
# 2. Added Low temperature data and a blue graph for Lows.
# 3. Added a loop so the menu repeats until the user selects Exit.
# 4. Added an exit message.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Display instructions and menu.
print("\nSitka Weather Temperature Viewer")
print("Select an option to view the weather data.")
print("Enter 'Highs' to view high temperatures.")
print("Enter 'Lows' to view low temperatures.")
print("Enter 'Exit' to quit the program.")

# Ask the user to enter their input for menu selection, using a while loop and if/elif menu.
while True:
    choice = input("\nEnter your choice: ").strip().lower()

    if choice == 'highs':
        # Plot and display the high temperatures in red.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == 'lows':
        # Plot and display the low temperatures in blue.
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == 'exit':
        # Display exit message.
        print("\nThank you for using the Sitka Weather Temperature Viewer.")
        break

    else:
        print("Invalid choice. Please enter Highs, Lows, or Exit.")
