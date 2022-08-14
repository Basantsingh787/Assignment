#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to count the number of even and odd numbers from a series of numbers.


# In[4]:


n=int(input("enter the number of days= "))
list_of_numbers=[]
even=0
odd=0
for i in range(n): 
    num=int(input("enter number"))
    list_of_numbers.append(num)
    if list_of_numbers[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print(list_of_numbers)
print("numbers of even days"  , even)
print("numbers of odd days"  , odd)
enter the number of days= 5
enter number1
enter number2
enter number3
enter number4
enter number5
[1, 2, 3, 4, 5]
numbers of even days 2
numbers of odd days 3
