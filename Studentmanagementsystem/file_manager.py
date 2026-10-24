import os
from student import Student, GraduateStudent

FILE_NAME = "students.txt"


# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()


# ---------------- Save Student ----------------
def add_student():
    try:
        roll = input("Enter Roll Number: ")

        if search_student(roll, display=False):
            print("Student already exists!")
            return

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")
        specialization = input("Enter Specialization: ")

        student = GraduateStudent(
            roll, name, age, course, marks, specialization
        )

        with open(FILE_NAME, "a") as file:
            file.write(
                f"{student.get_roll_no()},"
                f"{student.name},"
                f"{student.age},"
                f"{student.course},"
                f"{student.marks},"
                f"{student.specialization}\n"
            )

        print("\nStudent Added Successfully!")

    except Exception as e:
        print("Error:", e)


# ---------------- View Students ----------------
def view_students():

    try:

        with open(FILE_NAME, "r") as file:

            data = file.readlines()

            if not data:
                print("\nNo Student Records Found.")
                return

            print("\n========== STUDENT RECORDS ==========")

            for line in data:

                record = line.strip().split(",")

                student = GraduateStudent(
                    record[0],
                    record[1],
                    record[2],
                    record[3],
                    record[4],
                    record[5]
                )

                student.display()

    except Exception as e:
        print("Error:", e)


# ---------------- Search Student ----------------
def search_student(roll=None, display=True):

    if roll is None:
        roll = input("Enter Roll Number: ")

    try:

        with open(FILE_NAME, "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[0] == roll:

                    if display:

                        student = GraduateStudent(
                            data[0],
                            data[1],
                            data[2],
                            data[3],
                            data[4],
                            data[5]
                        )

                        print("\nStudent Found")
                        student.display()

                    return True

        if display:
            print("Student Not Found.")

        return False

    except Exception as e:
        print("Error:", e)


# ---------------- Delete Student ----------------
def delete_student():

    roll = input("Enter Roll Number to Delete: ")

    try:

        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:

            for line in lines:

                if line.startswith(roll + ","):
                    found = True
                    continue

                file.write(line)

        if found:
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found.")

    except Exception as e:
        print("Error:", e)