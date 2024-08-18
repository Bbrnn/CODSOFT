def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by 0 is not allowed."

def main():
    while True:
        print("\nSelect the operation you'd like to perform")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            # User to choose among the five options
            operation_type = int(input("Enter the choice of operation you'd like to perform (1-5):\n"))

            if operation_type == 5:
                print("Exiting the program. Goodbye!")
                break  # Exit the loop and terminate the program

            if operation_type not in [1, 2, 3, 4]:
                print("Invalid choice. Please choose a number between 1 and 4.")
                continue  # Restart the loop to ask for a valid operation

            # User to input two numbers
            x = float(input("Enter the first number:\n"))
            y = float(input("Enter the second number:\n"))

            # Apply the logic of each choice of operation
            if operation_type == 1:
                print("The addition of", x, "and", y, "=", add_numbers(x, y))
            elif operation_type == 2:
                print("The subtraction of", x, "and", y, "=", subtract_numbers(x, y))
            elif operation_type == 3:
                print("The multiplication of", x, "and", y, "=", multiply_numbers(x, y))
            elif operation_type == 4:
                result = divide_numbers(x, y)
                print("The division of", x, "by", y, "=", result)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
