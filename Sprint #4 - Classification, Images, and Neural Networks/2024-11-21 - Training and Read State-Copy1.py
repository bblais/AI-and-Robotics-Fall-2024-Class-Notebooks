#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
import cv2
from image_defs import *


# ## Get the image slicing to work with one image
# 
# - You need a thresholded (black and white)
# - you may need to truncate the image to omit stuff outside the board

# In[72]:


training_boards_folder='images/2024-11-21 - training board images'
image=imread(f"{training_boards_folder}/test0.jpg")
imshow(image)


# if you need to truncate, do it here (I don't really, but I can truncate a bit)

# In[73]:


image=image[30:260,20:340,:]
imshow(image)


# In[ ]:





# In[55]:


gray,black_and_white=get_gray_and_threshold_image(image,threshold=90)

figure()
imshow(gray,cmap=cm.gray)
colorbar()


figure()
imshow(black_and_white,cmap=cm.gray)
colorbar()



# In[56]:


corners=find_corners(black_and_white,plotit=True)


# In[57]:


im3=straighten_image(image,corners)
figure(figsize=(20,8))

subplot(1,2,1)
imshow(image)

subplot(1,2,2)
imshow(im3)


# In[58]:


from Game import Board
state=Board('2222/2222/2222/2222')
print(state)
squares=get_board_squares_from_image(im3,state.shape)


# In[59]:


import os


# In[60]:


training_squares_folder='images/2024-11-21 - training squares'

if not os.path.exists(training_squares_folder):
    print(f"Making folder {training_squares_folder}")
    os.mkdir(training_squares_folder)


nr,nc=state.shape
saveit=True

count=0
for r in range(nr):
    for c in range(nc):

        subplot(nr,nc,count+1)
        imshow(squares[count])

        shape=squares[count].shape
        piece=state.board[count]
        
        title(f"Piece {piece}")
        if c==0:
            ylabel(shape[0])

        if r==nr-1:
            xlabel(shape[1])
        gca().set_xticklabels([])
        gca().set_yticklabels([])


        if saveit:
            piece_folder=f"{training_squares_folder}/piece_{piece}"
            if not os.path.exists(piece_folder):
                print(f"Making folder {piece_folder}")
                os.mkdir(piece_folder)
            
            fname=f"{piece_folder}/square{count}_{piece}.jpg"
            print(fname)
            imsave(fname,squares[count])
        
        
        count+=1        



# In[61]:


training_squares_folder='images/2024-11-21 - training squares'

if not os.path.exists(training_squares_folder):
    print(f"Making folder {training_squares_folder}")
    os.mkdir(training_squares_folder)


nr,nc=state.shape
saveit=True

count=0
for r in range(nr):
    for c in range(nc):

        subplot(nr,nc,count+1)
        imshow(squares[count])

        shape=squares[count].shape
        piece=state.board[count]
        
        title(f"Piece {piece}")
        if c==0:
            ylabel(shape[0])

        if r==nr-1:
            xlabel(shape[1])
        gca().set_xticklabels([])
        gca().set_yticklabels([])


        if saveit:
            piece_folder=f"{training_squares_folder}/piece_{piece}"
            if not os.path.exists(piece_folder):
                print(f"Making folder {piece_folder}")
                os.mkdir(piece_folder)
            
            fname=f"{piece_folder}/square{count}_{piece}.jpg"
            print(fname)
            imsave(fname,squares[count])
        
        
        count+=1        



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Now we want to loop through boards

# In[62]:


from glob import glob


# In[63]:


glob(training_boards_folder+"/*.jpg")


# In[64]:


board_filenames=glob(training_boards_folder+"/*.jpg")
print(len(board_filenames))


# In[68]:


count=1
for filename in board_filenames:
    subplot(3,4,count)
    image=imread(filename)
    imshow(image)

    image=image[30:260,20:340]  # truncate if you need to
    
    base,name=os.path.split(filename)
    title(name)
    count+=1


# Put in the Game board definitions

# In[66]:


from Game import *


# In[67]:


game_boards=[
    '0000/0000/0000/0000',
    '1111/1111/1111/1111',
    '1111/1111/1111/1111',
    '1111/1111/1111/1111',
    '0000/0000/0000/0000',
    '2222/2222/2222/2222',
    '2222/2222/2222/2222',
    '0202/2020/0202/0202',
    '2222/2222/2222/2222',
    '1101/1011/0000/1111',
]


# In[69]:


count=0
for filename,board_string in zip(board_filenames,game_boards):
    state=Board(board_string)
    print(filename,board_string)
    image=imread(filename)

    image=image[30:260,20:340,:]  # truncate if you need to

    
    gray,black_and_white=get_gray_and_threshold_image(image,threshold=90)
    corners=find_corners(black_and_white,plotit=False)
    im3=straighten_image(image,corners)
    squares=get_board_squares_from_image(im3,state.shape)


    training_squares_folder='images/2024-11-21 - training squares'
    
    if not os.path.exists(training_squares_folder):
        print(f"Making folder {training_squares_folder}")
        os.mkdir(training_squares_folder)
    
    
    nr,nc=state.shape
    saveit=True

    figure()
    plot_count=0
    for r in range(nr):
        for c in range(nc):
    
            subplot(nr,nc,plot_count+1)
            imshow(squares[plot_count])
    
            shape=squares[plot_count].shape
            piece=state.board[plot_count]
            
            title(f"Piece {piece}")
            if c==0:
                ylabel(shape[0])
    
            if r==nr-1:
                xlabel(shape[1])
            gca().set_xticklabels([])
            gca().set_yticklabels([])
    
    
            if saveit:
                piece_folder=f"{training_squares_folder}/piece_{piece}"
                if not os.path.exists(piece_folder):
                    print(f"Making folder {piece_folder}")
                    os.mkdir(piece_folder)
                
                fname=f"{piece_folder}/square{count}_{piece}.jpg"
                print(fname)
                imsave(fname,squares[plot_count])
            
            
            plot_count+=1  
            count+=1




# ## if you want just the middle of the square, you can truncate the squares like ....

# In[70]:


count=0
for filename,board_string in zip(board_filenames,game_boards):
    state=Board(board_string)
    print(filename,board_string)
    image=imread(filename)

    image=image[30:260,20:340,:]  # truncate if you need to

    gray,black_and_white=get_gray_and_threshold_image(image,threshold=90)
    corners=find_corners(black_and_white,plotit=False)
    im3=straighten_image(image,corners)
    squares=get_board_squares_from_image(im3,state.shape)


    squares=[sq[20:40,20:40,:] for sq in squares]

    training_squares_folder='images/2024-11-21 - training squares'
    
    if not os.path.exists(training_squares_folder):
        print(f"Making folder {training_squares_folder}")
        os.mkdir(training_squares_folder)
    
    
    nr,nc=state.shape
    saveit=True

    figure()
    plot_count=0
    for r in range(nr):
        for c in range(nc):
    
            subplot(nr,nc,plot_count+1)
            imshow(squares[plot_count])
    
            shape=squares[plot_count].shape
            piece=state.board[plot_count]
            
            title(f"Piece {piece}")
            if c==0:
                ylabel(shape[0])
    
            if r==nr-1:
                xlabel(shape[1])
            gca().set_xticklabels([])
            gca().set_yticklabels([])
    
    
            if saveit:
                piece_folder=f"{training_squares_folder}/piece_{piece}"
                if not os.path.exists(piece_folder):
                    print(f"Making folder {piece_folder}")
                    os.mkdir(piece_folder)
                
                fname=f"{piece_folder}/square{count}_{piece}.jpg"
                print(fname)
                imsave(fname,squares[plot_count])
            
            
            plot_count+=1  
            count+=1




# In[ ]:





# In[ ]:





# In[ ]:





# ## You can save flipped/rotated versions like...

# In[51]:


count=0
for filename,board_string in zip(board_filenames,game_boards):
    state=Board(board_string)
    print(filename,board_string)
    image=imread(filename)
    gray,black_and_white=get_gray_and_threshold_image(image,threshold=90)
    corners=find_corners(black_and_white,plotit=False)
    im3=straighten_image(image,corners)
    squares=get_board_squares_from_image(im3,state.shape)


    training_squares_folder='images/2024-11-21 - training squares'
    
    if not os.path.exists(training_squares_folder):
        print(f"Making folder {training_squares_folder}")
        os.mkdir(training_squares_folder)
    
    
    nr,nc=state.shape
    saveit=True

    figure()
    plot_count=0
    for r in range(nr):
        for c in range(nc):
    
            subplot(nr,nc,plot_count+1)
            imshow(squares[plot_count])
    
            shape=squares[plot_count].shape
            piece=state.board[plot_count]
            
            title(f"Piece {piece}")
            if c==0:
                ylabel(shape[0])
    
            if r==nr-1:
                xlabel(shape[1])
            gca().set_xticklabels([])
            gca().set_yticklabels([])
    
    
            if saveit:
                piece_folder=f"{training_squares_folder}/piece_{piece}"
                if not os.path.exists(piece_folder):
                    print(f"Making folder {piece_folder}")
                    os.mkdir(piece_folder)
                
                fname=f"{piece_folder}/square{count}_{piece}.jpg"
                print(fname)
                imsave(fname,squares[plot_count])
            
            
            plot_count+=1  
            count+=1





## flipped 
for filename,board_string in zip(board_filenames,game_boards):
    state=Board(board_string)
    print(filename,board_string)
    image=imread(filename)
    gray,black_and_white=get_gray_and_threshold_image(image,threshold=90)
    corners=find_corners(black_and_white,plotit=False)
    im3=straighten_image(image,corners)
    squares=get_board_squares_from_image(im3,state.shape)


    ## flipped 
    squares=[np.fliplr(sq) for sq in squares]


    training_squares_folder='images/2024-11-21 - training squares'
    
    if not os.path.exists(training_squares_folder):
        print(f"Making folder {training_squares_folder}")
        os.mkdir(training_squares_folder)
    
    
    nr,nc=state.shape
    saveit=True

    figure()
    plot_count=0
    for r in range(nr):
        for c in range(nc):
    
            subplot(nr,nc,plot_count+1)
            imshow(squares[plot_count])
    
            shape=squares[plot_count].shape
            piece=state.board[plot_count]
            
            title(f"Piece {piece}")
            if c==0:
                ylabel(shape[0])
    
            if r==nr-1:
                xlabel(shape[1])
            gca().set_xticklabels([])
            gca().set_yticklabels([])
    
    
            if saveit:
                piece_folder=f"{training_squares_folder}/piece_{piece}"
                if not os.path.exists(piece_folder):
                    print(f"Making folder {piece_folder}")
                    os.mkdir(piece_folder)
                
                fname=f"{piece_folder}/square{count}_{piece}.jpg"
                print(fname)
                imsave(fname,squares[plot_count])
            
            
            plot_count+=1  
            count+=1
        


# In[ ]:




