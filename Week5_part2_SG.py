# Imports the module sys into python
import sys

def calculate_monthly_cost():
    # Ask the user to input the wattage of the device
    watts = float(input("Please enter the wattage of your device: "))
    
    # Check if the input is valid, else exit the program
    if watts <= 0:
        print("Sorry, the input must be above 0.\n"
              "Please try again.\n" "Now exiting!!!")
        sys.exit()
    
    # Ask the user to input the number of hours the device runs per day
    hours = float(input("How many hours in a day does it run? "))
    
    # Check if the input is valid, else exit the program
    if hours <= 0:
        print("Sorry, the input must be above 0.\n"
              "Please try again.\n" "Now exiting!!!")
        sys.exit()

    # Ask the user to input the electric rate in cents per kilowatt per hour
    cents_kwh = float(input("How much is your electric rate per"
                            " kilowatt an hour in cents? "))
    
    # Check if the input is valid, else exit the program
    if cents_kwh <= 0:
        print("Sorry, the input must be above 0.\n"
              "Please try again.\n" "Now exiting!!!")
        sys.exit()

    # Calculate the monthly rate by multiplying watts by the number of hours
    # divided by 1000, multiplied by cents_kwh, and multiplied by 30
    monthly = (((watts * hours) / 1000) * cents_kwh * 30)
    
    # Print the monthly rate, rounding it to two decimal places
    print("You will pay monthly $", round(monthly, 2),
          "more on your electric bill")

# Call the function
calculate_monthly_cost()