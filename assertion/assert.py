c = int(input("Enter the temperature in Clecius: "))
f = (c*9/5)+32
assert(f<=32), "Its freezing outside"
print("Temperature in Fahrenheit is : ",f)