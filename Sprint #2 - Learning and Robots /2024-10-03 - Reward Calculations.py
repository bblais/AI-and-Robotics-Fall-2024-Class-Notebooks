#!/usr/bin/env python
# coding: utf-8

# In[1]:


Q=0


# In[2]:


α=0.3


# In[3]:


reward=+1


# In[4]:


Q=Q+α*(reward-Q)
print(Q)


# In[5]:


reward=+1
Q=Q+α*(reward-Q)
print(Q)


# In[6]:


reward=+1
Q=Q+α*(reward-Q)
print(Q)


# In[7]:


reward=-1
Q=Q+α*(reward-Q)
print(Q)


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pyplot import figure,plot,grid,legend,xlabel,ylabel,title
from tqdm.notebook import tqdm


# In[9]:


from pylab import rand


# In[10]:


Q=0


# In[11]:


Qs=[Q]
for i in range(100):
    reward=+1
    Q=Q+α*(reward-Q)

    Qs.append(Q)

plot(Qs,'-o')


# In[12]:


Q=0
Qs=[Q]
for i in range(100):
    reward=-1
    Q=Q+α*(reward-Q)

    Qs.append(Q)

plot(Qs,'-o')


# In[13]:


Q=0
Qs=[Q]
for i in range(100):
    r=rand()  # between 0 and 1
    if r<0.1: # 10% of the time
        reward=-1
    else:
        reward=+1
    
    Q=Q+α*(reward-Q)

    Qs.append(Q)

plot(Qs,'-o')


# In[14]:


Q=0
Qs=[Q]
for i in range(1000):
    r=rand()  # between 0 and 1
    if r<0.1: # 10% of the time
        reward=-1
    else:
        reward=+1
    
    Q=Q+α*(reward-Q)

    Qs.append(Q)

plot(Qs,'-o')


# In[16]:


from numpy import mean


# In[17]:


mean(Qs)


# In[19]:


Q=0
α=0.01
Qs=[Q]
for i in range(1000):
    r=rand()  # between 0 and 1
    if r<0.1: # 10% of the time
        reward=-1
    else:
        reward=+1
    
    Q=Q+α*(reward-Q)

    Qs.append(Q)

plot(Qs,'-o')


# In[20]:


mean(Qs)


# In[21]:


Q=0
α=0.001
Qs=[Q]
for i in range(1000):
    r=rand()  # between 0 and 1
    if r<0.1: # 10% of the time
        reward=-1
    else:
        reward=+1
    
    Q=Q+α*(reward-Q)

    Qs.append(Q)

plot(Qs,'-o')


# In[ ]:




