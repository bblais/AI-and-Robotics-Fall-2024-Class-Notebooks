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
    return 9


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


def table_move(state,player):
    
    T=Table()
    
    T[9]=Table()
    T[9][1]=-100
    T[9][2]=-100
    T[9][3]=-100
    
    T[8]=Table()
    T[8][1]=-100
    T[8][2]=-100
    T[8][3]=+100
    
    T[7]=Table()
    T[7][1]=-100
    T[7][2]=+100
    T[7][3]=-100

    T[6]=Table()
    T[6][1]=+100
    T[6][2]=-100
    T[6][3]=-100

    T[5]=Table()
    T[5][1]=-100
    T[5][2]=-100
    T[5][3]=-100
    
    T[4]=Table()
    T[4][1]=-100
    T[4][2]=-100
    T[4][3]=+100

    
    T[3]=Table()
    T[3][1]=-100
    T[3][2]=+100
    T[3][3]=-100
    

    T[2]=Table()
    T[2][1]=+100
    T[2][2]=-100
    

    T[1]=Table()
    T[1][1]=-100
    
    
    print("\t",f"Player {player} at state {state}.")
    print("\t","Table:",T)
    print("\t","Table values at state ",state,":",T[state])
    
    
    
    
    move=top_choice(T[state])
    
    print("\t","Top choice is ",move)
    
    return move
table_agent=Agent(table_move)


# In[ ]:


g=Game()
g.run(table_agent,monkey_agent)


# In[ ]:


T=Table()
for state in range(1,22):
    T[state]=Table()
    
    for move in [1,2,3]:
        
        if move>state:
            continue
        
        T[state][move]=-100
        
        if state%4==0:  # 4, 8, 12, 16, etc...
            T[state][3]=+100
            
        if state%4==3:  # 3, 7, 11, etc...
            T[state][2]=+100

        if state%4==2:  # 2, 6, 10, etc...
            T[state][1]=+100

        if state%4==1:  # 1, 5, 9, etc...
            pass
        
        
            

T


# In[ ]:


10%3


# In[ ]:




