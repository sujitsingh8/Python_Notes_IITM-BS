# Pie Chart

import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15]) # Create an array of values, Each value represents a portion of the whole
mylabels=["Apples","Bananas","Cherries","Dates"] # Create labels for each slice of the pie chart

'''
Draw the pie chart
y → data values
labels → names shown for each slice
startangle=90 → rotates the chart so it starts from the top '''
plt.pie(y,labels=mylabels,startangle=90)
plt.show() # Display the pie chart