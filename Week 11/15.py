# Print number of students only after aplying previous filters

import pandas as pd
scores=pd.read_csv('scores.csv')

print(scores[scores['Physics']>85].shape[0])
# 7
print(scores[scores['Physics'].between(70,85)].shape[0])
# 10
print(scores[scores['Physics'].between(60,70)].shape[0])
# 9
print(scores[scores['Physics']<60].shape[0])
# 4