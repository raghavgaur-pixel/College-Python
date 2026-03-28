'''class ABC():
    class_var = 0
    def __init__(self,var):
        ABC.class_var += 1
        self.var = var
        print("The Object value is : ", var)
        print("The value of class variable is : ", ABC.class_var)

obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)'''

class Sample:
    num = 0
    def __init__(self,var):
        Sample.num+=1
        self.var = var
        print("The Object Value is = ", var)
        print("The count of object created = ", Sample.num)

S1 = Sample(15)
S2 = Sample(35)
S3 = Sample(45)