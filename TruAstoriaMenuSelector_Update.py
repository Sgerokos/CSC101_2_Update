# Welcome the user to the establishment
print("Hello! Welcome to Tru Astoria.")
print("\nWhat would you like to order today?")

# Define the menu items and prices
menu_items = {
    1: ("Tru Burger", 1872),
    2: ("Classic Cheeseburger", 1664),
    3: ("Salmon Burger", 1976),
    4: ("Vegetable Panini", 1560),
    5: ("Greek Roast Chicken Panini", 1768),
    6: ("Fried Chicken Sandwich", 1768),
    7: ("Cubano", 1768),
    8: ("Falafel Wrap", 1664),
    9: ("Grilled Chicken Wrap", 1664),
    10: ("Turkey Avocado BLT", 1872)
}

# Display the menu items
while True:
    print("\nMenu:")
    for num, item in menu_items.items():
        name, price = item
        print(f"{num}. {name} - ${price / 100:.2f}")

    # Ask the user to select an item
    try:
        selection = int(input("\nEnter the number of the item you would like to order: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check if the selection is valid
    if selection not in menu_items:
        print("Invalid selection. Please enter a number between 1 and 10.")
        continue

    # Display the selected item and price
    name, price = menu_items[selection]
    print(f"\n{name} - ${price / 100:.2f}")

    # Ask the user if they want to order another item
    while True:
        choice = input("\nWould you like to order another item? (y/n): ")
        if choice.lower() == "y":
            break
        elif choice.lower() == "n":
            print("Thank you for your order. Enjoy your meal!")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")