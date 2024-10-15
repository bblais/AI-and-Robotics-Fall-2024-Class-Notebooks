#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Robot373 import *


# In[12]:


left,right=Motors("ab")
bob,sally=Sensors(None,None,"us","touch")


# In[13]:


try:
    while True:
        print("the value of eyes is:",bob.value)
        print("the value of the touch sensor is:",sally.value)
        Wait(0.1)
except KeyboardInterrupt:  # wait for a control-C
    pass

Shutdown()


# In[15]:


left.power=100
right.power=100

while bob.value>10:
    print("going")
    print("eyes",bob.value)

    left.power=100
    right.power=100

print("stopping")
left.power=0
right.power=0


# In[ ]:




