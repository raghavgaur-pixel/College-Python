'''def diff(x,y): # function header
    return x-y # function body

a = 20
b = 10
operation = diff # function name assigned to a variable
print(f"The difference would be of {operation(a,b)}") # function called using variable name'''

# ============================================================================================

'''def my_function():
    print("Hello from a function")

my_function()'''

# ============================================================================================

'''def my_function(fname):
    print(f"{fname} Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")'''

# ============================================================================================

'''def my_func(fname, lname):
    print(f"{fname} {lname}")

my_func("Emil", "Refsnes")'''

# ============================================================================================

'''def func():
    for i in range(4):
        print("Hello World")

func()'''

# ============================================================================================

'''def func(i):
    print("Hello World", i)
func(5+2*3)'''

# ============================================================================================

'''def func(i):
    print("Hello World", i)
j = 10
func(j)'''

# ============================================================================================

'''def total(a,b):
    result = a+b
    print(f"Sum of {a} and {b} = {result}")

a = int(input("Enter Num 1 : "))
b = int(input("Enter Num 2 : "))
total(a,b)'''

# ============================================================================================

'''def sum(a,b=10):
    return(a+b)

print(sum(10))'''

# ============================================================================================

'''num1 = 10
print(f"Global Variable num1 = {num1}")

def func(num2):
    print(f"In Function - Local Variable num2 = {num2}")
    num3 = 30
    print(f"In Function - Local Variable num3 = {num3}")


func(20)
print(f"Num1 again = {num1}")

# print(f"num3 outside function = {num3}")'''

# ============================================================================================

'''var = "Good"
def show():
    global var1
    var1 = "Morning"
    print(f"In function var is - {var}")
show()
print(f"Outside function, var1 is - {var1}")
print(f"Var is - {var}")'''

# ============================================================================================

'''def cube(x):
    return(x**3)

num = 10
result = cube(num)
print(f"Cube of {num} = {result}")'''

# ============================================================================================

'''def func(x):
    return 5*x

print(func(3))
print(func(5))
print(func(9))'''

# ============================================================================================

'''def display():
    print("Hello")      # ERROR - TypeError: display() takes 0 positional arguments but 1 was given
display("HI")'''

# ============================================================================================

'''def display(str):
    print(str)          # ERROR - TypeError: display() missing 1 required positional argument: 'str'
display()'''

# ============================================================================================

'''def display(str):
    print(str)
str = "Hello"
display(str)'''

# ============================================================================================

'''def display(str, int_x, float_y):
    print(f"The string is : {str}", end = '\t')
    print(f"The Integer Value is : {int_x}", end = '\t')
    print(f"The floating point value is : {float_y}", end = '\t')
display(float_y = 56789.045, str = "Hello Raghav", int_x = 1234)'''

# ============================================================================================

def func(child3, child2, child1):
    print(f"The youngest child is {child3}")
    print(f"The kid with maximum aura is {child2}")

func(child1="Emil", child2 = "Raghav", child3 = "Linus")