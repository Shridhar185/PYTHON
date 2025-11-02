
""" 
def read():
    miles=float(input("enter miles: "))
    gas=float(input("enter gas vol: "))
    return (miles,gas)  #also written as return miles,gas
def disp(miles,gas):
    milage=float(miles/gas)
    print("mileage is: ",milage)
    print("rounded milage: ",round(milage,2)) #2nd parameter is no of numbers after point
    
def main():
    miles,gas=read()
    disp(miles,gas)
if __name__=='__main__':
    main()
 """





""" 
#to use named arguments 
def show(name="hello"):  #default name is hello
    print("name is : ",name)
show()
show("ram")              #passing value
show(name="hari")        #calling function by named argument
 """






#to define a global variable
""" tax=0
def cal(amount,taxt):
    global tax
    tax=amount*taxt
def main():
    cal(100,10)
    print(tax)

if __name__=='__main__':
    main()
 """


#use not when it is false and some action to be perfomed
a=False 
if not a: 
    print(a)


""" 
taxr=0.05  #global constant
def cal(amt):
    tax=amt*taxr
    return tax
a=cal(1000)
print("tax: ",a) """










""" 
data=[]
while True:
    name=input("enter name: ")
    data.append(name)
    choice=input("enter another name(y/n):")
    if(choice=='n'):
        break
for ele in data:
    print(ele)
"""
    
    
    
    
"""     
def add(movies):
    movie=[]
    name=input("enter movie name: ")
    year=int(input("enter year: "))
    rate=float(input("rating: "))
    movie=[name,year,rate]
    movies.append(movie)
def delete(movies):
    name=input("enter movie name to delete: ")
    for movie in movies:
        if movie[0]==name:
            movies.remove(movie)
def disp(movies):
    if len(movies)==0:
        print("no movies ")
    for movie in movies:
        print(movie)
def main():
    movies=[]
    while True:
        print("1.add movie\n2.delete movie\n3.display movie\nexit")
        opt=int(input("enter option: "))
        if opt==1:
            add(movies)
        elif opt==2:
            delete(movies)
        elif opt==3:
            disp(movies)
        elif opt==4:
            break   
if __name__=='__main__':
    main()
  """   
    



 



"""     
def view(courses):
    print("present courses are: ")
    for item in courses:
        print(item,end=" ")
    print()
    item=input("enter course to view: ")
    if item in courses:
        print(item,":",courses[item])
    else:
        print("not present ")
    print()
    
def add(courses):
    newcode=input("enter code: ")
    newcourse=input("enter course: ")
    courses[newcode]=newcourse

def dele(courses):
    item=input("enter a course to delete: ")
    if item in courses:
        courses.pop(item)
        print("course deleted ")
    print()
                       
def main():
    courses={}
    courses={"cs1":["cs"],"cs2":["ec"],"cs3":["enc"]}
    while True:
        opt=int(input("enter option "))
        if opt==1:
            view(courses)
        elif opt==2:
            add(courses)
        elif opt==3:
            dele(courses)
        elif opt==4:
            break
if __name__=='__main__':
    main()
 """  



 



#standard modules----->math,random,csv,tkinter,decimal
#functions in random module-->random(),randint(),randrange()

import random
n=random.random()   #generate betweeen 0.0 and 1.0 -->not display 1
print(n)
n1=random.randint(0,1)
print(n1)           #from 0 to 100
n1=random.randrange(0,1)
print(n1)           #from 1 to 99
n1=random.randrange(0,100,2)
print(n1)           #from 1 to 98 generate even numbers


























