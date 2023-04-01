# Import the sys package into python
import sys

# Welcome the user to the establishment
print("Hello, Welcome to Tru Astoria")
print("\nWhat Would You Enjoy Today?")

# Initialize variables
sales_tax = 0.0875
price = 0
order = ""
anything_else = "Y"

# Continue looping until the user decides not to add more items
while anything_else == "Y":

    # Ask the user to input a number for one of the items
    burger_sandwiches_wraps = int(input("Please Choose \n1 For Tru Burger"
                                        "\n2 For Classic Cheeseburger,"
                                        "\n3 For Salmon Burger,"
                                        "\n4 For Vegetable Panini,"
                                        "\n5 For Greek Roast Chicken Panini,"
                                        "\n6 For Fried Chicken Sandwich,"
                                        "\n7 For Cubano,"
                                        "\n8 For Falafel Wrap"
                                        "\n9 For Grilled Chicken Wrap,"
                                        "\n10 For Turkey Avocado BLT:"))

    # Display the selected item and ask if the user wants to add it to their order
    if burger_sandwiches_wraps == 1:
        item_name = "Tru Burger"
        item_price = 18.72
        item_description = ("sautéed onions, roasted red pepper, bacon,"
                            "\nSwiss cheese, sriracha maple mayo, brioche bun.")

    elif burger_sandwiches_wraps == 2:
        item_name = "Classic Cheeseburger"
        item_price = 16.64
        item_description = ("Lettuce, tomato, onion,"
                            "and American cheese on brioche bun.")

    elif burger_sandwiches_wraps == 3:
        item_name = "Salmon Burger"
        item_price = 19.76
        item_description = ("char-grilled wild-caught Atlantic salmon burger with a"
                            "\nsignature Worcestershire sauce, shredded cabbage,"
                            "\nand mustard aioli.")

    elif burger_sandwiches_wraps == 4:
        item_name = "Vegetable Panini"
        item_price = 15.60
        item_description = ("farmers pick of fresh grilled,"
                            "\nvegetables, sun dried tomato aioli on a pressed Italian roll.")

    elif burger_sandwiches_wraps == 5:
        item_name = "Greek Roast Chicken Panini"
        item_price = 17.68
        item_description = ("breaded chicken breast,"
                            "\nAmerican cheese, guacamole spread, tomatoes,"
                            "\nhoney mustard, on a brioche.")

    elif burger_sandwiches_wraps == 6:
        item_name = "Fried Chicken Sandwich"
        item_price = 17.68
        item_description = ("breaded chicken breast, American cheese,"
                            "\nguacamole spread, tomatoes, honey mustard, on a brioche.")

    elif burger_sandwiches_wraps == 7:
        item_name = "Cubano"
        item_price = 17.68
        item_description = ("pulled pork, deli ham,"
                            "Swiss cheese, pickles, and mustard.")

    elif burger_sandwiches_wraps == 8:
        item_name = "Falafel Wrap"
        item_price = 16.64
        item_description = ("hummus, tabbouleh, tahini sauce,"
                            "rugula, falafel fritters.")

    elif burger_sandwiches_wraps == 9:
        item_name = "Grilled Chicken Wrap"
        item_price = 16.64
        item_description = ("grilled chicken, lettuce, tomato,"
                            "red onion, and garlic aioli in a flour tortilla.")

    elif burger_sandwiches_wraps == 10:
        item_name = "Turkey Avocado BLT"
        item_price = 17.68
        item_description = ("smoked turkey, bacon, lettuce, tomato,"
                            "avocado, and mayo on whole wheat bread.")

    else:
        print("\nInvalid input. Please enter a number between 1 and 10.")
        continue

    print(f"\nYou have selected the {item_name}.")
    print(f"Description: {item_description}")
    print(f"Price: ${item_price:.2f}")

    add_item = input(f"\nWould you like to add the {item_name} to your order? (Y/N): ").upper()

    if add_item == "Y":
        price += item_price
        order += f"{item_name}, "

    # Ask if the user wants to add more items
    anything_else = input("\nWould you like to add anything else to your order? (Y/N): ").upper()

    # Calculate the total price
    total_price = price * (1 + sales_tax)

    # Display the order summary and total price
    print("\nYour order:")
    print(order[:-2])  # Remove the trailing comma and space
    print(f"\nSubtotal: ${price:.2f}")
    print(f"Sales Tax: ${price * sales_tax:.2f}")
    print(f"Total: ${total_price:.2f}")

    print("\nThank you for dining with us at Tru Astoria! Enjoy your meal!")