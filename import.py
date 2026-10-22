# Program to demonstrate built-in modules: math, random, and datetime
import math
import random
import datetime

# Take input from the user
num = float(input("Enter a number: "))

# Square root using math module
sqrt_result = math.sqrt(num)
print("\nSquare Root:", sqrt_result)

# Generate a random number using random module
random_number = random.randint(1, 100)
print("Random Number (1 to 100):", random_number)

# Display current date and time using datetime module
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)