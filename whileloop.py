n = int(input("Enter a number: "))

# Store the original value
num = n

# Print numbers from 1 to N
print("Numbers from 1 to N:")
for i in range(1, n + 1):
    print(i)

# Print numbers from N to 1
print("Numbers from N to 1:")
while n >= 1:
    print(n)
    n -= 1

# Print multiplication table
print("Multiplication Table:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)