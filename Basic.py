# run a python file is like this direcly on the command line:
#to strart into terminal use py 
#to exit from terminal use exit()
#we can use comment like this """ """
#print() function use comma for multiple variables and + for strings is used 

#________________________________________________________________________
#to check python version
#import sys
#to check python version
# print(sys.version)
# #to check flatform
# print(sys.platform)
# # prints out a list of directories that Python searches for modules when importing them. 
# #print(sys.path)
# # prints out a dictionary containing information about currently loaded modules. 
# print(sys.modules)
#sys.argv[0] contains the name of the script itself,script Basic.py is being executed from path d:/VS_Code/python/
#print("path",sys.argv)      #['d:/VS_Code/python/Basic.py']




#________________________________________________________________________________
#casting

# x=10
# print(type(x))
# fl=float(x)
# print(type(fl))
# c1=complex(x)
# print(type(c1))

# y=str(x)    
# print(y+" hello")
# print(type(y))

# z=10.00
# print(type(z))
# str1=str(z)
# print(type(str1))
 

# ________________________________________________________________________
#string can either be single quote or in double quote
#variables are case sensitive,can contain(a-z,0-9,_,A-Z),start with(a-z,A-Z,_)
#number of variables matches the number of values

# x,y,z=10,20,'hello'
# print(x,y,z)

# #passing string as character to multiple variables but length same as variables
# a,b,c='ram'  
# print(a)            #prints r
# print(a,b,c)        #prints r a m

# #p,q,r=10            #give error

# #collection of values in a list
# animals=['cat',100,'bat']
# p,q,r=animals
# print(p,q,r)        #cat 100 bat
 

# ________________________________________________
#To create a global variable inside a function, you can use the global keyword. then that variable can be used outside function

# x=100           #IT will be global
# def num():
#     global x
#     x=10        #it is not global so to make use global it override previous value
#     print("inside fucntion: ",x)
# num()
# print("outside fucntion:",x)



#_____________________________________________________________________________________________
#datatypes
#size of int increase as value of int increases
# import sys
# x=1
# print(type(x))              #int
# print(sys.getsizeof(x))     #28bytes
# y=-10000000000000000
# print(type(y))              #int
# print(sys.getsizeof(y))     #32bytes

# f1=1.0
# print(type(f1))             #float
# print(sys.getsizeof(f1))    #24bytes
# f2=12322344543442323453.34343212
# print(sys.getsizeof(f2))    #24bytes

# #written with a 'j' or 'J' suffix to denote the imaginary part.
# c1=3+5j
# print(type(c1))             #complex
# print(sys.getsizeof(c1))    #32 bytes


#String_________________________________________________________________
# ch1='h'
# print(type(ch1))            #str
# print(sys.getsizeof(ch1))   #50bytes
# str1='hello world'
# print(sys.getsizeof(str1))  #60bytes




#multi line strings______________________________
#do it in either three double quotes or three single quotes
# import sys
# a="""hello this is world of nowhere
# and this is vscode doing
# python code"""
# print(a)
# print(a[0])                   #h
# print(sys.getsizeof(a))       #116





#boolean___________________________________________________________
# x=True
# print(x)                    #True
# print(type(x))              #bool
# print(sys.getsizeof(x))     #28

#the bool() function allow to evaluate any value
#any string,number,list tuple dictionary,set are true anf false if they empty
# print(bool('hello'))          #true
# print(bool(15))               #true
# print(bool(" "))              #true
 
# #for below flase_________________
# print(bool(""))               #flase
# print(bool())                 #flase
# print(bool(0))
# print(bool(None))
# print(bool(False))

# #used to determine if an object is of a certain data type:
# x = 200
# print(isinstance(x, int))

# #logical operations____________________________
# #and or not
# print(2<5 and 3<2)              #false
# print(2<1 or 5<2)               #false
# print(not(23<234 and 234<234))  #true




#bytes______________________________________________________________
#Bytes objects in Python are immutable, meaning once they are created, their contents cannot be changed.

# x=b"hello"
# print(x)
# print(type(x))              #bytes
# print(sys.getsizeof(x))     #38
# x=b'5'
# print(x)                    #b'5'
# print(sys.getsizeof(x))     #34

#bytearray____________________________________
# import sys
# x=bytearray(b'hello')
# print(x)                    #bytearray(b'hello')
# print(sys.getsizeof(x))     #62
# print(x[2])                 #104


# _________________________________________________________
# x=memoryview(b'24')         #to view memory we require bytes object
# print(x)




# _________________________________________________________
# list1=['cat','dog','rat']
# print(type(list1))          #list
# print(sys.getsizeof(list1)) #88bytes
# list1=[5]
# print(sys.getsizeof(list1)) #64bytes
# list3=[2,3,4,5]
# print(sys.getsizeof(list3)) #88bytes
# list4=[2.034,4,23233,324,'hello',45455,9,121,2]
# print(type(list4))
# print(sys.getsizeof(list4)) #136 bytes




#dict________________________________________________________________________
# import sys
# dict={'name':'ram','age':25}
# print(dict)
# print(type(dict))               #dict
# print(sys.getsizeof(dict))      #184
# dict1={1:'one',2:'two'}
# print(sys.getsizeof(dict1))     #224


# ____________________________________________________________________________________
# import random
# print(random.randrange(1,10))     #1-9
 




#______________________________________________________________________________________________
#Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
#float() - constructs a float number from an integer literal
#str() - constructs a string from a wide variety of data types






#______________operators________________________________________________________________________________________________
#pyhon not supports increament and decreament operators


#Arithmetic Operators-->+,-,*,/,%,**,//
# print(5/2)              #2.5
# print(5//2)             #2
# print(5**2)             #25

#Comparison Operators-->==,!=,<,>,<=,>=

#logical operators----->and,or,not
#print(10<5 and 15<23)   #False

# _______________________________________________
#bitwise operators--> &,|,^(xor),~(not),<<(left shoft),>>(right shift)

# print(3&3)              #3
# print(3|3)              #3
# print(3^3)              #0
# print(~3)               #-4
# print(~100)             #-101
# print(3&~3)             #0
# print(100&~100)         #0
# print(3|~3)             #-1
# print(100|~100)         #-1
# print(3^~3)             #-1
# print(100^~100)         #-1
 
# print(6&3)              #2
# print(12&6)             #4


#Assignment Operators-->=,+=,-=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=




#Identity Operators---->is(true if refer same object),is not(true if not same object refer)
#is  and not are keywords
# a=10
# b=15
# a=b                     #a and b refer to the same object.
# print(a is b)           #true
# print(a is not b)       #False
# c='hello'
# a=c                     ##a and b refer to the same object.
# print(a is c)           #true
# x=a=b
# print(x is b)           #true

# p=100
# q='string'
# r=p
# q=r
# print(p is q)         #true


#Membership Operators--->in(true if specified value present),not in































