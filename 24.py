# Histograms-

import matplotlib.pyplot as plt
import numpy as np

'''
Generate 250 random values following a normal (Gaussian) distribution
170 → mean (average value)
10  → standard deviation (spread of data)
250 → number of data points '''
x=np.random.normal(170,10,250)

plt.hist(x) # Create a histogram, It shows how the data is distributed across value ranges (bins)
plt.show() # Display the histogram