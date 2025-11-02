#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries cannot have two items with the same key:
#The values in dictionary items can be of any data type:


# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# print(thisdict)
# print(thisdict["brand"])
# print(len(thisdict))
# print(type(thisdict))

#use the dict() constructor to make a dictionary.
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)


 
# car = {"brand": "Ford","model": "Mustang","year": 1964}
# #Get the value of the  key by get() method
# x = car.get("model")
# #The keys() method will return a list of all the keys in the dictionary.
# x = car.keys()
# print(x)                    #dict_keys(['brand', 'model', 'year', 'color'])
# #The values() method will return a list of all the values in the dictionary.
# x = car.values()
# print(x)                    #dict_values(['Ford', 'Mustang', 1964, 'white'])
# #The items() method will return each item in a dictionary, as tuples in a list.
# x = car.items()
# print(x)                    #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')])         

# #Check if Key Exists
# if "model" in car:
#     print('yes')

# #Change Values
# car["year"]=2018
# #Add a new item to the original dictionary,
# car["color"] = "white"
# # update() method will update the dictionary with the items from the given argument.
# #if item not present then it will add another item to dict
# #method is used to update multiple key-value pairs in a dictionary at once. 
# car.update({"year": 2020})
 


# #The pop() method removes the item with the specified key name:
# #car.pop("model")
# #popitem() method removes the last inserted item
# car.popitem()
# #to delete complete dictionary
# #del car
# #to delete 1 item by key
# del car["model"]
# #The clear() method empties the dictionary:
# car.clear()





#*loops____________________________________________________________________________________
# #Print all key names in the dictionary, one by one:
# car = {"brand": "Ford","model": "Mustang","year": 1964}
# for x in car:
#   print(x)
# #use the keys() method
# for x in car.keys():
#   print(x)

# #Print all values in the dictionary, one by one:
# for x in car:
#   print(car[x])
# #use the values() method
# for x in car.values():
#   print(x)

# #Loop through both keys and values, by using the items() method:
# for x, y in car.items():
#   print(x, y)
# for x in car:
#    print(x,car[x])
#________________________________________________________________________






#Copy a Dictionary__________________________________________________________________
#cannot copy by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#the copy() method: Here chnages will not effected
# car = {"brand": "Ford","model": "Mustang","year": 1964}
# mydict = car.copy()
# print(mydict)
# #o make a copy is to use the built-in function dict().
# mydict = dict(car)
# print(mydict)




#***nested dictionaries_________________________________________________________
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#______OR_______
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])

#Loop Through Nested Dictionaries
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])


#__________________________________________________________________________________
#for each key we can have more than one value 
# nos={1:"one,obe",2:"two",3:"three",5:"five",6:"six"}   #{key:value}
# print(nos)
# print(nos.get(1))            #one,obe
# #del nos[1]
# print(nos)
# for x in nos:
#    print(x,nos[x])
# #print all keys as list
# k=list(nos)
# print(k)
# #print all values as list
# v=list(nos.values())
# print(v)
# #print each item in tuple with all tuples in list
# #[(1, 'one,obe'), (2, 'two'), (3, 'three'), (5, 'five'), (6, 'six')]
# i=list(nos.items())
# print(i)
#___________________________________________________________________________________





#to convert list to dictionary
movie=[['kgf',2023],['rrr',2022]]
print(movie)
movie=dict(movie)
print(movie)      #to convert to list
movie=list(movie)
print(movie)      #keys to list




#dictionary of lists
course={"cs1":["cs","abs",45],"cs2":["ec","xyz",50],"cs3":["enc","pqr",30]}
print(course["cs1"])
print(course.get("cs2"))
for item in course:
    print(item,"  ",course[item]) 
list1=list(course)
print(list1) 





#Creating a list of dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
print(people[0])
#changing dict value
people[1]["age"]=30
print(people)
#adding dictionary to list
new_person = {"name": "David", "age": 40}
people.append(new_person)
print(people)

for person in people:
    print(person)
    # print(person["name"], "is", person["age"], "years old")
name=input("enter name to search :")

for person in people:    
    if person["name"]==name:
        print("found")
    else:
       print("not found")





#dictionary methods__________________________________________________________________
# Method	           Description
# clear()	        Removes all the elements from the dictionary
# copy()	        Returns a copy of the dictionary
# fromkeys()	    Returns a dictionary with the specified keys and value
# get()	            Returns the value of the specified key
# items()	        Returns a list containing a tuple for each key value pair
# keys()	        Returns a list containing the dictionary's keys
# pop()	            Removes the element with the specified key
# popitem()	        Removes the last inserted key-value pair
# setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	        Updates the dictionary with the specified key-value pairs
# values()	        Returns a list of all the values in the dictionary
#________________________________________________________________________________________








