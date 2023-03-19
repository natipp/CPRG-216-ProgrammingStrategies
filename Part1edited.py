# Part 1: Daily Profit Calculator

# Circle phones divides phones into 5 categories:

# Category  Description     Average Profit Per Unit
# 1         Apple iPhone    $120.45
# 2         Android Phone   $99.50
# 3         Apple Tablet    $75.69
# 4         Android Tablet  $65.73
# 5         Windows Tablet  $50.00

# Define a dictionary that maps product numbers to average profit per unit
product_profit = {
    1: 120.45,
    2: 99.50,
    3: 75.69,
    4: 65.73,
    5: 50.00
}

# List of valid product numbers
valid_product_numbers = list(product_profit.keys())

# Initialize the profit accumulator
profit = 0.0

# Print the welcome message
print("Welcome to Circle Phones' Profit Calculator!")

while True:
    # Get the product number
    product_number = int(
        input("Enter product number 1-5, or enter 0 to stop:\n"))

    # Check if the user wants to stop
    if product_number == 0:
        print(f"Your total profit for today is: {profit}")
        break

    # Validate the product number
    if product_number not in valid_product_numbers:
        print("Invalid input, please enter a valid number")
        continue

    else:
        # Get the quantity sold
        quantity_sold = int(input("Enter quantity sold:\n"))

        # Calculate the profit
        profit += quantity_sold * product_profit[product_number]

# Print the final profit
print(f"Your total profit for today is: {profit}")