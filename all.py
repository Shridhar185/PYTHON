
""" print(1,2,3,4)
print(1,2,3,4,5,sep='   ') #we can change gap between two numbers 
print(1,2,3,4,5,sep='\n')  # to write line by line
 """



"""         
#n=int(input("enter number of terms: "))
n=10
i=1

while i<=n:        #while is condition controlled loop 
    print(i,end=" ")
    i+=1  #i++ not used in python 
print("\n")

for i in range(n):
    print(i)
print("\n")
for i in range(1,n+1):   #range is a function ,for is a collection controlled loop
    print(i,end=" ")
print("\n")

print("odd numbers:",end=" ")
for i in range(1,10,2): #third is step,second is exclusive 
    print(i,end=" ")           #odd numbers
print("\n")

print("reverse:",end=" ")
for i in range(n,1,-1):   #to reverse 
    print(i,end=" ")
print()

#the first n even  integers 
for i in range(0,n*2,2):
    print(i,end=" ")
print("\n")
 """




""" 
print("enter exit when done: ")
while True:  #error if write true first is capital
    data=input("enter int:")
    if data=="exit":
        break
    x=int(data)         #we should convert it to int
    print("square is: ",x*x)
print("done")
print("\n")
 """
 

 
""" 
#..............................>not correct
mi_amt=float(input("enter invest money: "))  
mi_rate=float(input("enter month interest rate: "))     
m=int(input("enter months: "))                

future_amt=0
for i in range(m):
    future_amt+=mi_amt
    rate_amt=future_amt*mi_rate
    future_amt+=rate_amt

print(future_amt)
 """




































    
 
 
 

""" 
def fib(n):
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence

a=fib(10)
print(a) """




""" n=1
temp=1
for i in range(1,n+1):
    temp=temp*i
print(temp) """


n1=5
temp=1
i=1
while i<n1+1:
    temp*=i
    i=i+1
print(temp)


#fibonacci series
""" 
n = 10 
fn = [0,1]
for i in range(2,n):
    f=fn[i-1]+fn[i-2]
    fn.append(f)
print(fn) 
 """
 


""" 
n=10
fn=[0,1]
i=2
while i<n:
    f=fn[i-1]+fn[i-2]
    fn.append(f)
    i+=1
print(fn) 
"""


""" 
#without list fibonacci series
n = 10
# Initialize the first two Fibonacci numbers
a, b = 0, 1
i = 0
while i < n:
    print(a, end=' ')
    a, b = b, a + b  # Update a and b for the next Fibonacci number
    i += 1

 """

  




""" 
n=10
sum=0
for i in range(n):
    sum+=i
    
print(sum)

 """




""" 
n=0
n+=20
print(n)
print()
n+=30
print(n)
 """




""" i=0
for i in range(2,5):
    print(i)
  """   




""" 
n=input("enter no: ")
n=int(n)
sum=0
i=1
while sum<n:
    sum+=i
    i+=1
print("sum",sum)
 """



""" 
s="shridhar"
c='r'
count=0
for i in s:
    if(i==c):
        count+=1
print(count)
 """