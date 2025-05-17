from calculator import Calculator

def display_menu():
    """Display the calculator's menu options."""
    print("\nSimple Calculator")
    print("================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulo (Remainder)")
    print("8. Floor Division")
    print("0. Exit")
    return input("\nEnter choice (0-8): ")

def get_number(prompt):
    """Get a valid number input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    calc = Calculator()
    
    operations = {
        "1": {"name": "Addition", "func": calc.add, "inputs": 2},
        "2": {"name": "Subtraction", "func": calc.subtract, "inputs": 2},
        "3": {"name": "Multiplication", "func": calc.multiply, "inputs": 2},
        "4": {"name": "Division", "func": calc.divide, "inputs": 2},
        "5": {"name": "Power", "func": calc.power, "inputs": 2},
        "6": {"name": "Square Root", "func": calc.square_root, "inputs": 1},
        "7": {"name": "Modulo", "func": calc.modulo, "inputs": 2},
        "8": {"name": "Floor Division", "func": calc.floor_division, "inputs": 2},
    }
    
    while True:
        choice = display_menu()
        
        if choice == "0":
            print("Thank you for using the calculator. Goodbye!")
            break
            
        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue
            
        operation = operations[choice]
        print(f"\nSelected operation: {operation['name']}")
        
        try:
            if operation["inputs"] == 1:
                num = get_number("Enter number: ")
                result = operation["func"](num)
                print(f"Result: {result}")
            else:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                result = operation["func"](num1, num2)
                print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()