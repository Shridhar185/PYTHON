#swap Write a program to swap two values of two variables without using third variable. 
# x,y=10,20
# print("before reverse x and y:",x,y)
# x,y=y,x
# print("after reverse x and y",x,y)
 


#Write a program to add two complex numbers. 
# a=2+5j
# b=10+25j
# print(a+b)
#____________________________________no inbuilt
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def add(self,other):
#         self.real=self.real+other.real
#         self.img=self.img+other.img
# #Instead of returning a tuple containing the real and imaginary parts separately, you can return a new Complex object 
#         return Complex(self.real,self.img)
#     def __str__(self):
#         return f"sum: {self.real} + {self.img}i"
# def main():
#     real1=int(input("enter real number: "))
#     img1=int(input("enter img number: "))
#     num1=Complex(real1,img1)
#     real2=int(input('enter other real number: '))
#     img2=int(input("enter other img number: "))
#     num2=Complex(real2,img2)
#     sum=num1.add(num2)
#     print(sum)

# if __name__=='__main__':
#     main()
#____________________________________________________








#Write a program to print whether a given number is prime or not. 
# import math
# x=13
# srt=math.ceil((math.sqrt(x)))
# count=0
# for i in range(1,srt+1):
#     if srt%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")





#Write a program to print all prime numbers within the given range.
#sqrt() always returns a floating-point result
#isqrt() returns an integer result by truncating any decimal part of the square root.
# import math
# x=1000
# primelist=[]
# for i in range(2,x+1):
#     is_prime=True
#     srt=math.isqrt(i)+1
#     for j in range(2,srt):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         primelist.append(i)
# print(primelist)




#Write a program to print whether a given number is Armstrong number or not.
# n=370
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if sum==n:
#     print("armstrong number")
# else:
#     print("not armstrong number")






#Write a program to reverse the given string and number__________
# import time 
# start=time.time()
# str2="hello"
# n=1234
# print(str2[::-1])
# str1=str(n)
# print(str1[::-1])
# end=time.time()
# print(start-end)
#________________________________________
#to check time in microseconds
# import timeit
# code="""str2="hello"
# n=1234
# print(str2[::-1])
# str1=str(n)
# print(str1[::-1])"""
# exectime=timeit.timeit(code,number=1)
# print(exectime)
# #____________________________________________no inbuilt
# str1='hello'
# rev_str=''
# for i in range(len(str1)):
#     temp=str1[len(str1)-i-1]
#     rev_str+=temp
# print(rev_str)
# #_______________________________
# n=123234
# rev_num=0
# no_of_diits=0
# while n>0:
#     digit=n%10
#     no_of_diits+=1
#     rev_num=rev_num*10+digit
#     n=n//10

# print(rev_num)
# print(no_of_diits)
# #_________________________________________________

    




 



#Write a program to reverse the array_______________________
# mylist=[12,34,45,23,45,23]
# #intialising list with specified length
# mylist1=[0]*len(mylist)
# for i in range(len(mylist)):
#     mylist1[i]=mylist[len(mylist)-i-1]
# print(mylist1)
#________________________________
#without using extra space
#________________________________
# mylist=[12,34,456,56,23,12234,45,1232]
# left=0
# right=len(mylist)-1
# while left<right:
#     mylist[left],mylist[right]=mylist[right],mylist[left]
#     right-=1
#     left+=1
# print(mylist)




#________________________________________________________________________________
#Write a program to find the maximum and minimum elements in the array. 
#Write a program to find second largest and second minimum elements in the array.
# mylist=[23,34,45,23,12,4523,45,23,5434,221,23,12,12,5,12,45,1,100000]
# max=mylist[0]
# sec_max=mylist[0]
# min=mylist[0]
# sec_min=mylist[0]
# for i in range(len(mylist)):
#     if max<mylist[i]:
#         sec_max=max
#         max=mylist[i] 
#     if mylist[i]!=max and mylist[i]>sec_max:
#         sec_max=mylist[i]
#     if min>mylist[i]:
#         sec_min=min
#         min=mylist[i]
#     if mylist[i]!=min and mylist[i]<sec_min:
#         sec_min=mylist[i]
# print("max: ",max)
# print("second max: ",sec_max)
# print("min: ",min)
# print("second min: ",sec_min)
#______________________________________________________________________________________




#Write a program to count the number of vowels and consonants in the string.
# str1="helloworld"
# count=0
# for i in range(len(str1)):
#     if str1[i] in ['a','e','i','o','u']:
#         count+= 1
# print("vowel: ",count)
# print("constant: ",len(str1)-count)




 


#_____code to get frequency of each number.......***incompleted************
# mylist=[1,2,223,34,2,4,3,25,6,6,8,6,4,5,8,9]
# no_checked=[0]*len(mylist)
# for i in mylist:
#     count=1
#     for j in no_checked:
#         if i==j:
#             continue
#     for j in range(i,len(mylist)):
#         if i==mylist[j]:
#             count+=1
#     print(i,":",count)
#     no_checked=i




def check_password(password):
    is_digit=False
    is_alpha=False
    special_char=False
    for ch in password:
        if ch.isdigit():
            is_digit=True
        elif ch.isalpha():
            is_alpha=True
        else:
            special_char=True
    if is_digit and is_alpha and special_char:
        print("password is strong")
    elif is_digit and is_alpha or is_alpha and special_char or is_digit and special_char:
        print("passoword is moderate")
    else:
        print("password is weak")

def main():
    password = input("Enter the password: ")
    check_password(password)
    
if __name__ == '__main__':
    main()





































