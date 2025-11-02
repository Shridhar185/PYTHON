# string literal with the print() function:
print("Hello")
print('Hello')

#Assign String to a Variable
a = "Hello"
print(a)

#multiline strings using either 3 double quotes or 3 single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings are Arrays of bytes representing unicode characters.
# Python does not have a character data type
a = "Hello, World!"
print(a[0])                 #first char h
print(a[-1])                #last char  !


#Looping Through a String
for x in "hello":
  print(x)

#len() function returns the length of a string
a = "Hello, World!"
print(len(a))

#in keyword for to check if a certain phrase or character is present in a string,
#phrase is a group of words
txt = "The best things in life are free!"
print('s' in txt)                       #return true
print("free" in txt)                    #return true
print("are free" in txt)                #return true

#not in keyword To check if a certain phrase or character is NOT present in a string
txt = "The best things in life are free!"
print("expensive" not in txt)           #give True

#string slicing-->index start from 0
str1="hello world"
print(str1[:5])          #print upto 5 index i,e   0 1 2 3 4
print(str1[2:5])         #print between index of   2 3 4
print(str1[5:])          #print index after 5 i,e  5 6 7 8______
print(str1[-5:-2])       #wor

#String Concatenation
a = "Hello"
b = "World"
print(a+" "+b)
print(a+"/"+b)



# Format Strings
#WKT we cannot combine strings and numbers
#the format() method takes the passed arguments,
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))          #My name is John, and I am 36
#The format() method takes unlimited number of arguments
quantity = 3                    #index 0
itemno = 567                    #index 1
price = 49.95                   #index 2
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#use index numbers {0} for correct placeholders
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#escape character \
#\t	Tab     \b	Backspace       \n	New Line        \\	Backslash
#To insert characters that are illegal in a string, use an escape character.
a="karnataka is in \"india\""       #karnataka is in "india"
print(a)






#conversion of list to string and string to list
string="hello"
mylist=list(string)
print(mylist)             #['h', 'e', 'l', 'l', 'o']
string=''.join(mylist)
print(string)             #hello



#__________any() built in function______
#to check any number or alphabet or lower or upper value present in string 
s = "abc123"
if any(c.isalpha() for c in s):
    print("String contains alphabetic characters")
else:
    print("String does not contain alphabetic characters")

#_______OR________

s = "hell123"
print(True if True in [i.isalnum() for i in s] else False)
print("good" if True in [i.isalpha() for i in s] else "bad")









#__________________________________________________________________________________________
#check all methods of strings
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning
#___________________________________________________________________________________________






 