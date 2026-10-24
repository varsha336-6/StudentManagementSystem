from abc import ABC, abstractmethod

# ---------- Abstraction ----------
class Person(ABC):

    @abstractmethod
    def display(self):
        pass


# ---------- Parent Class ----------
class Student(Person):

    def __init__(self, roll_no, name, age, course, marks):
        self.__roll_no = roll_no        # Encapsulation
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    # Getter
    def get_roll_no(self):
        return self.__roll_no

    # Setter
    def set_roll_no(self, roll):
        self.__roll_no = roll

    # ---------- Polymorphism ----------
    def display(self):
        print("\n----------------------------")
        print("Roll No :", self.__roll_no)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Course  :", self.course)
        print("Marks   :", self.marks)
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