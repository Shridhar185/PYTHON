#tuples
#A tuple is a collection which is ordered and unchangeable. and allow duplicate values.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#tuples are immutable in Python.



# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# #One item tuple, remember the comma:
# thistuple = ("apple",)
# print(type(thistuple))

# #contain different data types:
# tuple1 = ("abc", 34, True, 40, "male")
# print(type(tuple1))             #tuple

# #use the tuple() constructor to make a tuple.
# list1=["red","white","yellow","green"]
# tuple1=tuple((list1))
# print(tuple1)

# tuple2=tuple(("red"))
# print(type(tuple2))             #tuple

# thistuple = ("apple", "banana", "cherry")
# #slicing is same as string
# #aceess
# print(thistuple[1])             #banana

#modify WKT that tuple is unchangeable______________________________________
#thistuple[1]="mango"           #give error
#to modify tuple we convert it to list then modify then convert to tuple
# x = ("apple", "banana", "cherry")
# y = list(x)                     #list conversion
# y[1] = "kiwi"                   #here we modify we can append or remove can use any list methods
# x = tuple(y)                    #tuple conversion
# print(x)



# #add tuple to tuple_________________________________
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)                   #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')



# del keyword can delete the tuple completely
#del thistuple                   #deleted entire tuple
#print(thistuple)                #gived error because tuple not exists





#Unpacking a Tuple_____________________________________________________________
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#we can extract the tuple  values back into variables. This is called "unpacking":
#number of variables and number of elements in tuple should same
# fruits = ("apple", "banana", "cherry")         #packing
# a,b,c= fruits                                  #unpacking
# print(a)
# print(b)
# print(c)

# #use * if number of variables less than elements
# a,*b=fruits
# print(a)                        #apple
# print(b)                        #['banana', 'cherry']
# *c,d=fruits
# print(c)                        #['apple', 'banana']
# print(d)                        #cherry




#looping is same as of list______________________________________


#methods of tuple_____________________________________
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = thistuple.count(5)
# print(x)                        #2
# print(thistuple.index(8))       #3























#**********************************************************************************************************************************
#____________________________sets__________________________________________
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
#duplicates are not allowed (True and 1 is considered the same value)
#set can print in any order
# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# print(len(thisset))
# print(type(thisset))                        #set
# #A set can contain different data types:
# thisset = {"apple", 1,"banana", "cherry", 0, False, True, 0}
# print(thisset)          #it prints only 5 items and not prints duplicates (False, True, 0)



# #add items_______________________________________________________________________
# thisset.add("orange")
# print(thisset)

#add 2 sets  by update() method if item same in both sets it prints only unique although it has 2 same items
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya","apple"}
# thisset.update(tropical)
# thisset.remove("apple")             #it removes all duplicates items of same present
# print(thisset)

#object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)




#remove item________________________________________________________________________
# thisset = {"apple", "banana", "cherry","mango","peru"}
# thisset.remove("banana")         
# print(thisset)
# #If the item to remove does not exist, remove() will raise an error.to avoid error use discard method
# thisset.discard("appl")
# print(thisset)
# #Remove a random item by using the pop() method:
# x = thisset.pop()
# print(x)                    #popped item
# print(thisset)
# #The clear() method empties the set
# thisset.clear()
# #del keyword will delete the set completely:
# del thisset




#Join Sets____________________________________________________________________________________
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
#The union() method returns a new set with all items from both sets.
set3 = set1.union(set2)
print(set3)
#You can use the | operator instead of the union() method, and you will get the same result.
set3 = set1 | set2
print(set3)

#join multiple sets_________________________
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
myset = set1 | set2 | set3 |set4
print(myset)

#The union() method allows you to join a set with other data types, like lists or tuples.
#The  | operator only allows you to join sets with sets
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#The update() method inserts all items from one set into another. and not return new set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Both union() and update() will exclude any duplicate items.




#intersection______________________________________________
#The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
#You can use the & operator instead of the intersection() method
set3 = set1 & set2
print(set3)

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}
set3 = set1.intersection(set2)
print(set3)                     #{False, True, 'apple'}


#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(x)                        #{'apple'}

 
#difference________________________________________________________________
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)                     #{"banana", "cherry"}
#ou can use the - operator instead of the difference() method
set3 = set1 - set2
print(set3)


#The difference_update() method will also keep the items from the first set that are not in the other set
#it not returns new set 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


#symmetric difference______________________________________________________________
#it contains elements that are not present in both sets
#contains the elements that are exclusive to each set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)                     #{'google', 'banana', 'microsoft', 'cherry'}
#You can use the ^ operator instead of the symmetric_difference() method,
set3 = set1 ^ set2
print(set3)

#The symmetric_difference_update() method update set by items which exclusive in both sets
#it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)




#set methods__________________________________________________________________________________________________________________
# Method	             Shortcut	        Description
# add()	 	                            Adds an element to the set
# clear()	            	            Removes all the elements from the set
# copy()	 	                        Returns a copy of the set
# difference()	            -	        Returns a set containing the difference between two or more sets
# difference_update()	    -=	        Removes the items in this set that are also included in another, specified set
# discard()	 	                        Remove the specified item
# intersection()	         &	        Returns a set, that is the intersection of two other sets
# intersection_update()	     &=	        Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	                    Returns whether two sets have a intersection or not
# issubset()	            <=	        Returns whether another set contains this set or not
#  	                        <	        Returns whether all items in this set is present in other, specified set(s)
# issuperset()	            >=	        Returns whether this set contains another set or not
#  	                        >	        Returns whether all items in other, specified set(s) is present in this set
# pop()	 	                            Removes an element from the set
# remove()	                        	Removes the specified element
# symmetric_difference()	^	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	    Inserts the symmetric differences from this set and another
# union()	                |	        Return a set containing the union of sets
# update()	                |=	        Update the set with the union of this set and others
#_________________________________________________________________________________________________________________________