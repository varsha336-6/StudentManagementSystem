# Create and write data into the file
file = open("student.txt", "w")
file.write("Name: Varsha\n")
file.write("Course: B.Tech CSE\n")
file.write("College: GNA University\n")
file.close()

# Read and display the file content
file = open("student.txt", "r")
print("File Content:")
print(file.read())
file.close()

# Append new data to the file
file = open("student.txt", "a")
file.write("City: Ludhiana\n")
file.write("Year: Second Year\n")
file.close()

# Display the updated file content
file = open("student.txt", "r")
print("\nUpdated File Content:")
print(file.read())
file.close()