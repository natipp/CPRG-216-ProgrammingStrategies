profit_margins = {1: 120.45,
                  2: 99.50,
                  3: 75.69,
                  4: 65.73,
                  5: 51.49}

product_number = 0
quantity_sold = 0
total_profits = 0
week_days = ""
count = 0
all_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Welcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by\nweek or you can divide the week into weekdays and the weekend.\n")
print("Welcome to Circle Phones Profit calculator\n")

while(True):
    count = 0
    total_profits = 0
    print("\nYou can calculate the profit of the company according to a specific day or by a week or divide\nthe week into weekdays and weekend\n")
    print("Enter:\n")
    print("1 - For specific Day\n")
    print("2 - For the Week\n")
    print("3 - For week Business Days\n")
    print("4 - For weekend days\n")
    print("0 - Exit\n")

    user_entry = int(input(""))
    if(user_entry in range(1, 5)):
        while(True):
            if(user_entry == 1):
                if(week_days == ""):
                    week_days = input("\nEnter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n\n")
                    print("\nFor " + week_days.title())
                else:
                    product_number = int(input("\nEnter product number 1-5, or 0 to stop:\n\n"))
                    if(product_number == 0):
                        break
                    elif(product_number not in range(0,6)):
                        print("Invalid input, please enter a valid number\n")
                        continue
                    quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                    total_profits += (quantity_sold * profit_margins[product_number])
            
            elif(user_entry == 2):
                if(count < 7):
                    print(f"\nFor {all_week[count].title()}")
                if(count == 7):
                    print(f"\nYour total profit for the week is: ${total_profits:.2f}\n")
                    if(total_profits >= 10000):
                        print("You did good this week")
                    else:
                        print(f"More hard work needed... The last week wasn't the best")
                    break
                product_number = int(input("\nEnter product number 1-5, or 0 to stop:\n\n"))
                if(product_number == 0):
                    count += 1
                    continue
                elif(product_number not in range(0,6)):
                    print("Invalid input, please enter a valid number\n")
                    continue

                quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                total_profits += (quantity_sold * profit_margins[product_number])
                count += 1
            
            elif(user_entry == 3):
                print(count)
                if(count < 5):
                    print(f"\nFor {all_week[count]}")
                if(count == 5):
                    print(f"\nYour total profit for the week (business days) is: ${total_profits:.2f}\n")
                    if(total_profits >= 10000):
                        print("You did good this week (business days)")
                    else:
                        print(f"More hard work needed... The last week (business days) wasn't the best")
                    break
                product_number = int(input("\nEnter product number 1-5, or 0 to stop:\n\n"))
                if(product_number == 0):
                    count += 1
                    continue
                elif(product_number not in range(0,6)):
                    print("\nInvalid input, please enter a valid number\n")
                    continue

                quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                total_profits += (quantity_sold * profit_margins[product_number])
                count += 1
            

            elif(user_entry == 4):
                if(count < 2):
                    print(f"\nFor {all_week[count+5]}")
                if((count + 5) == 7):
                    print(f"\nYour total profit for the weekend is: ${total_profits:.2f}\n")
                    if(total_profits >= 10000):
                        print("You did good this weekend")
                    else:
                        print(f"More hard work needed... The last weekend wasn't the best")
                    break
                product_number = int(input("\nEnter product number 1-5, or 0 to stop:\n\n"))
                if(product_number == 0):
                    count += 1
                    continue
                elif(product_number not in range(0,6)):
                    print("\nInvalid input, please enter a valid number\n")
                    continue

                quantity_sold = int(input("\nEnter quantity sold:\n\n"))
                total_profits += (quantity_sold * profit_margins[product_number])
                count += 1

    elif(user_entry == 0):
        print("\nProgram End!")
        break
    else:
        print("\nInvalid input, please enter a valid input")
        continue
    if(user_entry == 1):
        print(f"\nYour total profit for {week_days.title()} is: ${total_profits:.2f}\n")
        if(total_profits >= 10000):
            print(f"You did good this {week_days.title()}")
        else:
            print(f"More hard work needed... The last {week_days.title()} wasn't the best")
