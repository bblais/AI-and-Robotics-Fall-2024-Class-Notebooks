#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from classy import *


# In[3]:


board_picture_folder='images/2024-11-21 - training board images'
square_images_folder='images/2024-11-21 - training squares'
image_to_use_for_corners="images/2024-11-21 - training board images/test0.jpg"

corners= array([[ 64.,  33.],
       [295.,  31.],
       [313., 255.],
       [ 44., 256.]], dtype=float32) 


# In[4]:


images=image.load_images(square_images_folder)

# this line makes sure the target values = 0,1,2 in the right order
# although not strictly necessary, it makes read_state a lot easier
images=remap_targets(images,new_target_names=['piece_0','piece_1','piece_2'])
summary(images)


# In[5]:


data=image.images_to_vectors(images)


# In[6]:


data_train=data  # training on all data


# In[7]:


C=CSC()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))


# In[8]:


C.save("CSC_trained.json")


# In[ ]:




