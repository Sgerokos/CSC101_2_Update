# The variable lbs ask's the user to input the weight in pounds
lbs = float(input("Please Enter Weight in Pounds: "))

# The variable height ask's the user to input height in inches
height = float(input("Please Enter Height in Inches: "))

# The variable kgs is set to the variable lbs multiplied by 0.45359237 to calculate the weight in kg
kgs = lbs * 0.45359237

# The variable meters is set to the variable height multiplied by 0.0254 to calculate the height in meters
meters = height * 0.0254

# The variable bmi is set to the variable kgs divided by the square of meters
bmi = kgs / meters ** 2

# Print's the variable bmi calculated
print("Your BMI is: ", round(bmi, 4))