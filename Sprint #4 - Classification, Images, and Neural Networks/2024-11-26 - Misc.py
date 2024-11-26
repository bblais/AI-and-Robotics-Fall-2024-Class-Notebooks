#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board("1111/0000/0000/2222")
state


# In[10]:


state.show_locations()


# In[4]:


moves=state.moves(1,"s","xsw","xse")
moves


# In[5]:


move=[2, 6]


# In[19]:


def forward(n):
    print("Forward ",n)


def right(a):
    print("Rotate ",a)


# In[20]:


def make_move(state,player,move):
    start,end=move
    start_row=state.row(start)
    start_col=state.col(start)

    print(move)
    print(start_row,start_col)

    # get to the start square
    forward(start_col)
    right(90)
    forward(start_row)

    if end-start==4:
        forward(1)
    elif end-start==5:  # SE
        right(-45)
        forward(1)
    elif end-start==3:  # SW
        right(45)
        forward(1)
    else:
        raise ValueError("You can't get there from here.")


# In[7]:


state.row(6)


# In[15]:


state.show_locations()


# In[21]:


make_move(state,1,[6,10])


# In[ ]:




