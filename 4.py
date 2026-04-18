# Calculate total marks of the topper from scores.csv-

''' Using the concept of file handling '''

f = open('scores.csv', 'r') # Open the file "scores.csv" in read mode
scores = f.readlines()[1:] # Read all lines from the file and skip the first line (header)

max_total = 0 # Variable to store the highest total marks found so far

for record in scores: # Loop through each student record (each line in the file)
    fields = record.split(',') # Split the line using comma (,) to separate each field
    
    if int(fields[8]) > max_total: # fields[8] contains the total marks column, 
    # Convert it to integer and compare with current max_total
    
        max_total = int(fields[8]) # Update max_total if a higher total is found

print("Max Score:",max_total) # Print the highest total marks (topper's total)
# Max Score: 281