"""
Group Members: Nathalia Pinzon, Anna Ruan, Jubril Somid

Date: 19-Mar-2023

Program Description:
This program can be used to calculate the profits of Circle Phones for a given time period. 

It is capable of calculating profits for the followign time periods:
    - One day
    - One weeek
    - One work week
    - One weekend

Inputs:
    - Time period to be calculated
    - Product number
    - Quantity for each product

Processing:
    - The total profits for the given time periods are calculated based on the prices defined on the dictionary.
    - The program runs in a loop until the user specifies that they wish to exit.

Outputs:
    - The total profit for the given time period, with a descriptive message.
    = A message (congratulating or encouraging) that reflects the performance for period
"""

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
all_week = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

# Display welcome message to the user
print("Welcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by\nweek or you can divide the week into weekdays and the weekend.\n")
print("Welcome to Circle Phones Profit calculator\n")

# Loop until the user chooses to exit the program
while (True):

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
    if (user_entry in range(1, 5)):
        while (True):

            # If user chooses to calculate profits for a specific day
            if (user_entry == 1):

                # Ask the user what day they want to calculate profits for
                if (week_days == ""):
                    week_days = input(
                        "\nEnter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n\n")
                    print("\nFor " + week_days.title())

                else:
                    # Get user input for the product number
                    product_number = int(
                        input("\nEnter product number 1-5, or 0 to stop:\n\n"))

                    # If user chooses to stop, break out of this loop
                    if (product_number == 0):
                        break

                    # If user inputs an invalid product number, display an error message and continue
                    elif (product_number not in range(0, 6)):
                        print("Invalid input, please enter a valid number\n")
                        continue

                    # If user inputs a valid product number, ask for the quantity sold and calculate the profits.
                    quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                    total_profits += (quantity_sold *
                                      profit_margins[product_number])

            # If user chooses to calculate profits for the entire week
            elif (user_entry == 2):

                # Print a message for the respective day of the week
                if (count < 7):
                    print(f"\nFor {all_week[count].title()}")

                # Print the total profits once the user has input the profits for all the days of the week
                if (count == 7):
                    print(
                        f"\nYour total profit for the week is: ${total_profits:.2f}\n")

                    # If the total profits are greater than or equal to 10000, display a congratulatory message
                    if (total_profits >= 10000):
                        print("You did good this week")

                    # Otherwise, display a message that more hard work is needed
                    else:
                        print(
                            "More hard work needed... The last week wasn't the best")
                    break

                # Get user input for the product number
                product_number = int(
                    input("\nEnter product number 1-5, or 0 to stop:\n\n"))

                # If user chooses to stop, break out of this loop
                if (product_number == 0):
                    count += 1
                    continue

                # If user inputs an invalid product number, display an error message and continue
                elif (product_number not in range(0, 6)):
                    print("Invalid input, please enter a valid number\n")
                    continue

                # If user inputs a valid product number, ask for the quantity sold and calculate the profits.
                quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                total_profits += (quantity_sold *
                                  profit_margins[product_number])

                # Increment the count
                count += 1

            # If user chooses to calculate profits for the business days of the week
            elif (user_entry == 3):

                # Print a message for the respective day of the week
                if (count < 5):
                    print(f"\nFor {all_week[count]}")

                # Print the tota profits once the user has input the profits for all the business days
                if (count == 5):
                    print(
                        f"\nYour total profit for the week (business days) is: ${total_profits:.2f}\n")

                    # If the total profits are greater than or equal to 10000, display a congratulatory message
                    if (total_profits >= 10000):
                        print("You did good this week (business days)")

                    # Otherwise, display a message that more hard work is needed
                    else:
                        print(
                            f"More hard work needed... The last week (business days) wasn't the best")
                    break

                # Get user input for the product number
                product_number = int(
                    input("\nEnter product number 1-5, or 0 to stop:\n\n"))

                # If user chooses to stop, break out of this loop
                if (product_number == 0):
                    count += 1
                    continue

                # If user inputs an invalid product number, display an error message and continue
                elif (product_number not in range(0, 6)):
                    print("\nInvalid input, please enter a valid number\n")
                    continue

                # If user inputs a valid product number, ask for the quantity sold and calculate the profits.
                quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                total_profits += (quantity_sold *
                                  profit_margins[product_number])

                # Increment the count
                count += 1

            # If user chooses to calculate profits for the weekend
            elif (user_entry == 4):

                # Print a message for the respective day of the week
                if (count < 2):
                    print(f"\nFor {all_week[count+5]}")

                # Print the total profits once the user has input the profits for all the weekend days
                if ((count + 5) == 7):
                    print(
                        f"\nYour total profit for the weekend is: ${total_profits:.2f}\n")

                    # If the total profits are greater than or equal to 10000, display a congratulatory message
                    if (total_profits >= 10000):
                        print("You did good this weekend")

                    # Otherwise, display a message that the user needs to work harder
                    else:
                        print(
                            f"More hard work needed... The last weekend wasn't the best")
                    break

                # Get user input for the product number
                product_number = int(
                    input("\nEnter product number 1-5, or 0 to stop:\n\n"))

                # If user chooses to stop, break out of this loop
                if (product_number == 0):
                    count += 1
                    continue

                # If user inputs an invalid product number, display an error message and continue
                elif (product_number not in range(0, 6)):
                    print("\nInvalid input, please enter a valid number\n")
                    continue

                # If user inputs a valid product number, ask for the quantity sold and calculate the profits.
                quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                total_profits += (quantity_sold *
                                  profit_margins[product_number])
                count += 1

    # If user chooses to exit the program
    elif (user_entry == 0):
        print("\nProgram End!")
        break

    # If user entry is invalid, display an error message and continue
    else:
        print("\nInvalid input, please enter a valid input")
        continue

    # Print the total profits for when a user chooses to calculate profits for a specific day
    if (user_entry == 1):
        print(
            f"\nYour total profit for {week_days.title()} is: ${total_profits:.2f}\n")

        # If the total profits are greater than or equal to 10000, display a congratulatory message
        if (total_profits >= 10000):
            print(f"You did good this {week_days.title()}")

        # Otherwise, display a message that more hard work is needed
        else:
            print(
                f"More hard work needed... The last {week_days.title()} wasn't the best")
