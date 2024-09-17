#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("bob")
print("sally")

print("bob")
print("sally")

print("bob")
print("sally")

print("bob")
print("sally")

print("bob")
print("sally")

print("bob")
print("sally")

print("bob")
print("sally")


# In[ ]:


for i in range(10):
    print("bob")
    print("sally")
    


# In[ ]:


for i in [10,20,30,40]:
    print(i)


# In[ ]:


list(range(10))


# In[ ]:


reset()
for i in range(10):
    print(i)
    
#draw some more


# In[ ]:


from Game import *


# In[ ]:


state=Board(3,3)
state[5]=1

state


# In[ ]:


def initial_state():
    state=Board(3,3)
    state[5]=1
    state[7]=2
    
    return state


# In[ ]:


initial_state()


# In[ ]:


state.show_locations()


# In[ ]:


print("bob")
print(10)
print("sally")

print("bob")
print(20)
print("sally")

print("bob")
print(30)
print("sally")

print("bob")
print(40)
print("sally")


# In[ ]:


for value in [10,20,30,40]:
    print("bob")
    print(value)
    print("sally")    


# In[ ]:


for i in range(4):
    value = i*10+10
    print("bob")
    print(value)
    print("sally")    


# In[ ]:


state=Board(5,5)
state.show_locations()


# In[ ]:


player=1


# In[ ]:


for location in range(20):
    if location in [4,9,14,19]:
        continue
    new_location=location+6
    print(location,new_location)
    


# In[ ]:


if player==1:
    other_player=2
else:
    other_player=1


# In[ ]:


other_player=3-player


# In[ ]:


state=Board(3,3)
state


# In[ ]:


def valid_moves(state,player):
    moves=[]
    
    if player==1:
        if state[0]==1 and state[3]==0:
            moves.append([0,3])
        if state[2]==1 and state[5]==0:
            moves.append([2,5])
        if state[4]==1 and state[7]==0:
            moves.append([4,7])
            
    if player==2:
        if state[3]==2 and state[0]==0:
            moves.append([3,0])
        if state[4]==2 and state[1]==0:
            moves.append([4,1])
            
    return moves


# In[ ]:


state=Board(3,3)
state[0]=1
state[3]=1
state[4]=2
state


# In[ ]:


valid_moves(state,1)
state.show_locations()


# In[ ]:


def valid_moves(state,player):
    moves=[]
    
    if player==1:
        for start in range(6):
            end=start+3
            if state[start]==1 and state[end]==0:
                moves.append([start,end])
            
    if player==2:
        if state[3]==2 and state[0]==0:
            moves.append([3,0])
        if state[4]==2 and state[1]==0:
            moves.append([4,1])
            
    return moves


# In[ ]:


state=Board(3,3)
state[0]=1
state[2]=1
state[4]=2
state


# In[ ]:


valid_moves(state,1)


# In[ ]:




