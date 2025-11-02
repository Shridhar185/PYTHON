# def gpay(amount):
#     if amount>499:
#         bill=amount-100
#     else:
#         bill=amount
#     return bill
# def phonepe(amount):
#     if amount>499:
#         bill=amount-50
#     else:
#         bill=amount
#     return bill
# def creditcard(amount):
#     if amount>499:
#         bill=amount-200
#     else:
#         bill=amount
#     return bill
# def main():
#     while(1):
#         amount=int(input("enter recharge amount: "))
#         if amount<=0:
#             print("invalid amount")
         
#         print("mode of payment\n1.gpay wallet\n2.phonepay wallet\n3.creditcard")
#         mode=int(input("select mode of payment: "))
#         if mode==1:
#             bill=gpay(amount)
#             print("your bill: ",bill)
#         elif mode==2:
#             bill=phonepe(amount)
#             print("your bill: ",bill)
#         elif mode==3:
#             bill=creditcard(amount)
#             print("your bill: ",bill)
#         else:
#             print("select valid option")
#             break
# if __name__=='__main__':
#     main()




# class Deposit:
#     def __init__(self,amount,period,age):
#         self.amount=amount
#         self.period=period
#         self.age=age
#     def days_rate(self):
#         if(self.period<30):
#             if age>60 and self.amount>=50000:
#                 self.amount+=self.amount*0.1
#             return self.amount
#         elif(self.period>=30 and self.period<=60):
#             if age>60 and self.amount>=50000:
#                 self.amount=self.amount+self.amount*0.06+self.amount*0.01
#             else:
#                 self.amount+=self.amount*0.06 
#             return self.amount
#         elif(self.period>=61 and self.period<=90):
#             if age>60 and self.amount>=50000:
#                 self.amount=self.amount+self.amount*0.065+self.amount*0.01
#             else:
#                 self.amount+=self.amount*0.065 
#             return self.amount
#         elif(self.period>=91 and self.period<=180):
#             if age>60 and self.amount>=50000:
#                 self.amount=self.amount+self.amount*0.07+self.amount*0.01
#             else:
#                 self.amount+=self.amount*0.07
#             return self.amount
#         elif(self.period>=181 and self.period<=365):
#             if age>60 and self.amount>=50000:
#                 self.amount=self.amount+self.amount*0.08+self.amount*0.01
#             else:
#                 self.amount+=self.amount*0.08 
#             return self.amount
#         else:
#             if age>60 and self.amount>=50000:
#                 self.amount=self.amount+self.amount*0.085+self.amount*0.01
#             else:
#                 self.amount+=self.amount*0.085 
#             return self.amount
# while(1):
#     amt=int(input("enter amount: "))
#     days=int(input("input days: ")) 
#     age=int(input("enter age:"))
#     obj=Deposit(amt,days,age)
#     total_amt=obj.days_rate()
#     print(total_amt)








 














