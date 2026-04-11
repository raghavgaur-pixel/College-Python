# class Base1(object):
#     def __init__(self):
#         print("Base1 Class")

# class Base2(object):
#     def __init__(self):
#         print("Base2 Class")

# class Derived(Base1, Base2):
#     pass

# D = Derived()

# def add(x,y,z=0):
#     return x+y+z

# print(add(2,3))
# print(add(2,3,4))

# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
    
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")

#     def type(self):
#         print("India is a developing country.")

# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
    
#     def language(self):
#         print("English is the most widely spoken language of USA.")

#     def type(self):
#         print("USA is a developed country.")

# obj_ind = India()
# obj_usa = USA()

# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()

'''Method Overriding'''

# class Parent():
#     def __init__(self):
#         self.value = "Inside Parent"
#     def show(self):
#         print(self.value)

# class Child(Parent):
#     def __init__(self):
#         self.value = "Inside Child"
#     def show(self):
#         print(self.value)

# obj1 = Parent()
# obj2 = Child()

# obj1.show()
# obj2.show()

class Parent():

    def display(self):
        print("Inside Parent")

class Child(Parent):

    def show(self):
        print("Inside Child")

class GrandChild(Child):

    def show(self):
        print("Inside Grand Child")

g = GrandChild()
g.show()
g.display()