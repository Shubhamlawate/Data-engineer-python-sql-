
# try:
#     num =int(input("Enter num"))
#     print(10/num)
# except ZeroDivisionError:
#     print("zero")
# except  ValueError:
#     print(" above 18")
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program finished.")
