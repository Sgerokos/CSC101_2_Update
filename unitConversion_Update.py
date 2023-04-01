# The variable feet asks the user to input the number of feet
feet = float(input("Please Enter the Value for Feet: "))

# The variable meters multiplies the number of feet by 0.305 to calculate meters
meters = feet * 0.305

# The variable inch multiplies feet by 12 to calculate inches
inch = feet * 12

# The variable centimetre multiplies inch by 0.3937 to calculate centimetres
centimetre = inch * 0.3937

# Print the output that shows the conversion of feet to meters, inches, and centimetres
print(feet, "Feet Are", meters, "In Meters", inch, "In Inches", centimetre, "In Centimetres")