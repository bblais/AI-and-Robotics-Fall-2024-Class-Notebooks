#!/usr/bin/env python
# coding: utf-8

# - assume you have a set of training squares

# In[3]:


from pylab import imread,imsave
from numpy import atleast_2d
import os
from classy import *


# In[4]:


images=image.load_images('images/2024-11-21 - training squares')


# In[ ]:





# In[ ]:





# In[1]:


from pylab import imread,imsave
from numpy import atleast_2d
import os

# train the classifier - it'd be better to load



# images=image.load_images('images/training squares/',delete_alpha=True)  #<=========
# images=remap_targets(images,new_target_names=['blank','player1','player2'])
# data=image.images_to_vectors(images,verbose=True)  # train on all of them

# classifier=NaiveBayes()
# classifier.fit(data.vectors,data.targets)

# classifier.save("previously_saved_classifier_result.json")

# if you don't need to train the classifier
classifier=NaiveBayes()
#classifier=kNearestNeighbor()
classifier.load('previously_saved_classifier_result.json')




# get the picture
fname='current_board.jpg'              # for the robot
take_picture(fname)
im=imread(fname)

# slice the picture into squares of the right size
square_size=50 # choose a size that works for you
import json
with open('locations.json') as json_file:
    locations = json.load(json_file)

count=0
# for debugging
if not os.path.exists('images/predicted'):
    os.mkdir('images/predicted')

values=[]
for r,c in locations:
    sr=r-square_size//2
    er=sr+square_size
    sc=c-square_size//2
    ec=sc+square_size   
    subimage=im[sr:er,sc:ec,:]

    # convert the square image to a data vector for the classifier
    vector=subimage.ravel()
    prediction=classifier.predict(atleast_2d(vector))[0]

    values.append(prediction)

    # for debugging
    #imsave('images/predicted/square %d predicted as %s.jpg' % (count,data.target_names[prediction]),subimage)

    count+=1


# reconstruct the state from the predictions
state=Board(4,4)                                      #<========= change the size
state.board=values

print("Current state is:")
print(state)

x=input("""
Hit return if this is correct, otherwise type a character 
and the state will be read from current_board.txt.""")

if x:
    print("Reading from file...")
    state=read_state_from_file('board.txt')

print("Using")
print(state)


# In[ ]:




