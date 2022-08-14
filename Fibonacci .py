#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to get the Fibonacci series between 0 to 50


# In[4]:


n1=int(input("enter the first number of range  "))
n2=int(input("enter the last number of range   "))
print("fibbonacci series between" ,n1,"to"  ,n2, "is")
a=0
b=1
for i in range(n1,n2):  
    c=a+b
    a=b
    b=c
    print(a, end=" ") 
    if (b>n2):
        break

