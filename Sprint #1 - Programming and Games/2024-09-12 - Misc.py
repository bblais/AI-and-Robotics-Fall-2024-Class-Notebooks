#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def once(a):
    return 1*a

def twice(a):
    return 2*a

def thrice(a):
    return 3*a


# In[ ]:


twice(5)


# In[ ]:


def myfunction(value,name):
    
    if name=="once" or name=="one":
        return once(value)
    
    if name=="twice" or name=="two":
        return twice(value)

    if name=="thrice":
        return thrice(value)
    
    # if it gets this far, there is a problem!
    print("I don't know what ",name," is!")


# In[ ]:


def myfunction(value,name):
    
    if name=="once" or name=="one":
        return once(value)
    
    elif name=="twice" or name=="two":
        return twice(value)

    elif name=="thrice":
        return thrice(value)
    else:
        # if it gets this far, there is a problem!
        print("I don't know what ",name," is!")


# In[ ]:


myfunction(5,"twice")


# In[ ]:


myfunction(5,"bob")


# In[ ]:


myfunction(5,"two")


# In[ ]:


for i in range(20):
    
    if i>10:
        print("bob",i)
    elif i<5:
        print("sally",i)
    else:
        print("X")
        


# In[ ]:


for i in range(20):
    
    if i>10:
        print("bob",i)
        
    if i<5:
        print("sally",i)
    else:
        print("X")
        


# In[ ]:




