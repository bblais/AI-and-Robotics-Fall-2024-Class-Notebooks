#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Game import *


# In[ ]:


state=Board(4,5)
state


# In[ ]:


state[0]=1
state[1]=2


state


# In[ ]:


state.board=[2,1,2,2,1,2,1,1,1,1,1,1,1,1,1,2,1,2,2,1]


# In[ ]:


state


# In[ ]:


win_status(state,2)

