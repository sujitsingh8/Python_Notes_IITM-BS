# conditions under conditions

# Lecture 2.9 Last Problem (Flowchart)
# Convert the given flowchart into python code-

print('Travel from City A to City B')
Time=int(input('Enter time:'))
Longer=int(input('Define Longer:'))
if(Time>=Longer):
    Price=int(input('Enter price:'))
    Higher=int(input('Define higher'))
    if(Price>=Higher):
        print('Train')
    else:
        print('Coach')

else:
    Price=int(input('Enter price:'))
    Higher=int(input('Define Higher:'))
    if(Price>=Higher):
        print('Daytime flight')
    else:
        print('Red eye flight')
        
print('Arrive city B')