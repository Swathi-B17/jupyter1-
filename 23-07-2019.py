#!/usr/bin/env python
# coding: utf-8

# ### Day 7
# ### Date:23-07-2019
# ### Day Objectives
# 
# *Tuples
# 
# *Dictionaries
# 
# *Linear and Binary Search
# 
# *Data Arithmetic
# 
# *Iterations and Generations
# 
# *Functional Programming

# #### Python Tuples

# In[1]:


t1 = (1001,'name', 72, 90)


# In[2]:


t1


# In[3]:


t1[0]


# In[4]:


t1[2:]


# In[8]:


t2 =(321,654,789098)
#Accessing all the second digits of elements in a list
print(str(t2[0])[1] , str(t2[1])[1] ,str(t2[2])[1])


# In[9]:


t2 =(321,654,789098)
#Accessing all the second digits of elements in a list
print(str(t2[0])[1]+str(t2[1])[1]+str(t2[2])[1])


# In[10]:


#Function to calculate the Average of all elements in a tuple
def averageTuple(t):
    sum = 0
    for i in range(0, len(t)):
        sum += t[i]
    return sum/len(t)

averageTuple(t2)
    


# In[11]:


def averageLinearDS(t):
    sum=0
    for i in range(0, len(t)):
        sum+= t[i]
    return sum/len(t)

li = [123,243,456,678,890]

averageLinearDS(li)


# In[14]:


#Function to search in a Linear Data Structure

def searchLinearDS(ds,key):
    for i in range(0, len(ds)):
        if ds[i] ==key:
            return i
    return -1
    
searchLinearDS(li, 456)
    


# In[ ]:


#Function to calculate the Average of all elements in a tuple
def averageLinearDS(t):
    sum = 0
    #for i in range(0, len(t)):
    #    sum += t[i]
    for item in t:
        sum += item
        return sum/len(t)
    
        


# ### Iterable Objects
# 
# 

# In[15]:



s="python"
for i in s:
    print(i)


# In[17]:



s="python"
for i in s:
    print(i,end='')


# In[20]:


#Function to identify the maximum elements in a DS using Iterable Object

#def maxElementDS(ds):
#m
max[123,456]


# In[19]:


def maxElementDS(ds):
    m=0
    for item in ds:
        if item > m:
            m = item
    return m
maxElementDS(li)


# In[22]:


def maxElementDS(ds):
    m=ds[0]
    for item in ds:
        if item < m:
            m = item
    return m
maxElementDS(li)


# ### Python Dictionaries

# In[26]:


d1 = {'name1':1234567789,'name2':3214567891}
d1['name2']


# In[25]:


d1.keys()#All keys in a dictionary are unique


# In[27]:


d1.values()


# In[28]:


print (d1['name2'])


# In[29]:


d1['name3']=654987416
d1


# In[30]:


d1.pop('name3')#removes a key and value 
d1


# In[32]:


#Contact Application
#Display,Add, Modify and Delete contacts

contacts = {}

def addContact(d,name, phone):
    d[name]=phone
    return

addContact(contacts, 'name1',3149565648)

def displayContacts(contacts):
    for name,phone in contacts.items():
        print(name,":",phone)
    return
    
    


# In[33]:


addContact(contacts,'name2',565621546)
addContact(contacts,'name1',315785156)


# In[34]:


displayContacts(contacts)


# In[39]:


contacts = {}

def addContact(d,name, phone):
    d[name]=phone
    return

addContact(contacts, 'name1',3149565648)

def displayContacts(contacts):
    for name,phone in contacts.items():
        print(name,":",phone)
    return
def modifyContacts(contacts,name,newphone):
    contacts[name] = newphone
    return


# In[40]:


addContact(contacts,'name2',565621546)
addContact(contacts,'name1',3156)


# In[41]:


displayContacts(contacts)


# In[ ]:





# In[42]:


contacts = {}

def addContact(d,name, phone):
    d[name]=phone
    return

addContact(contacts, 'name1',3149565648)

def displayContacts(contacts):
    for name,phone in contacts.items():
        print(name,":",phone)
    return
def deleteContact(contacts,name):
    contacts.pop(name)
    return


# In[43]:


addContact(contacts,'name2',565621546)


# In[44]:


displayContacts(contacts)


# ### looping over collections

# In[46]:


colors=['red','blue','white']
for i in range (len(colors)-1,-1,-1):
    print(colors[i])


# In[47]:


contacts.items()


# In[50]:


li2=[1,2,3,4,50]
li2=list(reversed(li2))

type(li2)

li2


# In[52]:


li2=[1,2,3,4,50]
li2.reverse()


# In[ ]:


### Regular Expression


# [0-9]Regular Expression for all single digits
# [0,1,2,3,....9]
# 
# 
# 
# 
# [a-z]Regular Expression for all lowercase alphabet
# [A-Z]Regular Expression for all uppercase alphabet
# 
# [01]

# In[ ]:


# Function to validate college student roll no
# Function to validate indian numbers starting 9,8,7 ,6and have 10 digits
# Function to validate email address
    username@domain.extension
    username={string of length 9.can contain digits,_,alphabet}
    domain={string of 9.can contain digits and alphabet}
    extension ={length of 3.Only alphabet}


# In[56]:


import re
n=input('enter number')
m=re.fullmatch("[6-9]/d{9}",n)
if m!=None:
    print("valid mobile number")
else:
    print("invalid mobile number")


# In[ ]:


[9876][0-9]{9}#logic for mobile number checking in Rex


# In[ ]:


^[a].{5}[a]$ #logic for email checking

