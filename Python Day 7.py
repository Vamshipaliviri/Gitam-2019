#!/usr/bin/env python
# coding: utf-8

# In[1]:


#factorial using recursion

def fact(n) :

     if n==0:
       
        return 1 
   
     else :
       
        return n*fact(n-1)


n=int(input("Enter The Number"))

result=fact(n)

print("The factorial of",n,"is",result)


# In[4]:


#python programming for printing the fibonacci series upto nth term

def fibonacci(n):

    if(n==1):

        return 1
 
    elif(n==2):

        return 2

    elif(n>2):

        return fibonacci(n-1)+fibonacci(n-2)




n=int(input("Enter the Number"))

print(fibonacci(n))


# In[5]:


#to compute the gcd value using recursion 

def gcd(a,b):

    if(b==0):

        return a

    else:

        return gcd(b,a%b)




num=int(input("Enter The Number"))

n=int(input("enter The Number"))

print(gcd(num,n))
    


# In[6]:


#power of the number using recursion python

def power(a,b):

    if b==1:
       
       return a
    
    return a*power(a,b-1)



num=int(input("Enter The Number"))

n=int(input("Enter The power"))

print("",power(num,n))
    


# In[ ]:


#sum of even number
def printeven(n):  
    cnt=0;
    sum=0;
    while(cnt!=n):
        if(cnt%2==0):
        sum=sum+cnt;
        cnt=cnt+1;
  return sum;
        
print(printeven(20));    
print(printeven(7));


# In[16]:


def factlist(n):
    i=1;
    while(i!=n):
      if(n%i==0):
        print(i,end=" ");
      i=i+1;
    return i;
factlist(12);


# In[19]:


#List  
list1=[1,2,3,4,5];
print(list1)
print(list1[0])


# In[20]:


list2=["Akhil","Vamshi","Sai Teja"]
for x in list2:
    print(x);


# In[25]:


#List example with particular index
list1=[1,2,3,4,5,6,7]
for x in list1:
    print(x,end=" ")
    
print();
print(list1[4]);
print(list1[3:6]);
print(list1[0:7]);
print(list1[:5])


# In[33]:


list1=[1,2,3,4,5,6,7,8,9,10]
for x in list1:
    print(x,end=" ")

print();
print(list1[1:-1]);
print(list1[2:-2]);
print(list1[::2]);
print(list1[::3]);


# In[32]:


list1=["Vamshi","Sai surya","Sai teja"]
print(list1);
list1[2]=15;
print(list1);
list1[1]=12;
print(list1);
del list1[0]
print(list1)
list2=[1,2,3];
print(list2);
print(list1+list2);


# In[39]:


#Adding a number to list
list1=[1,2,3,4,5,6,7,8,9]
print(list1);
list1[3]="abcg";
list1[4]="hi";
del list1[2];
list1.append(124);
print(list1);


# names1=["amir","barry"]
# loc=names1.index('edward')
# print(loc)

# ggt
# 

# In[51]:


list1=["gitam","python",1,5,"programming"]
print(list1)
n=list1.index("python");
print(n)
list1.index(1)
print(len(list1))
list1.insert(2,"hi")
list1.append("bye")
print(list1)
list1.pop(4)
print(len(list1))
list1.insert(4,"hello")
print(list1)


# In[53]:


list1=["gitam","python",1,5,"programming"]
print(list1)
n=list1.index("python");
print(n)
list1.index(1)
print(len(list1))
list1.insert(2,"hi")
list1.append("bye")
print(list1)
list1.pop(4)
print(len(list1))
list1.insert(4,"hello")
print(list1)
list1.reverse()
print(list1)


# In[55]:


#linear search
def linearsearch(a,key):
    flag=0;
    for i in range(len(a)):
        if a[i]==key:
            flag=1;
            break
    if(flag!=0):
        print("Target is Found")
    else:
        print("target is not found")

a=[1,4,2,8,54,78,34,56,32]
key=int(input("Enter The Number to search"))
linearsearch(a,key)
 


# In[59]:


#Duplicate linear search
def linearsearchdup(a,key):
    flag=0;
    for i in range(len(a)):
        if a[i]==key:
            flag=flag+1;
            
    print(flag)        
    if(flag!=0):
        print("Target is Found")
    else:
        print("target is not found")

a=[145,576,423,76,432,7,875,543]
key=int(input("Enter The Number to search"));
linearsearchdup(a,key)
 


# In[72]:


#binary search 
def binarysearch(list1,key):
    low=0;
    high=len(list1)-1;
    found=false;
    while low<=high and not found:
        mid=(low+high)//2;
        if(key==list1[i]):
            found = true;
        elif key<list1[mid]:
            low=mid+1;
        else key>list1[mid]:
            high=mid-1;
    if(found==true):
        print("element is found");
    else:
        print("Element Not found");
        
list1=[564,654,465,6546,5]     
key=int(input("Enter the Number"))
binarysearch(list1,key):
        


# In[75]:


def linearexample(a,key):
    for i in range(len(a)):
        if a[i]==key:
            print(i,end=" ")

a=[1,2,3,4,5,6,7,8]
linearexample(a,5)


# In[103]:


def linearexample(a,5):
    for i in range(len(a)):
        if a[i]==key:
            j=0
            while j!=i+1:
                print("!",end=" ");
                j=j+1
            print(end=" " );
   



a=[1,5,5,3,76,5,6,5,4,5,6,4]
linearexample(a,5)
    
    


# In[99]:


def linearexample(a,key):
    for i in range(len(a)):
        if a[i]==key:
            print(i,end=" ")

a=[1,2,3,4,5,6,7,8]
linearexample(a,5)


# In[100]:


def linear1(a):
    sum=0;
    for i in range(len(a)):
        if(a[i]%3==0 and a[i]%5==0):
            sum=sum+a[i]
    print(sum)
a=[15,12,2,9,18,36,45]
linear1(a)


# In[106]:


def linear2(a):
    for i in range(len(a)):
        if i==0 or i==(len(a)-1):
            print(a[i],end=" ")
        else:
                print(a[i-1]*a[i+1],end=" ")
    print(a[i])
    
    
    
a=[1,2,3,4,5]    
linear2(a)
    
    


# In[107]:


def linear3(a):
    for i in range(len(a)):
        if i==0 or i==(len(a)-1):
            print(a[i],end=" ")
        elif(a[i-1]%2==0 and a[i+1]%2==0):
            print(a[i],end=" ")
        else:print(end=" ")
            
a=[1,6,9,4,16,19,22]    
linear3(a)         


# In[ ]:





# In[1]:


def conversion(n):
    list=[];
    while n!=0:
        r=n%10;
        list.append(r);
        n=n//10
    list.reverse()
    return list
    
n=int(input("ENTER A NUMBER"))
print(conversion(n))


# In[3]:


def linear8(a):
    sum=0;
    i=0;
    for i in range(len(a)):
        sum=sum+a[i];
        i=i+1
    print(sum)
a=[1,6,9,4,16,19,12]    
linear8(a)


# In[4]:


sum(a)


# In[ ]:





# In[ ]:





# In[ ]:




