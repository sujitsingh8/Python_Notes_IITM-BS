# Scatter plot(2 datasets)-

import matplotlib.pyplot as plt
import numpy as np

# -------- First set of data --------

x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6]) # Create array for x-axis values (first dataset)
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86]) # Create array for y-axis values (first dataset)

plt.scatter(x,y) # Plot the first scatter plot, Each (x, y) pair is shown as a dot

# -------- Second set of data --------

x=np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,1,12]) # Create array for x-axis values (second dataset)
y=np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85]) # Create array for y-axis values (second dataset)

plt.scatter(x,y) # Plot the second scatter plot, These points will appear on the same graph as the first dataset

plt.show() # Display the final graph with both scatter plots