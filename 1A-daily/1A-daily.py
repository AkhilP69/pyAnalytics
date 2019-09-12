# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:49:45 2019

@author: AKHIL
"""

#Daily Practise File
#-----------------------------
#Data Structures
#%%
list1 = [10,11,12,13,14,15,"x","y","z","a","b", True, False]  #list type of object with data
list1  		              #prints in spyder IDE
type(list1)             #type of object = 'list'
print(list1)            #print when running complete file
list1
#-----------------------------
list2 = ['m','n','o','p','q','r','s']
sorted(list2)           # : ['m', 'n', 'o', 'p', 'q', 'r', 's']
list2.count('m')        # : 1
len(list2)              # : 7
dir(list)               # opens directory : ['__add__','__class__',....,'remove','reverse','sort']
#%%
#tuple - multiple type of objects, immutable: ( round brackets)
tuple1 = (9,8,7,6, 'x', 'y')
tuple1                  # : (9, 8, 7, 6, 'x', 'y')
print(tuple1)           # : (9, 8, 7, 6, 'x', 'y')
type(tuple1)            # : tuple
#%%
#Dictionary - key-value pairs : { curly bracket and colon}
dict1 = {1:'Akhil', 2:'Anil', 3:'Priyanka'}
dict1
type(dict1)
car = { 'brand':'Ford', 'model': 'Hatchback', 'year' : 1998}
type(car)
car
car['brand']
car.get('year')
dir(car)
#%% { curly bracket, comma}
#Set - ordered collection of simple items, immutable
set1 = set(['asia','africa','europe','north_america','south_america','australia'])
set1
type(set1)

set2 = {'ASIA',"AFRICA","ASIA"}  #better way
set2            # : {'AFRICA', 'ASIA'}--> considers only unique values
set3 = {'Australia', 'south_america', 'AFRICA'}
set3
sorted(set3)
set2.union(set3) #set2 | set3
# A.intersection(B)
set2.intersection(set3) #set2 & set  : 'AFRICA'
type(set2)
print(set2)
#%% #Strings : 'single quote'  or "doublequote"
#strings as text in string; imutable
str1 = 'Python'
type(str1)
print(str1)
str2="Akhil"
str2.lower()
#dict?
dir(str)
#%% - Sequence
#sequence - tuple and list are used
list1

#for loop : indentations with colon : Run next 2 lines together
for i in list1:
    print(i,end="\t")   # '\t' puts a tab at the end instead of goign to new line
  
for i in list1:    print(i)
for i in list1[0:5]:    print('Akhil {}'.format(i/10))

tuple1
list5 = ['a',1]
list5
for i in tuple1:
    print(i)
for i in range(1, 100, 2):    print(i, end=' ')
#odd nos between x & y    
#%% frozen ( round bracket, comma)
#frozen set- accepts iterable object as input parameter.
tupleFZ1 = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
type(tupleFZ1)  

# converting tuple to frozenset 
frozenset1 = frozenset(tupleFZ1) 
frozenset1
type(frozenset1)

dict1
frozenset2 = frozenset(dict1)
type(frozenset2)
frozenset2
#keys of dictionary made as frozen set

#%%
#zip - map the similar index of multiple containers 
# initializing lists 
name = [ "Dhiraj", "Kounal", "Akhil", "Pooja" ] 
rollno = [ 4, 1, 3, 2 ] 
marks = [ 90, 50, 60, 70 ] 
# using zip() to map values 
mapped = zip(name, rollno, marks) 
# converting values to print as set 
mapped = set(mapped) 
mapped
namez, rollnoz, marksz = zip(*mapped)
namez


#%%
#numpy - array - same data type
import numpy
numpy.array([10,20])

import numpy as np
np1 = np.arange(1,10)
np.sqrt(np.mean(np.arange(1,10000000)))
np1
type(np1)
np?
dir(np)
np.mean?
np2 = np.array([ 90, 50, 60, 70 ])
np2
np.sort(np2)

np3 = np.array([[1,4],[3,1],[5,6],[10,50]])
np3
np3.shape
np3.reshape((8,-1))
#%%
#pandas - dataframe, excel like
#https://mode.com/python-tutorial/pandas-dataframe/
import numpy as np
import pandas as pd
pd?
dir(pd)
#df = pd.DataFrame({'column':[<column entries>]})
df1 = pd.DataFrame({'rollno':[1,2,3,4], 'name': [ "Dhiraj", "Kounal", "Akhil", "Pooja" ], 'marks':[ 40, 50, 60, 70 ], 'gender':['M','M','M','F']})
df1
type(df1) 

df1.columns
df1.describe()
df1.dtypes
df1.shape  # rows and columns
df1.groupby('gender').size()
df1.groupby('gender')['marks'].mean()
df1.groupby('gender').aggregate({'marks': [np.mean, 'max','min','std','count']})

#%%
#Graphs https://python-graph-gallery.com/
import matplotlib.pyplot as plt
#https://matplotlib.org/
df1.groupby('gender').size()
df1.groupby('gender').size().plot(kind='bar')
plt.hist(df1.marks)

#https://seaborn.pydata.org/index.html
import seaborn as sns
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
iris.head()
iris.tail()
df1.groupby('gender').size()
iris.groupby('species').size().plot(kind='bar')
sns.pairplot(iris)


#%%
#Load Inbuilt Datasets
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars.data.head()

#%%
#Load from Excel/ CSV and export to
data = mtcars.data
data.head()
type(data)
data.to_csv('mtcars.csv')
data.to_excel('mtcarsExcel.xlsx','sheet3', header=False)

#writing to multiple sheets
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
# Write each dataframe to a different worksheet. you could write different string like above if you want
data.to_excel(writer, sheet_name='sheet1')
data.to_excel(writer, sheet_name='sheet2')
# Close the Pandas Excel writer and output the Excel file.
writer.save()

#%%
data.to_excel?
#load from CSV and Excel
data2a
data2a = pd.read_csv('mtcars.csv') #when csv is in project folder
data2b = pd.read_csv('G:/pyWork/pyProjects/pyAnalytics/mtcars.csv')
#csv in any other location - full path
data2b
data2a.head()

data2c = pd.read_excel('test.xlsx','sheet1',header=0)
#header=None
data2c.head()