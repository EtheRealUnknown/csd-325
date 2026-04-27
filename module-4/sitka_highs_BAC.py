import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Load data once
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        low = int(row[6])

        highs.append(high)
        lows.append(low)

# Menu loop
while True:
    print("\n--- Sitka Weather Menu ---")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        # Plot highs
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == '2':
        # Plot lows
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == '3':
        print("Exiting program. Goodbye!")
        sys.exit()

    else:
        print("Invalid choice. Please select 1, 2, or 3.")