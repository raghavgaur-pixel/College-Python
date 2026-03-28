class Odd_Even:
    even = 0
    
    def check(self,num):
        if num%2 == 0:
            print(num, "is Even number")
        else:
            print(num, "is Odd Number")
        
n = Odd_Even()
x = int(input("Enter a value: "))
n.check(x)        