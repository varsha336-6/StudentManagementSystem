def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is not possible."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Modulus by zero is not possible."
    return a % b

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display menu
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter your choice (1-5): "))

# Calling the appropriate function
if choice == 1:
    print("Result =", addition(num1, num2))
elif choice == 2:
    print("Result =", subtraction(num1, num2))
elif choice == 3:
    print("Result =", multiplication(num1, num2))
elif choice == 4:
    print("Result =", division(num1, num2))
elif choice == 5:
    print("Result =", modulus(num1, num2))
else:
    print("Invalid choice!")
