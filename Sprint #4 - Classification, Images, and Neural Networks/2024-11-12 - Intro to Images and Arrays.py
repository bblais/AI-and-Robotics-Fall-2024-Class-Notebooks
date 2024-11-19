#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[4]:


im=imread("images/cats.jpg")


# In[5]:


imshow(im)


# In[10]:


subim=im[800:1200,1500:1800,:]
imshow(subim)


# In[19]:


figure(figsize=(20,8))
for i in range(3):
    subplot(1,3,i+1)
    subim=im[800:1200,1500:1800,i]
    imshow(subim,cmap=cm.grey)
    colorbar()


# In[ ]:





# In[ ]:





# In[7]:


1213*1820


# In[9]:


subim=im[800:1000,250:750,:]
imshow(subim)


# In[20]:


im=imread("images/connect4.png")
imshow(im)


# In[21]:


im.shape


# In[25]:


figure(figsize=(20,8))
for i,color in zip(range(3),['red','green','blue']):
    subplot(1,3,i+1)
    imshow(im[:,:,i],cmap=cm.grey)
    title(color)
    colorbar()


# ## Now your turn.....
# 
# - get some pics
# - for each pic
#     - view the entire image
#     - look at the size (im.shape) -- does it make sense?
#     - look at individual channels (red, green, blue) -- does it make sense?
#     - extract individual squares

# In[26]:


im=imread('images/chess-board-png-8-2225905603.png')
imshow(im)


# In[27]:


im.shape


# In[33]:


figure(figsize=(30,8))
for i,color in zip(range(4),['red','green','blue','transparent']):
    subplot(1,4,i+1)
    imshow(im[:,:,i],cmap=cm.gray)
    title(color)
    colorbar()


# In[34]:


im=imread('images/chess-board-png-8-2225905603.png')
red=im[:,:,0]
green=im[:,:,1]
blue=im[:,:,2]

gray=0.2989*red+0.5870*green+ 0.1140*blue
imshow(gray)


# In[35]:


gray.shape


# In[36]:


imshow(gray,cmap=cm.gray)


# In[ ]:




