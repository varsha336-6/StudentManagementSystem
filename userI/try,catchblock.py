# Exception Handling Example

# 1. Handle Invalid User Input
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Error: Please enter a valid number.")

# 2. Handle Division by Zero
try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")

# 3. Handle File Not Found
try:
    file = open("data.txt", "r")
    print("\nFile Content:")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
