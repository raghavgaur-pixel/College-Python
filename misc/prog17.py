'''num = int(input("Enter any number from 0-30: "))

if num>=0 and num<10:
    print("It is in range 0-10")
elif num>=10 and num<20:
    print("It is in range 10-20")
elif num>=20 and num<30:
    print("It is in the range 20-30")
else:
    print("Out of range")'''

'''num = int(input("Enter any number: "))
if num==0:
    print("The number is zero")
elif num>0:
    print("The number is positive")
else:
    print("The number is negative")'''

'''score = int(input("Enter your score: "))

if score>=90 and score<=100:
    print("Grade S")
elif score>=80 and score<90:
    print("Grade A")
elif score>=70 and score<80:
    print("Grade B")
elif score>=60 and score<70:
    print("Grade C")
elif score>=50 and score<60:
    print("Grade D")
elif score>=40 and score<50:
    print("Grade E")
elif score<40:
    print("Grade U")
else:
    print("Invalid Marks, please provide between the range!")'''

'''a = 33
b = 200
if b>a:
    print("b is greater than a")'''


'''a = 33
b = 33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")'''

'''a = 200
b = 22
if b>a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")'''

'''a = 5
b = 1
if a>b: print("a is greater than b")'''

'''a = 200
b = 33
c = 500
if a>b and c>a:
    print("Both conditions are true")'''

'''x = 14
if x > 10:
    print("Above 10")
    if x>20:
        print("and also above 20, wild stuff gang")
    else:
        print("dissapointment, it ain't above 20")'''


'''a = 2
b = 330
print("A") if a>b else print("B")'''

'''a = 200
b = 33
c = 500
if a>b or a>c:
    print("Are bhai, har jagah a kaise jeet jaata hai")'''

'''i = 0
while i<=10:
    print(i, end=' ')
    i = i+1'''

'''a,b = 0,1
while a<1000:
    print(a, end=' ')
    a,b = b, a+b'''

'''i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i+=1'''

'''i = 1
while i<6:
    print(i)
    i+=1'''

'''i = 0
while i<6:
    i+=1
    if i == 3:
        continue
    print(i)'''

'''i = 1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")'''

'''for i in range(1,5):
    print(i, end=" ")'''

'''for i in range(1,10,2):
    print(i, end=" ")'''

# Counter Controlled
'''i = 0
while i<=10:
    print(i, end=' ')
    i+=1'''

# Condition Controlled
'''i = 1
while i>0:
    print(i, end=" ")
    i+=1
    if i == 10:
        break'''

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)'''

'''for x in "banana":
    print(x)'''

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break'''

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)'''

'''for index in range(5):
    print(index+1)'''

'''sum = 0
for num in range(101):
    sum+=num

print(sum)'''


'''for i in range(5):
    print()
    for j in range(10):
        print("*", end='')'''


'''for j in range(-4,0,1):
    a = " "
    print(a*(-j)+(int((j+5))*"*"))'''

'''for letter in "HELLO":
    print(letter, end=' ')
print("Done")

i = 10
while i<0:
    print(i)
    i-=1
else:
    print(i,"is not negative so loop did not execute")'''

mfirst="save earth"
print(mfirst)

print(mfirst[0])
print(mfirst[3])
print(mfirst[-1])
print(mfirst[-3])
print(mfirst[1:3])