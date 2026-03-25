with open("myfile.txt", 'r') as f:
    l = f.readlines()
    mini = len(l[0])
    foundlower = False
    for i in range(len(l)):
        if len(l[i]) < mini:
            mini = len(l[i])
        else:
            continue
        if foundlower == True:
            print("The shortest line is: ", l[i])
    if foundlower == False:
        print("The shortest line is: ", l[0])