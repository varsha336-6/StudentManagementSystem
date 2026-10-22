# Student Management System
# Python Library Used
import datetime

FILE_NAME = "students.txt"

# Function to add student
def add_student():
    try:
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")

        file = open(FILE_NAME, "a")
        file.write(roll + "," + name + "," + course + "\n")
        file.close()

        print("Student Added Successfully.")
    except Exception:
        print("Error while adding student.")

# Function to view students
def view_students():
    try:
        file = open(FILE_NAME, "r")
        data = file.readlines()
        file.close()

        if len(data) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            for line in data:
                print(line.strip())

    except FileNotFoundError:
        print("No student file found.")

# Function to search student
def search_student():
    try:
        roll = input("Enter Roll Number to Search: ")
        file = open(FILE_NAME, "r")
        found = False

        for line in file:
            if line.startswith(roll + ","):
                print("Record Found:", line.strip())
                found = True

        file.close()

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")

# Function to delete student
def delete_student():
    try:
        roll = input("Enter Roll Number to Delete: ")

        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()

        file = open(FILE_NAME, "w")
        found = False

        for line in records:
            if not line.startswith(roll + ","):
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Student Deleted Successfully.")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")

# Main Program
while True:
    print("\n===== Student Management System =====")
    print("Date & Time:", datetime.datetime.now())
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            delete_student()

        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number.")