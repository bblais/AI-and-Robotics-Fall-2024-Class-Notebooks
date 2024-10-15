#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Nim functions!")

def initial_state(): 
    """ returns  - The initial state of the game"""
    return 9

def valid_moves(state,player):
    """returns  - a list of the valid moves for the state and player"""

    if state==2:
        return [1,2]
    elif state==1:
        return [1]
    else:
        return [1,2,3]

def show_state(state,player):
    """prints or shows the current state"""
    print(f"There are >>{state} sticks<<< for player {player}.")

def update_state(state,player,move):
    """returns  - the new state after the move for the player"""

    new_state=state-move

    return new_state


def win_status(state,player):
    """    returns  - 'win'  if the state is a winning state for the player, 
               'lose' if the state is a losing state for the player,
               'stalemate' for a stalemate
               None otherwise
    """

    if state==0:
        return 'lose'

    if state==1:
        return 'win'


    return None
    


# Some markdown!

# In[ ]:




