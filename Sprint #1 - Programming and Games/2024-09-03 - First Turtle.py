#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from mplturtle import *


# In[ ]:


reset()  # only include figsize for class
forward(50)
right(30)
forward(50)


# In[ ]:


reset(figsize=(3,3))  # only include figsize for class
forward(50)
right(30)
forward(50)


# ## draw a square

# In[ ]:


reset(figsize=(3,3))  # only include figsize for class
pencolor("red")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[ ]:


reset(figsize=(3,3))  # only include figsize for class
pencolor("red")

size=80
print("here")
for i in range(4):
    forward(50)
    right(90)
    print("there")
    
print("another place")


# In[ ]:


reset(figsize=(3,3))  # only include figsize for class
pencolor("red")

size=80
print("here")
for i in range(4):
    forward(size)
    right(90)
    print("there")
    
print("another place")


# In[ ]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)


# In[ ]:


reset(figsize=(3,3))  # only include figsize for class
pencolor("red")

square(80)


# In[ ]:


reset(figsize=(3,3))  # only include figsize for class
pencolor("red")

square(80)

forward(160)
square(80)



# In[ ]:


reset(figsize=(3,3))  # only include figsize for class
pencolor("red")

square(80)

penup()
forward(160)
pendown()

square(80)



# In[ ]:




