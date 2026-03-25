a = 5
b = 1

ret = ((a<=b) or (a!=b))
print("Return value of first expression is:", ret)

ret = ((a<b) and (a==b))
print("Return value of second expression is:", ret)

ret = not ((a<b) and (a==b))
print("Return value of third expression is:", ret)