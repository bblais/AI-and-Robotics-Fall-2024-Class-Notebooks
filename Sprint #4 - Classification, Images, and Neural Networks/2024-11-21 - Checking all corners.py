#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
import cv2
from image_defs import *
from glob import glob


# In[2]:


training_boards_folder='images/2024-11-21 - training board images'


# In[5]:


training_boards_folder='images/Jason Board Images'


# In[6]:


board_filenames=glob(training_boards_folder+"/*.jpg")
print(len(board_filenames))


# In[17]:


count=0
figure(figsize=(20,18))
for filename in board_filenames:
    image=imread(filename)
    image=image[100:800,250:1350,:]  # truncate if you need to
    
    gray,black_and_white=get_gray_and_threshold_image(image,threshold=180)
    subplot(4,5,count+1)
    imshow(gray,cmap=cm.gray)
    colorbar()
    count+=1


count=0
figure(figsize=(20,18))
for filename in board_filenames:
    image=imread(filename)
    image=image[100:800,250:1350,:]  # truncate if you need to
    gray,black_and_white=get_gray_and_threshold_image(image,threshold=160)
    subplot(4,5,count+1)
    corners=find_corners(black_and_white,plotit=True)
    count+=1


# In[ ]:




