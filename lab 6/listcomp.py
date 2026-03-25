'''cubes = []
for i in range(11):
    cubes.append(i**3)
print(f"Cubes of members from 1-10 : {cubes}")'''

'''num_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in num_list:
    sum += i
print("Sum of elements in the list =", sum)
print("Average of elements in the list =", float(sum/float(len(num_list))))'''

'''num_list = [1,2,3,4,5]
for index,i in enumerate(num_list):
    print(i, "is at index :", index)'''

'''num_list = [1,2,3,4,5]
for i in range(len(num_list)):
    print(f"Index : {i}")'''

'''num_list = [1,2,3,4,5]
it = iter(num_list)
for i in range(len(num_list)):
    print(f"Element at index {i} is {next(it)}")'''

'''def check(x):
    if x % 2 == 0 or x % 4 == 0 :
        return 1
evens = list(filter(check, range(2,22)))
print(evens)'''

'''def add_2(x):
    x += 2
    return x
num_list = [1,2,3,4,5,6,7]
print(f"Original List is : {num_list}")
new_list = list(map(add_2, num_list))
print("Modified list is :", new_list)'''

'''import functools

def add(x,y):
    return x+y

num_list = [1,2,3,4,5]
print(f"Sum of calues in list = {functools.reduce(add, num_list)}")'''

