#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from glob import glob
from image_defs import *
import os
from Game import Board


# In[2]:


board_picture_folder='images/rotoimages/'
square_images_folder='images/rotoimages squares'
image_to_use_for_corners="images/rotoimages/roto1.jpg"

from corners import *


# In[4]:


filename=image_to_use_for_corners


# In[5]:


image=imread(filename)
subplot(2,1,1)
imshow(image)

# these few lines are specific to your image
im3=straighten_image(image,corners)


subplot(2,1,2)
imshow(im3)


# In[6]:


state=Board('102/000/000')
squares=get_board_squares_from_image(im3,
                                     state.shape,
                                     middle_pixels=20)  # <=== check this


# In[7]:


nr,nc=state.shape
plot_count=0
figure(figsize=(10,10))
for r in range(nr):
    for c in range(nc):

        subplot(nr,nc,plot_count+1)
        imshow(squares[plot_count])

        shape=squares[plot_count].shape
        piece=state.board[plot_count]
        
        title(f"Piece {piece}")
        if c==0:
            ylabel(shape[0])

        if r==nr-1:
            xlabel(shape[1])
        gca().set_xticklabels([])
        gca().set_yticklabels([])

        
        plot_count+=1  
        



# In[ ]:




