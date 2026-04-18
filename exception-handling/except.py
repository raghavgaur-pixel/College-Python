'''try:
    num = int(input("Enter the number : "))
    print(num**2)
except (KeyboardInterrupt, ValueError, TypeError):
    print("Please check before you enter............. Program Terminating")
print("Bye!")'''

'''import sys


try:
    file = pen('File1.txt')
    str = f.readline()
    print(str)
except IOError:
    print("Error occured during input.")
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected Error:", sys.exc_info()[0])'''

'''try:
    file = open('File1.txt')
    str = file.readline()
    print(str)

except IOError:
    print("Error occurred during Input.")
else:
    print("Program Terminating Succesfully")'''

'''try:
    file = open('File1.txt')
    str = file.readline()
    print(str)
except:
    print("Error occured")
else:
    print("Program Terminating Succesfully")'''

'''try:
    num = 10
    print(num)
    raise ValueError
except ValueError:
    print("Value Error Occured")'''

def Divide(num, den):
    try:
        quo = num/den
        print("The quotient is", quo)
    except ZeroDivisionError:
        print("You cannot divide a number by zero.")

Divide(10,0)