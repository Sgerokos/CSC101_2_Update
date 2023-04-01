# The variable feet asks the user to input the number of feet
feet = float(input("Please Enter the Value for Feet: "))

# The variable meters multiplies the number of feet by 0.305
meters = feet * 0.305

# Prints the output in feet and shows its conversion in meters as well
print(feet, "Feet Are", meters, "In Meters")

# The variable lbs asks the user to input the weight in pounds
lbs = float(input("Please Enter Weight to be Converted in Pounds: "))

# The variable kgs is set to the variable lbs multiplied by 0.454 to calculate the output
kgs = lbs * 0.454

# Prints the output in kilograms and rounds it to the 3rd decimal number
print("The Weight in Kilograms is", round(kgs, 3), "kgs")