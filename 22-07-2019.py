#!/usr/bin/env python
# coding: utf-8

# In[46]:


#Define a function to perform sum of natural numbers


def naturalnum(n) :
        n=(n*(n+1)/2)
print(round(n))
        
naturalnum(30)


# In[39]:


#Using String slicing reverse the middle characters of ur mobile number

B = '9515306420'
B[5:3:-1]


# In[52]:


#Define a function to print Armstrong number
def arm(num):
    count=0
    n=num
    while(n>0):
        rem=n%2
        count=count=rem**3
        n=n/10
    if(num==count):
       print(num,"is armstrong")
    else:
         print("is not armstrong")
arm(789)    


# In[ ]:




