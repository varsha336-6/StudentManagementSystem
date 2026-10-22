name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks1 = float(input("Enter marks in Python: "))
marks2 = float(input("Enter marks in Mathematics: "))

total = marks1 + marks2
average = total / 2

print("\n----- Student Information -----")
print("Name:", name)
print("Age:", age)
print("Total Marks:", total)
print("Average Marks:", average)