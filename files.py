#file is name of memory location that stores data permanently
#variable memory will be destroyed after the execution therefore we use the file 
#read and text modes are default
# open will written the file object
# x mode is for empty file

 

""" 
f=open("hello.txt","w")     #here f is a fileobject
f.write("hello world\n")        #\n it writes to new line
f.write("this is ")
f.write("karnataka") 
f.close()                    #close method of file object 
 """


""" f=open("hello.txt")  #to open a file 
print(f.read()) """




""" 
#to delete a file 
import os
if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    print("file not available ")
 """



#types of reading................................................................................................................................
""" 
with open("hello.txt","w") as f:             #text file is by default without .txt also it works
    f.write("hello world ")
    f.write("good morning\n")
with open("hello.txt","a") as f:             #a mode is to append here it is add new value to the file without deleting old files
    f.write("hello world")                   #if w mode in above line it deletes all previous values
with open("hello.txt") as f:
    #print(f.readline())                     #it display only first line
    #print(f.readline(10))                   #it prints first 10 characters 
    #print(f.readlines())                    #it prints all values as list
    #print(f.read())                         #prints values as there in a file
    
    for data in f:
        print(data)                          #without\n in f.write it not printing line by line 
    
    #while True:
    #    li=f.readline()
    #    if not li:  #this should be written compulsury
    #        break
    #    print(li) 
 """






#write a items in a list into a file
""" list1=["hello","world","india"]
with open("sample1","w") as f:
    for item in list1:
        f.write(item+"\n")   #write takes only one argument,if items were integers first we need to convert them to string as str(item)
#to read lines in a file into list
list1=[]
with open("sample1") as fi:
    #print(fi.read())--->too print as it is in file 
    for line in fi: 
        line=line.replace("\n","")
        list1.append(line)
print(list1)
"""







"""      
#to read names from user and write into a file 
names = []
n = int(input("Enter the number of names: "))
for i in range(n):
    name = input("Enter name: ")
    names.append(name)
print(names)
with open("sample.txt", "w") as file:
    for name in names:
        file.write(name + "\n")                      #file.write(name,"\n") here we should concatenate  
with open("sample.txt", "r") as file:                # because write method takes only one argument
    print(file.read())
 """






""" 
def writemovies(movies):
    with open("movies.txt","w") as f:
        for m in movies:
            f.write(m+"\n")

def readmovies():
    movies=[]
    with open("movies.txt","r") as f:
        for l in f:
            l=l.replace("\n"," ")
            movies.append(l)
    return movies

def listmovies(movies):
    if len(movies)==0:
        print("no movies")
        return
    for i in range(len(movies)):
        movie=movies[i]
        print(i+1,": ",movie)

def addmovie(movies):
    movie=input("enter movie name: ")
    movies.append(movie)
    writemovies(movies)
    print(movie," added")

def deletemovie(movies):
    if len(movies)==0:
        print("no movies")
        return
    ind=int(input("enter movie index to delete: "))
    movie=movies.pop(ind-1)
    writemovies(movies)
    print(movie," deleted")

def main():
    movies=[]
    print("movie list program")
    while(1):
        print("1.add movie\n2.delete movie\n3.display movies\nexit")
        opt=int(input("enter your option: "))
        if opt==1:
            addmovie(movies)
        elif opt==2:
            deletemovie(movies)
        elif opt==3:
            listmovies(movies)
        elif opt==4:
            break
        else:
            print("invalid option")

if __name__=='__main__':
    main()
 """












""" 
def add(movies):
    movie=input("enter a movie: ")
    movies.append(movie)               #in w mode it display all movies in list but writes only one movie in file
    with open("movies","a") as file:   # in "a" mode the values will stiil there even after exection
        file.write(movie+"\n")         #if "w" mode wriiten then each time values will be overriden by new values, therefore display only one movie 

def disp(movies):
    with open("movies","r") as file:    #writes what there on file,not which on list
        print(file.read())
    #for movie in movies:
    #    print(movie)                    #writes what there on list, not which on file

def delete(movies):
    movie=input("enter movie to delete: ")
    if movie in movies:
        movies.remove(movie)
        with open("movies","w") as file:
            for movie in movies:
                file.write(movie+"\n")
        print("movie deleted")    
        disp(movies)
    else:
        print("movie not found ")
 
def main():
    movies=[]
    print("movie list program")
    while(1):
        print("1.add movie\n2.delete movie\n3.display movies\nexit")
        opt=int(input("enter your option: "))
        if opt==1:
            add(movies)
        elif opt==2:
            delete(movies)
        elif opt==3:
            disp(movies)
        elif opt==4:
            break
        else:
            print("invalid option")

if __name__=='__main__':
    main()
 """





 




























#csv is an comma seperated values
#writer(file)--->it converts data into csv and returns csv writer object for file
#reader(),writer() are functions of csv file    and writerows() is method of csv writer object

# import csv
# movies=[["kgf",2022,10],["rrr",2022,9.8]]
# with open("movies.csv","w",newline='') as file:
#     writer=csv.writer(file,delimiter="\t")   #de;imeter argument is optional
#     writer.writerows(movies)
# with open("movies.csv",newline='') as file:
#     reader=csv.reader(file,delimiter="\t")
#     #print(file.read())     #the above delimeter helps to add  tab space between readings-->
#     for li in movies:
#         print("name:",li[0]," year:",li[1]," rating:",li[2])
#         #print(li)  #it prints in form of list 






import csv
student=[] 
n=int(input("no of inputs: "))
for i in range(n):
    name=input("enter name: ")
    usn=input("enter usn: ")
    divi=input("enter division: ")
    student.append([name,usn,divi])
with open("stulist.csv","w",newline='') as file:  #with is used to auto close and open file 
    writer=csv.writer(file)
    writer.writerows(student)
with open("stulist.csv","r",newline='') as file:
    reader=csv.reader(file)
    for li in reader:
        print(li)









 














#binary files are not readable 

#reading and writing from binary files
""" import pickle
movies=[["kgf",2022,10],["rrr",2022,9.8]]
with open("movies.bin","wb") as file:
    pickle.dump(movies,file)
with open("movies.bin","rb") as file:
    movies=pickle.load(file)
    for movie in movies:
        print(movie)
"""





""" 
import pickle
movies=[]
n=int(input("enter no of movies: "))
for i in range(n):
    name=input("enter movie name: ")
    year=int(input("enter movie year: "))
    rate=float(input("enter rating: "))
    movies.append([name,year,rate])
with open("movies.bin","wb") as file:
    pickle.dump(movies,file)
with open("movies.bin","rb") as file:
    movies=pickle.load(file)
    for movie in movies:
        print(movie) """