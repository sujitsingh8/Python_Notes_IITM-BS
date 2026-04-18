''' Counting the most occurred word: '''

l=['it','was','is','then','it','was','was']
s=set(l) # it converts list l to a set

d={}
max=0
word=''
for x in s:
    d[x]=0
for x in l:
    d[x]+=1
    if d[x]>max:
        max=d[x]
        word=x
print(d)
# {'it': 2, 'was': 3, 'is': 1, 'then': 1}
print('max is', max, 'word is', word) 
# max is 3 word is was