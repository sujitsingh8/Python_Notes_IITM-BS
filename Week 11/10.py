import pandas as pd
scores=pd.read_csv('scores.csv')

print(type(scores)) # DataFrame
# <class 'pandas.core.frame.DataFrame'>

print(type(scores['Name'])) # Any column in DataFrame is known as Series
# <class 'pandas.core.series.Series'>