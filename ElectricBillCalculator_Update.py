# Ask the user for the wattage of their device
watts = float(input("Please Enter the Wattage of Your Device: "))

# Ask the user for the number of hours their device will be on in a day
hours = float(input("How Many Hour's in a Day Does it Run? "))

# Ask the user for the electric rate in cents per kilowatt per hour
cents_kwh = float(input("How Much is Your Electric Rate Per Kilowatt an Hour in Cents? "))

# Calculate the monthly rate in dollars
monthly = watts * hours / 1000 * cents_kwh * 30

# Print the monthly rate rounded to two decimal places
print("You Will Pay Monthly $", round(monthly, 2), "More on Your Electric Bill")