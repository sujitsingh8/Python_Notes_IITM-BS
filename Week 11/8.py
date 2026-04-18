import pandas as pd
scores=pd.read_csv('scores.csv')
print(scores['Total'].sort_values()) # '.sort_values' return sorted data of the particular column in ascending order

'''
3     173
24    174
22    181
12    187
2     188
8     189
19    196
1     198
10    204
27    209
0     210
17    210
16    216
29    219
21    221
15    224
26    227
13    227
4     240
28    240
14    244
5     247
6     250
7     252
20    252
25    254
18    261
23    276
9     281
11    281
Name: Total, dtype: int64 '''