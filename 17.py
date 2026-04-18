# Find number of female and male students scored above average in each subject

import pandas as pd
scores=pd.read_csv('scores.csv')

subject=['Mathematics','Physics','Chemistry']

for sub in subject:
    print('Above average in:',sub)
    avg=scores[sub].mean()
    print("Female:",scores[(scores['Gender']=='F') & (scores[sub]>avg)].shape[0])
    print("Male:",scores[(scores['Gender']=='M') & (scores[sub]>avg)].shape[0])
    
'''
Above average in: Mathematics
Female: 7
Male: 9
Above average in: Physics
Female: 5
Male: 8
Above average in: Chemistry
Female: 9
Male: 9 '''