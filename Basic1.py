#conditions____________________________
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# #else statement doesn't accept a condition
# else:
#   print("hello")



#conditions iin shortcut____________-
# a=50
# b=34
# if a > b: print("a is greater than b")
# print("a is large") if a>b else ("b is large")
# print("A") if a > b else print("=") if a == b else print("B")



# #and keyword 
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
# #or keyword
# if a > b or a > c:
#   print("At least one of the conditions is True")
# #not keyword
# if not a > b:
#   print("a is NOT greater than b")



#Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#if statements cannot be empty if we dont have contenet then write pass statement to avoid error
a = 33
b = 200
if b > a:
  pass


#it creates an infinite loop i will never increment beyond 3,
# i = 0
# while i < 6:
#   if i == 3:
#     continue
#   i += 1
#   print(i)



#_______________1 2 3 
i = 1
while i < 6:
  print(i,end=' ')
  if i == 3:
    break
  i += 1
print()
#_______________1 2 4 5 6
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i,end=' ')
print()



fruits = ["apple","orange","banana", "cherry"]
for x in fruits:
  #print(x, end=' ')             #apple orange banana
  if x == "banana":
    break
  print(x,end=' ')               #apple orange


for x in fruits:
  if x == "banana":
    continue
  print(x)                       #apple orange cherry


for x in range(6): 
  print(x)                       #0 1 2 3 4 5 
for x in range(2, 6):
  print(x)                       #2 3 4
#3rd parameter is steps
for x in range(2, 30, 3):
  print(x)                       #2 5 8 ,,,,,,,,,,,
  


#nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)



#printing values along with index
#to get indexes  use the enumerate() function in Python
#enumerate() built in function keep tracking index of an each item while looping over list,tuple, or strings

names=["ram","ravan","raj","lion"]
print("index\tname")
for i,name in enumerate(names):
  print(f"{i}\t{name}")



















 




















 

























