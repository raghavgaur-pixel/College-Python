'''with open("myfile.txt", 'a') as f:
    l = ["NAE NIGGA NAE NAE\n", "NIGGA NIGGA NAE NAE.\n"]
    f.writelines(l)'''

'''with open("myfile.txt", 'rb') as f:
    for line in f:
        print(line)
    
#checking is the file is closed
print(f.closed)'''

'''file = open("myfile.txt", 'rb')
for line in file:
    print(line)

print(f"File is closed ? : {file.closed}")'''

'''with open("myfile.txt", 'r') as file:
    line = file.readline()
    words = line.split()
    print(words)'''

with open("myfile.txt", 'rb') as f:
    print("Position of the file pointer before reading is :", f.tell())
    print(f.read(10))
    print("Position of the file pointer after reading is :", f.tell())
    print("Setting 3 bytes from the current position of file pointer")
    f.seek(3,1)
    print(f.read())
