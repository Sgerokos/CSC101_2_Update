# Imports the sys package into python
import sys

# Welcome the user to the establishment
print("Hello, welcome to Tru Astoria")
print("\nWhat would you like to order today?")

# Set the sales tax to 8.75%
sales_tax = 0.0875

# Initialize the price variable to 0
price = 0

# Set anything_else to 'Y' until the user changes it
anything_else = "Y"

# Continue the loop as long as anything_else is 'Y'
while anything_else == "Y":
    
    # Ask the user to input a number for one of the items
    choice = int(input("Please choose \n1 for Tru Burger"
                       "\n2 for Classic Cheeseburger,"
                       "\n3 for Salmon Burger,"
                       "\n4 for Vegetable Panini,"
                       "\n5 for Greek Roast Chicken Panini,"
                       "\n6 for Fried Chicken Sandwich,"
                       "\n7 for Cubano,"
                       "\n8 for Falafel Wrap"
                       "\n9 for Grilled Chicken Wrap,"
                       "\n10 for Turkey Avocado BLT:"))    
     
    # If the input is below 1 or above 10, display an error message   
    if choice < 1 or choice > 10:
        print("You have entered an invalid number for burgers, sandwiches, and wraps."
              "\nPlease enter a number between 1 and 10 for this selection.")   
    
    # If a valid choice is made, add the item's price to the total and display the selection
    elif choice == 1:
        price += 18.72
        print("Tru Burger - sautéed onions, roasted red pepper, bacon," 
              "\nSwiss cheese, sriracha maple mayo, brioche bun." 
              "\nThis is $18.72")
    # ...
    # (Repeat for all other choices)
    # ...

    # Check if the user wants to add more items
    anything_else = input("Would you like to add something else? \
        \nPlease enter Y for Yes or N for No:")
    
    # If the user selects 'N', calculate and display the total, tax, and suggested tips
    if anything_else == "N":            
        tax = price * sales_tax
        total = price + tax
        ten_tip = total * 0.10
        fifteen_tip = total * 0.15
        twenty_tip = total * 0.20

        print("The total is:", round(total, 2), 
              "\nThe sales tax is:", round(tax, 2), 
              "\n10% tip is:", round(ten_tip, 2), 
              "15% tip is:", round(fifteen_tip, 2), 
              "20% tip is:", round(twenty_tip, 2))
        sys.exit()
                  
    # If the user enters an invalid input, display an error message
    elif anything_else != "N" and anything_else != "Y":
        print("Bad input:", anything_else)