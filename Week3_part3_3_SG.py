# Prints a hello and welcomes the user to donor match
print("Hello")
print("Welcome to the Donor Match Program")

# Define valid blood types
valid_blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

while True:
    # Requests the user to input the type of blood they have
    blood_type = input("\nPlease enter your blood type. "
                       "You may enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

    # Validate user input
    if blood_type not in valid_blood_types:
        print("Sorry, that is not a valid blood type. "
              "Please enter one of the following: A+, A-, B+, B-, O+, O-, AB+, AB-")
        continue

    print(f"\nYou input {blood_type}.")

    # Ask for the recipient's blood type
    recipient_blood_type = input("\nPlease enter the recipient's blood type. "
                                 "You may enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

    # Validate user input
    if recipient_blood_type not in valid_blood_types:
        print("Sorry, that is not a valid blood type. "
              "Please enter one of the following: A+, A-, B+, B-, O+, O-, AB+, AB-")
        continue

    print(f"\nThe recipient's blood type is {recipient_blood_type}.")

    # Define a dictionary for blood type compatibility
    compatibility = {
        "A+": {"A+": "compatible", "A-": "not compatible", "B+": "not compatible", "B-": "not compatible", "O+": "not compatible", "O-": "not compatible", "AB+": "compatible", "AB-": "not compatible"},
        "A-": {"A+": "compatible", "A-": "compatible", "B+": "not compatible", "B-": "not compatible", "O+": "not compatible", "O-": "compatible", "AB+": "compatible", "AB-": "compatible"},
        "B+": {"A+": "not compatible", "A-": "not compatible", "B+": "compatible", "B-": "not compatible", "O+": "not compatible", "O-": "not compatible", "AB+": "compatible", "AB-": "not compatible"},
        "B-": {"A+": "not compatible", "A-": "not compatible", "B+": "compatible", "B-": "compatible", "O+": "not compatible", "O-": "compatible", "AB+": "compatible", "AB-": "compatible"},
        "O+": {"A+": "compatible", "A-": "compatible", "B+": "compatible", "B-": "compatible", "O+": "compatible", "O-": "compatible", "AB+": "compatible", "AB-": "compatible"},
        "O-": {"A+": "compatible", "A-": "compatible", "B+": "compatible", "B-": "compatible", "O+": "not compatible", "O-": "compatible", "AB+": "compatible", "AB-": "compatible"},
        "AB+": {"A+": "compatible", "A-": "compatible", "B+": "compatible", "B-": "compatible", "O+": "compatible", "O-": "compatible", "AB+": "compatible", "AB-": "compatible"},
        "AB-": {"A+": "compatible", "A-": "compatible", "B+": "compatible", "B-": "compatible", "O+": "compatible", "O-": "compatible", "AB+": "compatible", "AB-": "compatible"}
}

    # Determine compatibility
    result = compatibility[blood_type][recipient_blood_type]

    # Print result
    if result == "compatible":
        print("\nThe donor is compatible with the recipient. You may proceed.")
    else:
        print("\nThe donor is not compatible with the recipient. Please find another donor.")

    # Ask if the user wants to try again
    try_again = input("\nWould you like to try again? Please enter 'yes' or 'no': ")

    if try_again.lower() != "yes":
        break