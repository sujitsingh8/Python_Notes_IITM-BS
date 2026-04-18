# Bar chart-

import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"]) # Create an array for x-axis categories (labels), These are categorical values
y=np.array([3,8,1,10]) # Create an array for y-axis values, These are numerical values corresponding to each category

# -------- Vertical Bar Chart --------

plt.bar(x,y) # Draw a vertical bar chart, x → categories, y → heights of bars
plt.show() # Display the vertical bar chart

# -------- Horizontal Bar Chart --------

plt.barh(x,y) # Draw a horizontal bar chart, x → categories (shown on y-axis), y → lengths of bars
plt.show() # Display the horizontal bar chart