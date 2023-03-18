profit_margins = {1: 120.45,
                  2: 99.50,
                  3: 75.69,
                  4: 65.73,
                  5: 51.49}

print("Welcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by\nweek or you can divide the week into weekdays and the weekend.\n")
print("Welcome to Circle Phones Profit calculator\n")
print("You can calculate the profit of the company according to a specidic day or by a week or divide\nthe week into weekdays and weekend\n")
print("Enter:\n")
print("1 - For specific Day\n")
print("2 - For the Week\n")
print("3 - For week Business Days\n")
print("4 - For weekend days\n")
print("0 - Exit\n")
product_number = 0
quantity_sold = 0
total_profits = 0
week_days = ""
count = 0
all_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

user_entry = int(input(""))