# Print maximum and minimum marks obtained by boys and girls

import pandas as pd
scores=pd.read_csv('scores.csv')

# print(scores[scores['Gender']=='M']) # Prints all data of boys from dataset

'''
    CardNo       Name Gender DataofBirth   CityTown  Mathematics  Physics  Chemistry  Total
0        0  Bhuvanesh      M       7 Nov      Erode           68       64         78    210
1        1     Harish      M       3 Jun      Salem           62       45         91    198
2        2   Shashank      M       4 Jan    Chennai           57       54         77    188
6        6     Sameer      M      23 Mar      Ambur           81       82         87    250
7        7     Aditya      M      15 Mar    Vellore           84       92         76    252
8        8      Surya      M      28 Feb  Bengaluru           74       64         51    189
9        9   Clarence      M       6 Dec  Bengaluru           97       92         92    281
11      11      Rahul      M      30 Apr  Bengaluru           97       92         92    281
13      13       Gopi      M       6 May    Madurai           65       73         89    227
16      16    Tauseef      M      30 Dec     Trichy           87       86         43    216
17      17     Arshad      M      14 Dec    Chennai           62       81         67    210
19      19   Vetrivel      M      30 Aug     Trichy           56       78         62    196
20      20     Kalyan      M      17 Sep    Vellore           93       68         91    252
24      24  Siddharth      M      26 Dec    Madurai           44       72         58    174
26      26         JK      M      22 Jul    Chennai           74       71         82    227
27      27      Jagan      M       4 Mar    Madurai           81       76         52    209
29      29     Naveen      M      13 Oct    Vellore           72       66         81    219 '''

# print(scores[scores['Gender']=='M']['Total']) # Prints only "Total" column of boys only from dataset

'''
0     210
1     198
2     188
6     250
7     252
8     189
9     281
11    281
13    227
16    216
17    210
19    196
20    252
24    174
26    227
27    209
29    219
Name: Total, dtype: int64 '''

print(scores[scores['Gender']=='M']['Total'].max()) # Prints max Total from boys data
# 281

print(scores[scores['Gender']=='M']['Total'].min()) # Prints min Total from boys data
# 174

print(scores[scores['Gender']=='F']['Total'].max()) # Prints max Total from girls data
# 276

print(scores[scores['Gender']=='F']['Total'].min()) # Prints min Total from girls data
# 173