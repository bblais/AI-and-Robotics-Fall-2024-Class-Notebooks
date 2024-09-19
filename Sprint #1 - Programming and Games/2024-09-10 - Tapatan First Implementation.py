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


# since `valid_moves` returns a list, it will help to learn a small amount about python lists.

# In[ ]:


# in python, the hashtag in code = comment
a=[]     # an empty list


# In[ ]:


a


# In[ ]:


a.append(5)
a.append("bob")
a.append( [1,2,3] )


# In[ ]:


a


# In[ ]:


a.append("sally")


# In[ ]:


a


# In[ ]:


state.show_locations()


# In[ ]:


# 0  1  2 
# 3  4  5 
# 6  7  8 

def valid_moves(state,player):
    
    moves=[]
    
    if state[0]==0: 
        moves.append(0)
        
    if state[1]==0: 
        moves.append(1)
        
    if state[2]==0: 
        moves.append(2)
    
    if state[3]==0: 
        moves.append(3)

    if state[4]==0: 
        moves.append(4)
        
    if state[5]==0: 
        moves.append(5)
    
    if state[6]==0: 
        moves.append(6)
    
    if state[7]==0: 
        moves.append(7)
    
    if state[8]==0: 
        moves.append(8)
        
        
    return moves
    


# In[ ]:


def count_pieces(state):
    count=0
    for location in range(9):
        if state[location]!=0:
            count=count+1
            
    return count


# In[ ]:


state


# In[ ]:


count_pieces(state)


# In[ ]:


def valid_moves(state,player):
    
    moves=[]
    
    if count_pieces(state)<9:  # temporaily set to 9 to behave like ttt
        # placement
        for location in range(9): 
            if state[location]==0:
                moves.append(location)
    else:
        # sliding
        pass
        
        
    return moves
    


# In[ ]:


state=initial_state()

valid_moves(state,1)


# In[ ]:


state[2]=2
state[5]=1
state[7]=2
valid_moves(state,1)


# In[ ]:


state


# In[ ]:


def update_state(state,player,move):
    if isinstance(move,int):  # placement
        new_state=state
        new_state[move]=player
        
    else:  # sliding
        start,end=move
        new_state=state
        new_state[start]=0
        new_state[end]=player
        
    return new_state


# In[ ]:


state=initial_state()
state[3]=state[6]=1
state[1]=state[4]=2
state


# In[ ]:


update_state(state,2,5)


# In[ ]:


update_state(state,1,[6,7])


# In[ ]:


def win_status(state,player):
    # 0  1  2 
    # 3  4  5 
    # 6  7  8 

    if player==1:
        other_player=2
    else:
        other_player=1
    
    if state[0]==state[1]==state[2]==player:
        return "win"
    if state[3]==state[4]==state[5]==player:
        return "win"
    if state[6]==state[7]==state[8]==player:
        return "win"
    if state[0]==state[3]==state[6]==player:
        return "win"
    if state[1]==state[4]==state[7]==player:
        return "win"
    if state[2]==state[5]==state[8]==player:
        return "win"
    if state[0]==state[4]==state[8]==player:
        return "win"
    if state[6]==state[4]==state[2]==player:
        return "win"
    
    if not valid_moves(state,other_player):
        return "stalemate"
    
    return None


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


def show_state(state,player):
    print(state)


# In[ ]:


def monkey_move(state,player):
    return random.choice(valid_moves(state,player))
monkey_agent=Agent(monkey_move)


# In[ ]:


g=Game()
g.run(monkey_agent,monkey_agent)


# In[ ]:


state=initial_state()
state.board=[2,1,2,2,1,1,0,1,0]
state


# In[ ]:


win_status(state,1)


# In[ ]:




