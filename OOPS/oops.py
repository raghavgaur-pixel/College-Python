'''class ABC:
    var = 10

obj = ABC()
print(obj.var)'''


'''class Sample:
    x,y = 10,20

S = Sample()

print("Value of x = ", S.x)
print("Value of y = ", S.y)
print("Value of x + y = ", S.x+S.y)'''

'''class Student:
    mark1,mark2,mark3 = 45,91,71

    def process(self):
        sum = Student.mark1 + Student.mark2 + Student.mark3
        avg = sum/3

        print("Total Marks = ", sum)
        print("Average Marks = ", avg)

        return
    
S = Student()
S.process()'''

class ABC():
    class_var = 0
    def __init__(self,var):
        ABC.class_var += 1
        self.var = var
        print("The Object value is : ", var)
        print("The value of class variable is : ", ABC.class_var)
    def __del__(self):
        ABC.class_var -= 1
        print("Object with value", self.var, " is going out of scope.")

obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)
del obj1
del obj2
del obj3
