#name="Varsha"
#age=20
#height=5.5
#is_student=True

#print("My name is", name)
#print("Data Type:", type(name))

#print("I am " ,age,"years old")
#print("Data Type:", type(age))

#print("I am", height, "feet tall")
#print("Data Type:", type(height))

#print("I am a student:", (is_student))
#print("Data Type:", type(is_student))

# Global variable
name = "Python"

def display():
    # Local variable
    message = "Hello"

    print("Inside Function:")
    print("Global Variable:", name)
    print("Local Variable:", message)

# Function call
display()

print("\nOutside Function:")
print("Global Variable:", name)

# Uncomment the line below to see the error
# print("Local Variable:", message)