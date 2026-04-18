# Apply more than one type of filters

import pandas as pd
scores=pd.read_csv('scores.csv')

# it will print number of female students with marks more than 85 in physics
print(scores[(scores['Gender']=='F') & (scores['Physics']>85)].shape[0])
# 3

# pandas uses it's own operator types like for "&&" in pyhton, pandas use "&"

# it will print number of male students with marks more than 85 in physics
print(scores[(scores['Gender']=='M') & (scores['Physics']>85)].shape[0])
# 4

#...........................................................................................................

subject=['Mathematics','Physics','Chemistry']

for sub in subject:
    print('Above 85 in:',sub)
    print("Female:",scores[(scores['Gender']=='F') & (scores[sub]>85)].shape[0])
    print("Male:",scores[(scores['Gender']=='M') & (scores[sub]>85)].shape[0])

'''
Above 85 in: Mathematics
Female: 4
Male: 4
Above 85 in: Physics
Female: 3
Male: 4
Above 85 in: Chemistry
Female: 6
Male: 6 '''