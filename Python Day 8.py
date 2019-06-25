#!/usr/bin/env python
# coding: utf-8

# In[2]:


list=["abcd",403,2.03,"Beamers",33.3]
print(list[1:3])


# In[3]:


s="eduzip"
s[2:]


# In[17]:


#binarysearch Program For sorted list
def binarysearch(a,lindex,rindex,key):
    while lindex<=rindex:
        mindex=lindex+(rindex-lindex)//2
        if a[mindex]==key:
            return mindex
        if a[mindex]>key:
            rindex=mindex-1
        else :
            lindex=mindex+1
    return -1;
a=[1,4,8,9,75,82,94,112]
key=int(input("Enter The Element To search"))
res=binarysearch(a,0,7,key)
if res!=-1:
    print("It is Found")
else:
    print("It is Not found")


# In[20]:


#Bubble sort 
def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        print(a[i],end=" ")
        
list1=[3256,234,436,768,345,56]
bubblesort(list1)


# In[ ]:


#insert of numbers into list
def insert(a,n):
    i=0
    while i<=n:
        k=int(input("Enter the elements in a[",i));
        i=i+1
        
n=int(input("How Many elements u want to insert"))
insert(a,n)
print("The Elements are :")


# In[2]:


#string
str="application"
print(str)

str1='application'
print(str1)

str2="""Application Test
        working
        completed
        list
        strings
        Python"""
print(str2)


# In[6]:


str="Application"
print(str)
print("str[0]=",str[0])
print("str[1]=",str[1])
print("str[-3]=",str[-3])
print("str[-2]=",str[-2])
print("str[2]=",str[2])
print("str[2:-2]=",str[2:-2])
print("str[3:5]=",str[3:5])
print("str[:7]=",str[:7])


# In[7]:


s='foo'
t='bar'
print('barf' in 2*(s+t))


# In[12]:


# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
     
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  
  
s=str(input("Enter The Character"))

ans = isPalindrome(s) 
  
if ans == True: 
    print("Yes") 
else: 
    print("No") 


# In[6]:


#count of digits of a number
n=int(input("Enter The Number"))
cnt=0
while n!=0:
    cnt=cnt+1
    n=n//10
print(cnt)    


# In[4]:


def countchars(str):
    return len(str)
s=str(input("Enter a String"))
countchars(s)


# In[2]:


def countdigit(n):
    return len(n)

countdigit("123456789")

#Count of upper case letters
def countOfUpperCaseChars(str):
    cnt=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=65 and ord(str[i])<=90:
            cnt=cnt+1;
        
    return cnt;
         


print(countOfUpperCaseChars('HIknashdghgUIHUIib'))
print(countOfUpperCaseChars('LYTUD'))

# In[13]:


str='H'
str1='i'
str1.islower()


# In[4]:


def printdigits(str):
    return print(str)


str="Applications"
printdigits(str)


# In[14]:


#Displaying the numbers which are present in the string
def printdigits(str):
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            print(lst[x],end="")
    return " "     
          
print(printdigits("Mike testing 123123"))        


# In[13]:


#adding the digits in the strings
def printingdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            a=int(str[i])
            sum=sum+a;
    return sum


print(printingdigits("kdjfh657546hd657"))


# In[20]:


#adding the even numbers in the strings
def evensumdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            a=int(str[i])
            if(a%2==0):
                sum=sum+a;
    return sum            

         

print(evensumdigits("kgf18646hjayhj"))


# In[ ]:




