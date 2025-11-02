#inheritance and polymorphism....................................
#create an oop allow to enter customer ad employee data





#it is not coorectly displaying person details its also display id and pan 
class person:
    def __init__(self,f,l,e):
        self.fname=f
        self.lname=l
        self.email=e
    def get(self):
        return self.fname+" "+self.lname+" "+self.email
class customer(person):
    def __init__(self,f,l,e,i):
        person.__init__(self,f,l,e)       
        self.__id=i
    def get(self):
        return person.get(self)+" "+str(self.__id)
class employee(person):
    def __init__(self,f,l,e,p):
        person.__init__(self,f,l,e)
        self.__pan=p
    def get(self):
        return person.get(self)+" "+str(self.__pan)
def show(obj):     #always use subclasses at first then parent classes
    if isinstance(obj,customer):
        print("customer name ,email,id: ",obj.get())
    elif isinstance(obj,employee):
        print("employee name ,email,pan: ",obj.get())
    else:
        print("person name ,email: ",obj.get())

def main():
    while True:
        n=int(input("1.customer\n2.emplouee\n3.person\n4.exit\nenter option: "))
        if n==1:
            f,l,e,i=input("enter fname ,lname,email,id: ").split()
            c=customer(f,l,e,i)
            show(c)
        elif n==2:
            f,l,e,p=input("enter fname ,lname,email,pan: ").split()
            c=employee(f,l,e,p)
            show(c)
        elif n==3:
            f,l,e=input("enter fname ,lname,email: ").split()
            c=person(f,l,e)
            show(c)
        elif n==4:
            break
        else:
            print("invalid option ")


if __name__=='__main__':
    main()
