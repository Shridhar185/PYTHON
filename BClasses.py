#Python does not have built-in support for Arrays, but Python Lists can be used instead.
#array methods____________________________________________
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
#__________________________________________________________






# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# #To create a class, use the keyword class:
# class Myclass:
#     x=10
# #creating an object 
# obj=Myclass()
# print(obj.x)



#The __init__() Function it is built in 
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties
#__init__ is a special method also known as a constructor. 
#These special methods are identified by their names, which start and end with double underscores 
#self can be named anything instead of self we can write any word

# class Person:
#     def __init__(self,name,age):            #constructor method
#         self.name=name                      #self parameter is a reference to the current instance of the class, 
#         self.age=age                        #self is used to access variables that belong to the class.
# p1=Person("ram",25)
# print(p1.name)
# print(p1.age)
# print(p1)
#the above line prints the default string representation of the object, which includes the class name and its memory address. 
#to print desired string representation use the __str__ method



#__________  __str__  method_________________________________
#__str__ method in the class to return the desired string representation. H
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"name:{self.name} age:{self.age}"
# p1 = Person("John", 36)
# print(p1)



#the methods in class are 2 types--> instance(object) method and class method
#Methods are functions that are defined within a class and are associated with objects (instances) of that class.

#Object Methods_________________________________________________________
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):            
#        print(f"name:{self.name} age:{self.age}")
# #creaating instance to call method
# p1=Person("ram",25)                
# p1.show()
# #modify object properties
# p1.age=30
# p1.show()

# #delete object properties
# del p1.age
# #delete object 
# del p1

 

#static method_____________________________________________
#the @staticmethod indicates that it not require any instance to access
#a static method is not an object method.
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):            
#        print(f"name:{self.name} age:{self.age}")
#     @staticmethod
#     def disp():
#         print("the function is executed")
# #invoking the disp() static method of the Person class directly. 
# Person.disp()

 

#class method________________________________________________
#defined using the @classmethod decorator.
#it  receive the class itself as the first parameter, conventionally named cls.
# class calc:
#     @classmethod
#     def add(cls,x,y):
#         return x+y
# #Calling class methods without creating instances
# print(calc.add(10,20))




#The pass Statement
#if no content in class just print pass
class Person:
    pass




#_______________________________Inheritance______________________________
#there are 4 types inheritance in python 
#sinlge inheritance:Single inheritance involves a subclass inheriting from a single superclass.
#multiple inheritance:The subclass inherits attributes and methods from all the superclasses.
#Multilevel Inheritance:A subclass inherits from a superclass, and another subclass inherits from the first subclass, forming a hierarchy.
#Hierarchical Inheritance:involves multiple subclasses inheriting from a single superclass.

#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#A parent class is a class that serves as a blueprint or template for other classes.
#A child class is a class that inherits attributes and methods from its parent class.

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print("person: ",self.firstname, self.lastname)

# class Student(Person):
#   def stuinfo(self):
#     print("student:",self.firstname,self.lastname)

# # Call the __init__ method of the parent class. if we dont call parent init method then we can pass only age
# class Student2(Person):
#   def __init__(self,fname,lname,age):
#     Person.__init__(self,fname,lname)
#     self.age=age
#   def stuinfo(self):
#     print("student2: ",self.firstname,self.lastname,self.age)

# #while using super() function don't need to pass self explicitly as an argument. 
# class Student3(Person):
#   def __init__(self,fname,lname,email):
#     super().__init__(fname,lname)
#     self.email=email
#   def stuinfo(self):
#     print("student3: ",self.firstname,self.lastname,self.email)
  
# x = Person("John", "Doe")
# x.printname()

# #from child object we can call both both parent and child method
# y = Student("Mike", "Olsen")
# y.printname()
# y.stuinfo()

# #another child add extra object property
# z=Student2("ram","ravan",30)
# z.stuinfo()

# a=Student3("shridhar","shridh","shri@hfht")
# a.stuinfo()




# import random 
# class Die:
#     def __init__(self):
#         self.value=1
#     def roll(self):
#         self.value=random.randrange(1,7)
# d=Die()
# count=int(input("enter no of dice to roll: "))
# for i in range(count):
#     d.roll()
#     print(f"dice {i+1}: {d.value}")








# import random 
# class Die:
#     def __init__(self):
#         self.value=1
#     def roll(self):
#         self.value=random.randrange(1,7)
# class Dice:
#     def __init__(self):
#         self.mylist=[]
#     def addroll(self,d):
#         d.roll()
#         self.mylist.append(d.value)
# #creating Die object
# d=Die()
# #creating Dice object  
# dc=Dice()
# count=int(input("enter no of dice to roll: "))

# #print as list all dice values
# for i in range(count):
#     dc.addroll(d)           #passing die object as argument
# print(dc.mylist)
 







#_______________________________iterators___________________________________
#An iterator is an object that contains a countable number of values.
#All these objects have a iter() method which is used to get an iterator:

#Return an iterator from a tuple, and print each value:
#looping through each item 
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(myit)             #<tuple_iterator object at 0x0000021AC70F18A0>


#Even strings are iterable objects, and can return an iterator:
#looping through each character using iter() method
# mystr = "banana"
# myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(myit)             #<str_ascii_iterator object at 0x00000286FA8FFF40>







#__iter__   and    __next__   methods in classes

# class dept:
#     def __init__(self):
#         self.list=[]
#     def addname(self,name):
#         self.list.append(name)
# d=dept()
# d.addname("ram")
# d.addname("raj")
# d.addname("ravan")
# for n in d.list:    #list is iteratable but instance of object is not iterable
#     print(n)  
            
    
    
#in above if we use it as (for n in d) then it shows that dept object is not iteratable 
#so to make it as iteratable we use iter and next methods
#iter just do start index as -1
#next method will keep on increasing the index,so you should provide break for it

#To prevent the iteration from going on forever, we can use the StopIteration statement.
#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done

# class dept:
#     def __init__(self):
#         self.list=[]
#     def addname(self,name):
#         self.list.append(name)
#     def __iter__(self):
#         self.index=-1
#         return self
#     def __next__(self):
#         if self.index >=len(self.list)-1:
#             raise StopIteration
#         self.index+=1
#         return self.list[self.index]
# d=dept()
# d.addname("ram")
# d.addname("raj")
# d.addname("ravan")
# for n in d:        
#     print(n) 
              







#__________________________encapsulation_____________________________
#Encapsulation restricts direct access to some of an object's components from outside the class and provides controlled access through methods, ensuring data integrity and enhancing security.
#to make attributes private use (__value=2)

# import random
# class Die:
#     def __init__(self):
#         self.__value=1
#     def getvalue(self):  # by this we can access the private value
#         return self.__value
#     def setvalue(self,value):  #by passing value here we can change value by outside
#         self.__value=value
# d=Die()
# #d.__value=10          #it doesn't actually change the __value attribute of the Die class; instead, it creates a new attribute __value specific to the d instance.
# #print(d.__value)      #without above line if you print this give attribute error-->'Die' object has no attribute '__value'
# #......to access and modify modify private value get and set methods
# print("current value: ",d.getvalue())
# d.setvalue(10)
# print("modified value: ",d.getvalue())






#encapsulation by public properties

# import random
# class Die:
#     def __init__(self):                 #constructor
#         self.__value=1
#     @property
#     def vaalue(self):   
#         return self.__value
#     @vaalue.setter                      #it is above property setter
#     def value1(self,newvalue):  
#         self.__value=newvalue

# d=Die()
# print("current value: ",d.vaalue)       #can be written as d.value1--->we can use either get or set method names
# d.value1=6                              #setter method and this name should be same
# print("modified value: ",d.vaalue)      #can be written as d.value1







#_______________Class Polymorphism_________________
#where we can have multiple classes with the same method name.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()










