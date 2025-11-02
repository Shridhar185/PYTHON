#File Handling
# Python provides a built-in open() function to interact with files.
#open() function to open a file. It takes two parameters: 
#the path to the file and the mode in which you want to open the file 
#modes--->(read mode, write mode, append mode, 
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode like ......mode=w,r
# "b" - Binary - Binary mode (e.g. images) like ......mode=rb,wb


# #to open file in read mode
# f=open("demo.txt")
# #By default the read() method returns the whole text 
# #print(f.read())

# #return one line by using the readline() method
# #print(f.readline())

# #The readlines() method  read all lines from a file and store them as separate strings in a list.
# print(f.readlines())
# #closing the file
# f.close()


#_________________________
# #in write mode for overwrite it create file if it not exists
# f=open("demo.txt",'w')
# f.write("this is newline it will  overwrite any existing content ")
# f.close()

#________________________________
# #in append mode add extra text to the file and if file not present it create file
# #how many times we execute that much time the text is added
# f=open ("demo.txt",'a')
# f.write("\n this is new line with old lines")
# f.close()

#________________________________
#to creting file it gives error if file already exists
#f=open("demo1.txt",'x')

 
#______________________________
# #deleting file
# #if file not present it gives error
# import os
# os.remove('demo1.txt')


#_______________________________
# #check if file exists
# import os
# if os.path.exists('demo.txt'):
#     os.remove('demo.txt')
# else:
#     print("file not present")


#_______________________________
#Remove the folder "myfolder":You can only remove empty folders.
import os
os.rmdir("myfolder")


