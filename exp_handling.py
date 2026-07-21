
try:
    num =int(input("Enter num"))
    print(10/num)
except ZeroDivisionError:
    print("zero")
except  ValueError:
    print(" above 18")
