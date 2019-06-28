#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
sum=0
pattern='back'
if re.match(pattern,'backup.txt'):
    sum+=1
if re.match(pattern,'text.back'):
    sum+=2
if re.search(pattern,'backup.txt'):
    sum+=4
if re.search(pattern,'text.back'):
    sum+=8
print(sum)    
         


# In[2]:


class className:
    #variables--Data(memory)
    #some functions and variables
    #Function-Used to perform the specific activity


# In[3]:


class demo:
    def test(self):
        print("test() for the class and method")
        return    
obj=demo()
obj.test()


# In[4]:



def test():
    print("Test() for function")
    return
test()


# In[5]:


class demo1:
    def fact(self,n):
        #return the factorial
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
        return fact
    
p1=demo1()
print(p1.fact(5))


# In[6]:



class demo2:
    def accept(self,p1,p2):
        self.p1=p1
        self.p2=p2
        return
    def display(self):
        print()


# In[9]:


class demo2:
    def __init__(self,p1,p2):        
        self.p1=p1
        self.p2=p2
        
    def add(self,p1,p2):
        return p1+p2
    
c1=demo2(10,20)
print(c1.add(100,200))


# In[19]:


#Some inheritence
class Person(object):
    #constructor
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
#Derive Class
class Employee(Person):
    def isEmployee(self):
        return True
emp=Person("TEJAS")
print(emp.getName(),emp.isEmployee())
emp1=Employee("TEJA")
print(emp1.getName(),emp1.isEmployee())


# In[21]:


import numpy as np
lst=[1,2,3,4]
array==np.array[lst]
print(array)


# In[34]:


import soundfile
import threading
import sys
import numpy 
lst=[1,2,3,4]
a=numpy.array(lst)
print(a)
#print(array.shape)
#print(array.dtype)


# In[36]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
array+10
print(array)


# In[37]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1)
a1.reshape(3,2)


# In[ ]:




