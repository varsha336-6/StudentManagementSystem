from abc import ABC, abstractmethod

# ---------- Abstraction ----------
class Person(ABC):

    @abstractmethod
    def display(self):
        pass


# ---------- Parent Class ----------
class Student(Person):

    def __init__(self, roll_no, name, age, course, marks):
        self.__roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = int(marks)

    # Getter
    def get_roll_no(self):
        return self.__roll_no

    # Setter
    def set_roll_no(self, roll):
        self.__roll_no = roll

    # Calculate Grade
    def calculate_grade(self):

        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    # Polymorphism
    def display(self):
        print("\n----------------------------")
        print("Roll No :", self.__roll_no)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Course  :", self.course)
        print("Marks   :", self.marks)
        print("Grade   :", self.calculate_grade())
        print("----------------------------")


# ---------- Inheritance ----------
class GraduateStudent(Student):

    def __init__(self, roll_no, name, age, course, marks, specialization):
        super().__init__(roll_no, name, age, course, marks)
        self.specialization = specialization

    # ---------- Method Overriding ----------
    def display(self):
    super().display()
    print("Specialization :", self.specialization)
    print("----------------------------")