#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Game import *


# Four functions to do:
# 
# 1. `initial_state()`   return the state for the start of the game
# 2. `valid_moves(state,player)` return a list of valid moves
# 3. `update_state(state, player, move )` return the new state
# 4. `win_status(new_state,player)` returns one of `"win"`,`"lose"`,`"stalemate"` or `None`

# ![image.png](attachment:bc05fd5e-23d8-4805-80af-ee57c896029f.png)

# - Rules: https://www.whatdowedoallday.com/tapatan/
# - What is state for this game:  3dx3 Board (9 numbers) 0 = empty, 1 = player 1 and 2 = player 2
# - What is a move for this game: single # (0-8 for the square locations) after 6 pieces, move = [start,end]

# In[ ]:


def initial_state():
    return Board(3,3)


# In[ ]:


initial_state()


# In[ ]:


state=initial_state()


# In[ ]:


state


# In[ ]:


state[2]=5
state[4]=10
state


# In[ ]:


state.show_locations()


# In[ ]:


state[6]=-5


# In[ ]:


state


# In[ ]:




