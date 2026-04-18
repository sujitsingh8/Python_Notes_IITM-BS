# first install matplotlib by running: pip install matplotlib

# Scatter plot-

''' Import pyplot module from matplotlib for plotting graphs '''
import matplotlib.pyplot as plt
''' Import numpy for working with numerical data and arrays '''
import numpy as np

'''
Create an array of x-axis values
These could represent any variable (e.g., age, study hours, etc.) '''
x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])

'''
Create an array of y-axis values
These could represent corresponding outcomes (e.g., marks, performance, etc.) '''
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

'''
Create a scatter plot
Each (x, y) pair is plotted as an individual point (dot) on the graph '''
plt.scatter(x,y)

''' Display the plot on the screen '''
plt.show()