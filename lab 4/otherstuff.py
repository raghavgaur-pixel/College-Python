'''list_a = [1,2,3,4,5]
print(list_a)

list_c = ["Good", "Going"]
print(list_c)

list_b = ['A', 'b', 'C', 'd', 'E']
print(list_b)

list_d = [1,'a', "bcd"]
print(list_d)

l = [1,2,3,4,5,6]
l5 = l [0:2]

print(l5)

S = [x**2 for x in range(10)]
print(S)

A = [3,4,5]
B = [value*3 for value in A]
print(B)

B = []
for i in A:
    B.append(i*3)
print(B)

C = [i for i in S if i%2 == 0]
print(C)

l = list()
print(l)

A=B=[10,20,30]
print(A,B)

num_list = [1,2,3,4,5,6,7,8,9,10]
print("num_list is: ", num_list)
print(f"First element in the list is {num_list[0]}")
print(f"num_list[2:5] = {num_list[2:5]}")
print(f"num_list[::2] = {num_list[::2]}")
print(f"num_list[1::3] = {num_list[1::3]}")

l2 = ["Delhi", "Chennai", "Mumbai"]
print(l2[0:2])

list = [10,20,30,40,50,60]
print(list[::2])
print(list[4:])

print(list[:3])
print(list[:])
print(list[-1])

i = 0
while i<4:
    print(list[i], end = ' ')
    i+=1

for i in list:
    print(i, end = ' ')

i = 0
while i<len(list):
    print(list[i])
    i+=1

i = 0
L = len(list)
while i<L:
    print(list[i], end = ' ')
    i+=1'''

num_list = [1,2,3,4,5,6,7,8,9,10]
print(f"List is : {num_list}")
num_list[5] = 100
print("List after updation is :", num_list)
num_list.append(200)
print("List after appending a value is : ", num_list)
del num_list[3]
print("List after deleting a value is : ", num_list)