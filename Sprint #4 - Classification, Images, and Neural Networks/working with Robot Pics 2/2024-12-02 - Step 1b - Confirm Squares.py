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


board_picture_folder='images/Robot Pics 2/'
square_images_folder='images/Robot Pics 2 squares'
image_to_use_for_corners="images/Robot Pics 2/image_filename50.jpg"

corners= array([[ 425.,   52.],
       [1205.,   30.],
       [1270.,  849.],
       [ 373.,  862.]], dtype=float32) 


# In[3]:


filename=image_to_use_for_corners


# In[4]:


image=imread(filename)
im3=straighten_image(image,corners)

subplot(2,1,1)
imshow(image)

subplot(2,1,2)
imshow(im3)


# In[5]:


state=Board('1111/0000/0000/2222')
squares=get_board_squares_from_image(im3,
                                     state.shape,
                                     middle_pixels=20)  # <=== check this


# In[6]:


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




