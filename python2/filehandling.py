# read file 
# file = open(r"C:\Users\Asus\OneDrive\Desktop\python\Data-engineer-python-sql-\python2\data.txt","r")

# data = file.read()
# print(data)
# file.close()

# file = open(r"C:\Users\Asus\OneDrive\Desktop\python\Data-engineer-python-sql-\python2\demo.txt","r")
# print(file.read())
# file.close()

# print(file.readline())
# file.close()

# print(file.readlines())
# file.close()

# write function

# file = open(r"C:\Users\Asus\OneDrive\Desktop\python\Data-engineer-python-sql-\python2\data.txt","w")

# file.write("hello karan")
# file.close()

#append to file

# file = open(r"C:\Users\Asus\OneDrive\Desktop\python\Data-engineer-python-sql-\python2\demo.txt","a")

# file.write("\nwelcome to file handling")

# file.close()

#with  statment

# with open(r"C:\Users\Asus\OneDrive\Desktop\python\Data-engineer-python-sql-\python2\demo.txt","r") as file:
#     print(file.read())

# with open(r"C:\Users\Asus\OneDrive\Desktop\python\Data-engineer-python-sql-\python2\data.txt","w") as file:
#     file.write("hello shubham ! welcome to python learning")


# CREATING NEW FILE
# file = open("newfile.txt","x")
# file.close()

#check file is exist

# import os
# if os.path.exists("newfile.txt"):
#     print("file exixting")
# else:
#     print("file is not existing")

# Deleting the file

# import os
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
#     print("file is deleting")
# else:
#     print("file is not found")

# file read by line by line

with open("C:\Users\Asus\OneDrive\Desktop\python\ newfile.txt","r") as file:
    for line in file:
        print(line.strip())