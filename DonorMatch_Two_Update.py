# Prints a hello and welcomes the user to donor match
print("Hello")
print("Welcome to the Donor Match Program")

# Requests the user to input the type of blood they have 
# The input can be A+, A-, B+, B-, O+, O-, AB+, AB-
blood_Type = input("\nPlease Input The Donor's Blood Type. You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

# This line will ask for the recipient's blood type
recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type. You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

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

# Check if donor's blood type exists in the dictionary
if blood_Type in compatibility_rules:
    # Check if recipient's blood type is compatible
    if recipient_Blood_type in compatibility_rules[blood_Type]:
        print(blood_Type, "And", recipient_Blood_type, "Are Compatible")
    else:
        print(blood_Type, "And", recipient_Blood_type, "Are Not Compatible")
else:
    print("You Have Entered" 
          "\nDonor's Blood Type:", blood_Type, 
          "\nAnd Recipient's Blood Type:", recipient_Blood_type, 
          "\nThis is an Improper Input." 
          "\nPlease Enter One of The Selections Listed A+, A-, O+, O-, AB+, AB-" 
          "\nFor The Donor and Recipient")