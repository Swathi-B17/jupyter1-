#!/usr/bin/env python
# coding: utf-8

# In[10]:


n=input('enter any value:')
n = int(n)#Type conversion to integer and reassign
n = n / 1231-124323874 # Expression evaluation using


# In[11]:


print("Hello world")#Single Parameter
print('Hello' + 'world')
print()


# In[12]:


a = b = c = 10 #Assigning a single value to multiple variable
a
print(a, b, '\n',c)
c
d, e, f = 123, 234, 345 #Assigning multiple values to multible variables
print(d,type(d), e, f)


# In[14]:


#Type conversions
print(type(n))
c= str(c)
print(type(c))
c= float(c)
print(type(c))


# 
# ### String slicing

# In[15]:


s1='Python programming'
s1[0] #Accessing the first character


# In[16]:


s1 = 'Python programming'
s1[-1] #Accessing the last character


# In[20]:


s1 ='Python programming'
s1[0:6] #Accessing the first six characters
s1[:6]


# In[18]:


s1[7:] #Accessing all characters from 7th index to last


# In[19]:


s1[7:len(s1)]


# In[25]:


# Reverse of a string
s1[::-1]


# In[23]:


s1[5::-1]


# In[24]:


s1[-1:6:-1] #Reverse of a substring


# In[12]:


s1[::-1]


# In[26]:


s2 ='123456789'
s2[-1:2:-1] #Reverse of last length of (s2)-3characters


# In[27]:


s2[5:2:-1] #Reverse of characters from index 5 to index 3


# In[28]:


s2[0::2] #Accessing alternate characters


# In[29]:


s2[0::3]


# In[30]:


s2[1::2]#Accessing even characeters


# In[32]:


s2[-1::-2]#Alternate characters in reverse order


# Functions in python

# In[34]:


Function to reverse string
def reverseString(s):
    return s[-1::-1]

reverseString(s2)


# In[36]:


print(reverseString(s2))
reverseString(s1)


# In[38]:


#Function to reverse asub string
def reverseSubstring(s, i, j):
    sub = s[i:j+1]
    return sub[::-1]

reverseSubstring('abcde', 0, 2)


# Conditional Control Structures

# In[44]:


#Function to test divisibility by 9 and not 10
def divisibilityTest(n):
    if n % 9 == 0 and n % 11 == 0 and n % 10==0:
        return True
    else:
        return False
    
divisibilityTest(990)


# In[45]:


# Recursive  Function for a power n

def powerN(a,n):
    if n == 0:
        return 1
    return a * powerN(a, n-1)

powerN(2, 6)


# In[19]:


#Function to check if a given string is a palindrome

def ispalindrome(s):
    if(s == s[::-1]):
        return True
    else:
        False
    
    isPalindrome('racecar')


# ### Iteration in python

# In[49]:


for i in  range(123,126):
    print(i)


# In[50]:


#Function to determine all numbers divisible by 
#7 in a given range [lb,ub]


def divisible7(lb, ub):
    for i in range(lb, ub +1):
        if i % 7 ==0:
            print(i)
    return

divisible7(1,70)
    


# In[60]:


# Function to generate N Prime numbers
from math import sqrt,floor
def isFactor(dividend, divisor):
    if dividend % divisor==0:
        return True
    
def isPrime(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if isFactor(n,i):
            return False
        return True
    

def genPrimes(k):
    primeCounter = 0
    seqCounter = 2
    while primeCounter < k:
        if isPrime(seqCounter):
            print(seqCounter, end=' ')
            primeCounter += 1
        seqCounter += 1
        
genPrimes(100)       


# ### Higher Order Computation

# In[9]:


num = 987 ** 987
print(type(num))
len(str(num))


# ### Python lists

# In[62]:


li=[1,2,3,4,5,6]
li


# In[63]:


li[-1]


# In[65]:


li=[1,2,3,4,5,6, 'python',5.6]
li


# In[66]:


li[-2:]


# In[67]:


li[6][0]


# In[68]:


type(li[6][0])


# In[69]:


li.append(123)
li
         


# In[70]:


li.append([321,543,765])#Adding an element to the list
li


# In[71]:


li.remove(5.6)#Deleting an element from the list specify the character
li


# In[1]:


li[8].remove(543)
li


# In[72]:


li.pop(3)#Removing an element from the list


# In[74]:


li.pop(6)
li.pop(-1)
li.sort()#Either ascending or Descending order
li


# In[4]:


li[8].insert(1, 543)
li


# In[ ]:




