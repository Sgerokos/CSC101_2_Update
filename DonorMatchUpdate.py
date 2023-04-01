# Prints a welcome message for the user
print("Hello")
print("Welcome to the Donor Match Program")

# Requests the user to input their blood type 
# The input can be A+, A-, B+, B-, O+, O-, AB+, AB-
blood_type = input("\nPlease input your blood type. "
                   "You may enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

# Define a function to display options for each blood type
def display_options(blood_type):
    print(f"\nYou input {blood_type}.")
    
    # Request the user to choose between facts, giving blood, or receiving blood
    info = int(input("What would you like to know about this blood type?"
                     "\nInput 1 for facts, 2 to give blood, 3 to receive blood: "))
    return info

# Define a dictionary to store information for each blood type
blood_info = {
    'A+': {
        'facts': "1 in 3 people have blood type A+. This blood type is one of the most common blood types.",
        'give': "You can give blood to A+ and AB+.",
        'receive': "You can receive blood from A+, A-, O+, and O-."
    },
    'A-': {
        'facts': "Only 1 in 16 people have blood type A-.",
        'give': "You can give blood to anyone with A or AB, regardless of them being negative or positive.",
        'receive': "You can receive blood from anyone with A- or O-."
    },
    # Add the other blood types with their respective information
}

if blood_type in blood_info:
    info = display_options(blood_type)
    blood_type_info = blood_info[blood_type]

    if info == 1:
        print("You have requested facts:")
        print(blood_type_info['facts'])
    elif info == 2:
        print("You have requested to give blood:")
        print(blood_type_info['give'])
    elif info == 3:
        print("You have requested to receive blood:")
        print(blood_type_info['receive'])
    else:
        print("Sorry, wrong input. Please input 1, 2, or 3 for this selection.")
else:
    print("Sorry, invalid blood type. Please input a valid blood type.")