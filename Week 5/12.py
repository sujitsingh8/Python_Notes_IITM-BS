''' Dictionaries: '''

# creating a dictionary which has name as key and phone number as value

d={} # this is a dictionary
d['joe']=9898989898 # creating key and assigning the value
d['nitin']=7878787878
d['ramya']=6767676767
print(d)
# {'joe': 9898989898, 'nitin': 7878787878, 'ramya': 6767676767}

print(d['joe']) # pass the key and you will gey value
# 9898989898

# print(d['iit']) # it will give error as there is nothing iit in dict
# print(d[0]) # indexing does not work in dictionaries