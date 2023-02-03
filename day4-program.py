#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={n:n*n for n in range(1,5)}
print(d)


# In[18]:


old={"apple":100,"Banana":50,"Orange":70}
new={prod:cost*10 for(prod,cost) in old.items()}
print(old)
print(new)


# In[6]:


old={"apple":100,"Banana":50,"Orange":70}
new={prod:cost for(prod,cost) in old.items() if cost>50}
print(old)
print(new)


# In[15]:


"""create a list with 8 costumer names ,display a dictionary which has costumer names along discounts
for them from a particular shop"""
#method1
import random
c1=random.randint(1,100)
c2=random.randint(1,100)
c3=random.randint(1,100)
c4=random.randint(1,100)
c5=random.randint(1,100)
c6=random.randint(1,100)
c7=random.randint(1,100)
c8=random.randint(1,100)
list1=[("costumer1",c1),("costumer2",c2),("costumer3",c3),("costumer4",c4),("costumer5",c5),("costumer6",c6),("costumer7",c7),("costumer8",c8)]
dict(list1)


# In[16]:


#Method2
import random
list1=["costumer1","costumer2","costumer3","costumer4","costumer5","costumer6","costumer7","costumer8"]
new={costumer:random.randint(1,100) for(costumer) in list1}
print(new)


# In[19]:


l1=["a","b","c"]
l2=[10,20,30]
d={a:b for(a,b) in zip(l1,l2)}
print(d)


# In[23]:


names=["Ravi","ram","Akash","Anvesh","Akhil"]
marks=[100,450,480,350,300]
d={a:b*0.2 for(a,b) in zip(names,marks)}  #out of 500
print(d)


# In[24]:


"bga'jk'"


# In[33]:


print("""hai""")
print("hai")


# In[7]:


m="Hello World"
print(m.upper())
print(m.lower())
print(m.capitalize())
print(m.replace("l","j"))
print(m.split("l"))
print(m.center(20,"*"))
print(m.islower())
print(m.isupper())
print(m.istitle())


# In[14]:


#get one string as input along with a character .findout and dispay whether that particular character  is present or not
str=input()
char=input()
if char in str:
    print("yes")
else:
    print("NO")


# In[9]:


#check whether the given string is palindrome r not
str=input("Enter:")
m=(str[::-1])
if m==str:
    print("palindrome")
else:
    print("not a palindrome")


# In[39]:


#2nd method 
str=input()
m=len(str)-2*(len(str))
for i in range(-1,-3):
    print(str[i])


# In[17]:


#check if our string contains space r not....if yes count the spaces
str=input()
char=" "
if char in str:
    print("yes")
    print(str.count(" "))
else:
    print("NO")


# In[26]:


str=input()
char=" "
count=0
c=0


for i in range(len(str)):
    if str[i]==char:
        c=1
        count+=1

if c==1:
    print("yes")
    
else:
    print("NO")
print(count)


# In[31]:


str=input()
char=" "

c=0


for i in range(len(str)):
    if str[i]==char:
        c=1
      
if c==1:
    print("yes")
    
else:
    print("NO")


# In[ ]:




