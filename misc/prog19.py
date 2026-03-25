'''fruit1 = input("Enter the name of the first fruit: ")
fruit2 = input("Enter the name of the second fruit: ")

if fruit1 < fruit2:
    print(f"{fruit1} comes before {fruit2} in the dictionary.")
elif fruit1 > fruit2:
    print(f"{fruit1} comes after {fruit2} in the dictionary.")
else:
    print(f"{fruit1} and {fruit2} are the same.")'''


"""str1 = "Geek"
str2 = "Geek"
str3 = str1

print("ID of str1 =", hex(id(str1)))
print("ID of str2 =", hex(id(str2)))
print("ID of str3 =", hex(id(str3)))
print(str1 is str1)
print(str1 is str2)
print(str1 is str3)

str1+="s"
str4="Geeks"

print("\nID of changed str1 =", hex(id(str1)))
print("ID of str4 =", hex(id(str4)))
print(str1 is str4)"""

'''string1 = "Abrar"
string2 = "Ahmed"
string3 = "ABCD"
string4 = "ABCD"
if string1 <= string2:
    print(f"{string1} is smaller, {string2} is greater")
if string2 >= string4:
    print(f"{string4} is smaller, {string2} is greater")
if string3 == string4:
    print(f"{string3} is equal to {string4}")
if string1 != string3:
    print(f"{string1} is not equal to {string3}")'''

s1 = 'String'
s2 = 'String'
s3 = 'String'

if s1 == s2:
    print("s1 and s2 are equal")

if s1.__eq__(s2):
    print("s1 and s2 are equal")