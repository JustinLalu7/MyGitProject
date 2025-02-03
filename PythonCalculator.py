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

def calculator():
    print("Select operation:")
    print("A. Add")
    print("B. Subtract")
    print("C. Multiply")
    print("D. Divide")
    
    choice = input("Enter choice (A/B/C/D): ")
    
    if choice in ('A', 'B', 'C', 'D'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'A':
            print(f"Result: {add(num1, num2)}")
        elif choice == 'B':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == 'C':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == 'D':
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()