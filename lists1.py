    
                     #lists# 
#s=[0]*5
#print(s)      #prints  5times 0




""" list1=[2,3,4,5,6]
print(list1)
list2=list1             #shallow copy
print(list2)
list1[-2]=56            #last element is -1
print(list1)
print(list2)            #changes done on list1 affect to list2

import copy
list3=copy.deepcopy(list1)   #changes in list1 does not affect to list2
print(list3)
list1[2]=23       
print(list1)                  
print(list2)                 #change will affect-->shallow copy
print(list3)                 #change will not affect---->deep copy
 """



#count(),reverse(),sort(),min(),max(),choice(),shuffle(),deepcopy()
#list--->append(item),insert(index,item),remove(item),index(item),pop(index)


""" 
list1=[1,2,3,4,5]
print("the length: ",len(list1))
list1.append(66)             #[value]   inserts element at end 
print(list1)        
list1.insert(1,66)           #[index,value]
print(list1)
list1.remove(66)             #[value]   removes first  element if two or more same element present 
print(list1)
val1=list1.pop(3)            #[index]   remove and returns an element,if index not specifies then removes last value 
print("popped element: ",val1)
print(list1)
list1.append(6)
print(list1)
count=list1.count(6)         #[value]   if value not present give zero,  it is case sensitive for strings in list 
print("total 6 in list: ",count)
val=list1.index(6)           #[value]    returns index of an value ,gives index of first value if two or more same  vlaue present 
print("index of 6 value: ",val)            
sort=sorted(list1)           #returns value therefore we store values in another variable and print
print(sort)
list1.reverse()
print(list1)
list1.sort()                 #in strings capital comes first, done on first letter of words, not returns value
print(list1) 
if 100 in list1:
    print("100 present")
else:
    print("100 not present ")
 """    



""" 
import random
list1=[234,45,23,6334,235,67]
min=min(list1)
max=max(list1)
print(min)
print(max)
ch=random.choice(list1)
print(ch)                  #choose random number in list1
random.shuffle(list1)
print(list1)               #shuffle values in a list
 """






""" list1=["apple","cat","bat","Rat"]
print(list1)
list1.sort()
print(list1)
list1[0]="banana"
print(list1)
 """





""" 
my_list = [3, 9, 7, 3, 6, 5, 7, 24, 6]
max_entry = max(my_list)
print("The maximum entry in the list is:", max_entry)
print(my_list[0:2])
print(my_list[0:6:2]) #from 0 to 6 of step 2 
 """




#immutable types----->str,int,float,bool
#mutable type---->list


#printing values in list by for and while loop
""" 
list1=[1,2,3,4,5,6]
for item in list1:
    print(item)
 """
 

""" 
list1=[1,2,3,4,5,6]
i=0
while i<len(list1):
    print(list1[i])
    i+=1 
"""



#adding list of lists
""" movies=[["rrr",5,2023]]
movie=[]
movie.append("kgf")
movie.append(5)
movie.append(2023)
movies.append(movie)
print(movies)
print(movies[1][0])
 """





""" 
tuple1=(1,2,3,3,4,5)
print(tuple1)
a,b,c,d,e,f=tuple1                 #assign values to variables, variables should be same as in tuple1otherwise give value error
print(b)
print(tuple1[1:4])
#tuple1[0]=10                      # type error: 'tuple' object does not support item assignment
"""




""" 
#generating random list
random_list=[0]*11                 #11 integers generate   why[0]
import random 
for i in range (len(random_list)):
    random_list[i]=random.randint(0,50)                #numbers in between 0 to 50 
random_list.sort()
print(random_list)
 """



""" 
import random
number=random.randrange(50,100,2) #random even int 
print(number)
number1=random.randint(50,100) #random int 
print(number1)
ele=int(input("enter no of elements in list: "))
l=list(range(ele))                          #how to take input of list of differnt datatypes 
print(l)
 """



""" 
#generating random list
import random
randlist=[0]*10
total=0
for i in range(len(randlist)):
    randlist[i]=random.randint(0,50)
    total+=randlist[i]
randlist.sort()
median_index=len(randlist)//2
avg=total/len(randlist)
print(randlist)
print("total: ",total)
print("median: ",randlist[median_index])
print("avg: ",avg)
print("min: ",min(randlist))
print("max: ",max(randlist))
 """




""" 
movies=[["kgf2",2022,9.8],["avengers",2019,9.9],["rrr",2022,9.5]]
for movie in movies:
    print(movie)    
for movie in movies:
    for item in movie:
        print(item,end=" ")
    print()
newmovie=["bahubali",2017,9.6]
movies.append(newmovie)       #append takes only one parameter 
for movie in movies:
    print(movie)
  """








 

 #to find no of times particular word occur in 2d list of sentences

list=["hello this is hello india ",
      "hello world i am in india",
      "hello world program"]
w=input("enter word to search: ")
count=0
flag=0
for item in list:
    words=item.split()
    for i in range(len(words)):
        if(words[i]==w):
            count+=1 
            flag=1
if flag==0:
    print("not found")
print(count)

