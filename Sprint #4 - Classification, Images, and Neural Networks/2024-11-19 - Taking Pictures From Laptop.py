#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
import os
from time import sleep
from IPython.display import clear_output


# ## need to install ffmpeg -- is there another solution for windows?

# In[ ]:


count=0
while True:
    fname=f"output{count}.jpg"
    os.system(f'ffmpeg -y -f avfoundation -framerate 30 -i "0" -vframes 1 {fname} >>out.log 2>&1')
    im=imread(fname)
    imshow(im)
    title(fname)
    show()
    sleep(2)
    count+=1
    clear_output(wait=True)

