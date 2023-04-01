import sys

# Welcome's the user to the establishment
print("Hello! Welcome to Tru Astoria")
print("\nWhat Would You Enjoy Today?")

sales_Tax = 0.0875
price = 0

while True:
    # Ask's the user to input a number for one of the items
    burger_Sandwiches_Wraps = int(input("Please Choose \n1 For Tru Burger"
                                        "\n2 For Classic Cheeseburger,"
                                        "\n3 For Salmon Burger,"
                                        "\n4 For Vegetable Panini,"
                                        "\n5 For Greek Roast Chicken Panini,"
                                        "\n6 For Fried Chicken Sandwich,"
                                        "\n7 For Cubano,"
                                        "\n8 For Falafel Wrap"
                                        "\n9 For Grilled Chicken Wrap,"
                                        "\n10 For Turkey Avocado BLT:"))

    if burger_Sandwiches_Wraps < 1 or burger_Sandwiches_Wraps > 10:
        print("You have Inputed an Invalid Number For Burgers, Sandwiches," 
        "and Wraps."
        "\nPlease Enter a number Between 1 - 10 For This Selection")      
    else:
        if burger_Sandwiches_Wraps == 1:
            price += 18.72
            print("Tru Burger - sautéed onions, roasted red pepper, bacon," 
                "\nSwiss cheese, sriracha maple mayo, brioche bun." 
                " This is $18.72")

        # ... (all other elif statements for choices 2-10)

        anything_Else = input("Would You Like Something Else? \
            \nPlease Enter Y For Yes or N For No:")

        if anything_Else == "Y":
            continue
        elif anything_Else == "N":
            tax = price * sales_Tax
            total = price + tax
            ten_Tip = total * 0.10
            fifteen_Tip = total * 0.15
            twenty_tip = total * 0.20

            print("Total: ", round(total, 2), 
                  "\nSales Tax: ", round(tax, 2), 
                  "\n10% Tip: ", round(ten_Tip, 2), 
                  "\n15% Tip: ", round(fifteen_Tip, 2), 
                  "\n20% Tip: ", round(twenty_tip, 2))
            sys.exit()

        else:
            print("Bad Input", anything_Else)