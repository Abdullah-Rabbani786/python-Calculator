import math

def calculator():
    while True:

        print("Python Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Square Root")
        print("8. Cube")
        print("9. Exit")

        try:
            choice = int(input("Select an operation (1-9): "))
            if choice == 9:
                print("Exiting the calculator. Goodbye!")
                break

            if choice in [1, 2, 3, 4, 5, 6]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == 2:
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == 3:
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == 4:
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
                elif choice == 5:
                    print(f"Result: {num1} % {num2} = {num1 % num2}")
                elif choice == 6:
                    print(f"Result: {num1} ^ {num2} = {num1 ** num2}")

            elif choice == 7:
                num = float(input("Enter a number: "))
                if num <= 0:
                    print("Error: Square root of a negative number and zero are can't be prosessed.")
                else:
                    print(f"Result: {num} = {math.sqrt(num)}")

            elif choice == 8:
                num = float(input("Enter a number: "))
                print(f"Result: {num} = {num ** 3}")

            else:
                print("Invalid choice. Please select a number between 1 and 9.")

            # Ask the user if they want to perform another calculation
            again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if again != 'yes':
                print("Exiting the calculator. Goodbye!")
                break

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

      

calculator()