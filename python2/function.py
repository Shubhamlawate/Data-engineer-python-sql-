# functions

#funnction definition 
# def sum(a,b):#parameters
#     sum=a+b
#     print(sum) #return function

# sum(2,5)


# avge of three numbers 

# def avg(a,b,c):
#     sum=a+b+c
#     print(sum/3)
#     return sum



# avg(345,456,35466)

#function types

#1 type  built function  range(),print().len(),type()
# 2 type user built function



# by defult function
# def mulit(a=1,b=1):
#     mul=a*b
#     print(mul)
#     return mulit
# print(mulit)

# mulit(4,5)

# recursive function also know as  cell stack 

# def show(n):
#     if(n == -6):
#         return
#     print(n)
#     show(n-1)

# show(5)



def fact(n):
    if(n==0 or n==1):
        return 1
    else:
         return n*fact(n-1)
    
t=fact(5)
print(t)