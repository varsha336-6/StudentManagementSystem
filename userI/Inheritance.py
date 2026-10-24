# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name :", self.name)
        print("Age  :", self.age)


# Child Class
class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display_person()      # Inherited method
        print("Course :", self.course)
        print("------------------------")


# Creating Objects
student1 = Student("Varsha", 20, "B.Tech CSE")
student2 = Student("Rahul", 21, "BCA")

# Display Information
student1.display_student()
student2.display_student()