#!/usr/bin/env python
# coding: utf-8

# - make a folder for just board pictures -- you only need a handful usually
# - pull out two for testing the read_state
# - make a different folder for having the square images for classification
# - select one image for getting the corners
#     - make sure to truncate the image (if needed) and copy this truncation into any other notebooks
# - for some reason the "Run All Cells" doesn't print out the corners, but executing the cells one-by-one does. weird.
# - copy the displayed "corners=..." at the end

# In[1]:


board_picture_folder='images/Robot Pics 2/'
square_images_folder='images/Robot Pics 2 squares'
image_to_use_for_corners="images/Robot Pics 2/image_filename50.jpg"


# In[2]:


get_ipython().run_line_magic('matplotlib', 'qt5')
from IPython.display import display
from matplotlib.widgets import TextBox


# To install, do this on a commandline
# > pip install pyqt5

# In[3]:


from pylab import *


# In[4]:


def on_click(event):
    from pylab import plot,show,close,figure
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
        close(fig)

        with open("corners.py","w") as fid:
            fid.write("from numpy import array,float32\n")
            fid.write("\n"+"corners="+corners.__repr__()+"\n")
            fid.write("print(corners.__repr__())\n")
            

    
    return coords


# In[5]:


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


# In[6]:


corners=[]
filename=image_to_use_for_corners


fig=figure()
ax=subplot(1,1,1)
image=imread(filename)
imshow(image)

cid = fig.canvas.mpl_connect('button_press_event', on_click)


# In[7]:


corners


# In[ ]:




