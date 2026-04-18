# List comprehension-

fruits=["mango",'apple','banana','orange','pineapple','watermelon','guava','kiwi']

'''
newlist=[]
for fruit in fruits:
    if 'n' in fruit:
        newlist.append(fruit.capitalize())
'''

newlist=[fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newlist)
# ['Mango', 'Banana', 'Orange', 'Pineapple', 'Watermelon']