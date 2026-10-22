# Class Definition
class Student:

    # Constructor
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    # Method to display information
    def display_info(self):
        print("Student Name :", self.name)
        print("Roll Number  :", self.roll_no)
        print("Course       :", self.course)
        print("--------------------------")


# Creating objects with different values
student1 = Student("Varsha", 101, "B.Tech CSE")
student2 = Student("Rahul", 102, "BCA")

# Accessing initialized attributes
print("Accessing Attributes:")
print(student1.name)
print(student2.course)
print("--------------------------")

# Displaying object information
student1.display_info()
student2.display_info()