#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *
from Game.minimax import *
from tqdm.notebook import tqdm


# ## Nim

# In[2]:


from nim import *


# ## Agents

# In[3]:


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


# ## Skittles Agent

# In[4]:


def skittles_move(state,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action

    # make/adjust the table

    if state not in S:
        # add a row to the table for each move
        S[state]=Table()
        moves=valid_moves(state,player)
        for action in moves:
            S[state][action]=1  # number of skittles/beads for each move
    
    move=weighted_choice(S[state])

    if move is None:  # there are no skittles in this row
        if last_state:
            S[last_state][last_action]=S[last_state][last_action]-1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0

        move=random_move(state,player)

    
    return move


# In[5]:


def skittles_after(status,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action

    if status=='lose':
        if last_state:
            S[last_state][last_action]=S[last_state][last_action]-1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0
                
    # does this double-count the learning if you lose on your own turn        
    


# In[6]:


skittles_agent1=Agent(skittles_move)
skittles_agent1.S=Table()
skittles_agent1.post=skittles_after

skittles_agent2=Agent(skittles_move)
skittles_agent2.S=Table()
skittles_agent2.post=skittles_after


# ## Q Agent

# In[7]:


def nim_print_Q(Q,pre="\t"):
    
    if Q and isinstance(Q[list(Q.keys())[0]],(float,int)): # just one row
        print(pre,"take 1\t take 2\t take 3")
        print(pre, end='')
        for move in [1,2,3]:
            try:
                print("%+.3f\t" % Q[move],end=' ')
            except KeyError:
                print("%+.3f\t" % 0,end=' ')
        print()        
    else:

        print(pre,"         take 1\t take 2\t take 3")
        for state in range(1,10):
            print(pre,f"state {state}:", end=' ')
            print(pre, end='')
            for move in [1,2,3]:
                try:
                    print("%+.3f\t" % Q[state][move],end=' ')
                except KeyError:
                    print("%+.3f\t" % 0,end=' ')
            print()


# In[8]:


def Q_move(state,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    verbose=info.verbose
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ
    
    if state not in Q:
        actions=valid_moves(state,player)
        Q[state]=Table()
        for action in actions:
            Q[state][action]=0  # initial value of table
    
    if verbose:
        print("\tLast state:",last_state)
        print("\tLast action:",last_action)
        print("\tCurrent State:",state)
    
    if learning:
        r=random.random()
        if r<ϵ:  # take a random move occasionally to explore the environment
            move=random_move(state,player)
            if verbose:
                print(f"\tLearning. Random {r:.3f} < ϵ {ϵ:.3f}. Taking random move.")
                print(f"\tmove={move}")
        else:
            move=top_choice(Q[state])
            if verbose:
                print(f"\tLearning. Random {r:.3f} > ϵ {ϵ:.3f}. Taking top choice move from ")
                nim_print_Q(Q[state])            
                print(f"\tmove={move}")
    else:
        if verbose:
            print(f"\tNot Learning. Taking top choice move from ")
            nim_print_Q(Q[state])            
        move=top_choice(Q[state])
    
    if not last_action is None:  # not the first move
        reward=0
        
        # learn
        if learning:
            if verbose:
                print(f"\tLearning Q table for player {player}.")
                nim_print_Q(Q)            
            
                line=f"Q[{last_state}][{last_action}] = {α:.1f} * ({reward} + {γ:.1f} * (max("
                line+=','.join([f"Q[{state}][{a}]" for a in Q[state]])
                line+=f") - Q[{last_state}][{last_action}])"
                print(line)
                line=f"        = {α:.1f} * ({reward} + {γ:.1f} * (max("
                line+=','.join([f"{Q[state][a]:.3f}" for a in Q[state]])
                line+=f") - {Q[last_state][last_action]:.3f})"
                print(line)
                
                val=α*(reward +
                        γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
                print(f"Q[{last_state}][{last_action}] = {val:3f}")
            
            Q[last_state][last_action]+=α*(reward +
                        γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
            
            if verbose:
                print(f"\tUpdated Q table for player {player}.")
                nim_print_Q(Q)            
        
    
    return move


# In[9]:


def Q_after(status,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    verbose=info.verbose

    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ

    if status=='lose':
        reward=-1
    elif status=='win':
        reward=1
    elif status=='stalemate':
        reward=.5 # value stalemate a little closer to a win
    else:
        reward=0
    
    
    if learning:
        if verbose:
            print(f"\tUpdating Q table for player {player}")
            print(f"\tLast state {last_state} action {last_action} reward {reward}")
            print(f"\tQ table.")
            nim_print_Q(Q)            
        
        if verbose:
            nim_print_Q(Q[last_state])            
            print(f"Q[{last_state}][{last_action}] = {α:.1f} * ({reward} - Q[{last_state}][{last_action}])") 
            print(f"Q[{last_state}][{last_action}] = {α:.1f} * ({reward} - {Q[last_state][last_action]:.3f})") 
            
            val=α*(reward - Q[last_state][last_action])
            line=f"Q[{last_state}][{last_action}] = {val:3f}"
            print(line)
            
        Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])

        if verbose:
            nim_print_Q(Q[last_state])
        
        if verbose:
            print(f"\tUpdated Q table for player {player}.")
            nim_print_Q(Q)            


# In[10]:


from copy import deepcopy


# In[11]:


Q1_agent=Agent(Q_move)
Q1_agent.post=Q_after
Q1_agent.Q=Table()  # makes an empty table
Q1_agent.learning=True
Q1_agent.verbose=True


Q1_agent.α=0.4  # learning rate
Q1_agent.ϵ=0.5  # how often to take a random move
Q1_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)


# In[12]:


Q2_agent=Agent(Q_move)
Q2_agent.post=Q_after
Q2_agent.Q=Table()  # makes an empty table
Q2_agent.learning=True
Q2_agent.verbose=True

Q2_agent.α=0.4  # learning rate
Q2_agent.ϵ=0.5  # how often to take a random move
Q2_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)


# In[13]:


print()
print()
for p,agent in enumerate([Q1_agent,Q2_agent]):
    Q=agent.Q
    if agent.verbose:
        print(f"Starting Q table for player {p+1}.")
    nim_print_Q(Q)            
    
g=Game(number_of_games=5)
g.save_states=True
g.run(Q1_agent,Q2_agent)

print()
print()
for p,agent in enumerate([Q1_agent,Q2_agent]):
    Q=agent.Q
    if agent.verbose:
        print(f"Final Q table for player {p+1}.")
    nim_print_Q(Q)            
    


# In[14]:


Q


# In[15]:


for gi,game in enumerate(g.games):
    print(f"Game {gi+1}")
    for s1,s2,m,p in zip(game['states'][:-1],game['states'][1:],game['moves'],game['players']):
        print(f"\tState {s1} move {m} player {p} --> State {s2}")


# In[30]:


Q1_agent.Q


# In[ ]:





# ## Minimax

# In[31]:


def minimax_move(state,player):
    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# ## Training

# In[32]:


agent1=Q1_agent
agent1.Q=Table()
agent2=Q2_agent
agent2.Q=Table()


# In[33]:


S=Storage()
one,two,ties,N=0,0,0,0


# In[34]:


N_test=100
N_train=1


# In[35]:


num_training_games=0
for i in tqdm(range(200)):
    Q1_agent.learning=True
    Q2_agent.learning=True
    g=Game(number_of_games=N_train)
    g.display=False
    result=g.run(agent1,agent2)

    
    Q1_agent.learning=False
    Q2_agent.learning=False
    g=Game(number_of_games=N_test)
    g.display=False
    result=g.run(agent1,agent2)
    one,two,ties,N=one+result.count(1),two+result.count(2),ties+result.count(0),N+len(result)
    
    num_training_games+=N_train
    S+=one/N*100,two/N*100,ties/N*100,num_training_games


# ## Progress

# In[36]:


y1,y2,y0,x=S.arrays()


# In[37]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pyplot import figure,plot,grid,legend,xlabel,ylabel,title
from tqdm import tqdm


# In[38]:


figure(figsize=(16,8))
plot(x,y1,label='One Win')
plot(x,y2,label='Two Win')
plot(x,y0,label='Tie')
legend()
xlabel('Number of Games')
ylabel('Percent')


# In[39]:


SaveTable(Q1_agent.Q,'Nim Q1 Table.json')
SaveTable(Q2_agent.Q,'Nim Q2 Table.json')


# ## Test

# In[25]:


Q1_agent.learning=False
Q2_agent.learning=False


# In[26]:


g=Game(number_of_games=1000)
g.display=False
result=g.run(minimax_agent,Q2_agent)
g.report()


# In[27]:


g=Game(number_of_games=1000)
g.display=False
result=g.run(random_agent,minimax_agent)
g.report()


# In[28]:


g=Game(number_of_games=1000)
g.display=False
result=g.run(random_agent,Q2_agent)
g.report()


# In[29]:


g=Game(number_of_games=1000)
g.display=False
result=g.run(random_agent,random_agent)
g.report()


# In[ ]:




