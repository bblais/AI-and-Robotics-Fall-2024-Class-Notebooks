#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from classy import *


# In[2]:


data=load_excel('data/iris.xls')


# In[3]:


data.vectors


# In[4]:


data.targets


# ## Do these shapes make sense?

# In[6]:


summary(data)


# In[7]:


data_train,data_test=split(data,0.2)


# ## Go to 2D for visualization

# In[29]:


subset=extract_features(data,[0,1])


# In[30]:


plot2D(subset)


# In[38]:


C=NaiveBayes()
C.fit(subset.vectors,subset.targets)
subset.vectors


# In[39]:


subset.targets


# In[40]:


subset.vectors[subset.targets==0]


# In[41]:


subset.vectors[subset.targets==0].mean(axis=0)


# In[32]:


C.means


# In[43]:


plot2D(subset,C)
C.plot_centers()
title("Naive Bayes")


# In[50]:


figure(figsize=(20,8))
k=1
subset=extract_features(data,[0,1])
C=kNearestNeighbor(k=k)
C.fit(subset.vectors,subset.targets)
subplot(1,2,1)
plot2D(subset,C)
title(f"kNearestNeighbor k={k}")

k=5
subset=extract_features(data,[0,1])
C=kNearestNeighbor(k=k)
C.fit(subset.vectors,subset.targets)
subplot(1,2,2)
plot2D(subset,C)
title(f"kNearestNeighbor k={k}")


# In[20]:


subset=extract_features(data,[2,3])
C=NaiveBayes()
C.fit(subset.vectors,subset.targets)
plot2D(subset,C)
C.plot_centers()


# ## Back to the 4D data

# In[21]:


data_train,data_test=split(data,0.2)


# In[22]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)

print("On the training data: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test data: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[23]:


C.means


# In[24]:


C=kNearestNeighbor(k=5)
C.fit(data_train.vectors,data_train.targets)

print("On the training data: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test data: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[25]:


C=CSC()
C.fit(data_train.vectors,data_train.targets)

print("On the training data: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test data: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[26]:


C.centers


# In[27]:


C.radii


# In[28]:


C.targets


# ## More work

# - try with RCE
# - try with CSC
# - try with data Alice Bob
# - try with data Simple Classification

# In[ ]:




