import re

'''txt = "The rain in Spain"

x = re.findall("[a-m]", txt)
print(x)'''

'''txt = "hello planet"

x = re.findall("he..o", txt)
print(x)'''

'''txt = "hello planet"

x = re.findall("planet$", txt)
if x:
    print("Yes the string ends with 'planet'")
else:
    print("No Match")'''

'''txt = "That will be 59 dollars"

x = re.findall("\\d", txt)
print(x)'''

'''txt = "hello planet"

x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No Match")'''

'''txt = "hello planet"

x = re.findall("he.*o", txt)
print(x)'''

'''txt = "hello planet"

x = re.findall("he.+o", txt)
print(x)'''

'''txt = "hello planet"

x = re.findall("he.?o", txt)
print(x)'''

'''txt = "hello planet"

x = re.findall("he.{2}o", txt)
print(x)'''

'''txt = "The rain is Spain falls mains in the plain!"

x = re.findall("falls|stays", txt)
print(x)

if x:
    print("Yes, there is atleast one match!")
else:
    print("No Match")'''

'''txt = "The rain in Spain"

x = re.findall("\\AThe", txt)
print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")'''

'''txt = "The rain in Spain"
x = re.findall(r"\bain", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No Match")'''

txt = "The rain in Spain"

'''x = re.findall(r"ain\b", txt)
print(x)

if x:
    print("Yes, there is atleast one match!")
else:
    print("No Match")'''

'''x = re.findall(r"\\Bain", txt)
print(x)

if x:
    print("Yes, there is atleast one match!")
else:
    print("No Match")'''

'''x = re.findall(r"ain\\B", txt)
print(x)

if x:
    print("Yes, there is atleast one match!")
else:
    print("No match")'''

'''x = re.findall("\\d", txt)
if x:
    print("Yes, there is atleast one match!")
else:
    print("No Match")'''

'''x = re.findall("\\D", txt)
print(x)
if x:
    print("Yes, there is atleast one match!")
else:
    print("No Match Found")'''

'''x = re.findall("\\s", txt)
print(x)
if x:
    print("Yes, there is atleast 1 match!")
else:
    print("No match")'''

'''x = re.findall("\\S", txt)
print(x)

if x:
    print("Yes, atleast 1 match was found!")
else:
    print("No match")'''

'''x = re.findall("\\w", txt)
print(x)
if x:
    print("Yes, atleast 1 match is found!")
else:
    print("No match found")'''

'''x = re.findall("\\W", txt)
print(x)
if x:
    print("Match found!")
else:
    print("No match found")'''

'''x = re.findall("Spain\\Z", txt)
print(x)
if x:
    print("Match Found!")
else:
    print("No match found!")'''

string = "She sells see shells on the sea shore"
'''pattern1 = "sells"
if re.match(pattern1, string):
    print("Match Found!")
else:
    print(pattern1, "is not present in the string")
pattern2 = "She"
if re.match(pattern2, string):
    print("Match Found!")
else:
    print(pattern2, "is not present in the string")'''

'''pattern = "sells"
if re.search(pattern, string):
    print("Match Found!")
else:
    print(pattern, "is not present in the string.")'''