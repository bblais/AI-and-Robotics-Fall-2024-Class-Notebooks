#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from classy import *


# In[3]:


ls "images/training squares"


# ## Do these numbers make sense?

# In[4]:


images=image.load_images('images/training squares/')
images=remap_targets(images,new_target_names=['blank','player1','player2'])
summary(images)


# In[5]:


images['data'][0].shape


# In[6]:


imshow(images['data'][0])


# ## Do these numbers make sense?

# In[7]:


data=image.images_to_vectors(images)


# # Classification

# In[8]:


data_train,data_test=split(data,test_size=0.2)


# In[9]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[10]:


C.means


# ## does this shape make sense?

# In[13]:


C.means.shape


# In[15]:


one_mean=C.means[1,:]
im0=one_mean.reshape((50,50,3))
im0=im0-im0.min()  # set the min to zero
im0=im0/im0.max()  # set the max to 1
imshow(im0)


# - visualize the other ones

# Some classifiers have more than 1 prototype per category.  for CSC and RCE they are called `C.centers`.

# In[16]:


C=CSC()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[17]:


C.centers.shape


# - visualize these

# ## can you visualize kNearestNeighbor this way?

# # Some more classification examples

# - try the digits folder
# - make a new folder with a handful of the categories from the hawkins_bitmaps

# In[ ]:




