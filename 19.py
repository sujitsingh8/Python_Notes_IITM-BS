# Show card no. of female and male students scored above average in each subject by using groupby

import pandas as pd
scores=pd.read_csv('scores.csv')

subject=['Mathematics','Physics','Chemistry']

for sub in subject:
    print('Above average in:',sub)
    avg=scores[sub].mean()
    
    # Filter students who scored more than the average in this subject
    # Then group them by Gender
    # .groups gives the card no. as the row index numbers of students in each gender group
    print(scores[scores[sub]>avg].groupby('Gender').groups)
    
'''
Above average in: Mathematics
{'F': [4, 14, 15, 21, 23, 25, 28], 'M': [6, 7, 8, 9, 11, 16, 20, 26, 27]}
Above average in: Physics
{'F': [5, 18, 23, 25, 28], 'M': [6, 7, 9, 11, 16, 17, 19, 27]}
Above average in: Chemistry
{'F': [3, 4, 5, 14, 15, 18, 23, 25, 28], 'M': [0, 1, 6, 9, 11, 13, 20, 26, 29]} '''