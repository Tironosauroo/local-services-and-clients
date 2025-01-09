from Calculator import Calculator
import cmd

print("Welcome to Calculator. Type 'commands' to get a of list commands. Type 'exit' to quit.")

while True:
    command = input("cmd> ").strip().lower()

    if command.lower() == "commands":
        print("Available commands:")
        print("1. Addition <a> <b> - Add two numbers")
        print("2. Subtraction <a> <b> - Subtract second number from the first")
        print("3. Multiplication <a> <b> - Multiply two numbers")
        print("4. Division <a> <b> - Divide first number by the second")
        print("5. Exit - Quit the calculator")

   
    elif command.startswith("addition"):
        try:
            numbers = list(map(float, command.split()[1:]))
            if not numbers:
                raise ValueError("No numbers provided.")
            calculator = Calculator(numbers)
            print(f"Result: {calculator.add()}")
        except ValueError as e:
            print(f"Error: {e}")

    # elif command.startswith("subtraction"):
    #     try:
    #         parts = command.split()
    #         if len(parts) < 2:
    #             raise ValueError("No numbers provided. Usage: subtraction <a> <b> ...")
    #         numbers = list(map(float, parts[1:]))
    #         calculator = Calculator(numbers)
    #         print(f"Result: {calculator.subtract()}")
    #     except ValueError as e:
    #         print(f"Error: {e}")
    #     except Exception as e: 
    #         print(f"Unexpected error: {e}")
    # elif command.startswith("subtraction"):
    #     try:
    #         parts = command.split()
    #         print(f"Received command: {command}")  # Лог для перевірки введеної команди
    #         if len(parts) < 2:
    #             raise ValueError("No numbers provided. Usage: subtraction <a> <b> ...")
    #         numbers = list(map(float, parts[1:]))
    #         print(f"Parsed numbers: {numbers}")  # Лог для перевірки отриманих чисел
    #         calculator = Calculator(numbers)
    #         result = calculator.subtract()
    #         print(f"Calculated result: {result}")  # Лог для результату
    #         print(f"Result: {result}")
    #     except ValueError as e:
    #         print(f"Error: {e}")
    #     except Exception as e: 
    #         print(f"Unexpected error: {e}")
    elif command.startswith("subtraction"):
        try:
            numbers = list(map(float, command.split()[1:]))
            if not numbers:
                raise ValueError("No numbers provided.")
            calculator = Calculator(numbers)
            print(f"Result: {calculator.subtract()}")
        except ValueError as e:
            print(f"Error: {e}")
   



