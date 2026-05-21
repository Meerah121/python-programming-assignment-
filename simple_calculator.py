def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        choice = input("\nChoose operation (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result = {result}")
        else:
            print("Invalid Input")
    except ValueError:
        print("Invalid number entered!")

if __name__ == "__main__":
    main()
