#!/usr/bin/env python
# coding: utf-8

# In[4]:


from Game import *
from Game.minimax import *


# Change of rules
# 
# - take 1, 2, or 3
# - taking last stick loses
# - being left with 2 sticks is a stalemate

# ## NimPlus 

# In[5]:


def initial_state(): 
    """ returns  - The initial state of the game"""
    return 21

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

    if state==2:
        return 'stalemate'

    return None
    


# ## Agents

# In[6]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)

def human_move(state,player):
    print("Player ", player)
    valid_move=False
    while not valid_move:
        move=int(input('What is your move? '))

        if move in valid_moves(state,player):
            valid_move=True
        else:
            print("Illegal move.")

    return move

human_agent=Agent(human_move)


# In[7]:


def minimax_move(state,player):
    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[ ]:





# In[8]:


def skittles_move(state,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action
    verbose=info.verbose

    
    if verbose:
        print("\t","Player ",player," is thinking...")
        print("\t","State: ",state)
        print("\t","Table:",S)
        print("\t","Last state,action: ",last_state,last_action)
    
    # make/adjust the table

    if state not in S:
        # add a row to the table for each move
        S[state]=Table()
        moves=valid_moves(state,player)
        for action in moves:
            S[state][action]=3  # number of skittles/beads for each move
    
        if verbose:
            print("\t","State ",state,"unknown...added to table")
            print("\t","Table",S)
    
    move=weighted_choice(S[state])
    if verbose:
        print("\t","Choosing from S[",state,"]",S[state],"....Move: ",move)

    if move is None:  # there are no skittles in this row
        if last_state:
            if verbose:
                print("\t","No possible moves!")
                print("\t","Modifying the table: removing one skittle from (state,action) ",last_state,last_action)
            S[last_state][last_action]=S[last_state][last_action]-1
            
            if verbose:
                print("\t","Table:",S)
                
            if S[last_state][last_action]<0:                
                S[last_state][last_action]=0
                if verbose:
                    print("\t","Negative skittles...fixing.")
                    print("\t","Table:",S)                
        else:
            if verbose:
                print("\t","Started in a bad state ",state,"with no moves and no last state.  Won't modify table.")
                  
                  

        move=random_move(state,player)

    
    return move

def skittles_after(status,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action
    verbose=info.verbose

    if verbose:
        print("\t","End of Game adjustments")
        print("\t","Player ",player," is thinking...")
        print("\t","Win Status: ",status)
        print("\t","Table:",S)
        print("\t","Last state,action: ",last_state,last_action)
        
    if status=='lose':
        if last_state:
            S[last_state][last_action]=S[last_state][last_action]-1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0
                
            if verbose:
                print("\t","Modifying the table: removing one skittle from (state,action) ",last_state,last_action)
                print("\t","Table:",S)

                
        else:
            if verbose:
                print("\t","No last state, so nothing to learn.")
            
                
    else:
        if verbose:
            print("\t","No adjustments needed.")
        
    # does this double-count the learning if you lose on your own turn        
    


# In[9]:


skittles_agent1=Agent(skittles_move)
skittles_agent1.S=Table()
skittles_agent1.post=skittles_after
skittles_agent1.verbose=False

skittles_agent2=Agent(skittles_move)
skittles_agent2.S=Table()
skittles_agent2.post=skittles_after
skittles_agent2.verbose=False


# In[11]:


g=Game()
g.run(skittles_agent1,skittles_agent2)


# In[12]:


SaveTable(skittles_agent1.S,'nim skittles1.json')
SaveTable(skittles_agent2.S,'nim skittles2.json')


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pyplot import figure,plot,grid,legend,xlabel,ylabel,title
from tqdm import tqdm


# In[14]:


agent1=skittles_agent1
agent1.S=Table()

agent2=skittles_agent2
agent2.S=Table()


# In[15]:


S=Storage()
one,two,ties,N=0,0,0,0


# In[16]:


for i in tqdm(range(30)):
    g=Game(number_of_games=100)
    g.display=False
    
    result=g.run(agent1,agent2)
    one,two,ties,N=one+result.count(1),two+result.count(2),ties+result.count(0),N+len(result)
    
    S+=one/N*100,two/N*100,ties/N*100,N
    
y1,y2,y0,x=S.arrays()    


# In[17]:


figure(figsize=(16,8))
plot(x,y1,label='One Win')
plot(x,y2,label='Two Win')
plot(x,y0,label='Tie')
legend()
xlabel('Number of Games')
ylabel('Percent')


# In[19]:


SaveTable(skittles_agent1.S,'nimplus skittles1.json')
SaveTable(skittles_agent2.S,'nimplus skittles2.json')


# ## Test the agent

# In[20]:


g=Game()
g.run(human_agent,skittles_agent2)


# In[21]:


g=Game(number_of_games=100)
g.display=False
result=g.run(minimax_agent,agent2)
g.report()


# In[22]:


g=Game(number_of_games=100)
g.display=False
result=g.run(agent1,minimax_agent)
g.report()


# In[27]:


g=Game()
g.run(skittles_agent1,random_agent)


# In[28]:


agent1.S


# In[38]:


for i in range(20):
    move=skittles_move(state=4,player=1,info=agent1)
    print(move)


# In[ ]:




