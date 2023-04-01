# Imports the module sys into python
import sys

# Prompt the user to input the wattage of the device in watts
watts = float(input("Enter the wattage of your device (in watts): "))

# If the input is less than or equal to zero, print an error message and exit the program
if watts <= 0:
    print("Sorry, the input must be greater than zero. Please try again.")
    sys.exit()

# Prompt the user to input the number of hours per day the device runs
hours = float(input("Enter the number of hours per day your device runs: "))

# If the input is less than or equal to zero, print an error message and exit the program
if hours <= 0:
    print("Sorry, the input must be greater than zero. Please try again.")
    sys.exit()

# Prompt the user to input the cost of electricity per kilowatt-hour (in cents)
cents_kwh = float(input("Enter the cost of electricity per kilowatt-hour (in cents): "))

# If the input is less than or equal to zero, print an error message and exit the program
if cents_kwh <= 0:
    print("Sorry, the input must be greater than zero. Please try again.")
    sys.exit()

# Calculate the monthly cost of running the device and round to two decimal places
monthly_cost = round(((watts * hours) / 1000) * cents_kwh * 30, 2)

# Print the monthly cost of running the device
print("Your device will cost $", monthly_cost, "per month to run.")