import pandas as pd
scores=pd.read_csv('scores.csv')
print(scores.shape) # '.shape' returns a tuple containing (rows,columns)
# (30, 9)

print(scores.count()) #'.count' prints the number of values in the each coulmn

'''
CardNo         30
Name           30
Gender         30
DataofBirth    30
CityTown       30
Mathematics    30
Physics        30
Chemistry      30
Total          30
dtype: int64 '''

print(scores['Total'].max())
# 281
print(scores['Total'].min())
# 173

print(scores['Total'].mean()) # '.mean' returns the average of the particular columns values
# 224.36666666666667
# Here it returned the average of total marks from the column total

print(scores['Total'].sum()) # '.sum()' return sum of the specified column's values
# 6731
# Here it returned the sum of the values in the column ‘Total’