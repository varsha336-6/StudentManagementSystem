# Class Definition
class Student:

    # Constructor
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    # Method to display student information
    def display_info(self):
        print("Student Name :", self.name)
        print("Roll Number  :", self.roll_no)
        print("Course       :", self.course)
        print("--------------------------")


# Creating Objects
student1 = Student("Varsha", 101, "B.Tech CSE")
student2 = Student("Rahul", 102, "BCA")

# Displaying Information
student1.display_info()
student2.display_info()