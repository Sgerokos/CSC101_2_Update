# The variable balance ask's the user to input the balance they wish to calculate 
balance = float(input("Please enter the balance you wish to calculate: "))

# The variable annual_interest_rate ask's the user to input the annual interest
annual_interest_rate = float(input("Please enter the annual interest rate percentage: "))

# The variable interest calculates the balance and annual interest
interest_earned = balance * annual_interest_rate / 1200

# Print's the interest calcualted to the 5th decimal number 
print(f"The interest earned on a balance of ${balance:.2f} at an annual interest rate of {annual_interest_rate:.2f}% is: ${interest_earned:.5f}") 