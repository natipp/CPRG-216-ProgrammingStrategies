# Part 1: Daily Profit Calculator

# Circle phones divides phones into 5 categories:

# Category  Description     Average Profit Per Unit
# 1         Apple iPhone    $120.45
# 2         Android Phone   $99.50
# 3         Apple Tablet    $75.69
# 4         Android Tablet  $65.73
# 5         Windows Tablet  $50.00

# Constants for prices
APPLE_IPHONE = 120.45
ANDROID_PHONE = 99.50
APPLE_TABLET = 75.69
ANDROID_TABLET = 65.73
WINDOWS_TABLET = 51.49

# List of valid product numbers
valid_product_numbers = [1, 2, 3, 4, 5]

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
        print(f"Your total profit for today is: {profit}"),
        break

    # Validate the product number
    if product_number not in valid_product_numbers:
        print("Invalid input, please enter a valid number")
        continue

    else:
        # Get the quantity sold
        quantity_sold = int(input("Enter quantity sold:\n"))

        # Calculate the profit
        # 1 - Apple iPhone
        if product_number == 1:
            profit += quantity_sold * APPLE_IPHONE

        # 2 - Android Phone
        elif product_number == 2:
            profit += quantity_sold * ANDROID_PHONE

        # 3 - Apple Tablet
        elif product_number == 3:
            profit += quantity_sold * APPLE_TABLET

        # 4 - Android Tablet
        elif product_number == 4:
            profit += quantity_sold * ANDROID_TABLET

        # 5 - Windows Tablet
        elif product_number == 5:
            profit += quantity_sold * WINDOWS_TABLET