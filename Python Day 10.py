#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Function to create a file and write some data 
def createfile(filename):
    f=open(filename,"w")
    for i in range(10):
        f.write("This is %d Line\n"%i)
    print("File is Created successfully and data Inserted successfully")
    f.close()
    return

createfile("file1.txt")
        
    


# In[3]:


#Function for the reading the data
def readfile(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        print(x)
    f.close()
    return

readfile("file.txt")


# In[4]:


kvps={'1':1,'2':2}
thecopy=dict(kvps)
kvps['1']=5
sum=kvps['1']+thecopy['1']
print(sum)


# In[8]:


names1=['A','B','C','D']
names2=names1
names3=names1[:]
names2[0]='A'
names3[1]='B'
sum=0
for ls in (names1,names2,names3):
    if ls[0]=='A':
        sum+=1
    if ls[1]=='B':
        sum+=10
print(sum)        
        
    


# In[10]:


print("Enter x to exit")
sourcefile=input("Enter the file name which do u want to copy\n")
if sourcefile==x:
    exit()
else:
    destination=input("Enterthe File name to copy in the folder\n")
    copyfile(sourcefile,destination)
    print("File Copied Successfully")
    print("Do u want to display the File then enter (y/n)")
    check=input()
    if check=='n':
        exit()
    else:
        c=open(destination,"r")
        c.read()
        print(c.read())
        c.close()          


# In[11]:


def createfile(filename):
    f=open(filename,"w")
    
        
    print("File is Created successfully and data Inserted successfully")
    f.close()
    return

createfile("file1.txt")
        


# In[13]:


print("Enter x to exit")
sourcefile=input("Enter the file name which do u want to copy\n")
x=exit()
if sourcefile==x:
    exit()
else:
    destination=input("Enterthe File name to copy in the folder\n")
    copyfile(sourcefile,destination)
    print("File Copied Successfully")
    print("Do u want to display the File then enter (y/n)")
    check=input()
    if check=='n':
        exit()
    else:
        c=open(destination,"r")
        c.read()
        print(c.read())
        c.close()      


# In[7]:


#Data is Append
def appendData(filename):
    f=open(filename,"a")
    f.write("New Line 1\n")
    f.write("New Line 2\n")
    f.close()
    return
appendData("file.txt")


# In[6]:


#Data Analysis 
def dataAnalysisWordCount(filename,word):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split()
    cnt=lst.count(word)
    return cnt

print(dataAnalysisWordCount("file.txt","rest"))
    


# In[24]:


#function to count the characters in the file

fname = input("Enter the name of the file:")
infile = open(fname, 'r')
characters = 0
for line in infile:
    characters = characters + len(line)
print(characters)


# In[26]:


#Function to Count the upper characters in the File 
def upperCaseCount(filename):
    cntUpper=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if  i.isupper():
            cntUpper+=1
    return cntUpper
upperCaseCount("file.txt")


# In[36]:


#Function to Count the lines in the given file
def countLines(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split("\n")
    return len(lst)
countLines("file.txt")


# In[43]:


#Checking Whether the given number is phone number or not
import re
def phoneNumberValidate(phone):
    pattern='^[6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phoneNumberValidate(9110528066))
print(phoneNumberValidate(91105280))


# In[46]:


import re
def phoneNumberValidate(phone):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phoneNumberValidate("09110528066"))
print(phoneNumberValidate("9110528066"))
print(phoneNumberValidate("+919110528066"))
print(phoneNumberValidate("+91911052806"))


# In[49]:


#validation of roll number
import re
def validateRollNumber(number):
    number=str(number)
    pattern="^[1][5][2][U][1][A][0][1-9][0-6][0-9]$"
    if re.match(pattern,number):
        return True
    return False
print(validateRollNumber("152U1A0555"))
print(validateRollNumber("2152U1A0600"))


# In[68]:


#validation of Given Email
import re
def validEmail(email):
    pattern="^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    if re.match(pattern,email):
        return True
    return False
print(validEmail("vamshi.paliviri@gmail.com"))
print(validEmail("$vamshi.paliviri@gmail.com"))
   


# In[75]:


#Validate of password
import re
def em(i):
    p="^[a-zA-Z0-9!@#$]{6,15}$"
    if re.match(p,i):
        return True

    return False
print(em('ALPHA%$'))    
print(em("passw8"))


# In[ ]:


#######################################################
####################ASIGNMENTS########################
###


# In[78]:


#Function on virtual machine 
def createfile(filename):
    f=open(filename,"w")
    print("File is Created successfully and data Inserted successfully")
    f.close()
    return

createfile("file2.txt")
        
    


# In[1]:


#need to write the data into the file
def createfile(filename):
    f=open(filename,"w")
    f.write(s)
    print(" data Inserted successfully")
    f.close()
    return

s=input("Enter the data into the file")
createfile("file2.txt")
        


# In[10]:


#Need to return the count of digits 
fname = input("Enter the name of the file:")
def countdigit(filename):
    
    length = len(x)
    digit = 0
    for i in x:
        
        if x[i].isnumeric():
            digit += 1
    return number

print(number)


# In[13]:


#function to count the characters in the file

fname = input("Enter the name of the file:")
infile = open(fname, 'r')
characters = 0
for line in infile:
    characters = characters + len(line)
print(characters)


# In[1]:


#need to count the special charecter
import re
def countSpl(filename):
    f=open(filename,"r")
    c=0
    pattern = "^[!@#$%^&*(),.?:{}|<>-]$"
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:    
        if(re.match(pattern,i)):
            c=c+1
    return c
print(countSpl("file2.txt"))


# In[2]:


import re
def createFile(filename):
    f=open(filename,"w")
    x=input("Enter your name")
    x=str(x)
    y=input("Enter your email")
    y=str(y)
    z=int(input("Enter your mobile number"))
    z=str(z)
    pattern1 = '^[a-zA-z ]{5,30}'
    pattern3 = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$|[0][4][0][6-9][0-9]{9}'
    pattern2 = "^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    if(re.match(pattern1,x)):
        f.write("Name:%s"%x)
    else:
        print("Enter valid name")
    if(re.match(pattern2,y)):
        f.write("\nEmail:%s"%y)
    else:
        print("Enter valid email")
    if(re.match(pattern3,z)):
        f.write("\nMobile number:%s"%z)
    else:
        print("Enter valid Mobile Number")
    print("File creation done")    
    f.close()
    return
createFile("filetest1.txt")


# In[ ]:




