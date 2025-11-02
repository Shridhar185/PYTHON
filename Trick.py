#exception leads to runtime error
#syntax error not executed the program
#semantic error occur when excepted output not printed
#eval is not keyword and it is keyword
#IDLE Integreted development life cycle
#objects are real world entities while classes are not real 
#33 keywords are there in python
#python is dynamically typed language datatype will changes wrt value
#ASCII  American Standard Code for Information Interchange
#python is case sensitive for identifiers and max identifier length is 79
#token is also known as lexical unit
#token is smallest individual unit of program
#tokens->keywords,identifier,literal,punctuation/seperation,operations
#comment is not token
#in is not keyword it is membership operator
#type casting also known as explicit type casting
#keywords can be lower case or uppercase
#begining underscore is used for private variables 
#boolean is subtype of integer datatype  True(1) False(0)
#python does not have switch statement
#do while loop is not used in python




#in is not work for int it give error
# 'int' object is not iterable
# x=100
# for i in x:
#     print(i)








print('ram','ravan','raj')          #ram ravan raj
print('ram','ravan','raj',sep='-')  #ram-ravan-raj
print(3+3.00,3**3.00)               #6.0 27.0
print("hello\\world")               #hello\world
print("hello\world")                #hello\world
str1="hello\world"
print(str1)                         #hello\world
print(ord('a'))                     #97
print(chr(67))                      #C  (it accept only integers)
print(round(10/3,2))                #3.33
print(round(3.34523,3))             #3.345



a=[23,43,55,623,5,623,23]
del a[2]                #remove 3rd element
a.insert(1,0)           #add 0 at index 1
print(a)                #[23, 0, 43, 623, 5, 623, 23]

a=[1,2,3,4]
a.extend(a)
print(a)                #[1, 2, 3, 4, 1, 2, 3, 4]

a=10,23,45,'hello',34
print(type(a))          #<class 'tuple'>

For=10
print(For)

#string is immutable
str1='thisismyplace'
print(str1[-4:])        #print last 4 characters
print(str1[:4])         #print first 4 characters
print(str1[:-4])        #print string otherthan last 4 char
print(str1[::-1])       #reverse string

a="hello"
b="world"
print([a]+[b])          #['hello', 'world']
print([a,b])            #['hello', 'world']

print('35'<'9')         #True (it checks first char of both)
a="hello"*3
print(a)                #hellohellohello

# a=None
# print(a+1)              #type error

print(0.1+0.1)          #0.2
print(0.1+0.2)          #0.30000000000000004    why....
print(0.2+0.3)          #0.5

for i in range(10,5,-1):
    print(i,end=' ')        #10 9 8 7 6
print()


#swapping two variable in one line
x=10
y=20 
x,y=y,x

a=10,00,000         #it is tuple
print(a)            #(10, 0, 0)










