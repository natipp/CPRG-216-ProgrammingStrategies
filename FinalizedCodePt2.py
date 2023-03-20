# Define the profit margins for each product in a dictionary
profit_margins = {1: 120.45,
                  2: 99.50,
                  3: 75.69,
                  4: 65.73,
                  5: 51.49}

# Initialize variables for product number, quantity sold, total profits, week days, and count
product_number = 0
quantity_sold = 0
total_profits = 0
week_days = ""
count = 0

# Define a list of all the days of the week
all_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Display welcome message to the user
print("Welcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by\nweek or you can divide the week into weekdays and the weekend.\n")
print("Welcome to Circle Phones Profit calculator\n")

# Loop until the user chooses to exit the program
while(True):
    # Reset the count and total profits for each loop
    count = 0
    total_profits = 0
    
    # Display menu options to the user
    print("\nYou can calculate the profit of the company according to a specific day or by a week or divide\nthe week into weekdays and weekend\n")
    print("Enter:\n")
    print("1 - For specific Day\n")
    print("2 - For the Week\n")
    print("3 - For week Business Days\n")
    print("4 - For weekend days\n")
    print("0 - Exit\n")
    
    # Get user input for the menu option
    user_entry = int(input(""))
    
    # If user input is valid, execute the chosen option
    if(user_entry in range(1, 5)):
        while(True):
            # If user chooses to calculate profits for a specific day
            if(user_entry == 1):
                # If the user hasn't input a day yet, ask for a specific day
                if(week_days == ""):
                    week_days = input("\nEnter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n\n")
                    print("\nFor " + week_days.title())
                # If the user has already input a day, ask for the product number and quantity sold
                else:
                    product_number = int(input("\nEnter product number 1-5, or 0 to stop:\n\n"))
                    # If user chooses to stop, break out of this loop
                    if(product_number == 0):
                        break
                    # If user inputs an invalid product number, display an error message and continue
                    elif(product_number not in range(0,6)):
                        print("Invalid input, please enter a valid number\n")
                        continue
                    # If user inputs a valid product number, ask for the quantity sold and calculate the profits.
                    quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                    total_profits += (quantity_sold * profit_margins[product_number])
            
            # If user chooses to calculate profits for the entire week
            elif(user_entry == 2):
                # If the count is less than 7 (total number of days in a week), display profits for each day of the week.
                if(count < 7):
                    print(f"\nFor {all_week[count].title()}")
                # If the count reaches 7, display the total profits for the week and a message based on the total profits calculated prior.
                if(count == 7):
                    print(f"\nYour total profit for the week is: ${total
