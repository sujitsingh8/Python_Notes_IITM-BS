import pandas as pd
scores=pd.read_csv('scores.csv')
print(scores['Total'].sort_values(ascending=False)) # return sorted data of the particular column in descending order

'''
11    281
9     281
23    276
18    261
25    254
7     252
20    252
6     250
5     247
14    244
28    240
4     240
13    227
26    227
15    224
21    221
29    219
16    216
0     210
17    210
27    209
10    204
1     198
19    196
8     189
2     188
12    187
22    181
24    174
3     173
Name: Total, dtype: int64 '''