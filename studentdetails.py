#You are given a class Student having attributes as name and age and a display method. Here, an object of student class with given name and age is created. This code uses display method to print information of the Student.

class Student:
    def __init__(self):
        self.name = ""
        self.age = 0

    def display(self):
        print(f"{self.name} {self.age}")

s = Student()
s.name, s.age = input().split()
s.display()
