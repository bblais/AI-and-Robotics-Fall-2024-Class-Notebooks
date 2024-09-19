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
    return 999


# In[ ]:


def valid_moves(state,player):
    if state==2:
        return [1,2]
    elif state==1:
        return [1]
    else:
        return [1,2,3 ]


# In[ ]:


def update_state(state,player,move):
    new_state=state-move
    return new_state


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


from Game.minimax import *


# In[ ]:


def minimax_move(state,player):
    values,actions=minimax_values(state,player,display=False)
    return top_choice(actions,values)
minimax_agent=Agent(minimax_move)


# In[ ]:


minimax_values(4,1)  # state, player


# In[ ]:


minimax_move(4,1)


# In[ ]:


g=Game()
g.run(monkey_agent,monkey_agent)


# In[ ]:


g=Game()
g.run(minimax_agent,monkey_agent)


# In[ ]:


g=Game(number_of_games=100)
g.display=False
result=g.run(minimax_agent,monkey_agent)
print(result)


# In[ ]:


g=Game(number_of_games=1)
result=g.run(minimax_agent,monkey_agent)
print(result)


# In[ ]:




