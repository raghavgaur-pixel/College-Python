'''class ABC():
    def __init__(self,val):
        print("In class method....")
        self.val = val
        print("The value is : ", val)

ob = ABC(10)'''


class Sample:
    def __init__(self, num):
        print("Constructor of class Sample...")
        self.num = num
        print("The value is: ", num)
S = Sample(10)