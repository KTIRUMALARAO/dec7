#!/usr/bin/env python
# coding: utf-8

# # Converting list to string 

# In[9]:


l=['Hi','This','Rao']
s=''
for i in l:
    s+=i
print(s)


# In[17]:


def string(seq):
    s1=''
    for i in seq:
        s1+=i
    return s1


# In[18]:


string(['hi','hello'])


# #  String to list

# In[25]:



li=[]
def list(s):
    for i in s:
        li.append(i)
    return li


# In[26]:


list('This is Tirumala Rao Konatham')


# # Decorator

# In[45]:


def outer(fn):
    def inner(*args,**kwargs):
        return fn(*args,**kwargs)
    return inner


# In[46]:


def sum1(a,b):
    return a+b


# In[47]:


sum1=outer(sum1)


# In[48]:


sum1(10,20)


# # Upper

# In[49]:


def upper(a):
    return a.upper()


# In[50]:


upper=outer(upper)


# In[51]:


upper('abcd')


# # With in decorator

# In[56]:


def outer(fn):
    def inner(*args,**kwargs):
        a,b=args
        return fn(a.upper(),b.upper())
    return inner


# In[57]:


def upper1(a,b):
    return a,b


# In[58]:


v = outer(upper1)


# In[59]:


v('anvb','hjfh')


# In[88]:


def outer(fn):
    def inner(*args,**kwargs):
        a,b=args
        return a+b
    return inner


# In[89]:


def add(a,b):
    return a,b


# In[90]:


b= outer(add)


# In[91]:


b(303,304)


# # Palindrome

# In[92]:


def outer(fn):
    def inner(*args,**kwargs):
        
        return fn(*args,**kwargs)
    return inner


# In[94]:


def palindrome(a):
    if a==a[::-1]:
        return 'palindrome'
    else:
        return 'Not a palindrome'


# In[95]:


palin = outer(palindrome)


# In[96]:


palin('MOM')


# In[99]:


palin('Tiru')


# In[178]:


def outer(fn):
    def inner(*args,**kwargs):
        a=args
        
        if a==a[::-1]:
            return fn(a.upper())
    return inner


# In[179]:


def palindrome1(a):
    return a


# In[180]:


pa = outer(palindrome1)


# In[181]:


pa('mom')


# In[182]:


pa('Tiru')


# # Factorial of a number#

# In[156]:


def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)


# In[157]:


fact(3)


# # Swap first and last elements in a list#

# In[161]:


def swap(l):
    size=len(l)
    temp=l[0]
    l[0]=l[size-1]
    l[size-1]=temp
    return l


# In[162]:


print(swap([1,2,3,4,5]))


# # Factores#

# In[164]:


def factors(s):
    print("The factors " ,s ," are ")
    for i in range(1,s+1):
        if s%i ==0:
            print(i)


# In[165]:


factors(24)


# In[168]:


def factors(s):
    print("The factors " ,s ," are ")
    print([i for i in range(1,s+1) if s%i ==0 ])


# In[170]:


factors(20)


# In[183]:


range


# In[184]:


dir(range)


# In[185]:


type(range)


# In[186]:


help(range)


# In[187]:


range(1,10)


# In[189]:


tuple(range(1,10))


# In[190]:


tuple(range(1,10,3))


# In[194]:


from functools import * 
import functools


# In[195]:


print(dir(functools))


# In[200]:


help(namedtuple)


# In[226]:


seq =['Rahul','shabina','Akash','Rahul','Akash','Shabina','rahul']


# In[227]:


type(seq)


# In[228]:


a =set(seq)


# In[229]:


a


# In[230]:


type(a)


# In[231]:


set


# In[232]:


dir(set)


# In[234]:


frozenset


# In[235]:


dir(frozenset)


# In[236]:


help(dir(frozenset))


# In[237]:


b=frozenset(a)


# In[238]:


b


# In[239]:


a


# In[240]:


seq


# In[241]:


b


# In[242]:


seq


# In[249]:


pass


# In[267]:


seq=[1,5,3,2,6,3,2,1]
result = [v for i,v in enumerate(seq) if v not in seq[:i]]


# In[268]:


result


# In[280]:


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            print(seen)


# In[281]:


de = dedupe([1,5,3,2,6,3,2,1])


# In[282]:


next(de)


# In[283]:


next(de)


# In[284]:


next(de)


# In[285]:


next(de)


# In[286]:


next(de)


# In[287]:


next(de)


# In[288]:


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            print(seen)


# In[ ]:




