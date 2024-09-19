#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Game import *


# In[ ]:


state=Board(3,3)
state.board=[random.choice([0,1,2]) for i in range(9)]
state


# In[ ]:


state=Board(6,7)
state.board=[random.choice([0,1,1,1]) for i in range(42)]
state


# In[ ]:


state.show_locations()


# In[ ]:


state


# In[ ]:


for row in state.rows():
    print("Row is ",row)


# In[ ]:


for row in state.rows(4):
    if row==[1,1,1,1]:
        print(row," player 1 wins")
    if row==[2,2,2,2]:
        print(row," player 2 wins")
    print("Row is ",row)


# In[ ]:


state


# In[ ]:





# In[ ]:


for col in state.cols(4):
    if col==[1,1,1,1]:
        print(col," player 1 wins")
    if col==[2,2,2,2]:
        print(col," player 2 wins")
    print("col is ",col)


# In[ ]:


for diag in state.diags(4):
    if diag==[1,1,1,1]:
        print(diag," player 1 wins")
    if diag==[2,2,2,2]:
        print(diag," player 2 wins")
    print("diag is ",col)


# In[ ]:


state=Board(3,3)
state.board=[random.choice([0,1,2]) for i in range(9)]
state


# In[ ]:


state.moves(1,"n","xne","xnw")


# In[ ]:


state=Board(5,5)
state.board=[random.choice([0,0,0,1,2]) for i in range(25)]
state


# In[ ]:


state.moves(1,"n","xne","xnw")


# In[ ]:


Board(3,3,3)


# In[ ]:


state


# In[ ]:


state[7]


# In[ ]:


state[1,2]


# In[ ]:




