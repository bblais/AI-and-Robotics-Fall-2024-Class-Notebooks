#!/usr/bin/env python
# coding: utf-8

# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from classy import *
from classy.image import read_warped_image
import cv2


# ## still needs debugging -- may work for your images

# In[2]:


im=imread('images/board images/test3.jpg')
imshow(im)


# In[3]:


im,warped_im,info=read_warped_image('images/board images/test3.jpg')
subplot(1,2,1)
imshow(im)
title('Original')
subplot(1,2,2)
if not warped_im is None:
    imshow(warped_im)
    title('Warped')


# In[4]:


im,warped_im,info=read_warped_image('images/chess-board-png-8-2225905603.png')
subplot(1,2,1)
imshow(im)
title('Original')
subplot(1,2,2)
if not warped_im is None:
    imshow(warped_im)
    title('Warped')


# In[29]:


im,warped_im,info=read_warped_image('images/83a1d1f1-0d06-454a-997f-06b454c2685a.jpg')
subplot(1,2,1)
imshow(im)
title('Original')
subplot(1,2,2)
if not warped_im is None:
    imshow(warped_im)
    title('Warped')


# In[30]:


info['ordered_corners']


# In[31]:


imshow(info['edges'])
colorbar()


# In[43]:


corners = cv2.goodFeaturesToTrack(info['edges'], 4, 0.5, 50)
imshow(im)

x=corners[:,:,0]
y=corners[:,:,1]
plot(x,y,'ro')


# In[42]:





# In[ ]:




