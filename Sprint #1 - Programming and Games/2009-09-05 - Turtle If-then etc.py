#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from mplturtle import *


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class
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


def square():

    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)


# In[ ]:


use_red=True

reset(figsize=(3,3))  # only include figsize for the projector in class

if use_red:
    pencolor("red")
else:
    pencolor("blue")


square()


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class

for i in range(5):

    print(i)
    square()
    forward(100)


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class

for bob in range(5):

    print(bob)
    
    if bob>2:
        pencolor("red")
        
    square()
    forward(100)


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class

for bob in range(5):

    print(bob)
    
    if bob%2==1:  # odd number
        pencolor("red")
    else:
        pencolor("blue")
        
    square()
    forward(100)


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class

use_red=False
for bob in range(5):

    print(bob)
    
    if use_red:  # odd number
        pencolor("red")
        use_red=False
    else:
        pencolor("blue")
        use_red=True
        
    square()
    forward(100)


# In[ ]:


from numpy.random import rand


# In[ ]:


rand()


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class


for bob in range(20):

    forward(50)
    
    r=rand()
    
    if r>0.5:
        right(90)
    else:
        left(90)
    


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class


for bob in range(200):

    forward(50)
    
    r=rand()*360-180
    #print(r)
    
    right(r)
    


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class


for bob in range(200):

    forward(rand()*100)
    
    r=rand()*360-180
    #print(r)
    
    right(r)
    


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class

forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[ ]:


def square():
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class
square()


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class
square()

penup()
forward(100)
pendown()

square()


# In[ ]:


def forward_up(distance):
    penup()
    forward(distance)
    pendown()


# In[ ]:


reset(figsize=(3,3))  # only include figsize for the projector in class
square()

forward_up(100)

square()


# In[ ]:




