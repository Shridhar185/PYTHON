import matplotlib.pyplot as plt

chart1 = [10,45,76,30, 50, 29, 56,100]
plt.plot(chart1)        
plt.show()

 



# class person():
#     def __init__(self,f,l,e):
#         self.f=f
#         self.l=l
#         self.e=e
#     def get(self):
#         return self.f+" "+self.l+" "+self.e
# class customer(person):
#     def __init__(self,f,l,e,id):
#         person.__init__(self,f,l,e)
#         self.id=id
#     def get(self):
#         return person.get(self)+" "+str(self.id)
# class employee(person):
#     def __init__(self,f,l,e,pan):
#         person.__init__(self,f,l,e)
#         self.pan=pan
#     def get(self):
#         return person.get(self)+" "+str(self.pan)
# def show(obj):
#     if isinstance(obj,customer):
#         print("name fnama,lnmae,email,id ",obj.get())
#     elif isinstance(obj,employee):
#         print("name,fname,lnmae,email,pan: ",obj.get())
#     else:
#         print("name ,fname,lnmae,email: ",obj.get())

# def main():
#     while(1):
#         print("1.customer\n2.employee\n3.person\n4.exit")
#         opt=int(input("enter option: "))
#         if opt==1:
#             f,l,e,i=input("enter fname,lname,email,id: ").split()
#             obj=customer(f,l,e,i)
#             show(obj)
#         elif opt==2:
#             f,l,e,p=input("enter fname,lname,email,pan: ").split()
#             obj=customer(f,l,e,p)
#             show(obj)
#         elif opt==3:
#             f,l,e=input("enter fname,lname,emai: ").split()
#             obj=customer(f,l,e)
#             show(obj)
            

    