#!/usr/bin/env python
# coding: utf-8

# In[2]:


str="Vamshi"
print(str.upper())
print(str.lower())


# In[4]:


s="Python is easy Programming"
s1="python"
print(s.islower())
print(s1.islower())


# In[7]:


s="Application"
s1="python"
print(s.isupper())
print(s1.isupper())


# In[8]:


s="Application"
s1="App1889"
print(s.isalpha())
print(s1.isalpha())


# In[9]:


s="Python programming"
s1="Python Programming"
print(s.istitle())
print(s1.istitle())


# In[17]:


s=" "
s1="Hi hello"
print(s.isspace())
print(s1.isspace())            #ASCII  number for space character is 32


# In[16]:


str="pythON"
str1="74649"
print(str.isnumeric())
print(str1.isnumeric())


# In[44]:


str="P* y* t* h* o* n"
print(" ".join(str))


# In[30]:


print("->".join(["python","programming","Easy"]))


# In[34]:


str1="kjdhg kjerhg jherdasdf hjkl"
print(str1.split('j'))


# In[42]:


s="Python Programming is easy to learn"
lst=s.split()
print(lst)
print(lst.index('is'))


# In[48]:


str="P* y* t* h* o* n"
print(str.split('*'))


# In[54]:


s="Python Programming"
print(s.replace("gra","Application"))


# In[55]:


str="Python Programming"
print(str.replace("Programming","Coding"))


# In[58]:


###TUPPLES
t1=("python","programming",1898,2019,"Machine learning","AI")
print("t1[0]=",t1[0])
print("t1[2]=",t1[2])
print("t1[-1]=",t1[-1])
print("t1[0:3]=",t1[0:3])
print("t1[-2][-1]=",t1[[-2][-1]])


# In[59]:


t1=("Python","Programming")
t2=("AI","HG","JHG")
t3=t1+t2
print(t3)


# In[60]:


t1=("pyt","on","c","qwerty")
t2=(67463276,64,46546,456865,65,6)
print(max(t1))
print(max(t2))
print(min(t1))
print(min(t2))
print(sum(t2))


# In[63]:


t1=(1,2,3,4,5)
t2=(6354564,64648,56486,654,86)
print(t1)
print(t2)
a=cmp(t1.t2)


# In[65]:


list1=["python","programming","6568","6834","Hello"]
print(list1)
t=tuple(list1)
print(t)


# In[71]:


#Dictionary
User1={'Name':'Vamshi','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066'}
print("User1[Name]=",User1['Name'])
print("User1[Email]=",User1['Email'])
print("User1[Age]=",User1['Age'])
print("User1[Mobile]=",User1['Mobile'])


# In[72]:


#Dictionary
User1={'Name':'Vamshi','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066','Address':'Hyderabad'}
print("User1[Email]=",User1['Email'])
print("User1[Address]=",User1['Address'])


# In[81]:


#Dictionary
User1={'Name':'Vamshi','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066'}
del User1['Email']
print(User1)


# In[82]:


#Dictionary
User1={'Name':'Vamshi','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066'}
User2=User1.copy()
print(User1)
print(User2)
User1['Address']='Hyderabad'
print(User1)
print(User2)


# In[87]:


User1={'Name':'Vamshi','Age':18,'Email':'Vamshi@gmail.com','Mobile':'9110528066'}
User2=User1.copy()
print(User1.values())
print(User2.values())


# In[90]:


#String Formatting
lst=["Python","Programming"]
print("%s %s"%(lst[0],lst[1]))


# In[97]:


list=["python","hyderabad","gitam"]
print("{0},{1},{2}".format(list[0],list[1],list[2]))


# In[92]:


print('abcdefcdghcd'.split('cd,2'))


# In[105]:


#Saving Contacts
contacts={}
def addContact(name,phone):
    if name not in contacts:
        contacts[name]=phone;
        print("Contact %s Added Successfully"%name)
    else:
        print("Contact %s already Exists"%name)
    return

addContact("Anil",91234567890)
addContact("Harsha",9963686540)
addContact("Anil",91234567890)
    


# In[108]:


#Searching
def searchContacts(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("%s does not exists"%name)
    return
searchContacts("Anil")
searchContacts("Ajay")
searchContacts("Harsha")
searchContacts("Kranth")


# In[111]:


#New Contacts is given as Dictionary
def importContacts(newContacts):
    contacts.update(newContacts)
    print(len(newContacts.keys()),"Contacts Added successfully")
    return 
newContacts={'Dinesh':9632147859,'Ajay':9988774455}
importContacts(newContacts)


# In[112]:


print(contacts)


# 

# In[123]:


#Delte a contact from My Contact List 
def deleteContact(name):
    if name in contacts:
        del contacts[name]
        print(name," is deleted from the contacts ")
    else:
        print(name,"is not existing in the contacts")
    return
deleteContact('Anil')
deleteContact('Naveen')


# In[121]:


print(contacts)


# In[127]:


def updateContact(name,phone):
    if name in contacts:
        contacts[name]=phone;
        print( name,": updated with new phone number")
    else:
        print(name,"not exists in the contact" )
    return ;
updateContact("Ajay",5648738309)
updateContact("anilesh",76436743838729891)
updateContact("rajesh",76436743838729891)


# In[125]:


lst=[1,2,3,4]
print("Value at :{0} value at :{1}".format(lst[0],lst[1]))
print("value at :{0} value at :{1}".format(lst[2],lst[3]))


# In[128]:


from math import floor as f1
f1(123.456)


# In[129]:


from math import factorial as fact
fact(5)


# In[131]:


import math
math.factorial(7)


# In[137]:


import random
def generateRandomNumbers(n,ll,ul):
    for i in range(0,n):
        print(random.randint(ll,ul),end=" ")
    return;
generateRandomNumbers(5,500,1000)


# In[ ]:





# In[ ]:




