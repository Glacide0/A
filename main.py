from calculator import Calculator

def main():
    calc = Calculator()
    
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1-4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {calc.add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {calc.subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {calc.divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()