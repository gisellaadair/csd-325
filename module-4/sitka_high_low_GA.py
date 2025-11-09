import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'sitka_weather_2018_simple.csv'

# Read the CSV file
dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {row}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot high temperatures
def plot_highs():
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.set_title("Daily High Temperatures - 2018", fontsize=20)
    ax.set_xlabel('', fontsize=12)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=14)
    plt.show()

# Plot low temperatures
def plot_lows():
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    ax.set_title("Daily Low Temperatures - 2018", fontsize=20)
    ax.set_xlabel('', fontsize=12)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=14)
    plt.show()

# Main menu
def menu():
    # Instructions shown when program starts
    print("\nWelcome to the Sitka Weather Viewer!")
    print("You can choose to see the high or low temperatures recorded in Sitka, Alaska (2018).")
    print("Instructions:")
    print(" - Type '1' to view HIGH temperatures (shown in red).")
    print(" - Type '2' to view LOW temperatures (shown in blue).")
    print(" - Type '3' to EXIT the program.\n")

    while True:
        print("--- Menu ---")
        print("1. Highs")
        print("2. Lows")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            plot_highs()
        elif choice == '2':
            plot_lows()
        elif choice == '3':
            print("\nThank you for exploring Sitka weather! Have a great day, Goodbye! ")
            sys.exit()
        else:
            print("Invalid selection. Please try again.\n")

# Run the program
if __name__ == "__main__":
    menu()