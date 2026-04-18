import pandas as pd
scores=pd.read_csv('scores.csv')

print(scores.head()) # it will print first 5 rows from the dataset

''' 
   CardNo       Name Gender  ... Physics Chemistry  Total
0       0  Bhuvanesh      M  ...      64        78    210
1       1     Harish      M  ...      45        91    198
2       2   Shashank      M  ...      54        77    188
3       3       Rida      F  ...      53        78    173
4       4     Ritika      F  ...      64        89    240

[5 rows x 9 columns] '''

print(scores.tail()) # it will print last 5 rows from the dataset

'''
    CardNo    Name Gender  ... Physics Chemistry  Total
25      25   Geeta      F  ...      75        92    254
26      26      JK      M  ...      71        82    227
27      27   Jagan      M  ...      76        52    209
28      28   Nisha      F  ...      83        83    240
29      29  Naveen      M  ...      66        81    219

[5 rows x 9 columns] '''