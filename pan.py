# string.py file in the same directory as your code, it might cause conflicts 

# object is a base class for all classes. 

#prints indexes with values and datatype of values 


import pandas as pd
ob=pd.Series([6.0,4,3,4])  #other than int and float it shows datatype as object
print(ob)                  #if 1 float value then converts all to float
              


#[3, 4, 5, 6]: This is a list of values. 
#index=['a', 'b', 'c', 'd']: This specifies the index labels associated with each value
#at everytime when it prints like table it also prints it datatype of values

""" 
import pandas as pd
ob=pd.Series([3,-4,5,6],index=['a','b','c','d'])
print(ob)
print(ob.values)           #give [3, 4, 5, 6]
print(ob.index)            #give Index(['a', 'b', 'c', 'd'], dtype='object')
print(ob['a'])             #give value at 'a' index label--->3
print(ob[['a']])           #give index label and value
print(ob[['a','d']])       #print as table with specified index labels and values
print(ob*2)                #multiply each values by 2
print(ob>0)                #check each value greater than 0 or not, based on that give true or false in place if values
print(ob[ob>0])            #print only values greater than 0
print('a' in ob)           #check indexlabel present or not in ob--->true
 """




""" 
import pandas as pd
labl=['a','b','c','d']
sdata=[1,2.2,'3',"rot"]
ob=pd.Series(sdata,index=labl)       # -->not prints values because not assign,if above line not present 
print(ob) 
 """






""" 
import pandas as pd
sdata = {'abc': 35000, 'ram': 71000, 'raj': 16000, 'ravan': 5000}
obj =pd.Series(sdata)
print(obj)                   #it treats keys as indexlabels 

#ways to check null values present or not
print(pd.isnull(obj))        
print(obj.isnull())
 """



 



""" 
#it prints it as table keys are column names and indexes are side numbers
import pandas as pd
import numpy as np
dict1 = {'name': ['ram', 'ravan', 'raj'],
         'usn': ['cs1', 'cs2', 'cs3'],
         'cgpa': [10, 7, 4]}
#df = pd.DataFrame(dict1)
#df = pd.DataFrame(dict1,columns=['usn','name','cgpa'])                     #by using columns we can change sequence of columns
df = pd.DataFrame(dict1,columns=['usn','name','cgpa'],index=[1,2,3])        #we can also specify indexlabel,if no of labels not compatible then give error
#print(df)
#print(df['name'])                   #print all names  and column name and datatype
#print(df.columns)                   #prints all column names and datatype

#add new column...........
#df['fees']=50000                     #for all fees will be same
#print(df)
#df['div']=['a','b','c']             #adding column with own values
#print(df)
#df['fees']=np.arange(3)             #fees will be 0 1 2
#print(df)
df.insert(2,'div',['a','b','c'])     #to add column at particular position 
print(df)

#to delete a column..............
#del df['div']
#print(df)

#to add new row..................
#df.loc[4]=['cs4','karna','8',50000]   #if we give same index which is present already then it update all those values
#print(df)

#selecting a row by indedxlabels.................
#print(df.loc[1])           #give info about index label 1
#print(df.loc[[1,3]])

#to delete a row---->not working
#df.drop(2)
#print(df)

#to update values by using indexlabel and column number
#df.loc[2,'cgpa']=5
#print(df)
#df.loc[[1,3],'fees']=[25000,25000]   #to update multiple rows
#print(df)

#to rename a column name----->not working
#df.rename(columns={'name':'stu_name'})
#print(df)
 """











 
""" 
#to read from csv file 
import pandas as pd
df=pd.read_csv('movies.csv')
print(df)
#operations on dataframes

 """






#handling null values 


import pandas as pd
import numpy as np
dict1 = {'name': ['ram', 'ravan', 'raj'],
         'usn': ['cs1', np.nan, np.nan],      #here 1 null value
         'cgpa': [10, 7, 4]}
df = pd.DataFrame(dict1)
print(df)
print(df.isnull())               #check null values present in table
print(df.isnull().sum())         #give number of null values in each column
print(df.isnull().sum().sum())   #check number of null values in table



""" 
import pandas as pd
from numpy import nan as na
data=pd.Series([1,na,3,4,na,5])
print(data)

#display which not contain null values
print(data.dropna())                 
print(data[data.notnull()])    

#filling the null values      
print(data.fillna(0))
#print(data.fillna(data.mean()))    #replace null value with mean of column values
#print(data.fillna(method='pad'))    #null filled with previous value
print(data.fillna(method='bfill'))    #null filled with next value
 """




""" 
import pandas as pd
from numpy import nan as na
data1=pd.DataFrame([[1,23,45,6],[na,na,67,na],[na,34,56,34]])
print(data1)
print()
print(data1.dropna())         #prints rows which not contain null values   
print()
#filling the null values
print("replacing null values with other values")
print(data1.fillna(0))             #replace null values  with 0
print(data1.fillna('null'))        #replace null values with null
#filling different values in null in different column
print(data1.fillna({1:25,0:100}))  #fill 100 in null values of 1 column and 25 in 2 column
 """




#merging and concatating differnt dataframes ?????.........
#pivot......
#spicy











#traspose........................
""" 
import pandas as pd
# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6],'C':[7,8,9]}
df = pd.DataFrame(data)

# Transpose the DataFrame
transposed_df = df.T

print("Original DataFrame:")
print(df)
print("\nTransposed DataFrame:")
print(transposed_df)
 """





#swapping......................................
""" 
import pandas as pd
# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6],'C':[7,8,9]}
df = pd.DataFrame(data)

# Swap the axes
swapped_df = df.swapaxes(0, 1)
transposed_df = df.T
print("Original DataFrame:")
print(df)
print("\nTransposed DataFrame:")
print(transposed_df)
print("\nSwapped Axes DataFrame:")
print(swapped_df)
 """








""" 
import pandas as pd
data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
data2 = {'ID': [2, 3, 4], 'Age': [25, 30, 22]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the DataFrames based on the 'ID' column
merged_df = pd.merge(df1, df2)
print(merged_df)
 """







""" 
import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-20'],
    'Metric': ['A', 'B', 'c', 'd'],
    'Value': [10, 20, 30, 40]
}

df = pd.DataFrame(data)
print(df)
# Pivot the DataFrame
pivoted_df = df.pivot(index='Date', columns='Metric', values='Value')
print(pivoted_df)
 """







