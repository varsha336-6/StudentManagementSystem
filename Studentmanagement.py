import os

FILE_NAME = "students.txt"

# Load students from file
def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    students.append(data)
    return students

# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(",".join(student) + "\n")

# Add student
def add_student(students):
    roll = input("Enter Roll Number: ")

    for student in students:
        if student[0] == roll:
            print("Student already exists!")
            return

    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    students.append([roll, name, course, marks])
    save_students(students)
    print("Student added successfully!")

# View students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 50)
    for student in students:
        print(f"Roll: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Course: {student[2]}")
        print(f"Marks: {student[3]}")
        print("-" * 50)

# Search student
def search_student(students):
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student[0] == roll:
            print("\nStudent Found")
            print(f"Roll: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Course: {student[2]}")
            print(f"Marks: {student[3]}")
            return

    print("Student not found.")

# Update student
def update_student(students):
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student[0] == roll:
            student[1] = input("Enter New Name: ")
            student[2] = input("Enter New Course: ")
            student[3] = input("Enter New Marks: ")

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")

# Delete student
def delete_student(students):
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student[0] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")

# Main program
students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students)

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice! Please try again.")
