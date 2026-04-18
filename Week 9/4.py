# Create a txt data file of contact numbers of indians (random numbers)

import random

# Number of records (≈250 MB)
t = 10000000  

# Open file in write mode
f = open("contacts.txt", "w")

for i in range(t):

    # Generate Indian mobile number (starts with 6-9)
    mobile = random.choice(['6', '7', '8', '9'])
    mobile = mobile + ''.join(str(random.randint(0, 9)) for j in range(9))

    f.write(mobile + "\n")

# Close file
f.close()

print("File generation completed!")