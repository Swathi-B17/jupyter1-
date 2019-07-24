#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to convert a given  list to a tuple. [5, 10, 7, 4, 15, 3] 

# In[4]:


t1=(5,10,7,4,15,3)
t1


# 2. Write a Python program to get the 4th element from first  and 4th element from last of a tuple. 
# ( "p" , "y" , "t", "h" , "o" , "n" , "p" , "r" , "o" , "g" , "r" , "a" , "m" , "m" , "i" , "n" , "g" )

# In[9]:


t1=( "p" , "y" , "t", "h" , "o" , "n" , "p" , "r" , "o" , "g" , "r" , "a" , "m" , "m" , "i" , "n" , "g" )
t1[3]


# In[10]:


t1=( "p" , "y" , "t", "h" , "o" , "n" , "p" , "r" , "o" , "g" , "r" , "a" , "m" , "m" , "i" , "n" , "g" )
t1[-4]


# 3. Write a python program to find largest number in a given list with out using max() .[10, 7 , 0 ,14 , 4 , 2 ]

# In[19]:


li=(10, 7 , 0 ,14 , 4 , 2) 
def maxElementDS(ds):
    m=0
    for item in ds:
        if item > m:
            m = item
    return m
maxElementDS(li) 


# 4. Write a python program to print all even numbers from a given list .[111 , 4 , 7 , 16 , 27 , 40 , 18 , 99 ,101, 14]

# In[1]:


lst=[111 , 4 , 7 , 16 , 27 , 40 , 18 , 99 ,101, 14]
for i in lst:
    if i%2 ==0:
        print(i)


# 5. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# In[2]:


# Sample Dictionary:{0:10,1:20}
#Expected Result:{0:10,1:20,2:30}
n={0:10,1:20}
n[2]=30
print(n)


# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the              form (x, x*x) 

# In[3]:


#Sample Dictionary ( n = 5) : 

#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
n=int(input("Enter a number"))
d={x:x*x for x in range(1,n+1)}
print(d)


# In[ ]:




