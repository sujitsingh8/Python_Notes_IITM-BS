''' human.txt is a file of human genes, sequence of actg
If the genes follow any sequence that means he/she is predisposed to some disease.

Suppose if 'gtatgac' is a sequence is present it means he/she is diabetic. '''

# Let write a program to find if a person is diabetic or not-

f=open('human.txt','r')
seq=f.read()
diab='gtatgac'
print(diab in seq) # prints True if person is diabetic
# False

print('GGGAAATTTCCCGGG' in seq) # prints True if person has Heart disease risk
# True