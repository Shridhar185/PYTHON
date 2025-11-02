

""" 
#printing string in character wise
a="shridhar"
for i in a:
    print(i)
print("\n")






a="shridhar"
char=input("enter char:")
count=a.count(char)     #count() is an method returns value that stored in count variable 
print("occurances of char in string: ",count)
print("\n")

 """




""" 
#ord(char) and len(str)------> are built in functions

print(ord("A"))          #print ascii value
print(ord(" "))
str1="hello world "
print(str1[1])           #give index value
print(str1[-2])          #print last 2nd character 
#str1[0]="d"             #type error we cannot change str--->string is immutable
#print(str1[20])         #index error

#string slicing 
print(str1[:5])          #print upto 5 index
print(str1[2:5])         #print between index of 2,3,4
print(str1[5:])          #print index after 5

#repetition operator
print("="*10)            #print 10 times a character 

#using in keyword
a="hello" in str1        #check present or not 
print(a)

if "l" in str1:
    print("found")

#looping over character
for char in str1:
    print(ord(char),end=" ") #ascii value of every char in string 
indx=str1.find("w")  #give index of w, give -1 if entered char or word not present 
print(indx)

n="12354"      #it should written in " "
check=n.isdigit() #check all numbers are digits
print(check)

str1=str1.title()
print(str1)
str2="apple"
print(str2.startswith("a"))   #true
print(str2.title())            #make first word capital
n="1,2,3,4,5"
n1=n.replace(",","-")          #replace , with -
print(n1)
 """

str3="hello"
s=" ".join(str3)
print(s)  #give spacing between letters
 


 











""" 
#print first word in sentence
str3="hello world in python "
i=str3.find(" ")
if i==-1:
    print("word not present ")
else:
    print(str3[0:i])
 """





""" 
str3="hello world in python "
str3=str3.replace("python","java") #to replace in a string 
print(str3)
words=str3.split() # split string into array
print(words[2]) #give third word in index
 """




""" 
arr =["hello","my","india"]
print(arr)
str6=" ".join(arr) #convert list to string type
print(str6)
 """




"""  
num="  23 3   4343"
print(num)
num=num.strip() #remove start and  end spaces 
print(num)
print("price:".ljust(20),"10.00".rjust(10))  #left and right justify
print("next price:".ljust(20),"10.00".rjust(10))
 """

    
     








