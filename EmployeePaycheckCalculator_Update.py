# Request's the user to input the employee's name
employees_Name = input("Please Enter The Employee's Name: ")

# Request's the user to input number of hours the employee worked
hrs_Worked = float(input("Please Enter The Number of Hours Worked in a Week: "))

# If the hours are zero or less than zero a message will prompt telling the user wrong input
if hrs_Worked <= 0:
    print("Sorry, you have entered an incorrect value for hours worked.")

# If a number above zero is entered the program will continue 
else:        
    pay_Rate = float(input("Please Enter Hourly Pay Rate: "))
    
    # If the pay rate is zero or less than zero a message will prompt telling the user wrong input
    if pay_Rate <= 0:
        print("Sorry, you have entered an incorrect value for hourly pay rate.") 
   
    # If a number above zero is entered the program will continue      
    else:         
        fed_Tax = float(input("Please Enter Federal Tax Withholding Rate: "))
        
        # If the federal tax is zero or less than zero a message will prompt telling the user wrong input
        if fed_Tax <= 0:
            print("Sorry, you have entered an incorrect value for federal tax withholding rate.") 
            
        # If a number above zero is entered the program will continue 
        else:               
            state_Tax = float(input("Please Enter State Tax Withholding Rate: "))
            
            # If the state tax is zero or less than zero a message will prompt telling the user wrong input
            if state_Tax <= 0:
                print("Sorry, you have entered an incorrect value for state tax withholding rate.") 
            
            # If a number above zero is entered the program will continue 
            else:               
                # Calculates the gross pay by multiplying hours worked by pay rate
                gross_Pay = hrs_Worked * pay_Rate
                
                # Calculates the federal withholdings by multiplying gross pay by federal tax
                fed_With = gross_Pay * fed_Tax
                
                # Calculates the state withholdings by multiplying gross pay by state tax
                state_With = gross_Pay * state_Tax
                
                # Calculates the total deductions by adding the state withholdings and the federal withholdings
                total_Deduc = state_With + fed_With
                
                # Calculates the net pay by subtracting total deductions from gross pay
                net_Pay = gross_Pay - total_Deduc
                
                # Prints the result's for the user to see. The \t is an escape key used for indenting
                print("Paycheck for", employees_Name)
                print("-------------------------------")
                print("Employee Information")
                print("Number of hours worked:\t", round(hrs_Worked, 2))
                print("Hourly pay rate:\t", round(pay_Rate, 2))
                print("-------------------------------")
                print("Deductions")
                print("Federal withholding:\t", round(fed_With, 2))
                print("State withholding:\t", round(state_With, 2))
                print("Total deductions:\t", round(total_Deduc, 2))
                print("-------------------------------")
                print("Net Pay:\t\t", round(net_Pay, 2)))