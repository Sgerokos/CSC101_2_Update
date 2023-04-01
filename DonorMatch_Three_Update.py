import sys

# Prints a hello and welcomes the user to donor match
print("Hello")
print("Welcome to the Donor Match Program")

# Requests the user to input the type of blood they have 
# The input can be A+. A-, B+, B-, O+, O-, AB+, AB-
blood_Type = input("\nPlease Input The Donor's Blood Type. You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

valid_blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

if blood_Type not in valid_blood_types:
    print("Incorrect input. Enter one of A+, A-, B+, B-, O+, O-, AB+, AB-")
    sys.exit()

# This line will ask for the recipient's blood type
recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type. You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

if recipient_Blood_type not in valid_blood_types:
    print("Incorrect input. Enter one of A+, A-, B+, B-, O+, O-, AB+, AB-")
    sys.exit()

# Compatibility rules stored in a dictionary
compatibility_rules = {
    "A+": ["A+", "AB+"],
    "A-": ["A+", "A-", "AB+", "AB-"],
    "B+": ["B+", "AB+"],
    "B-": ["B+", "B-", "AB+", "AB-"],
    "O+": ["A+", "B+", "O+", "AB+"],
    "O-": ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],
    "AB+": ["AB+"],
    "AB-": ["AB+", "AB-"]
}

# Check if recipient's blood type is compatible
if recipient_Blood_type in compatibility_rules[blood_Type]:
    print(blood_Type, "And", recipient_Blood_type, "Are Compatible")
else:
    print("Blood types are not compatible.")