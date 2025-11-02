#Lists are used to store multiple items in a single variable.
#lists are built-in data type in Python. and lists are ordered
#Lists are mutable sequences, meaning they can contain elements of different data types and the elements can be changed after the list is created. 

# my_list = [1, 2, 2, 3, 'hello', True]
# print(my_list[0])                   #1
# #slicing same as of strings based on index
# print(my_list[-1])                  #True-->last item
# my_list[1] = 'world'                #modify
# print(my_list)                      #[1, 'world', 3, 'hello', True]
 
# #use the list() constructor when creating a new list.
# newlist = list((100,"apple", "banana", "cherry")) # note the double round-brackets
# print(newlist)


# #changing 2 item by 1 item
# list1 = ["apple", "banana", "cherry","mango"]
# list1[1:3] = ["watermelon"]          
# print(list1)                        #['apple', 'watermelon', 'mango']

# #adding item at last by append method
# my_list.append(4)                   
# print(my_list)                      #[1, 'world', 3, 'hello', True, 4]     
# print(len(my_list))                 #7
# #inseting item at specified index by insert() method
# list1.insert(2,'orange')         
# print(list1)                        #['apple', 'watermelon', 'orange', 'mango']


# #removing items
# list1.remove("orange")              
# print(list1)
# #pop() method removes the specified index.if no index specified it removes last element
# list1.pop(2)                         
# print(list1)

#del keyword also removes the specified index
# del list1[0]    #delete first item
# del list1       #-------------->delete entire list
#list1.clear()    #delete all items in list but not list


#append elements from another list to the current list, use the extend() method.
#we can also add tuple items to an list by extend method
# list1 = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# list1.extend(tropical)
# print(list1)




# #looping through all items_____________________________________________________
# list1 = ["apple", "banana", "cherry"]
# for x in list1:
#   print(x)
# #Loop Through the Index Numbers
# for i in range(len(list1)):
#   print(list1[i])
# #While Loop
# i = 0
# while i < len(list1):
#   print(list1[i])
#   i = i + 1
# print()                       #it creates new line
# #Using List Comprehension
# [print(x) for x in list1]

# #creating newlist by using current list with specified condition
# words=['book','pen','cat','king']
# newwords=[]
# for x in words:
#     if len(x)==4:
#         newwords.append(x)
# print(newwords)
# #above using list Comprehension
# newwords=[x for x in words if len(x)==3]
# print(newwords)

# newlist = [x for x in range(10)]
# print(newlist)                  #0 to 9 in list
# #to print direct for even numbers-->print line by line
# [print(x) for x in range(10) if x%2==0]





# #sorting of lists_____________________________________________________________
# list1 = [100, 50, 65, 82, 23]
# list1.sort()                         #Sort the list ascending
# list1.sort(reverse = True)           #Sort the list descending

# #for strings By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# #unicode is standard unique number code point, for every character
# thislist = ["Orange", "mango", "Kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)                      #fist capital because of unicode
# thislist.sort(reverse = True)
# print(thislist)



# #customise sort___________________________
# thislist.sort(key = str.lower)       #first lower than capital
# #sorting based on nearest value to the particular value
# def nearest_to_target(value):
#     return abs(value - target_value)
# target_value=55
# list1.sort(key=nearest_to_target)
# print(list1)



#coping list___________________________________________________________________
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
newlist=thislist
mylist = thislist.copy()    #copping list if changes made in thislist will not affect 
mylist1=list(thislist)      #copping list if changes made in thislist will not affect 
thislist.append("mango")
print(thislist)             #thislist will be changed
print(newlist)              #changes based on thislist
print(mylist)               #mylist will not changed
print(mylist1)              #it also not changed




#joining lists_________________________________________________________________
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# list2=list1+list2
# print(list2)

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)
#we can also do it by using for loop indvidual append


#add items without using in built 
li=[]
for i in range(100):
    li.append(i)
print(li)

list1=[[]]
for ind,i in enumerate(range(100,200)):
    list1[ind]=i
print(list1)














#____________________________________________________________________________________________________
#list methods
# append()	        Adds an element at the end of the list
# clear()	        Removes all the elements from the list
# copy()	        Returns a copy of the list
# count()	        Returns the number of elements with the specified value
# extend()	        Add the elements of a list (or any iterable), to the end of the current list
# index()	        Returns the index of the first element with the specified value
# insert()	        Adds an element at the specified position
# pop()	            Removes the element at the specified position
# remove()	        Removes the item with the specified value
# reverse()	        Reverses the order of the list
# sort()	        Sorts the list
#____________________________________________________________________________________________________________

