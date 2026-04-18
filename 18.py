# groupby in pandas

import pandas as pd
scores=pd.read_csv('scores.csv')

# Group the data based on the 'Gender' column
# .groupby('Gender') creates groups for each unique gender (M and F)
# .groups shows the card no. as the row index numbers that belong to each group
print(scores.groupby('Gender').groups)

'''
{'F': [3, 4, 5, 10, 12, 14, 15, 18, 21, 22, 23, 25, 28], 
'M': [0, 1, 2, 6, 7, 8, 9, 11, 13, 16, 17, 19, 20, 24, 26, 27, 29]}
'''

'''
This means:
  - All rows where Gender = 'F' are present at index positions:
      3, 4, 5, 10, 12, 14, 15, 18, 21, 22, 23, 25, 28 
  - All rows where Gender = 'M' are present at index positions:
      0, 1, 2, 6, 7, 8, 9, 11, 13, 16, 17, 19, 20, 24, 26, 27, 29

So, groupby() is used to:
  - Split the data based on a column (Gender)
  - Collect rows belonging to each group '''

# Why CardNo becomes the row index in your output?

''' 
When you read the CSV using:
  cores = pd.read_csv('scores.csv')
    
pandas automatically creates its own index starting from 0, 1, 2, .... (from below header)

In our CSV file, the first column is:
  CardNo
  0, 1, 2, 3, ...

So pandas treats CardNo as a normal column, but its values look exactly like default index values. '''