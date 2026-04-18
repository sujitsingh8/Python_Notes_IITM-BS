import pandas as pd
scores=pd.read_csv('scores.csv')

print(scores[scores['Name']=='Nisha']) # it help to read data column wise

'''
    CardNo   Name Gender  ... Physics Chemistry  Total
28      28  Nisha      F  ...      83        83    240 

[1 rows x 9 columns] '''