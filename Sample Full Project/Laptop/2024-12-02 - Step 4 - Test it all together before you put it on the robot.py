#!/usr/bin/env python
# coding: utf-8

# In[1]:


from breakthrough import *
from my_robot_functions import *  
from classy import *
from pylab import imread,imsave,imshow,float32,figure
from image_defs import *


# In[2]:


if BP is None:
    print("Running on the laptop.")
    on_laptop=True
else:
    print("Running on the robot.")
    on_laptop=False
    


# ## Agent

# In[3]:


def get_move(state,player):
    if player==1:
        Q=LoadTable("Q1_breakthrough_table.json")
    else:
        Q=LoadTable("Q2_breakthrough_table.json")
        
    
    if state not in Q:
        return random_move(state,player)  # this is defined in my game functions import
    else:
        return top_choice(Q[state])


# ## Make Move

# In[4]:


def make_move(move):
    print("Making move ",move)
    
    board=Board(4,4)  # just to get the conversion functions for free
    
    start,end=move
    rs,cs=board.rc_from_index(start)  # convert to row, column
    re,ce=board.rc_from_index(end)
    
    distance_to_board=10
    length_column=4
    length_row=4

    type_of_move=ce-cs  # 0 for a forward move, +1 for a right-hand diagonal, -1 for left-hand diagonal
    distance_to_column=distance_to_board+length_column*cs
    distance_to_row=(4-rs)*length_row

    if type_of_move==0:  # forward

        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)
        arm_down()  # to push the piece
        move_forward( 1*length_row )
        arm_up()

        # go back
        move_backward(distance_to_row + 1*length_row)
        turn_robot_right_90()
        move_backward(distance_to_column)

    elif type_of_move==1:  # right-hand diagonal

        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)


        arm_down()  # to push the piece
        turn_robot_right_45()
        move_forward( 1*length_row )

        # go back
        move_backward(1*length_row)
        turn_robot_left_45()    
        move_backward(distance_to_row )
        turn_robot_right_90()
        move_backward(distance_to_column)

    elif type_of_move==-1:  # left-hand diagonal
        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)


        arm_down()  # to push the piece
        turn_robot_left_45()
        move_forward( 1*length_row )

        # go back
        move_backward(1*length_row)
        turn_robot_right_45()    
        move_backward(distance_to_row )
        turn_robot_right_90()
        move_backward(distance_to_column)

    else:
        raise ValueError("You can't get there from here.")


# ## Read State

# In[5]:


def read_state_from_file(filename):
    text=open(filename).read()
    text=text.strip()
    lines=[line.strip() for line in text.split('\n')]  # get rid of \n
    
    row=lines[0].split()
    R,C=len(lines),len(row)
    print(f"{R}x{C} board")
    state=Board(R,C)
    state.board=[int(val) for val in text.split()]  
    print(state)
    return state


# In[6]:


def read_state():
    from pylab import imread,imsave
    from numpy import atleast_2d
    import os

    state=Board(4,4)      #<========= change the size
    nr,nc=state.shape

    
    # load the classifier
    classifier=CSC()
    classifier.load('CSC_trained.json')
    
    
    # get the picture
    filename='current_board.jpg'              # for the robot
    take_picture(filename)


    # this part comes from your Make Training Squares script
    image=imread(filename)

    # these few lines are specific to your image
    corners= array([[ 64.,  33.],      # <=== check this
       [295.,  31.],
       [313., 255.],
       [ 44., 256.]], dtype=float32) 
    
    im3=straighten_image(image,corners)
    squares=get_board_squares_from_image(im3,
                                     state.shape,
                                     middle_pixels=20)  # <=== check this

    # for debugging
    if not os.path.exists('predicted'):
        os.mkdir('predicted')

    count=0
    values=[]
    
    for r in range(nr):
        for c in range(nc):
            # convert the square image to a data vector for the classifier
            vector=squares[count].ravel()
            prediction=classifier.predict(atleast_2d(vector))[0]
        
            values.append(prediction)
    
            # for debugging
            imsave('predicted/square %d predicted as piece %d.jpg' % (count,prediction),squares[count])

            count+=1

    
    # reconstruct the state from the predictions
    state.board=values

    print("Current state is:")
    print(state)

    x=input("""
    Hit return if this is correct, otherwise type a character 
    and the state will be read from board.txt... 
    or type in a Board string like 111/000/222: """)

    if x:
        if "/" in x and '0' in x:
            state=Board(x)
        else:
            print("Reading from file...")
            state=read_state_from_file('board.txt')

    print("Using")
    print(state)

    
    return state


# In[7]:


classifier=CSC()
classifier.load('CSC_trained.json')


# on the laptop, look at the image to see if the state is correct.  remove this imread and imshow on the robot

# In[8]:


if on_laptop:
    image=imread("current_board.jpg")
    imshow(image)


# In[9]:


if on_laptop:
    state=read_state()


# ## Now the entire project

# In[10]:


state=read_state()     #  read the state from the world
move=get_move(state,1)   # from an agent
make_move(move)        # robot motion to move pieces, etc...


# In[ ]:




