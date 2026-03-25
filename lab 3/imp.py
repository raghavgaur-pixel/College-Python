'''def func(name, *fav_subjects):
    print(f"\n{name} likes to read :- ")
    for subject in fav_subjects:
        print(subject, end=" ")

func("Goransh", "Mathematics", "Android Programming")
func("Richa", "C", "Data Structures", "Design and Analysis of Algorithms")
func("Krish")'''

'''def func(*kids):
    print(f"The youngest child is {kids[2]}")

func("Emil", "Tobias", "Linus")'''

'''def func(**kid):
    print(f"His last name is {kid['lname']}")

func(fname="Tobias", lname="Refsnes")'''

'''def display(name, course = "BTech"):
    print(f"Name : {name}\nCourse : {course}")

display(course = "BCA", name = "Arav")
display(name='Reyansh')'''

'''def func(country = "Norway"):
    print(f"I am from {country}")

func("Sweden")
func("India")
func()
func("Brazil")'''

'''def func(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
func(fruits)'''

'''sum = lambda x, y : x + y
print(f"Sum = {sum(3,5)}")

x = lambda a : a + 10
print(x(5))'''


'''x = lambda a, b : a * b
print(f"Product = {x(5,6)}")'''

'''x = lambda a,b,c : a + b + c
print(f"Sum = {x(5,6,2)}")'''

'''def func(n):
    return lambda a : a - n

x = func(2)
print(x(5))'''

'''str1 = "GeeksforGeeks"

# lambda returns a function object
rev_upper = lambda s : s.upper()[::-1]
print(rev_upper(str1))'''



'''def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
x = fact(3)
print(x)'''

'''def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)'''

'''def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter a number : "))
print(f"Factorial of {n} is {fact(n)}")'''

import rg

rg.welcome("Raghav Gaur")