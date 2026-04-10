try:
    num = int(input("Enter a number : "))
    print(num**2)
except (KeyboardInterrupt):
    print("You should have entered a number......... Program Terminating")
except (ValueError):
    print("Please check before you enter............ Program Terminating")
else:
    print("Executed without any error!")
print("Bye")