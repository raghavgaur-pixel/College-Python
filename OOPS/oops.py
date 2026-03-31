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

'''class ABC():
    class_var = 0
    def __init__(self,var):
        ABC.class_var += 1
        self.var = var
        print("The Object value is :", var)
        print("The value of class variable is : ", ABC.class_var)
    def __del__(self):
        ABC.class_var -= 1
        print("Object with value", self.var, " is going out of scope.")

obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)
del obj1
del obj2
del obj3'''

'''class Sample:
    num = 0
    def __init__(self,var):
        Sample.num+=1
        self.var = var
        print("The Object Value is =", var)
        print("The value of class variable is =", Sample.num)
    def __del__(self):
        Sample.num-=1
        print("Object with value", self.var, "is going out of scope.")

S1 = Sample(15)
S2 = Sample(35)
S3 = Sample(45)'''

class ABC():
    def __init__(self, name, var):
        self.name = name
        self.var = var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self, obj):
        return self.var - obj.var
    
obj = ABC("abcdef", 10)
print("The value stored in object is :", repr(obj))
print("The length of the name stored in object is :", len(obj))
obj1 = ABC("ghijkl", 1)
val = obj.__cmp__(obj1)
if val == 0:
    print("Both values are equal")
elif val == -1:
    print("First value is less than second")
else:
    print("The second value is less than first")