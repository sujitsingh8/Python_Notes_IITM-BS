# Filter

# filters students data whose physics marks are greater than 85

import pandas as pd
scores=pd.read_csv('scores.csv')

print(scores[scores['Physics']>85])

'''
    CardNo      Name Gender  ... Physics Chemistry  Total
5        5   Akshaya      F  ...      92        84    247
7        7    Aditya      M  ...      92        76    252
9        9  Clarence      M  ...      92        92    281
11      11     Rahul      M  ...      92        92    281
16      16   Tauseef      M  ...      86        43    216
18      18   Abirami      F  ...      92        97    261
23      23   Deepika      F  ...      91        88    276

[7 rows x 9 columns] '''

#...........................................................................................................

# filters students data whose physics marks are greater than 70 and less than 85

print(scores[scores['Physics'].between(70,85)])

'''
    CardNo       Name  ... Chemistry Total
6        6     Sameer  ...        87   250
10      10      Kavya  ...        68   204
13      13       Gopi  ...        89   227
17      17     Arshad  ...        67   210
19      19   Vetrivel  ...        62   196
24      24  Siddharth  ...        58   174
25      25      Geeta  ...        92   254
26      26         JK  ...        82   227
27      27      Jagan  ...        52   209
28      28      Nisha  ...        83   240

[10 rows x 9 columns] '''

#...........................................................................................................

# filters students data whose physics marks are greater than 60 and less than 70

print(scores[scores['Physics'].between(60,70)])

'''
    CardNo      Name Gender  ... Physics Chemistry  Total
1        1    Harish      M  ...      45        91    198
2        2  Shashank      M  ...      54        77    188
3        3      Rida      F  ...      53        78    173
15      15   Goutami      F  ...      58        90    224

[4 rows x 9 columns] '''

#...........................................................................................................

# filters students data whose physics marks are less than 70

print(scores[scores['Physics']<60])

'''
    CardNo      Name Gender  ... Physics Chemistry  Total
1        1    Harish      M  ...      45        91    198
2        2  Shashank      M  ...      54        77    188
3        3      Rida      F  ...      53        78    173
15      15   Goutami      F  ...      58        90    224

[4 rows x 9 columns] '''