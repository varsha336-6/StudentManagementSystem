from file_manager import (
    add_student,
    view_students,
    search_student,
    delete_student
)


def menu():

    while True:

        print("\n===================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("\nThank You for Using Student Management System!")
            break

        else:
            print("\nInvalid Choice! Please Try Again.")


if __name__ == "__main__":
    menu()