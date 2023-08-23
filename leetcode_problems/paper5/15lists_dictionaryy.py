# 15. Create a new dictionary using the list and dictionary defined below. The keys of
# the new dictionary will be the elements in the list so we will iterate over the
# elements in list. If the element is also in the dictionary, the value will be the values of
# that key in the dictionary. Otherwise, the value will be the length of the key.
# I/p:
# lst = ['data','science','artificial', 'intelligence'] dct = {'data': 5, 'science': 3, 'machine':
# 1, 'learning': 8}
# O/p:
# {'artificial': 10, 'data': 5, 'intelligence': 12, 'science': 3}

l = ['data','science','artificial', 'intelligence'] 
d = {'data': 5, 'science': 3, 'machine':1, 'learning': 8}
#create new dictionary
#conditions
#1. key should be element in list & value should be its length
#2. if element already exist in the other dict then just add that key-value pair here
op={}
for i in l:
    if i in d:
        op.update({i:d[i]})
    else:
        op.update({i:len(i)})
print(op)