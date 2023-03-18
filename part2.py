# Part 2: Daily, Weekly, and Weekend Profit Calculator

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
    # Print instructions
    print("You can calculate the profit of the company according to a specific day orby a week or divide the week into weekdays and weekend")
    print("Enter:")
    print("1 - For specific Day")
    print("2 - For the Week")
    print("3 - For Week Business Days")
    print("4 - For Weekend days")
    print("0 - Exit")

    # Read the user's choice
    choice = int(input(""))

    if choice == 0:
        print("Thank you for using Circle Phones' Profit Calculator!")
        break

    if choice == 1:
        # Read the day
        day = input(
            "Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n")

        if day == "Monday":
            print("For Monday")

        while True:
            # Get the product number
            product_number = int(
                input("Enter product number 1-5, or enter 0 to stop:\n"))

            # Check if the user wants to stop
            if product_number == 0:
                print(f"Total profit for the {day} is: ${profit:.2f}")

                # Customized comment
                if profit >= 10000:
                    print("You did well this period! Keep up the great work!")
                else:
                    print(
                        f"More hard work needed... The last {day} wasn't the best")
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

    elif choice == 2:
        # Reset the profit accumulator
        profit = 0.0

        # Loop through the days
        print("For Monday")
        while True:
            # Get the product number
            product_number = int(
                input("Enter product number 1-5, or enter 0 to stop:\n"))

            # Check if the user wants to stop
            if product_number == 0:
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

        print("For Tuesday")
        while True:
            # Get the product number
            product_number = int(
                input("Enter product number 1-5, or enter 0 to stop:\n"))

            # Check if the user wants to stop
            if product_number == 0:
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

        print("For Wednesday")
        while True:
            # Get the product number
            product_number = int(
                input("Enter product number 1-5, or enter 0 to stop:\n"))

            # Check if the user wants to stop
            if product_number == 0:
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

        print("For Thursday")
        while True:
            # Get the product number
            product_number = int(
                input("Enter product number 1-5, or enter 0 to stop:\n"))

            # Check if the user wants to stop
            if product_number == 0:
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

        print("For Friday")
        while True:
            # Get the product number
            product_number = int(
                input("Enter product number 1-5, or enter 0 to stop:\n"))

            # Check if the user wants to stop
            if product_number == 0:
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

        print("For Saturday")
        while True:
            # Get the product number
            product_number = int(
                input("Enter product number 1-5, or enter 0 to stop:\n"))

            # Check if the user wants to stop
            if product_number == 0:
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

        print("For Sunday")
        while True:
            # Get the product number
            product_number = int(
                input("Enter product number 1-5, or enter 0 to stop:\n"))

            # Check if the user wants to stop
            if product_number == 0:
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

        # Display the profit
        print(f"Total profit for the week is: ${profit:.2f}")

        # Customized comment
        if profit >= 10000:
            print("You did good this week")
        else:
            print(
                f"More hard work needed... The last week wasn't the best")
