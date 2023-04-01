# Import the sys package into Python
import sys

# Welcome the user to the establishment
print("Hello Welcome to Tru Astoria")
print("\nWhat Would You Enjoy Today?")

# Initialize variables
sales_tax = 0.0875
price = 0
order = ""
anything_else = "Y"

# Continue the loop while the user wants to order more items
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

    # If the input is below 1 or above 10, an error message will be printed
    if burger_sandwiches_wraps < 1 or burger_sandwiches_wraps > 10:
        print("You have input an invalid number for Burgers, Sandwiches,"
              "and Wraps."
              "\nPlease enter a number between 1 - 10 for this selection")

        # If 1 is selected, the item will be displayed
    elif burger_sandwiches_wraps == 1:

        print("Tru Burger - saut�ed onions, roasted red pepper, bacon,"
              "\nSwiss cheese, sriracha maple mayo, brioche bun."
              "\nThis is $18.72")

        # Ask the user if they want to add this to the order
        y_n = input("Do you want to add this to your order? "
                    "Y for Yes, N for No: ")

        # If Y is selected, the price will be added to the 'price' variable
        # The order will be added to the 'order' variable
        if y_n == "Y":
            price += 18.72
            order += "\nTru Burger: $18.72"

        # If N is selected, no price will be added to the 'price' variable
        # The 'order' variable will remain as it did before
        elif y_n == "N":
            order += ""

    # Similar code blocks for options 2 to 10

    # Check if the user wants to add more items
    anything_else = input("Would you like something else? \
        \nPlease enter Y for Yes or N for No:")

    # If N is selected, display the total and exit
    if anything_else == "N":
        # Calculate tax, total, and recommended tips
        tax = price * sales_tax
        total = price + tax
        ten_tip = total * 0.10
        fifteen_tip = total * 0.15
        twenty_tip = total * 0.20

        # Print the total, tax, and recommended tips, then exit
        print("Orders:", order, "\nTotal Without Tax", price,
              "\nThe Total With Tax is:", round(total, 2),
              "\nThe Sales Tax 8.75% is:", round(tax, 2),
              "\n10% Tip is:", round(ten_tip, 2),
              "\n15% Tip is:", round(fifteen_tip, 2),
              "\n20% Tip is:", round(twenty_tip, 2),
              "\nThank you for your order!")
        sys.exit()