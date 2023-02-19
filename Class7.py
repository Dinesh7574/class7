#!/usr/bin/env python
# coding: utf-8

# In[6]:


#arguments

def name(fname,mname,lname):
    print(fname)
    print(mname)
    print(lname)


# In[4]:


name("sachien",'ramesh','tendulkar')   #arguments


# In[5]:


name(mname = "sachien",lname = "ramesh",fname="tendulkar") #keyword arguments


# In[7]:


#posistion arg are shoud be in frist and keyword argument should in last 
def name(fname=None,mname=None,lname=None):
    print(fname)
    print(mname)
    print(lname)


# In[8]:


name("sachien",'ramesh')   


# In[13]:


def name(fname,mname=None,lname=None):
    print(fname)
    print(mname)
    print(lname)


# In[14]:


name(mname = "sachien",lname = "ramesh",fname="tendulkar")         #fname = posistion argument


# In[15]:


def add(a,b):
    return a+b


# In[16]:


add(2,1)


# In[59]:


def add(*args):
    print(args)
    print(args[0:3])
    b = 0
    for i in args:
        b= b+i
         
    print(b)
  


# In[60]:


add(1,2,3,4,5,6,7,8,9)


# In[ ]:




