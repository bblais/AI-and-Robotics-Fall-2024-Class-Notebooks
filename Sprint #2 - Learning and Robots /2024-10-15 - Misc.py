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


# In[ ]:


left.power=100
right.power=100

while True:
    value=bob.value
    if value<10:
        break

    Wait(0.2)
    print(value)


print("stopping")
left.power=0
right.power=0




# In[ ]:


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


# ## while loops

# In[16]:


value=0

while value<10:
    print(value)

    value=value+1

print(value)


# In[18]:


value=0

while True:
    print(value)

    value=value+1
    if value>=10:
        break

print(value)


# In[19]:


while True:

    r,g,b,_=color_sensor.value

    color=closest_color(r,g,b,
        red=[255,0,0],
        green=[0,255,0],
        white=[255,255,255],
                       )

    if color=="red":
        break

    if color!="white":
        break

    if color in ["red","green"]:
        break


if color=="red":
    # do something here
    pass
elif color=="green":
    # do something else
    pass
else:
    print("You can't get there from here.")
    
        


# In[ ]:


left.power=20
right.power=20

try:
    while True:
    
        r,g,b,_=color_sensor.value
    
        color=closest_color(r,g,b,
            red=[255,0,0],
            green=[0,255,0],
            white=[255,255,255],
            gray=[55,55,55],
            )
    
        if color=="red":
            print("saw red")
            left.power=-20
            right.power=-20
    
        if color=="green":
            print("saw green")
            left.power=20
            right.power=20

        Wait(.1)

except KeyboardInterrupt:  # control-C
    print("Breaking out.")

Shutdown()
    

