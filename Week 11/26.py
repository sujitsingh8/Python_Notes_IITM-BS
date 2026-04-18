# subplot example

# This program shows how to draw multiple plots in a single figure

import matplotlib.pyplot as plt
import numpy as np

# -------- First subplot --------

# Create x and y data
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(2,3,1) # Create a subplot in a 2 row * 3 column grid, Position 1 means first plot
plt.plot(x,y)

# -------- Second subplot --------

x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(2,3,2) # Position 2 means second plot
plt.plot(x,y)

# -------- Third subplot --------

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(2,3,3) # Position 3 means third plot
plt.plot(x,y)

# -------- Fourth subplot --------

x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(2,3,4) # Position 4 means fourth plot
plt.plot(x,y)

# -------- Fifth subplot --------

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(2,3,5) # Position 5 means fifth plot
plt.plot(x,y)

# -------- Sixth subplot --------

x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(2,3,6) # Position 6 means sixth (last) plot
plt.plot(x,y)

plt.show() # Display all subplots together in one figure