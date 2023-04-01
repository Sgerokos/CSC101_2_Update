# Prompt the user to enter the wattage of their device
watts = float(input("Please enter the wattage of your device: "))

# Confirm with the user if the input is correct
yes_no = input("The device's wattage is {:.2f} watts. Is this correct? Type y for Yes or n for No: ".format(watts))

if yes_no.lower() == "n":
    # Prompt the user to re-enter the wattage of their device
    watts = float(input("Please re-enter the wattage of your device: "))

# Prompt the user to enter the number of hours the device will be on in a day
hours = float(input("How many hours per day will the device be on? "))

# Confirm with the user if the input is correct
yes_no = input("The device will be running for {:.2f} hours per day. Is this correct? Type y for Yes or n for No: ".format(hours))

if yes_no.lower() == "n":
    # Prompt the user to re-enter the number of hours the device will be on in a day
    hours = float(input("Please re-enter the number of hours per day the device will be on: "))

# Prompt the user to enter the electric rate in cents per kilowatt hour
cents_kwh = float(input("What is your electric rate per kilowatt hour in cents? "))

# Confirm with the user if the input is correct
yes_no = input("Your electric rate is {:.2f} cents per kilowatt hour. Is this correct? Type y for Yes or n for No: ".format(cents_kwh))

if yes_no.lower() == "n":
    # Prompt the user to re-enter the electric rate in cents per kilowatt hour
    cents_kwh = float(input("Please re-enter your electric rate per kilowatt hour in cents: "))

# Calculate the monthly cost
monthly_cost = watts * hours * cents_kwh * 30 / 1000

# Display the monthly cost rounded to 2 decimal places
print("Your device will cost ${:.2f} more on your electric bill each month.".format(round(monthly_cost, 2)))