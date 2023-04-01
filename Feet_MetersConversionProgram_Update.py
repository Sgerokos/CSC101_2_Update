# Ask the user to input the number of feet
feet = float(input("Please enter the value for feet: "))

# Convert the number of feet to meters using the conversion factor
meters = feet * 0.305

# Print the output, rounding the meter value to two decimal places
print("{:.2f} feet are {:.2f} meters".format(feet, meters))