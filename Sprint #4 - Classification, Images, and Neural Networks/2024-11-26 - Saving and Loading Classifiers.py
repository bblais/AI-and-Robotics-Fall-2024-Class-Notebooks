#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from classy import *


# In[3]:


data=load_excel('data/iris.xls')


# In[4]:


C=NaiveBayes()
C.fit(data.vectors,data.targets)


# In[5]:


print("On the full data set:",C.percent_correct(data.vectors,data.targets))


# In[6]:


C.save("naive_bayes_iris_trained.json")


# In[7]:


C1=NaiveBayes()
C1.load("naive_bayes_iris_trained.json")


# In[8]:


print("On the full data set:",C1.percent_correct(data.vectors,data.targets))


# In[9]:


C=kNearestNeighbor()
C.fit(data.vectors,data.targets)
C.save("knn_iris_trained.json")


# # Perceptron
# 
# - linear units
# - no hidden layers
# 
# - (if everything linear, then even hidden units are the same as no hidden units)

# In[10]:


C=NumPyNetBackProp({
    'input':4,               # number of features
    'output':(3,'linear'),  # number of classes
    'cost':'mse',
})


# In[11]:


C.fit(data.vectors,data.targets,epochs=10000)
print("On the full data set:",C.percent_correct(data.vectors,data.targets))


# In[12]:


number_of_features=4
number_of_categories=3


# ## Backprop with hidden units

# In[13]:


C=NumPyNetBackProp({
    'input':number_of_features,               # number of features
    'hidden':[(5,'logistic'),],   # this size is "arbitrary"
    'output':(number_of_categories,'logistic'),  # number of classes
    'cost':'mse',
})
C.fit(data.vectors,data.targets,epochs=3000)


# In[14]:


print("On the full data set:",C.percent_correct(data.vectors,data.targets))


# In[15]:


C.save("backprop_iris_trained.json")


# In[ ]:




