""" 
class student:
    name="ram"  #the aatributes should be intialiszed
    div="c"
    usn=1
    def detail(self):  #it is an method
        print(self.name,self.div,self.usn) #self.dept give error because class not have dept attribute
        print(f"{self.name} is in {self.div} division and usn {self.usn}")  #format specifiers

a=student()     #a is an object or instance of an student class
print(a.name)   #accessing an attribute of  an object
a.detail()
a.name="ravan"  #set an attribute
print(a.name)
a.detail()

a.dept="cs" #what this mean
print(a.dept)

b=student()  # creating another object of class
b.name="raj"
b.usn="2"
b.div="C"
b.detail()
 """







#In Python, you cannot define multiple constructors with the same name and different parameters. 
#you defined two __init__ methods in the Student class, one with no parameters and the other with two parameters then
# The second __init__ method will override the first one
#self is an reference of an invoking object





#construcors with no parameters we pass values
""" 
class stu:
    def __init__(self):
        self.name=""
        self.price=0
    def info(self):
        print(self.name,self.price)
a=stu()
a.name="apple"
a.price=50
a.info() """








""" 
class Student:
    def __init__(self):                 #constructor
        print("no details")
    def __init__(self,n,d):
        self.name=n
        self.div=d
        print(self.name,self.div)
    def info(self):                     #it is an method
        print(f"{self.name} is in {self.div} division")  

#a=Student()            #it auto calls constructor and prints
a=Student("ram","c")    #create object and set attributes
a.info()
b=Student("raj","a")
b.info()
print(f"names: {a.name},{b.name}") #f must wriiten else all treated as string 
 """
 








""" 
class products:
    def __init__(self,name='',price=0.0,discount=0):  #if not default valued intialized then it runs only when 3 parameters passed
        self.name=name
        self.price=price
        self.discount=discount                     
    def getdiscprice(self):
        return self.price*self.discount/100
    def totalprice(self):
        return self.price-self.getdiscprice()
    def quality(self,qual):  #accpets parameter
        self.name+=qual
        #return qual
    def getdiscription(self):
        #dont use--->return  "name: ",self.name,"price: ",self.price,"discount: ",self.discount   # commas , to separate the values, which will result in creating a tuple, not a single string. 
        return f"name: {self.name}, discount price: {self.getdiscprice()}, total price: {self.totalprice()}"         #self.getdiscprice(self)--> passing self as an argument to the methods ,not necessary give error 
def showprod(prod):
    print("products: ")
    print(prod.getdiscription())

#we can also print it in main method
p=products("apple",50,20)
p.quality(" good")  # here passing parameter to method
showprod(p)
p=products("mango",60,10)
p.quality(" bad")
showprod(p)
 """







""" 
#we can use list for above code
class products:
    def __init__(self,name='',price=0.0,discount=0):  #if not default valued intialized then it runs only when 3 parameters passed
        self.name=name
        self.price=price
        self.discount=discount                     
    def getdiscprice(self):
        return self.price*self.discount/100
    def totalprice(self):
        return self.price-self.getdiscprice()
    def getdiscription(self):
        #dont use--->return  "name: ",self.name,"price: ",self.price,"discount: ",self.discount   # commas , to separate the values, which will result in creating a tuple, not a single string. 
        return f"name: {self.name}, discount price: {self.getdiscprice()}, total price: {self.totalprice()}"         #self.getdiscprice(self)--> passing self as an argument to the methods ,not necessary give error 
def showprod(prod):
    print("products: ")
    for pro in prod:
        print(pro.getdiscription())

#we can also print it in main method

#p=[products("apple",50,20),products("mango",60,10)]    
#showprod(p)   

# we can also do it by appending one by one  
p=[]                  # list p to store instances of the products class.             
p1=products("apple",50,20)     
p2=products("mango",60,10)
p.append(p1)
p.append(p2)
showprod(p)        

 """







"""  
class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def discountamount(self):
        return self.price * self.discount / 100

    def totalprice(self):
        return self.price - self.discountamount()

def showprods(products):
    print("Products are:")
    for i in range(len(products)):
        product = products[i]
        print((i+1), ".", product.name)

def showprod(product):
    print("The details of the product are: ")
    print("Name:", product.name)
    print("Price:", product.price)
    print("Discount Price:", product.discountamount())
    print("Total Price:", product.totalprice())

def main():
    products = [Product("apple", 100, 10), Product("banana", 40, 8), Product("mango", 80, 15)]
    showprods(products)
    
    while True:
        n = int(input("Enter product number: "))
        if 1 <= n <= len(products):
            prod = products[n - 1]
            showprod(prod)
        else:
            print("Invalid product number.")
        choice = input("View another product (y/n): ")
        if choice.lower() != "y":
            print("Bye")
            break

if __name__ == "__main__":
    main()
 """










#object composition is an creatinng complex objects by combining simpler objects or components.


#dice is an plural of die
import random
class Die:
    def __init__(self):
        self.value=1
    def roll(self):
        self.value=random.randrange(1,7)
class Dice:
    def __init__(self):
        self.list=[]
    def adddie(self,die):           #die is object Die class
        self.list.append(die)
    def rollall(self):
        for die in self.list:
            die.roll()           

# def main():
#     print("dice roller program ")
#     print()
#     count=int(input("enter no of dice to roll: "))
#     dice=Dice()
#     for i in range(count):
#         die=Die()
#         dice.adddie(die)
#     while True:
#         dice.rollall()
#         print("your roll: ",end=" ")
#         for die in dice.list:
#             print(die.value, end=" ")
#         print("\n")
#         choice=input("enter choice(y/n): ")
#         if choice!="y":
#             print("bye")
#             break
# if __name__=='__main__':
#     main()









# d=Die()                                     #creating a die object
# print("intial value: ",d.value)
# d.roll()                                    # it rolls the die 
# print("after roll value: ",d.value)
# d1=Dice()
# d1.adddie(d)                                #passing die object
# print("1st value : ",d1.list[0].value)      # d1.list  gives unreadable object
#                                             #[die.value for die in d1.list]
# d.roll()
# d1.adddie(d)
# print("2nd value : ",d1.list[1].value)   #how to access both values a time
 


""" 
n=int(input("enter no of die objects: "))
dic=Dice()
for i in range(n):
    di=Die()
    dic.adddie(di)
for i in dic.list:
    print("intial value: ",i.value)
print()
dic.rollall()
for i in dic.list:
    print("new values: ",i.value)
 """























#encapsulation
#Encapsulation restricts direct access to some of an object's components from outside the class and provides controlled access through methods, ensuring data integrity and enhancing security.
#to make attributes private use (__value=2)
""" 
import random
class Die:
    def __init__(self):
        self.__value=1
    def getvalue(self):  # by this we can access the private value
        return self.__value
    def setvalue(self,value):  #by passing value here we can change value by outside
        self.__value=value
d=Die()
#d.__value=10          #it doesn't actually change the __value attribute of the Die class; instead, it creates a new attribute __value specific to the d instance.
#print(d.__value)      #without above line if you print this give attribute error-->'Die' object has no attribute '__value'
#to access and modify modify private value get and set methods
print("current value: ",d.getvalue())
d.setvalue(10)
print("modified value: ",d.getvalue()) """


""" 
import random
class Die:
    def __init__(self):
        self.__value=1
    def getvalue(self):  # by this we can access the private value
        return self.__value
    def roll(self):
        self.__value=random.randrange(1,7)
     
d=Die()
print("current value: ",d.getvalue())
d.roll()
print("modified value: ",d.getvalue())
 """




#encapsulation by public properties
""" 
import random
class Die:
    def __init__(self):        #constructor
        self.__value=1
    @property
    def vaalue(self):   
        return self.__value
    @vaalue.setter                     #it is above property setter
    def value1(self,newvalue):  
        self.__value=newvalue
d=Die()
print("current value: ",d.vaalue)        #can be written as d.value1--->we can use either get or set method names
d.value1=6                               #setter method and this name should be same
print("modified value: ",d.vaalue)       #can be written as d.value1
 """





# import random
# class Die:
#     def __init__(self):        #constructor
#         self.__value=1
#     @property
#     def getvalue(self):   
#         return self.__value
#                          #dont use setter property
#     def roll(self):  
#         self.__value=random.randrange(1,7)
# d=Die()
# print("current value: ",d.getvalue)        #can be written as d.value1--->we can use either get or set method names
# d.roll()                               #setter method and this name should be same
# print("modified value: ",d.getvalue) 











#inheritance 
#method overloading--> methods have same name and different signature
#method overriding-->methods have same name and same signature  
#signature is methods which have same parameters and same return type
         

""" 
class products:
    def __init__(self,name='',price=0.0,discount=0):  #if not default valued intialized then it runs only when 3 parameters passed
        self.name=name
        self.price=price
        self.discount=discount                     
    def getdiscprice(self):
        return self.price*self.discount/100
    def totalprice(self):
        return self.price-self.getdiscprice()
    def getdiscription(self):
        #return f"name: {self.name}, discount price: {self.getdiscprice()}, total price: {self.totalprice()}"         #self.getdiscprice(self)--> passing self as an argument to the methods ,not necessary give error 
        return self.name
class book(products):   #inherit properties of product class
    def __init__(self,name='',price=0.0,discount=0,author=""):
        products.__init__(self,name,price,discount)
        self.author=author
    def getdiscription(self):
        return products.getdiscription(self)+" by "+self.author

def showprod(prod):
    print("products: ")
    for pro in prod:
        print(pro.getdiscription())
        
p=[products("apple",50,20),book("mango",60,10,"shri")]    
showprod(p) 
 """






""" 

#by using isinstance
 
class products:
    def __init__(self,name='',price=0.0,discount=0):  #if not default valued intialized then it runs only when 3 parameters passed
        self.name=name
        self.price=price
        self.discount=discount                     
    def getdiscprice(self):
        return self.price*self.discount/100
    def totalprice(self):
        return self.price-self.getdiscprice()
    def getdiscription(self):
        #return f"name: {self.name}, discount price: {self.getdiscprice()}, total price: {self.totalprice()}"         #self.getdiscprice(self)--> passing self as an argument to the methods ,not necessary give error 
        return self.name
class book(products):   #inherit properties of product class
    def __init__(self,name='',price=0.0,discount=0,author=""):
        products.__init__(self,name,price,discount)
        self.author=author
    def getdiscription(self):
        return products.getdiscription(self)+" by "+self.author
    
class movie(products):   #inherit properties of product class
    def __init__(self,name='',price=0.0,discount=0,year=0):
        products.__init__(self,name,price,discount)
        self.year=year
    def getdiscription(self):
        return products.getdiscription(self)+" at "+str(self.year)

def showprods(prod):
    print("products: ")
    for i in range(len(prod)):
        print((i+1),prod[i].getdiscription())   #prod.getdiscription() not works because it access by index 
    print()

def showprod(p1):
    print("product data")                     #product=p[n] by this we can also use product in place of p[n]
    print("name: ",p1.name)                   #access the name attribute of a specific class object using the index n
    if isinstance(p1,book):                   #determine whether an object is an instance of a specified class or a subclass of that class.
        print("book author: ",p1.author)      #access the author attribute of a specific book object using the index n  
    if isinstance(p1,movie):                  #isinstance(object,classname)
        print("movie year: ",p1.year)

p=[products("apple",50,20),book("marvel",60,10,"shri"),movie("rrr",67,58,2022),book("python",30,10,"abc")]    
showprods(p)
while True:
    n=int(input("enter product number: ")) 
    p1=p[n-1]
    showprod(p1)
    choice=input("enter choice: ")
    if choice!="y":
        break
 """








#methods of object class

#using str method--->return string for object
""" 
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x = {self.x} and y = {self.y}"
    def __str__(self):                           #this override the first one
        return "a="+str(self.x) + " b=" +str(self.y)

obj = MyClass(10, 20)
print(obj)  # This will call obj.__str__() method and print its string representation
 """



""" 
class products:
    def __init__(self,name='',price=0.0,discount=0):  #if not default valued intialized then it runs only when 3 parameters passed
        self.name=name
        self.price=price
        self.discount=discount                     
    def getdiscprice(self):
        return self.price*self.discount/100
    def totalprice(self):
        return self.price-self.getdiscprice()
    def __str__(self):                             #__str__ method in the class is used to define a string representation of the object when it is printed.
        return self.name +" | " +str(self.price)+" | "+str(self.totalprice())
 
p=[products("apple",50,20),products("mango",60,10)]    
for prod in p:
    print(prod) """









#__iter__   and    __next__   methods in classes
""" 
class dept:
    def __init__(self):
        self.list=[]
    def addname(self,name):
        self.list.append(name)
d=dept()
d.addname("ram")
d.addname("raj")
d.addname("ravan")
for n in d.list:    #list is iteratable
    print(n)  
"""            
    
    
#in above if we use it as (for n in d) then it shows that dept object is not iteratable 
#so to make it as iteratable we use iter and next methods
#iter just do start index as -1
#next method will keep on increasing the index,so you should provide break for it

""" 
class dept:
    def __init__(self):
        self.list=[]
    def addname(self,name):
        self.list.append(name)
    def __iter__(self):
        self.index=-1
        return self
    def __next__(self):
        if self.index >=len(self.list)-1:
            raise StopIteration
        self.index+=1
        return self.list[self.index]
d=dept()
d.addname("ram")
d.addname("raj")
d.addname("ravan")
for n in d:        
    print(n) 
               """





# a="10"<"5"
# print(a)
    



# mi=1000
# mir=.08/12/100
# m=12
# fv=0
# for i in range(m):
#     fv+=mi
#     mia=fv*mir
#     fv+=mia
# print(fv)
