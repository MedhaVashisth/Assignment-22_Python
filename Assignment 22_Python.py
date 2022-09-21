#!/usr/bin/env python
# coding: utf-8

# In[2]:


X = "iNeuron"
def func():
    print(X)


# In[3]:


func()


# In[4]:


X = "iNeuron"
def func():
    X='Nl!'


# In[6]:


func()
print(X)


# In[7]:


X = "iNeuron"
def func():
    X='Nl'
    print(X)


# In[8]:


func()
print(X)


# In[9]:


X = "iNeuron"
def func():
    X='Nl'
def nested():
    print(X)
    nested()


# In[10]:


func()
X


# In[12]:


def func():
X ='Nl'    
def nested():
nonlocal X
X = 'Spam'
nested()
print(X)


# In[13]:


func()


# In[ ]:




