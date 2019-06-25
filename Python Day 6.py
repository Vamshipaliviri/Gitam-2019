#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=10
if (x<30) :
    print("It is less than 30")


# In[4]:


x=100
y=500
if (x<y) :
    print(x,"is less than",y)


# In[10]:


n=int(input("Enter the Number"))
if(n%2==0) :
    print("The Given number",n,"is even ")
else :
    print("The Given Number",n,"is odd")


# In[11]:


x=10
if(x>15):
    print("Hello Good Morning")
else : 
    print("Hello Good Afternoon")


# In[12]:


x=int(input("Enter the number"))
y=int(input("Enter The Number"))
if(x>y):
    print(x,"is Larger than",y)
else:
    print(x,"is lesser than",y)
      


# In[15]:


x=int(input("Enter The Number"))
y=int(input("Enter The Number"))
if(x==y):
    print(" ",x**y)
else :
    print(" ",x*y)


# In[20]:


x=int(input("Enter the Number"))
if(x<0):
    print("It is Negative")
elif(x==0):
    print("It is Zero")
elif(x>0):
    print("It is positive integer")


# In[22]:


x=1
while(x<=9):
    print(x);
    x=x+1;


# In[ ]:


n=-22
while(n>=-45):
    print(n);
    n=n-1;


# In[ ]:


n=-22
while(n>=-45) :
    print(n);
    n=n-1;


# In[1]:


a=2
b=2
c=a+b
print(c)


# In[2]:


n=-22
while(n>=-45):
    print(n);
    n=n-1;


# In[ ]:


#Sum of even Numbers
n=1
sum=0
while(n<=100):
     if(n%2==0):
            sum=sum+n;
            n=n+1;
print(sum)
        
        


# In[33]:


#reversing of Numbers
n=int(input("enter the Number"))
rev=0
while(n>0):
    rem=n%10;
    print(rem)
    n=n//10;
   
    


# In[46]:


#Sum of even numbers
x=int(input("enter the number"))
sum=0
while(x!=0):
    r=x%10;
    if(r%2==0):
        sum=sum+r;
    x=x//10;
print(sum)        


# In[55]:


#Words of the digit in reverse
x=int(input("Enter The Number"))
while(x!=0):
    r=x%10;
    if(r==1):
        print("ONE")
    elif(r==2):
        print("TWO")
    elif(r==3):
        print("THREE")
    elif(r==4):
        print("FOUR")
    elif(r==5):
        print("FIVE")    
    elif(r==6):
        print("SIX")
    elif(r==7):
        print("SEVEN")    
    elif(r==8):
            print("EIGHT")
    elif(r==9):
        print("NINE")
    elif(r==0):
        print("ZERO") 
    x=x//10;
    


# In[56]:


x=int(input("Enter the number"))
y=int(input("Enter the number"))
z=int(input("Enter the number"))
digit=0
c=0
while(y<=z):
    j=y;
    while(j!=0):
        digit=j%10;
        if(digit==x):
            c=c+1;
        j=j//10;
    y=y+1;
print(c);


# In[57]:


3*1**3


# In[76]:


def printnaturalnumbers(n) :
 cnt=1;
 while(cnt<=n):
    print(cnt,end=" ");
    cnt=cnt+1;
 print()
 return


printnaturalnumbers(15);


# In[78]:


#factorial of given number
def fact(n) :
    fact=1;
    while(n!=0):
        fact=fact*n;
        n=n-1;
    print(fact);    
print(fact(5));
print(fact(10));
print(fact(4));


# In[81]:


def countpalindrome(n1,n2)
    cnt=0;
    sum=0  
    while(n1!=n2):
        temp=n1;
    while(n1>0):
        r=n%10;
        sum=sum*10+r;
        n1=n1/10;
        if(temp==sum):
            cnt=cnt+1;
        n1=temp;
    n1=n1+1;
print(cnt)   
return palindrome;

palindrome(1,10)


# In[ ]:




