'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")
    
class Teacher(Person):
    def __init__(self, name, age, exp, r_area):
        Person.__init__(self, name, age)
        self.exp = exp
        self.r_area = r_area
    def displayData(self):
        Person.display(self)
        print(f"Experience: {self.exp}\nResearch Area: {self.r_area}")

class Student(Person):
    def __init__(self, name, age, course, marks):
        Person.__init__(self, name, age)
        self.course = course
        self.marks = marks
    def displayData(self):
        Person.display(self)
        print(f"Course: {self.course}\nMarks: {self.marks}")


print("Teacher Deatils: ")
T = Teacher("Jaya", 43, 20, "Recommender Systems")
T.displayData()

print("Students Details: ")
S = Student("Mani", 20, "B.Tech", 78)
S.displayData()'''


class Parent:
    def __init__(self, txt):
        self.message = txt
    
    def printmessage(self):
        print(self.message)

class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)

x = Child("Hello, and welcome!")
x.printmessage()