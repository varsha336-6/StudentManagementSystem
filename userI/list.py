# Program to demonstrate dictionary operations

# Creating a Student Information Dictionary
student = {
    "Name": "Varsha",
    "Age": 21,
    "Course": "B.Tech CSE",
    "City": "Phagwara"
}

print("Original Dictionary:")
print(student)

# Accessing values
print("\nStudent Name:", student["Name"])
print("Course:", student["Course"])

# Adding a new key-value pair
student["College"] = "GNA University"
print("\nAfter Adding College:")
print(student)

# Updating a value
student["City"] = "Jalandhar"
print("\nAfter Updating City:")
print(student)

# Removing data
student.pop("Age")
print("\nAfter Removing Age:")
print(student)

# Displaying keys and values
print("\nKeys:", student.keys())
print("Values:", student.values())

# Using dictionary methods
print("\nItems:", student.items())
print("Length of Dictionary:", len(student))