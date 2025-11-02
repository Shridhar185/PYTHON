#numpy is an numerical python 





#for using multidimensional array we use numpy
#numpy provide efficeint storage
#it is fast about 50 times

#array is of same datatype and size is static 
#we store data in form of array  and its memory in contiguous block of memory
""" 
import numpy as np
arr1=[1,2,3,4,44]
print(arr1)        #it prints it as a list, as it is 
print(type(arr1))    #it shows type of data
arr2=np.array(arr1)
print(arr2)        #it prints it as array of same datatype, if only one string present then convert all to string,same for float
print(type(arr2))
 """



""" 
import numpy as np 
print(np.array([2,3,4,4.5,6,'7',99]))   #the single quote and double quote are same we cannnot differntiate as char and string 
print(np.array([2,3,4,4.5,6,'7',99],dtype=int))   #convert any type into int 
print(np.array([2,3,4,6,99],dtype='str')) 
print(np.array([2,3,4,6,99],dtype='U32'))        #to convert to char
print()
list1=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(list1))
print()

print(np.arange(1,8))                   #prints 1 to 7
print(np.arange(1,7).reshape(2,3))      #both elements and number of rows and columns should be compatible 
print(np.zeros(5))                      #print 5 float zeroes
print(np.ones(8))
print()
print(np.zeros((3,4)))                  #print zeroes in 3 rows and 4 columns,note there should be 2 brackets
print()
 """




#using attributes
""" import numpy as np 
arr3=np.arange(1,8)
print("dimension: ",arr3.ndim)          #prints number of dimensions
print("shape: ",arr3.shape)             #give no of elements as (7,) because 1 dimension 
print("datatype: ",arr3.dtype)
print("size: ",arr3.size)
print("item size: ",arr3.itemsize)      #give 4 because int is of 4 bytes,give 8 for float
print()

list1=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(list1)
print("dimension: ",arr.ndim)                         #prints number of dimensions of matrix--->2
print("shape: ",arr.shape) 

arr1=np.array([[[2,3],[4,6]]])
print(arr1)
print("dimension: ",arr1.ndim)                          #it is 3 dimension 
print("shape: ",arr.shape)                       
print()
arr2=np.array([[[2,3],[4,6]],[[3,8],[5,8]]])
print(arr2)
print("dimension: ",arr2.ndim)                          #it is 3 dimension 
print("shape: ",arr2.shape)                        
arr2=np.array([[[2,3,7],[4,8,6]],[[3,80,8],[5,67,8]]])                          
print("dimension: ",arr2.ndim)
print("shape: ",arr2.shape)                                       #no of layers, no of rows,no of columns
  """




#indexing numpy array 
""" import numpy as np
arr=np.arange(10)
print(arr)        #---->0 to 9
print(arr[5])     #value at 5h index
print(arr[5:8])   #values 5,6,7
arr_slice=arr[5:8]
arr_slice[1]=123      #change value at 6h index
print(arr)
arr_slice[:]=85       #change all 3 index values to 85
print(arr)
"""





""" 
import numpy as np
arr=np.arange(9).reshape(3,3)
print(arr)
print(arr[1,2])      #2nd row, 3rd column value
print()
print(arr[:2])       #print 0 and 1 row
print()
print(arr[2:])       #print 2nd row onwawrds
print()
print(arr[1,:2])     #print 2nd row upto 2columns
print() 
print(arr[:2,1:])    
 """




""" 
import numpy as np
names=np.array(['ram','raj','ravan','rat','cat','ram'])
data=[names=='ram']            #chekcs is ram is pressent in each index in names
print(data)                    #based on above checks it gives true or false
data=[names!='ram']
print(data)                    #give true where ram not present
 """



#swappint axes and transposing
import numpy as np
arr=np.arange(9).reshape(3,3)
print(arr)
print()
print(arr.transpose())       #converts row into columns and vice versa
arr=np.arange(8).reshape(4,2)
print(arr)
print()
print(arr.swapaxes(0,1))     #converts columns into rows









 
 





































