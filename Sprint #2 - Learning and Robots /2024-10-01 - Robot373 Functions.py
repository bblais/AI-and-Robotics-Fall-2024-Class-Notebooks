#!/usr/bin/env python
# coding: utf-8

# - The Robot373 library is at https://github.com/bblais/Robot373
# - Download and Install it with:
# 
# `pip install "git+https://github.com/bblais/Robot373" --upgrade`

# In[2]:


from Robot373 import *


# # Motors

# The `Motors` function defines where the motors are connected.  In this example, we have a motor on port A which we will label `left` and one on port B which we label as `right`

# In[ ]:


left,right=Motors("ab")


# if you have your left motor on port C and right motor on B, you'd use

# In[ ]:


left,right=Motors("cb")


# You can set the power on a motor to between -100 and 100, for full power backward to full power forward using  `motorname.power=value`

# In[ ]:


left.power=+50
right.power=-50


# The `Wait` command doesn't do anything -- it sits at that point for the number of seconds.  Recall that motor commands like `left.power=50` is like light switch and won't change until another `left.power` assignment.  
# 
# The following example runs the left motor for 5 seconds.

# In[ ]:


left.power=50
Wait(5)  # wait for 5 seconds
left.power=0


# You can also read the current position of a robot motor (related to the angle it has turned) by using the `position` attribute, like

# In[ ]:


left.position


# The units for this position are somewhat arbitrary, so you'll have to figure out how it relates to angle turned.  You can reset this with the `reset_position` function.

# In[ ]:


left.reset_position()


# In[ ]:





# The `Shutdown` command should be run only at the end of your script.  It disconnects the sensors, powers down motors, etc...

# In[ ]:


Shutdown()


# # Sensors

# The `Sensors` function defines where the sensors are connected and what type they are.  Use `None` if there is nothing connected.
# 
# This example has the ultrasonic distance sensor (i.e. eyes) connected on port S3 and a touch sensor connected on port S4.  There is nothing connected to ports S1 and S2.

# In[ ]:


eyes,touch=Sensors(None,None,"us","touch")


# To get the value of a sensor, use `sensorname.value`.  Depending on the type of sensor, you may get a single number (e.g. ultrasonic and touch) or multiple numbers (e.g. color).  The number means different things depending on the sensor.
# 
# Types of sensors:
# 
# - "touch":  ![image.png](attachment:4f257ea6-2c31-4c76-bf69-adb2a65b8a16.png)
# - "us" or "ultrasonic": ![image.png](attachment:9978ae50-107e-4fe9-8f6e-1c0007c0aa35.png)
# - "color": ![image.png](attachment:8f3dc623-7598-4c5d-aaa0-f2bdb7d108a6.png)
# - "ir":  ![image.png](attachment:6f4e3abe-c478-4cf9-a17c-cd423ec45d1f.png)
# - "gyro": ![image.png](attachment:a9058d16-7342-4089-9c95-13e5bc4839ee.png)

# ### To test a sensor, set up a loop and print the value

# The following will print out the value of the color sensor every 1/20 of a second until you hit `CTRL-C` (i.e. `KeyboardInterrupt`) to stop the program.

# In[ ]:


from Robot373 import *

color_sensor=Sensors(None,"color",None,None)

try:
    while True:
        color=color_sensor.value
        print(color)
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# ### TypeError: NoneType object....

# It takes a little bit for sensors to give reasonable values.  Until they warm up, they return `None` for their value.  To solve it, you need to wait until the sensor starts returning reasonable things.
# 
# Method #1:  Put a `Wait` command.

# In[ ]:


from Robot373 import *

color_sensor=Sensors(None,"color",None,None)
Wait(3)

try:
    while True:
        color=color_sensor.value
        print(color)
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# a better way is to check the sensor to be not None.

# In[ ]:


from Robot373 import *

color_sensor=Sensors(None,"color",None,None)

print("Waiting for sensor to warm up...")
while color_sensor.value is None:
    Wait(0.05)
print("done.")



try:
    while True:
        color=color_sensor.value
        print(color)
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# ## Colors

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Timers
# 
# You can make a timer with the `Timer` object.  The `timer.value` returns the time in seconds since the timer was reset.  An example would be this, which prints out a value every 0.1 seconds for 5 seconds.

# In[ ]:


timer=Timer()
while timer.value<5:
    print(left.position,right.position)
    Wait(.1)


# ## Images

# In[ ]:


from Robot373 import *

take_picture("my cool pic.jpg")

print('Pausing for a few seconds for another image, but with viewing')
for i in range(5,0,-1):
    print(i)
    Wait(1)
    
take_picture("my cool pic2.jpg")


# adjust the brightness

# In[ ]:


from Robot373 import *

take_picture("my cool pic.jpg",brightness=50)


# ### What if I want to keep changing the filename to not overwrite the file?

# In[ ]:


from Robot373 import *
import os

count=0
fname=f"image_filename{count}.jpg"
while os.path.exists(fname):
    count+=1
    fname=f"image_filename{count}.jpg"
    
take_picture(fname)    


# In[ ]:





# In[ ]:





# # Programming pattern -- flags

# It is a common programming pattern to have a true/false (i.e. boolean) variable called a flag that keeps track of an event that toggles.  For example, if you want to have something happen when a button is pressed -- but don't want to do that thing while you're holding the button down, you can use a flag.   Here's an example which prints something when a button is pressed and then again when the button is released.

# In[ ]:


touch=Sensors("touch",None,None,None)

pressed=False

while True:
    if touch.value and not pressed:
        print("Button Pressed")
        pressed=True
    elif not touch.value and pressed:
        print("Button Released")
        pressed=False


# compare is with the same code without the flag, and you'll see the difference immediately.

# In[ ]:


while True:
    if touch.value:
        print("Button Pressed")
    elif not touch.value:
        print("Button Released")


# # Running on the robot

# - Edit the files on your robot
#     - VS Code with the Remote SSH Extension
#     - FileZilla or any other SSH/SFTP client
# - Run the files on your robot
# 
# ```
# glop-/Users/bblais-> ssh pi@10.2.2.32
# pi@10.2.2.32's password:
# Linux dex 4.19.66-v7+ #1253 SMP Thu Aug 15 11:49:46 BST 2019 armv7l
# 
# The programs included with the Debian GNU/Linux system are free software;
# the exact distribution terms for each program are described in the
# individual files in /usr/share/doc/*/copyright.
# 
# Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
# permitted by applicable law.
# Last login: Mon Oct 17 14:06:26 2022 from 10.100.52.148
# pi@dex:~ $ cd python
# pi@dex:~/python $ ls
# motorAB_test.py
# pi@dex:~/python $ python motorAB_test.py
# ```

# ## Useful Robot Scripts

# In[ ]:





# These will be sketches of them.  I haven't debugged them, so there may even be typos!  :-)
# 

# - use the ultrasonic sensor to give distances in meters or feet (whichever you’re more comfortable with)
# 

# In[ ]:


from Robot373 import *

def distance_in_inches(distance_in_cm):
    return distance_in_cm/100*39


eyes,touch=Sensors(None,None,"us","touch")

try:
    while True:
        distance=eyes.value  # distance in cm
        print(distance_in_inches(distance))
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# - use the motor value to give degrees turned
# 

# In[ ]:


from Robot373 import *

def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

left,right=Motors("ab")

try:
    while True:
        print(degrees(left.position))
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# - use the motor value to give distance traveled, given the wheel size

# In[ ]:


from Robot373 import *

def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

def distance_traveled(position):
    wheel_diameter_cm=2
    pi=3.141592653589793235
    
    return pi*wheel_diameter_cm*degrees(position)/360

    
    

left,right=Motors("ab")

left.power=50
right.power=50



try:
    while True:
        print("distance traveled so far:",distance_traveled(left.position))
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# In[ ]:





# - given the axis size and wheel size, use the motor value to turn robot 90 degrees
# 

# In[ ]:


from Robot373 import *

def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

def distance_traveled(position):
    wheel_diameter_cm=2
    pi=3.141592653589793235
    
    return pi*wheel_diameter_cm*degrees(position)/360

    
    

left,right=Motors("ab")

left.power=50
right.power=-50

axis_length_cm=6
pi=3.14159
distance_needed=(axis_length_cm/2)*2*pi/4  # need a quarter turn of the robot



try:
    while distance_traveled(left.position)<distance_needed:
        print("distance traveled so far:",distance_traveled(left.position))
        Wait(0.01)
except KeyboardInterrupt:
    pass

Shutdown()


# Move 30 cm and stop

# In[ ]:


from Robot373 import *

left,right=Motors("ab")


def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

def distance_traveled(position):
    wheel_diameter_cm=2
    pi=3.141592653589793235
    
    return pi*wheel_diameter_cm*degrees(position)/360

    
    


left.power=50
right.power=50


try:
    while distance_traveled(left.position)<30:  # cm
        print("distance traveled so far:",distance_traveled(left.position))
        Wait(0.05)
except KeyboardInterrupt:
    pass

left.power=0
right.power=0






Shutdown()


# make some functions for the basic motions

# In[ ]:


from Robot373 import *

left,right=Motors("ab")


def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

def distance_traveled(position):
    wheel_diameter_cm=2
    pi=3.141592653589793235
    
    return pi*wheel_diameter_cm*degrees(position)/360

def go_forward(distance):
    from math import abs

    left.reset_position()
    
    left.power=50
    right.power=50


    try:
        while abs(distance_traveled(left.position))<distance:  # cm
            print("distance traveled so far:",distance_traveled(left.position))
            Wait(0.05)
    except KeyboardInterrupt:
        pass

    left.power=0
    right.power=0


def go_backward(distance):
    from math import abs
    
    left.reset_position()
    
    left.power=-50
    right.power=-50


    try:
        while abs(distance_traveled(left.position))<distance:  # cm
            print("distance traveled so far:",distance_traveled(left.position))
            Wait(0.05)
    except KeyboardInterrupt:
        pass

    left.power=0
    right.power=0
    
    
    
    
def turn_right(degrees):
    left.reset_position()
    
    left.power=50
    right.power=-50

    axis_length_cm=6
    pi=3.14159
    distance_needed=(axis_length_cm/2)*2*pi/360*degrees  # need a quarter turn of the robot

    try:
        while distance_traveled(left.position)<distance_needed:
            print("[turning right] distance traveled so far:",distance_traveled(left.position))
            Wait(0.01)
    except KeyboardInterrupt:
        pass
    
    left.power=0
    right.power=0
    
    
go_forward(30)
Wait(1)

turn_right(90)
Wait(1)

go_forward(40)
Wait(1)
    
    
    
Shutdown()


# In[ ]:





# - use the color sensor to distinguish two colors (could be black and white, or any other pair of colors)

# In[ ]:


from Robot373 import *

color_sensor=Sensors(None,"color",None,None)  # color on sensor port S2
print("Waiting for sensor to warm up...")
while color_sensor.value is None:
    Wait(0.05)
print("done.")

try:
    while True:
        r,g,b,something=color_sensor.value
        print(r,g,b,something)
        print(closest_color(r,g,b,
                maroon=[128,0,0],
                gray=[128,128,128],
                white=[256,256,256],
                black=[0,0,0],
                ))
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# - forward until you see a color

# In[4]:


from Robot373 import *
left,right=Motors("ab")
color_sensor=Sensors(None,"color",None,None)  # color on sensor port S2

left.power=50
right.power=50

while True:
    r,g,b,_=color_sensor.value
    print(r,g,b)
    color=closest_color(r,g,b,
            white=[256,256,256],
            black=[0,0,0],
            )
    print(color)
    if color=="black":
        break
    Wait(0.05)

Shutdown()


# In[ ]:





# In[6]:


from Robot373 import *

def until_color(target_color,**kwargs):
    while True:
        r,g,b,_=color_sensor.value
        print(r,g,b)
        color=closest_color(r,g,b,
                            **kwargs
                )
        print(color)
        if color==target_color:
            break
        Wait(0.05)

def forward():
    left.power=50
    right.power=50

left,right=Motors("ab")
color_sensor=Sensors(None,"color",None,None)  # color on sensor port S2

forward()
until_color("black",
                white=[256,256,256],
                black=[0,0,0],)


Shutdown()


# In[ ]:





# - use the touch sensor to do each of the following:
#     - do something if the sensor is pressed
#     - do something only if the sensor is pressed and then released
#     - do something if the sensor is “double clicked” within a reasonably short time period

# In[ ]:





# - go forward for 3 seconds if a button is **pressed**

# In[ ]:


from Robot373 import *

eyes,touch=Sensors(None,None,"us","touch")

left,right=Motors("ab")


# do nothing until the touch sensor is pressed
while not touch.value:
    Wait(0.01)

left.power(50)
right.power(50)

Wait(3)

Shutdown()


# - go forward for 3 seconds if a button is **pressed and released**

# In[ ]:


from Robot373 import *

eyes,touch=Sensors(None,None,"us","touch")

left,right=Motors("ab")


# do nothing until the touch sensor is pressed
while not touch.value:
    Wait(0.01)

# do nothing until the touch sensor is released
while touch.value:
    Wait(0.01)
    
    
left.power(50)
right.power(50)

Wait(3)

Shutdown()


# - go forward for 3 seconds if a button is **double-clicked**

# In[ ]:


from Robot373 import *

def wait_for_double_click(touch):
    
    double_click_time=0.5  # seconds
    timer=Timer()
    count=0
    stop=False
    while not stop:
        
        # do nothing until the touch sensor is pressed
        while not touch.value:
            Wait(0.01)

        # do nothing until the touch sensor is released
        while touch.value:
            Wait(0.01)
        
        count+=1

        if count>=2:  # double-click
            if timer.value>double_click_time:  # too long between "clicks":
                timer._reset()  # restart the timer at t=0
                count=0
        else:
            stop=True
        

eyes,touch=Sensors(None,None,"us","touch")

left,right=Motors("ab")

wait_for_double_click(touch)
    
    
left.power(50)
right.power(50)

Wait(3)

Shutdown()

