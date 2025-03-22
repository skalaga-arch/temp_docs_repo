from calculator import operations

def main():
    print("Simple Calculator")
    print("Options: add | subtract | multiply | divide")
    operation = input("Choose operation: ").strip().lower()

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "add":
            result = operations.add(num1, num2)
        elif operation == "subtract":
            result = operations.subtract(num1, num2)
        elif operation == "multiply":
            result = operations.multiply(num1, num2)
        elif operation == "divide":
            result = operations.divide(num1, num2)
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
