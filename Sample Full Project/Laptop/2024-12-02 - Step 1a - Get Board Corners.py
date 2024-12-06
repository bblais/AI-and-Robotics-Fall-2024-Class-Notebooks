#!/usr/bin/env python
# coding: utf-8

# - make a folder for just board pictures -- you only need a handful usually
# - pull out two for testing the read_state
# - make a different folder for having the square images for classification
# - select one image for getting the corners
#     - make sure to truncate the image (if needed) and copy this truncation into any other notebooks
# - for some reason the "Run All Cells" doesn't print out the corners, but executing the cells one-by-one does. weird.
# - copy the displayed "corners=..." at the end

# In[15]:


board_picture_folder='images/2024-11-21 - training board images'
square_images_folder='images/2024-11-21 - training squares'
image_to_use_for_corners="images/2024-11-21 - training board images/test0.jpg"


# In[16]:


get_ipython().run_line_magic('matplotlib', 'qt5')
from IPython.display import display


# To install, do this on a commandline
# > pip install pyqt5

# In[17]:


from pylab import *


# In[18]:


def on_click(event):
    from pylab import plot,show,close
    global ix, iy
    global corners,fig,ax
    
    
    ix, iy = event.xdata, event.ydata
    global coords
    coords = [int(ix), int(iy)]
    
    corners.append([coords[0],coords[1]])  # x, y not row/col
    
    ax.plot(ix,iy,'go')
    fig.canvas.draw()
    show()

    if len(corners)==4:
        corners=array(sort_corners(corners)).astype(float32)
        print("\n","corners=",corners.__repr__(),"\n",)
        close(fig)
        corners=[]
        
    
    return coords


# In[19]:


def sort_corners(corners):
    import numpy as np
    new_corners=[]
    mx,my=np.mean(corners,axis=0)
    
    for i in range(4):
            
        for x,y in corners:
            # top left
            if x<mx and y<my and i==0:
                new_corners.append([x,y])
        
            # top right
            if x>mx and y<my and i==1:
                new_corners.append([x,y])
        
            # bottom right
            if x>mx and y>my and i==2:
                new_corners.append([x,y])
        
            # bottom left
            if x<mx and y>my and i==3:
                new_corners.append([x,y])

    return new_corners


# In[20]:


corners=[]
filename=image_to_use_for_corners


fig=figure()
ax=subplot(1,1,1)
image=imread(filename)

#image=image[:,300:1400]  # truncate if you need to
imshow(image)

cid = fig.canvas.mpl_connect('button_press_event', on_click)


# In[ ]:




