# Import sys package for exit functionality
import sys

# Display welcome message
print("Hello, welcome to Tru Astoria")
print("\nWhat would you enjoy today?")

# Set the sales tax to 8.75%
sales_tax = 0.0875

# Initialize the 'anything_else' variable to 'Y'
anything_else = "Y"

# Initialize the 'order' variable as an empty string
order = ""
price = 0

def menu():
    global order, price, anything_else
    
    # Display menu options and take input from user
    burger_sandwiches_wraps = int(input("Please choose \n1 for Tru Burger"
                                        "\n2 for Classic Cheeseburger,"
                                        "\n3 for Salmon Burger,"
                                        "\n4 for Vegetable Panini,"
                                        "\n5 for Greek Roast Chicken Panini,"
                                        "\n6 for Fried Chicken Sandwich,"
                                        "\n7 for Cubano,"
                                        "\n8 for Falafel Wrap"
                                        "\n9 for Grilled Chicken Wrap,"
                                        "\n10 for Turkey Avocado BLT:"))

    # Check if user input is valid
    if burger_sandwiches_wraps < 1 or burger_sandwiches_wraps > 10:
        print("You have input an invalid number for Burgers, Sandwiches," 
              "and Wraps."
              "\nPlease enter a number between 1 - 10 for this selection")

    # Process menu selection and update order and price
    else:
        menu_items = [
            ("Tru Burger - sautéed onions, roasted red pepper, bacon," 
             "\nSwiss cheese, sriracha maple mayo, brioche bun.", 18.72),
            ("Classic Cheeseburger - Lettuce, tomato, onion," 
             "and American cheese on brioche bun.", 16.64),
            # Add remaining menu items
        ]
        
        item, item_price = menu_items[burger_sandwiches_wraps - 1]
        print(f"{item}\nThis is ${item_price:.2f}")

        y_n = input("Do you want to add this to your order? "
                    "Y for Yes, N for No: ")

        if y_n == "Y":
            price += item_price
            order += f"\n{item}: ${item_price:.2f}"

def confirmation():
    global anything_else
    anything_else = input("Would you like something else? "
                          "\nPlease enter Y for Yes or N for No:")

def main():
    global anything_else

    while anything_else == "Y":
        menu()
        confirmation()

    if anything_else == "N":
        tax = price * sales_tax
        total = price + tax

        tip_options = [0.10, 0.15, 0.20]
        tips = [total * tip for tip in tip_options]

        print(f"Orders: {order}\nTotal without tax: ${price:.2f}",
              f"\nThe total with tax is: ${total:.2f}",
              f"\nThe sales tax (8.75%) is: ${tax:.2f}")

        for percentage, tip in zip(tip_options, tips):
            print(f"{int(percentage * 100)}% tip is: ${tip:.2f}")

        sys.exit()

main()