# Write a python code using functions which calculates the number of upper case letters, 
# lower case letters, total number of characters andnumber of words

def upper(s):
    upper=0
    for c in s:
        if(c.isupper()):
            upper+=1
    return (upper)

def lower(s):
    lower=0
    for c in s:
        if(c.islower()):
            lower+=1
    return (lower)

def characters(s):
    chars=0
    for c in s:
        if(c==' '):
            chars+=1
    return (chars)

def words(s):
    words=1
    for c in s:
        if(c==' '):
            words+=1
    return (words)

sentence=input('Enter the sentence: ')
uletters=upper(sentence)
print(f'\nTotal number of upper case characters: {uletters}')
lLetters=lower(sentence)
print(f'\nTotal number of lower case characters: {lLetters}')
chars=characters(sentence)
print(f'\nTotal number of characters: {chars}')
words=words(sentence)
print(f'\nTotal number of words: {words}')