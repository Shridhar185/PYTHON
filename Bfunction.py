#function can wriiten in 4 ways based on return and arguments
#function  is 2 types user defined and in built function 
#function by default follows position al argument
#keyword argument is also known as named arguement
#function that returns some value is called fruitful fucntion or none void function
#function scope can be local or global
#global variable defined under __main__ section 
#python resolves the scope using LEGB rule-->Local Enclosing Global  Builtin
#in fucntions arguments are called actual arguments and paramters are called formal arguments
#if function return  no value but for it retruns None
#a funciton can return multiple values
#position argument also known as required argument

#________________________functions_________________________________________________
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# function is defined using the def keyword:
def my_function():
  print("Hello from a function")
my_function()         #Calling a Function

#data can be passed into functions as arguments.
#no of arguments and parameters mentioned should be same 
def my_function(fname):     #parameter
  print("name is : ",fname)
#in python + is for only concatenation therefore use only string
  print("name is: "+fname)   
my_function("ram")          #arguments


#Default Parameter Value________________________________
#when function called without argument then function uses default value
#if we pass argument then passed argument is printed 
def my_function(country = "India"):
  print("I am from " + country)
my_function("USA")
my_function()





#global and local scope
a=10        #a is global
def hi():
  print(a)   
hi()
#________________10
a=10
def hi1():
  a=15
  print(a)
hi1()
print(a)
#________________15 10
a=100
def hi2():
  global a
  a=15
  print(a)
hi2()
print(a)
#__________________15 15
a=1000
def hi3():
  global a
  print(a)
  a+=100
hi3()
print(a)
#___________________1000 1100







#Arbitrary arguments________________________________
#If the number of arguments is unknown, add a * before the parameter name:
#it prints all names in tuple format      names:  ('ram', 'ravan', 'raj')
#Arbitrary arguments, also known as *args in Python, allow you to pass a variable number of arguments to a function.
def names(*name):
  print("names: ",name)
names("ram","ravan","raj")
#_______OR_________
def print_arguments(*args):
    for arg in args:
        print(arg)
print_arguments("apple", "banana", "cherry")


#Keyword Arguments_________________________________
#You can also send arguments with the key = value syntax.
#for keywords both parameter and arguments names should be same
#when order of the arguments does not matter. Keyword Arguments are often shortened to kwargs
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "ram", child2 = "ravan", child3 = "raj")


#Arbitrary Keyword Arguments, **kwargs___________________________
#in above number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])     #His last name is ravan
  print("name: ",kid)                           #name:  {'fname': 'ram', 'lname': 'ravan'}
my_function(fname = "ram", lname = "ravan")

 
#Passing a List as an Argument_________________________________
def my_function(food):
  for x in food:
    if x==food[len(food)-1]:
      break
    print(x,end=' ')
    print(food[3])
fruits = ["apple", "banana", "cherry",12]
my_function(fruits)


#Positional-Only Arguments__________________________________________
#function parameters can only be passed by position and cannot be passed by keyword
#use a single forward slash (/) in the parameter list of the function definition. 
#Parameters before the slash are positional-only, while parameters after the slash can be specified by position or keyword.
def func(a, b, /, c, d):
    print(a, b, c, d)
func(10,15,20,100)          #for keywords both parameter and arguments names should be same
func(23,856,c=100,d=589)
func(45,76,98,d=100)
#....below error
#....func(123,345,c=234,100)               #positional argument after the keyword argument not allowed,here we dont know 100 specified c or d therefore error
#....func(a=10, b=15, c=20, d=100)


#Keyword-Only Arguments__________________________________________________
# after the * use only keyword arguments 
def my_function(*, x):
  print(x)
my_function(x = 3)
#________OR__________
def func(a, b, *, c, d):
    print(a, b, c, d)
func(1, 2, c=3, d=4)
func(a=1, b=2, c=3, d=4)
func(100,b=2343,c=23223,d=234)
#.....error
#.....func(a=100,20,c=1000,d=1223)


#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a ,b , c , d)
my_function(5, 6, c = 7, d = 8)








#Return Values_________________________________________
def my_function(x):
  return 5 * x
print(my_function(3))




#returning a tuple_______________________________________
def get_user_info():
    name = "John"
    age = 30
    return name, age
print(get_user_info())          #('John', 30)
#_________OR___________
user_name, user_age = get_user_info() 
print("name: ",user_name)
print("age: ",user_age)

#tuples are immutable, which means you cannot use the add element or delete element
def mytuple():
  tuple1=()
  for i in range(10):
    tuple1+=i,
  return tuple1
print(mytuple())                #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)




#returning list________________________
def list1():
  listvalue=[10,23,34,54,23,12,3]
  return listvalue
print(list1())

#_______OR________
def listfn():
  listval=[]
  for i in range(12):
    listval.append(i)
  return listval
print(listfn())




#returning dictionary___________________________________________________
def mydict():
  dict1={}
  for i in range(5,10):
    dict1[i]=i            #here both key and value name same 
  return dict1
print(mydict())           #{5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

#index as key for value
def mydict1():
    dict1={}
    for i,val in enumerate(range(5,10)):
        #print(f"key:{i},value:{val}")
        dict1[i]=val        #i holds index 
    return dict1
print(mydict1())




#returning a set_______________________________________________________
#set preserves the insertion order.
def myset():
  set1=set()
  for i in range(10):
    set1.add(i)
  return set1
print(myset())




#The pass Statement______________________________________________
#function definitions cannot be empty, if no content then write pass to avoid error
def myfunction():
  pass
myfunction()




#recursion_______________________________________________________________

def fact(n):
  if n==1:
    return 1
  return n*fact(n-1)
n=5
print(fact(n))





#print this pattern 1 2 4 7 11 16 22

#Factorial sequence:
# Factorial of 2: 2
# Factorial of 3: 6
# Factorial of 4: 24
# Factorial of 5: 120

#print this pattern 1 3 6 10 15 21 28.....not understand
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)







#_____________Function Polymorphism_______________________
#polymorphism means many forms
#eg:len() furnction used to find length of string lists and dictionaries and tuples etc

















 

























