#class and objects

# note the object from class
#befor object creat class and pass
# class Student:
#     name="shubh"
#     age=20
#     college="vcet"

# s1 = Student()
# s2 = Student()

# print(s1.name )
# print(s2.age)

#construtor init
#syntax
# class Boy:
#     def __init__(self):
#         pass

# class Student:
#     def __init__(self):
#         print("self construtor")

# s1 =Student()
# S2 =Student()

# key word pass
# class Student:
#     def __init__(self,name):
#         self.name=name

# S1 = Student("shubh")
# print(S1.name)
# s1=Student("karan")
# print(s1.name)

#Instance Attribute
# class car:
#     def __init__(self,name,brand):
#         self.name=name
#         self.brand=brand

# c1=car("tr","tata") # object
# c2=car("yt","mahendra")
 
# print(c1.name)
# print(c2.name)

# # class atriburt
# class student:
#     college ="vcet college"
#     def __init__(self,name):
#         self.name=name
# s1=student("karan")   # object
# print(s1.college) 

#Instance Method
# class student:
#     def __init__(self,name):
#         self.name=name

#     def display(self):
#         print("name:",self.name)



# s2 = student( "shu")
# s2.display()

#type of method 
#1 instance method

# class demo:
#     def self(self):
#         print("instnces method")

# d1=demo()
# d1.self()
     
#2 staticmethod

# class demo:

#      @staticmethod
#      def add(a,b):
#         return a+b
# print(demo.add(12,34))

#Four Pillars of OOP

#encapsulation

# class bank:
#     def __init__(self,balnace):
#         self.balnace=balnace

#     def deposit(self,amount):
#         self.balnace+=amount
#     def show(self):
#         print(self.balnace)
# b =bank(1000)
# b.deposit(1000)
# b.show()

#abstraction
# from abc import ABC ,abstractmethod

# class Animal(ABC):
    
     # @abtractmethod
#     def sound(self):
#         pass

# class dog(Animal):
#     print("bark")

# d=dog()
# d.sound()

#inheritance  ( Single inheirtance)

# class Animal:
#     def sound(self):
#         print("Animal")
# class dog(Animal):
      
#         pass
# d = dog()
# d.sound()
#

# maltiple inhertance

# class father:
#     def manoy(self):
#         print("protic")
# class mather:
#     def love(self):
#         print("lovely")
# class child(father,mather):
#     pass
# f = child()
# f.manoy()
# f.love()

# maltilevel inhertance

# class grandfther:
#     def land(self):
#         print("land property")
# class father(grandfther):
#     def home(self):
#         print("home")
# class sun(father):
#     pass

# p = sun()
# p.land()
# p.home()

#Hierarchical Inheritance

# class father:
#     def home(self):
#         print("home father")
# class sun(father):
#     pass
# class daughter(father):
#     pass
# f =sun()
# m=daughter()

# f.home()
# m.home()
# method overriderng


# class Animal:
#     def sound(self):
#         print("Animal")
    
# class dog(Animal):
#     def sound(self):
#         print("bark")

# d=dog()
# d.sound()
# super( )method
# class parent:
#     def __init__(self):
#         print("conscter")
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("childconsscters")
# p=child()# polymorphism
#runtime overrideng
# class brid:
#     def fty(self):
#         print("good")
# class superd(brid):
#     def fty(self):
#         print("runtime override")

# b =superd()
# b.fty()

# dock typing
# class dog:
#     def speek(self):
#         print("bhooooooooo")
# class cat:
#     def speek(self):
#         print("meauuuuuuuuuuuuu")
# def maek_sound(Animal):
#      Animal.speek()

# maek_sound(dog())
# maek_sound(cat())

#opreter overloading

# class number:

#     def __init__(self,value):
#         self.value=value
    
#     def __add__(self,other):
#         return self.value + other.value
# n1 =number(123)
# n2 =number(234)
# print(n1+n2)

#Composition ("Has-A" Relationship)

# Composition means one class contains an object of another class.

# class Engine:
#     def start(self):
#          print("start engine")

# class car:
#     def __init__(self):
#           self.engine =Engine()
    
#     def drive(self):
#          self.engine.start()
#          print("car drived")

# car =car()
# car.drive()
    

    
