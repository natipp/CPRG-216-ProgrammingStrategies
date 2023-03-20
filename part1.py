#Date: March 18th 2023
#This program is to create an application that automatically calculated Circle Phones' total profit
#for one-day period
profit_margins = {1: 120.45,
                  2: 99.50,
                  3: 75.69,
                  4: 65.73,
                  5: 51.49}

print("Welcome to Circle Phones' Profit calculator.")

product_number = 0
quantity_sold = 0
total_profits = 0
while(True):
    product_number = int(input("Enter product number 1-5, or enter 0 to stop:\n\t"))
    if(product_number == 0):
        break
    elif(product_number not in range(0,6)):
        print("Invalid input, please enter a valid number")
        continue
    quantity_sold = int(input("Enter quantity sold:\n\t"))
    total_profits += (quantity_sold * profit_margins[product_number])

print(f"Your total profit for today is: {total_profits:.2f}")
