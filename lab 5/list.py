'''l1 = [3,4,6,7]
l1.append(70)
print(l1)

A = [100,90,80,50]
l1.extend(A)
print(l1)'''


'''l = [1,'a',"abc",[2,3,4,5],8.9]
i = 0
while i<(len(l)):
    print("l["+str(i)+"] = ", l[i])
    i+=1'''

'''L = ['a','b',['cc','dd',['eee','fff']],'g','h']
print(L[2])
print(L[2][2])
print(L[2][2][0])'''

'''L = ['a', ['bb','cc'],'d']
L[1][1] = 0
print(L)
L[1].insert(0,'xx')
print(L)

L[1].extend([1,2,3])
print(L)

x = L[1].pop(1)
print(L)
print(x)

del L[1][1]
print(L)

L[1].remove('xx')
print(L)

print(len(L))
print(len(L[1]))'''

'''L = [[1,2,3], [4,5,6], [7,8,9]]
for list in L:
    for number in list:
        print(number, end = ' ')'''

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list1
print("list1 is: ", list1)
print("list2 is: ", list2)
list3 = list1[2:6]
print("list3 is: ", list3)