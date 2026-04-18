# Calculate total marks of the topper from scores.csv-

# First install pandas by running:
''' pip install pandas '''

''' Using pandas '''

# Import the pandas library and give it a short name 'pd'
import pandas as pd

# Read the CSV file 'scores.csv' and store it as a DataFrame
scores = pd.read_csv('scores.csv')

# Select the 'Total' column and find the maximum value in it
print("Max Score:",scores['Total'].max())
# Max Score: 281

# Similarly we can find the min marks of the student using ".min()"

''' A DataFrame is a 2-dimensional data structure that stores data in:
        Rows → each row is one record (e.g., one student)
        Columns → each column is one field (e.g., Name, Marks, Total) '''