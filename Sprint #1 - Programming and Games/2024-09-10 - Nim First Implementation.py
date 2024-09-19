#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Game import *


# Four functions to do:
# 
# 1. `initial_state()`   return the state for the start of the game
# 2. `valid_moves(state,player)` return a list of valid moves
# 3. `update_state(state, player, move )` return the new state
# 4. `win_status(state,player)` returns one of `"win"`,`"lose"`,`"stalemate"` or `None`

# - What is state for this game:  single #
# - What is a move for this game: single #. (1,2, or 3)

# In[ ]:


def initial_state():
    return 21


# In[ ]:


initial_state()


# In[ ]:


def valid_moves(state,player):
    if state==2:
        return [1,2]
    elif state==1:
        return [1]
    else:
        return [1,2,3 ]


# In[ ]:


valid_moves(21,1)


# In[ ]:


valid_moves(2,1)


# In[ ]:


def update_state(state,player,move):
    new_state=state-move
    return new_state


# In[ ]:


update_state(21,1,3)


# In[ ]:


def win_status(new_state,player):
    
    if new_state==1:
        return "win"
    
    if new_state==0:
        return "lose"
    
    return None
    
    


# In[ ]:


def show_state(state,player):
    print(state)


# ## Agents

# In[ ]:


def human_move(state,player):
    
    while True:
        move=eval(input("Enter your move"))

        if move not in valid_moves(state,player):
            print("That is not a valid move")
        else:
            break
    
    return move

human_agent=Agent(human_move)


# In[ ]:


def monkey_move(state,player):
    return random.choice(valid_moves(state,player))
monkey_agent=Agent(monkey_move)


# In[ ]:


monkey_move(21,1)


# In[ ]:


state=initial_state()


# In[ ]:


human_move(state,1)


# In[ ]:


g=Game()


# In[ ]:


g.run(human_agent,human_agent)


# In[ ]:


g.run(human_agent,monkey_agent)


# In[ ]:




