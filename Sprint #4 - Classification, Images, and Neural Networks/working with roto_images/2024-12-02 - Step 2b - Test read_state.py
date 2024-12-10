#!/usr/bin/env python
# coding: utf-8

# In[9]:


from classy import *
from pylab import imread,imsave,imshow,float32,figure,subplot,title,text,axis
from numpy import atleast_2d
import numpy as np
from image_defs import *
from glob import glob
from my_robot_functions import *
from Game import Board


# In[10]:


board_picture_folder='images/rotoimages/'
square_images_folder='images/rotoimages squares'
image_to_use_for_corners="images/rotoimages/roto1.jpg"

# from corners import *
corners= array([[ 415.,   46.],
       [1293.,   84.],
       [1402.,  839.],
       [ 276.,  801.]], dtype=float32)


# - if you want to test the read_state function, pretending to be the robot, copy one of the board images to current_board.jpg

# In[11]:


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


# ## Read State

# In[12]:


filenames=glob("images/test rotoimages/*.jpg")
print(filenames)


# In[13]:


C=int(np.ceil(np.sqrt(len(filenames))))
R=int(np.ceil(len(filenames)/C))

for f,filename in enumerate(filenames):
    subplot(R,C,f+1)
    
    state=Board(3,3)      #<========= change the size
    nr,nc=state.shape
    
    # load the classifier
    classifier=CSC()
    classifier.load('CSC_trained.json')
    
    # this part comes from your Make Training Squares script
    image=imread(filename)
    
    im3=straighten_image(image,corners)
    squares=get_board_squares_from_image(im3,
                                     state.shape,
                                     middle_pixels=20)  # <=== check this
    
    imshow(image)
        
    count=0
    values=[]
    
    for r in range(nr):
        for c in range(nc):
            # convert the square image to a data vector for the classifier
            vector=squares[count].ravel()
            prediction=classifier.predict(atleast_2d(vector))[0]
        
            values.append(prediction)
    
            count+=1
    
    
    # reconstruct the state from the predictions
    state.board=values
    
    title(str(state),fontsize=5)
    axis('off')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


def read_state():
    from pylab import imread,imsave
    from numpy import atleast_2d
    import os

    state=Board(3,3)      #<========= change the size
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
    corners= array([[ 418.,   46.],     # <=== check this
       [1293.,   91.],
       [1402.,  839.],
       [ 283.,  801.]], dtype=float32) 

    
    im3=straighten_image(image,corners)
    squares=get_board_squares_from_image(im3,
                                     state.shape,
                                     middle_pixels=20)  # <=== check this

    # for debugging
    if not os.path.exists('predicted'):
        os.mkdir('predicted')

    count=0
    values=[]
    if on_laptop:
        figure()

    
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


# In[19]:


filename='current_board.jpg'              # for the robot
image=imread(filename)
imshow(image)


# In[20]:


state=read_state()     #  read the state from the world


# In[ ]:




