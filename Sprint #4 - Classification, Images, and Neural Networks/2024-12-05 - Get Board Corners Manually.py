#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'qt5')


# 
# > pip install pyqt5

# In[2]:


from pylab import *


# In[3]:


def on_click(event):
    from pylab import plot,show,close
    global ix, iy
    global corners,fig,ax
    
    ix, iy = event.xdata, event.ydata
    global coords
    coords = [int(ix), int(iy)]
    
    corners.append([coords[1],coords[0]])  # row,col not x, y
    
    ax.plot(ix,iy,'go')
    fig.canvas.draw()
    show()

    if len(corners)==4:
        corners=array(sort_corners(corners)).astype(float32)
        print("\n","corners=",corners.__repr__(),"\n",)
        close(fig)
        corners=[]
    
    return coords


# In[4]:


def sort_corners(corners):
    import numpy as np
    new_corners=[]
    mr,mc=np.mean(corners,axis=0)
    
    for i in range(4):
            
        for r,c in corners:
            # top left
            if r<mr and c<mc and i==0:
                new_corners.append([r,c])
        
            # top right
            if r<mr and c>mc and i==1:
                new_corners.append([r,c])
        
            # bottom right
            if r>mr and c>mc and i==2:
                new_corners.append([r,c])
        
            # bottom left
            if r>mr and c<mc and i==3:
                new_corners.append([r,c])

    return new_corners


# In[5]:


corners=[]
filename="images/board to reconstruct - was test9.jpg"


fig=figure()
ax=subplot(1,1,1)
arr=imread(filename)
imshow(arr)


cid = fig.canvas.mpl_connect('button_press_event', on_click)


# In[ ]:





# In[ ]:




