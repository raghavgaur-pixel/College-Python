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

class Student:
    mark1,mark2,mark3 = 45,91,71

    def process(self):
        sum = Student.mark1 + Student.mark2 + Student.mark3
        avg = sum/3

        print("Total Marks = ", sum)
        print("Average Marks = ", avg)

        return
    
S = Student()
S.process()