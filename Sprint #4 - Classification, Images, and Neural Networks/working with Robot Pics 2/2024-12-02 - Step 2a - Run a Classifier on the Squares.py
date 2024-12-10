#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[3]:


from classy import *


# In[4]:


board_picture_folder='images/Robot Pics 2/'
square_images_folder='images/Robot Pics 2 squares'
image_to_use_for_corners="images/Robot Pics 2/image_filename50.jpg"

from corners import *


# In[5]:


images=image.load_images(square_images_folder)

# this line makes sure the target values = 0,1,2 in the right order
# although not strictly necessary, it makes read_state a lot easier
images=remap_targets(images,new_target_names=['piece_0','piece_1','piece_2'])
summary(images)


# In[6]:


data=image.images_to_vectors(images)


# In[7]:


data_train=data  # training on all data


# In[8]:


C=CSC()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))


# In[9]:


C.save("CSC_trained.json")


# In[ ]:




