#!/usr/bin/env python
# coding: utf-8

#   # Document Title
#   
#   ### Date:20 july 2019
#   
#   ### Session objectives
#   * to introduce Jupiter notebooks
#   * to teach ***markdown*** syntax
#   * to introduce **python** basics
#     * Basic Syntax(Variables,Assignment,Data Types)
#     * Control Structures
#       1. conditional
#       2. Repetitive
#  
#   <img src='data:image/jpeg;base64,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'/>
#   
#   link to main website:basicshttps://sites.google.com/s/1yeSSGH522DNWzca4ax_U65K66pmssyta/p/1EAIny72NQRVcWDHW8zV4T_fDqtauHzVe/

# ### python Basics

# In[6]:


print("Hello world !")
print("Hello","world " , end=" ")
print("Hello"+"world ")


# In[8]:


#This is a comment

n = input("Enter a value")
print('\n', n)


# In[ ]:



