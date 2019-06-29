#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Create a series of numbers by passing a list of values
import pandas as pd
a=pd.Series([1,3,4,5,6,7])
print(a)


# In[9]:


#Missing values then it can na of the numpy
import numpy as np
a1=pd.Series([1,2,3,4,np.nan,6])
print(a1)


# In[10]:


#Create a list of dates with in particular range
dates=pd.date_range('20190601',periods=10)
print(dates)


# In[12]:


a2=pd.DataFrame(pd_random.randn(6,4),index=dates,columns=list('ABCD'))
print(a2)


# In[21]:



a2=pd.DataFrame({'A':1.,
                 'B':pd.Timestamp('20190601'),
                 'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                 'D':np.array([3]*4,dtype='int32'),
                 'E':pd.Categorical(["test","train","test","train"]),
                 'F':"foo"})
print(a2)


# In[22]:


#Step 1: Make All the turtle package to be imported
import turtle as tt
#turtle method creates an dreturns the object
a1=tt.turtle()
#forward method moves 100 pixel
tt.format(100)
tt.done()


# In[ ]:




