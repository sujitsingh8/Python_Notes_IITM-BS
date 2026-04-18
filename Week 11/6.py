# What else can we do with pandas?


# This prints the entire scores dataset in the form of the table
import pandas as pd
scores=pd.read_csv('scores.csv')
print(scores) # printing dataframe

'''
    CardNo       Name  ... Chemistry Total
0        0  Bhuvanesh  ...        78   210
1        1     Harish  ...        91   198
2        2   Shashank  ...        77   188
3        3       Rida  ...        78   173
4        4     Ritika  ...        89   240
5        5    Akshaya  ...        84   247
6        6     Sameer  ...        87   250
7        7     Aditya  ...        76   252
8        8      Surya  ...        51   189
9        9   Clarence  ...        92   281
10      10      Kavya  ...        68   204
11      11      Rahul  ...        92   281
12      12   Srinidhi  ...        71   187
13      13       Gopi  ...        89   227
14      14     Sophia  ...        93   244
15      15    Goutami  ...        90   224
16      16    Tauseef  ...        43   216
17      17     Arshad  ...        67   210
18      18    Abirami  ...        97   261
19      19   Vetrivel  ...        62   196
20      20     Kalyan  ...        91   252
21      21     Monika  ...        74   221
22      22      Priya  ...        57   181
23      23    Deepika  ...        88   276
24      24  Siddharth  ...        58   174
25      25      Geeta  ...        92   254
26      26         JK  ...        82   227
27      27      Jagan  ...        52   209
28      28      Nisha  ...        83   240
29      29     Naveen  ...        81   219

[30 rows x 9 columns] '''