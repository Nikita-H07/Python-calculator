def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("===== Simple Calculator =====")
print("Operations: + | - | * | /")
print("=============================")

while True:
    print("\n1. Calculate")
    print("2. Exit")
    
    choice = input("\nEnter choice (1/2): ")
    
    if choice == '2':
        print("Goodbye! 👋")
        break
    
    elif choice == '1':
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            print(f"Result: {add(num1, num2)}")
        elif operator == '-':
            print(f"Result: {subtract(num1, num2)}")
        elif operator == '*':
            print(f"Result: {multiply(num1, num2)}")
        elif operator == '/':
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid operator!")
    
    else:
        print("Invalid choice! Enter 1 or 2.")
