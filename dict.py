



#dictionary
 




"""
nos={1:"one,obe",2:"two",3:"three",5:"five",6:"six"}   #{key:value}
print(nos)
print(nos.get(1))            #1 is a key
print(nos[2])                #if key not present give key error
del nos[3]                   #to delete, if not present give key error
print(nos)
x=nos.pop(6)                 #return and remove value
print(x)
print(nos)
nos.clear()   #it delete all items in dict
print(nos)
print(nos.get(2)) 
"""




""" 
nos={1:"one,obe",2:"two",3:"three",5:"five",6:"six"} 
for item in nos:
    print(item," ",nos[item])
print()
for item in nos.keys():
    print(item)               #here we can also get values by above print method
print()
for name in nos.values():
    print(name)
print()
for code,name in nos.items():
    print(code,"       ",name)
print() """
 




""" 
nos={1:"one",4:"four",2:"two",3:"three",5:"five",6:"six"}
print(nos)
nos=list(nos) #convert key to list 
print(nos) """



# nos=list(nos.items())   #error ------convert both value and key to list 
# print(nos)
# nos.sort()             #based on key it sort 
# print(nos)

#nos=list(nos.values())----->error
#print(nos)












countries={'mx':'Mexico','in':'india','us':'usa'}
for key,value in countries.items():
    print(key,value)
print()
for i,j in countries.items():
    print(i,j)

nos={'1':'one','2':'two','3':'three'}
for item in nos:
    print(item)
print("with keys access method")
for item in nos.keys():
    print(item)
for item in nos.values():
    print(item)
for item in nos.items():
    print(item)




""" 
#to convert list to dictionary
movie=[['kgf',2023],['rrr',2022]]
print(movie)
movie=dict(movie)
print(movie)      #to convert to list
movie=list(movie)
print(movie)      #keys to list """



#dictionary of lists
""" 
course={"cs1":["cs","abs",45],"cs2":["ec","xyz",50],"cs3":["enc","pqr",30]}
print(course["cs1"])
print(course.get("cs2"))
for item in course:
    print(item,"  ",course[item]) 
list1=list(course)
print(list1) """


#dictionaries of dictioniaries
""" cont={"kannada":{"name":"kgf","rating":5,"year":2023},
      "telagu":{"name":"rrr","rating":5,"year":2022}}
print(cont["kannada"]["rating"])
 """








# Creating a list of dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
print(people[0])
people[1]["age"]=30
print(people)
new_person = {"name": "David", "age": 40}
people.append(new_person)
print(people)
for person in people:
    print(person)
    # print(person["name"], "is", person["age"], "years old")
ti=input("enter name to search :")
for person in people:    
    if person["name"]==ti:
        print("found")
